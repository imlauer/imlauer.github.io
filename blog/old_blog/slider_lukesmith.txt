---
title: "Generate videos cli"
date: 2025-12-02T02:03:33-03:00
---
El script está hecho para que el audio dure lo msimo que el video

#### Si el audio dura más tiempo entonces tenes que usar el script tal cual está, si el audio dura menos tenes que hardcodear el valor de `totseconds` a 5 o a los segundos que pongas por imágen.

##### TODO (para hacer):

1. Arreglar el script si el audio dura menos que las imágenes porque genera valor negativo.
2. Subir video automáticamente a YouTube y a Archive.
3. Crear un artículo automáticamente basado en imágenes.
4. Crear un audio con espeak que tenga la misma duración que el video (contá cuántas imágenes tenes y multiplicá por cada segundo cada imágen).
5. Enlazá las URLs de archive automáticamente 
6. Hacer script para juntar videos (no imagenes) con ffmpeg.
7. Subtitular audios subilos a youtube y descargalos con yt-dlp.
8. Pasar los subtitulos a un llm o a chatgpt para que haga un resumen.
9. Generar un archivo de audio con los subtitulos de chatgpt.

Sacá las fotos horizontales, grabá el audio (despues de grabar el audio subi el volumen con ffmpeg 4 veces mas el comando esta en la publicacion interesantes-comandos), disponé de espacio disponible.

Subí el audio a youtube esto lo hago usando un script para agregar una imagen al audio porque no se puede subir audios a youtube y descargá los subtítulos usando esto: [https://imlauera.github.io/srt_to_txt/](https://imlauera.github.io/srt_to_txt/)

El archivo para subir audios a youtube está en este blog (crear blog post) se llama.

```bash
yt-dlp --ignore-config --write-subs --write-auto-sub --sub-lang es --sub-format "srt" --skip-download https://www.youtube.com/watch?v=VIDEO_ID
sed -E '/^[0-9]+$|^$/d; /^[0-9]{2}:/d' video.en.srt > subtitles.txt
```

Ahora copiá y pegá los subtitulos por partes a ChatGPT y pedile que haga un resumen luego guardalos en un archivo llamado `chatgpt.txt`.

Ahora generamos el audio, podes usar piper-tts.

```bash
cat chatgpt.txt | espeak-ng -v es -w rock.wav
ls *.jpg | sort | ./slider_gen_timestamps.sh > video
./slider -i video -a rock.wav
```

**Lo haremos usando el script de LukeSmith: `slider`.**


### Agarré la transcripción del audio lo tire a chatgpt y lo pasé a `cat chatgpt.txt | espeak-ng -v es -w rock.wav` que me generó un archivo de audio y luego se lo pasé a `slider`.

Primero grabá el audio y después ajustá los timestamp para la longitud de ese audio.

#### Tenes que pasar el archivo de audio con `-a` de lo contrario tirará un error, más abajo explico como solucionarlo.

```bash
$ ./slider
Give an input file with -i.
The file should look as this example:

00:00:00        first_image.jpg
00:00:03        otherdirectory/next_image.jpg
00:00:09        this_image_starts_at_9_seconds.jpg
etc...

Timecodes and filenames must be separated by Tabs.
```

#### Tuve que cambiar porque no me tomaba m4a como un archivo de audio.

```bash
case "$(file --dereference --brief --mime-type -- "$audio")" in
	audio/*) ;;

```

a

```bash
case "$(file --dereference --brief --mime-type -- "$audio")" in
	video/*) ;;

```


El script tiene un problema y no me permite generar videos **sin audio** porque el `video.prep` generaba un valor negativo entonces hice lo siguiente

```bash
cd .cache/slider/mi_video
```

Y acá están las imágenes generadas por magick con la resolución corregida.

Entonces edito el archivo video.prep arreglo el tiempo negativo del último archivo y ejecuté:

```bash
ffmpeg -hide_banner -y -f concat -safe 0 -i "video.prep" -fps_mode vfr -c:v libx264 -pix_fmt yuv420p "video.mp4"
```
Y dejo el ultimo nombre archivo sin nada abajo


##### Lo podes conseguir clonando su repo (mas abajo pegue el codigo del script)

```bash
git clone https://github.com/lukesmithxyz/voidrice
cd .local/bin/
./slider
```

Cambie esto en el codigo: `-vsync vfr` lo reemplace por `-fps_mode vfr`.

---

#### Esto te sirve para generar los timestamps (una imagen cada 5 segundos) lo guarde como `slider_gen_timestamps.sh`.



```bash
#!/bin/bash

# Usage: ./gen_timestamps.sh *.jpg
# or:    ls *.jpg | sort | ./gen_timestamps.sh

sec=0

while read -r file; do
    # Format seconds → HH:MM:SS
    timestamp=$(printf "%02d:%02d:%02d" $((sec/3600)) $(((sec/60)%60)) $((sec%60)))

    printf "%s\t%s\n" "$timestamp" "$file"

    # Add 20 seconds for next file
    sec=$((sec + 5))
done
```

#### Ahora en la carpeta en donde tengas todas las imagenes ejecuta:

```bash
ls *.jpg | sort | bash gen.sh > video
```

#### Ahora creamos el video:

```bash
./slider -i video -a audio.mp3
```

Si el audio es m4a tendras que hacer una ligera modificacion en el codigo que expliqué en este mismo articulo más arriba.

### Mi version de Slider

```bash
#!/bin/sh

# Give a file with images and timecodes and creates a video slideshow of them.
#
# Timecodes must be in format 00:00:00.
#
# Imagemagick and ffmpeg required.

# Application cache if not stated elsewhere.
cache="${XDG_CACHE_HOME:-$HOME/.cache}/slider"

while getopts "hvrpi:c:a:o:d:f:t:e:x:s:" o; do case "${o}" in
	c) bgc="$OPTARG" ;;
	t) fgc="$OPTARG" ;;
	f) font="$OPTARG" ;;
	i) file="$OPTARG" ;;
	a) audio="$OPTARG" ;;
	o) outfile="$OPTARG" ;;
	d) prepdir="$OPTARG" ;;
	r) redo="$OPTARG" ;;
	s) ppt="$OPTARG" ;;
	e) endtime="$OPTARG" ;;
	x) res="$OPTARG"
		echo "$res" | grep -qv "^[0-9]\+x[0-9]\+$" &&
			echo "Resolution must be dimensions separated by a 'x': 1280x720, etc." &&
			exit 1 ;;
	p) echo "Purge old build files in $cache? [y/N]"
		read -r confirm
		echo "$confirm" | grep -iq "^y$" && rm -rf "$cache" && echo "Done."
		exit ;;
	v) verbose=True ;;
	*) echo "$(basename "$0") usage:
  -i  input timecode list (required)
  -a  audio file
  -c  color of background (use html names, black is default)
  -t  text color for text slides (white is default)
  -s  text font size for text slides (150 is default)
  -f  text font for text slides (sans serif is default)
  -o  output video file
  -e  if no audio given, the time in seconds that the last slide will be shown (5 is default)
  -x  resolution (1920x1080 is default)
  -d  tmp directory
  -r  rerun imagemagick commands even if done previously (in case files or background has changed)
  -p  purge old build files instead of running
  -v  be verbose" && exit 1

esac done

# Check that the input file looks like it should.
{ head -n 1 "$file" 2>/dev/null | grep -q "^00:00:00	" ;} || {
	echo "Give an input file with -i." &&
	echo "The file should look as this example:

00:00:00	first_image.jpg
00:00:03	otherdirectory/next_image.jpg
00:00:09	this_image_starts_at_9_seconds.jpg
etc...

Timecodes and filenames must be separated by Tabs." &&
	exit 1
	}

if [ -n "${audio+x}" ]; then
	# Check that the audio file looks like an actual audio file.
	case "$(file --dereference --brief --mime-type -- "$audio")" in
		audio/*) ;;
		*) echo "That doesn't look like an audio file."; exit 1 ;;
	esac
	totseconds="$(date '+%s' -d $(ffmpeg -i "$audio" 2>&1 | awk '/Duration/ {print $2}' | sed s/,//))"
fi

prepdir="${prepdir:-$cache/$file}"
outfile="${outfile:-$file.mp4}"
prepfile="$prepdir/$file.prep"

[ -n "${verbose+x}" ] && echo "Preparing images... May take a while depending on the number of files."
mkdir -p "$prepdir"

{
while read -r x;
do
	# Get the time from the first column.
	time="${x%%	*}"
	seconds="$(date '+%s' -d "$time")"
	# Duration is not used on the first looped item.
	duration="$((seconds - prevseconds))"

	# Get the filename/text content from the rest.
	content="${x#*	}"
	base="$(basename "$content")"
	base="${base%.*}.jpg"

	if [ -f "$content" ]; then
		# If images have already been made in a previous run, do not recreate
		# them unless -r was given.
		{ [ ! -f "$prepdir/$base" ] || [ -n "${redo+x}" ] ;} &&
			magick -size "${res:-1920x1080}" canvas:"${bgc:-black}" -gravity center "$content" -resize 1920x1080 -composite "$prepdir/$base"
	else
		{ [ ! -f "$prepdir/$base" ] || [ -n "${redo+x}" ] ;} &&
			magick -size "${res:-1920x1080}" -background "${bgc:-black}" -fill "${fgc:-white}" -font "${font:-Sans}" -pointsize "${ppt:-150}" -gravity center label:"$content" "$prepdir/$base"
	fi

	# If the first line, do not write yet.
	[ "$time" = "00:00:00" ] || echo "file '$prevbase'
duration $duration"

	# Keep the information required for the next file.
	prevbase="$base"
	prevtime="$time"
	prevseconds="$(date '+%s' -d "$prevtime")"
done < "$file"
# Do last file which must be given twice as follows
#
# Si el audio dura menos el tiempo que el video el endtime deberia ser 3.

longitud_audio_float=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $audio)
longitud_audio=$(printf "%.0f" $longitud_audio_float)

cantidad_imagenes=$(cat $file | wc -l)

## 3 segundos cada imagen
longitud_video=$((cantidad_imagenes*5))

endtime=""

((longitud_audio >= longitud_video)) && endtime="$((totseconds-seconds))"

((longitud_video > longitud_audio)) && endtime="5"

echo "file '$base'
duration ${endtime:-5}
file '$base'"
} > "$prepfile"
if [ -n "${audio+x}" ]; then
	ffmpeg -hide_banner -y -f concat -safe 0 -i "$prepfile" -i "$audio" -c:a aac -vsync vfr -c:v libx264 -pix_fmt yuv420p "$outfile"
else
	ffmpeg -hide_banner -y -f concat -safe 0 -i "$prepfile" -vsync vfr -c:v libx264 -pix_fmt yuv420p "$outfile"
fi

# Might also try:
# -vf "fps=${fps:-24},format=yuv420p" "$outfile"
# but has given some problems.
```


### Old Slider

```bash
#!/bin/sh

# Give a file with images and timecodes and creates a video slideshow of them.
#
# Timecodes must be in format 00:00:00.
#
# Imagemagick and ffmpeg required.

# Application cache if not stated elsewhere.
cache="${XDG_CACHE_HOME:-$HOME/.cache}/slider"

while getopts "hvrpi:c:a:o:d:f:t:e:x:s:" o; do case "${o}" in
	c) bgc="$OPTARG" ;;
	t) fgc="$OPTARG" ;;
	f) font="$OPTARG" ;;
	i) file="$OPTARG" ;;
	a) audio="$OPTARG" ;;
	o) outfile="$OPTARG" ;;
	d) prepdir="$OPTARG" ;;
	r) redo="$OPTARG" ;;
	s) ppt="$OPTARG" ;;
	e) endtime="$OPTARG" ;;
	x) res="$OPTARG"
		echo "$res" | grep -qv "^[0-9]\+x[0-9]\+$" &&
			echo "Resolution must be dimensions separated by a 'x': 1280x720, etc." &&
			exit 1 ;;
	p) echo "Purge old build files in $cache? [y/N]"
		read -r confirm
		echo "$confirm" | grep -iq "^y$" && rm -rf "$cache" && echo "Done."
		exit ;;
	v) verbose=True ;;
	*) echo "$(basename "$0") usage:
  -i  input timecode list (required)
  -a  audio file
  -c  color of background (use html names, black is default)
  -t  text color for text slides (white is default)
  -s  text font size for text slides (150 is default)
  -f  text font for text slides (sans serif is default)
  -o  output video file
  -e  if no audio given, the time in seconds that the last slide will be shown (5 is default)
  -x  resolution (1920x1080 is default)
  -d  tmp directory
  -r  rerun imagemagick commands even if done previously (in case files or background has changed)
  -p  purge old build files instead of running
  -v  be verbose" && exit 1

esac done

# Check that the input file looks like it should.
{ head -n 1 "$file" 2>/dev/null | grep -q "^00:00:00	" ;} || {
	echo "Give an input file with -i." &&
	echo "The file should look as this example:

00:00:00	first_image.jpg
00:00:03	otherdirectory/next_image.jpg
00:00:09	this_image_starts_at_9_seconds.jpg
etc...

Timecodes and filenames must be separated by Tabs." &&
	exit 1
	}

if [ -n "${audio+x}" ]; then
	# Check that the audio file looks like an actual audio file.
	case "$(file --dereference --brief --mime-type -- "$audio")" in
		audio/*) ;;
		*) echo "That doesn't look like an audio file."; exit 1 ;;
	esac
	totseconds="$(date '+%s' -d $(ffmpeg -i "$audio" 2>&1 | awk '/Duration/ {print $2}' | sed s/,//))"
fi

prepdir="${prepdir:-$cache/$file}"
outfile="${outfile:-$file.mp4}"
prepfile="$prepdir/$file.prep"

[ -n "${verbose+x}" ] && echo "Preparing images... May take a while depending on the number of files."
mkdir -p "$prepdir"

{
while read -r x;
do
	# Get the time from the first column.
	time="${x%%	*}"
	seconds="$(date '+%s' -d "$time")"
	# Duration is not used on the first looped item.
	duration="$((seconds - prevseconds))"

	# Get the filename/text content from the rest.
	content="${x#*	}"
	base="$(basename "$content")"
	base="${base%.*}.jpg"

	if [ -f "$content" ]; then
		# If images have already been made in a previous run, do not recreate
		# them unless -r was given.
		{ [ ! -f "$prepdir/$base" ] || [ -n "${redo+x}" ] ;} &&
			magick -size "${res:-1920x1080}" canvas:"${bgc:-black}" -gravity center "$content" -resize 1920x1080 -composite "$prepdir/$base"
	else
		{ [ ! -f "$prepdir/$base" ] || [ -n "${redo+x}" ] ;} &&
			magick -size "${res:-1920x1080}" -background "${bgc:-black}" -fill "${fgc:-white}" -font "${font:-Sans}" -pointsize "${ppt:-150}" -gravity center label:"$content" "$prepdir/$base"
	fi

	# If the first line, do not write yet.
	[ "$time" = "00:00:00" ] || echo "file '$prevbase'
duration $duration"

	# Keep the information required for the next file.
	prevbase="$base"
	prevtime="$time"
	prevseconds="$(date '+%s' -d "$prevtime")"
done < "$file"
# Do last file which must be given twice as follows
endtime="$((totseconds-seconds))"
echo "file '$base'
duration ${endtime:-5}
file '$base'"
} > "$prepfile"
if [ -n "${audio+x}" ]; then
	ffmpeg -hide_banner -y -f concat -safe 0 -i "$prepfile" -i "$audio" -c:a aac -vsync vfr -c:v libx264 -pix_fmt yuv420p "$outfile"
else
	ffmpeg -hide_banner -y -f concat -safe 0 -i "$prepfile" -vsync vfr -c:v libx264 -pix_fmt yuv420p "$outfile"
fi

# Might also try:
# -vf "fps=${fps:-24},format=yuv420p" "$outfile"
# but has given some problems.
```
---

echo "Hola, esto es una prueba. Este es el fin del año 2025. Chau." | wc -c

### Espeak aproximadamente lee 60 caracteres cada 5 segundos (para escribir el texto). Y espeak hace pausas con puntos y comas. O sea 90 caracteres si hay mucha puntuación 90 caracteres si es texto continuo.

#### 89 caracteres 5 segundos aproximadamente. Entonces cuando no llegas hace esto:

time espeak-ng -v es "Empecé al día comiendome un asadito que no cociné con lechuga y una ensalada de papas ja" - 5370ms

Usé eso para la regla de 3 simple de la función de vim (más abajo).



```bash
bc -l

89-51
38
89-55
34
```

Después tenes que hacer 90 caracteres son 5 segundos. Entonces los 38 caracteres que faltan serían 2,1 segundos por regla de 3 simple es decir 2100 milisegundos, y el otro 34 caracteres serían 1,8 segundos es decir 1800 milisegundos.

#### Ejemplo:

Empecé al día comiendome un asadito que no cociné con lechuga y una ensalada de papas ja. - 89 caracteres.
Acá están todos los cubiertos que tuve que limpiar. <break time='2100ms'/> - 51 caracteres.
Acá se puede apreciar como dejé todo limpio y ordenado. <break time='1800ms'/> - 55 caracteres.

#### Para tomar una pausa de 1 minuto `espeak -m -v mb-us1 "<speak>Hello, <break time='60s'/> this is a test.</speak>"`


Le pregunte a Claude y me dijo que se puede hacer todo con vim.

Definimos esta funcion en `.vimrc`.

# Ahora deje de usar esto estyo usando `generar_video.sh` de nobloatnews.

#### Esta es la que estoy usando ahora Y FUNCIONA MUY BIEN MUY SINCRONIZADO MEJOR QUE EL DE ABAJO.

```bash
:function! AddBreak()
:  let line = getline('.')
:  let len = strlen(line)
:  if len < 90 && line !~ '<break time='
:    let missing = 90 - len
:    let ms = (missing * 5370) / 90
:    call setline('.', line . " <break time='" . ms . "ms'/>")
:  endif
:endfunction
```

---

Y uso los scripts que están en el repo de nobloatnews.

```bash
:function! AddBreak()
:  let line = getline('.')
:  let len = strlen(line)
:  if line !~ '<break time='
:    " Calcular tiempo de habla (60ms por carácter)
:    let speech_time = len * 60
:    " El break debe completar 5000ms
:    let break_time = 5000 - speech_time
:    " Asegurar que el break no sea negativo
:    if break_time < 500
:      let break_time = 500
:    endif
:    call setline('.', line . " <break time='" . break_time . "ms'/>")
:  endif
:endfunction

```

Y ahora abrí el archivo del script y llama a esta funciona: `:%g/./call AddBreak()`

No se puede poner `<break time='5000ms'/>` solo tenes que agregar una palabra antes, no sé por qué.


---

Perfecto, con **Arch + Bash + Vim** se puede hacer algo *muy cómodo e interactivo* 👍
La idea correcta no es “medir en vivo” mientras escribes, sino:

👉 **tener una referencia fija de cuántas palabras ≈ 5 segundos**
👉 y que **Vim te marque visualmente** hasta dónde llegas.

Te propongo una solución **realista, rápida y usable en Vim**, sin hacks raros.

---

# 🧠 Idea general

1. Fijas velocidad de `espeak-ng`
2. Calculas **palabras ≈ 5 segundos**
3. En Vim:

   * un comando o mapping
   * que **resalte** las palabras que entran en 5 segundos
   * y te avise cuando te pasas

---

# 1️⃣ Fija velocidad de eSpeak

Ejemplo recomendado:

```bash
espeak-ng -v es -s 160
```

Haz una prueba larga y calcula:

```bash
time espeak-ng -v es -s 160 "$(cat texto.txt)"
wc -w texto.txt
```

Supongamos que obtienes:

```
8 palabras/segundo
```

➡️ **5 segundos ≈ 40 palabras**

---

# 2️⃣ Script Bash: marcar límite de palabras

Crea este script:

```bash
#!/bin/bash
# ~/bin/espeak_5s.sh

MAX=40

# texto hasta el cursor
texto=$(sed 's/\n/ /g')

contador=0
salida=""

for palabra in $texto; do
  contador=$((contador+1))
  salida="$salida $palabra"
  if [ $contador -ge $MAX ]; then
    break
  fi
done

echo "$salida"
```

Hazlo ejecutable:

```bash
chmod +x ~/bin/espeak_5s.sh
```

---

# 3️⃣ Integración con Vim (la parte importante 🔥)

### Opción A — Comando visual (recomendado)

En tu `~/.vimrc`:

```vim
command! Espeak5s call Espeak5s()
function! Espeak5s()
  let l:words = 40
  let l:text = getline(1, '$')->join(' ')
  let l:list = split(l:text)
  let l:limit = min([l:words, len(l:list)])

  " Limpiar highlight previo
  silent! call matchdelete(1)

  " Obtener posición del último word
  let l:pos = matchstrpos(l:text, join(l:list[:l:limit-1], ' '))[1]

  " Resaltar
  call matchadd('Visual', '\%' . (l:pos+1) . 'c.*')
endfunction
```

Usas en Vim:

```
:Espeak5s
```

✔️ Todo lo que **pase de 5s queda resaltado**
✔️ Tú escribes normalmente
✔️ Ejecutas cuando quieras

---

### Opción B — Mapping rápido

```vim
nnoremap <leader>5 :Espeak5s<CR>
```

Ahora solo presionas:

```
\5
```

---

# 4️⃣ Bonus: aviso en tiempo real (opcional)

Si quieres que **te avise mientras escribes**:

```vim
autocmd TextChanged,TextChangedI * call EspeakWarn()

function! EspeakWarn()
  let max = 40
  let count = len(split(join(getline(1,'$'))))
  if count > max
    echohl ErrorMsg | echo "⚠ Excedes 5 segundos de narración" | echohl None
  else
    echo "OK (" . count . "/" . max . " palabras)"
  endif
endfunction
```

---

# 🧩 Resultado final

✔️ Escribes normal en Vim
✔️ Sabes cuándo pasas de 5 segundos
✔️ No dependes de audio en tiempo real
✔️ Totalmente Bash + Vim + Arch-friendly 🐧

---

Si quieres, en el próximo mensaje puedo:

* Ajustar por **frases** en vez de palabras
* Usar **párrafos automáticos**
* O hacer un plugin Vim limpio (`autoload/`, `plugin/`)

Dime qué nivel de precisión necesitas 🎯


---

#### Subí el audio a YouTube y descargá los subtitulos para pegarlos con esto.

```bash
#!/bin/bash
# Script para añadir subtítulos SRT a un video
# Uso: ./add_subtitles.sh video.mp4 subtitulos.srt [salida.mp4] [estilo]

set -e

# Verificar argumentos
if [ $# -lt 2 ]; then
    echo "========================================"
    echo "Añadir Subtítulos a Video"
    echo "========================================"
    echo ""
    echo "Uso: $0 <video.mp4> <subtitulos.srt> [salida.mp4] [estilo]"
    echo ""
    echo "Estilos disponibles:"
    echo "  tiktok    - Estilo TikTok (grande, bold, amarillo)"
    echo "  instagram - Estilo Instagram (blanco con sombra)"
    echo "  youtube   - Estilo YouTube (blanco con fondo negro)"
    echo "  simple    - Estilo simple (blanco básico)"
    echo "  custom    - Personalizado (edita el script)"
    echo ""
    echo "Ejemplos:"
    echo ""
    echo "  # Estilo TikTok (default)"
    echo "  $0 mi_video.mp4 subtitulos.srt"
    echo ""
    echo "  # Estilo Instagram con nombre personalizado"
    echo "  $0 mi_video.mp4 subs.srt video_final.mp4 instagram"
    echo ""
    echo "  # Estilo YouTube"
    echo "  $0 clip.mp4 subtitulos.srt resultado.mp4 youtube"
    echo ""
    exit 1
fi

VIDEO="$1"
SUBTITLES="$2"
OUTPUT="${3:-${VIDEO%.*}_con_subs.mp4}"
STYLE="${4:-tiktok}"

# Verificar que los archivos existen
if [ ! -f "$VIDEO" ]; then
    echo "Error: El video '$VIDEO' no existe"
    exit 1
fi

if [ ! -f "$SUBTITLES" ]; then
    echo "Error: El archivo de subtítulos '$SUBTITLES' no existe"
    exit 1
fi

# Verificar ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "Error: ffmpeg no está instalado"
    exit 1
fi

echo "========================================"
echo "Añadiendo Subtítulos"
echo "========================================"
echo "Video: $VIDEO"
echo "Subtítulos: $SUBTITLES"
echo "Estilo: $STYLE"
echo "Salida: $OUTPUT"
echo ""

# Definir estilos de subtítulos
case "$STYLE" in
    tiktok)
        # Estilo TikTok: Grande, bold, amarillo con borde negro grueso
        SUBTITLE_STYLE="FontName=Arial,FontSize=28,PrimaryColour=&H00FFFF,OutlineColour=&H000000,BackColour=&H80000000,Bold=1,Outline=3,Shadow=0,MarginV=40,Alignment=2"
        echo "Aplicando estilo TikTok (amarillo, bold, grande)"
        ;;
    instagram)
        # Estilo Instagram: Blanco con sombra suave
        SUBTITLE_STYLE="FontName=Arial,FontSize=24,PrimaryColour=&H00FFFFFF,OutlineColour=&H000000,BackColour=&H80000000,Bold=1,Outline=2,Shadow=1,MarginV=50,Alignment=2"
        echo "Aplicando estilo Instagram (blanco con sombra)"
        ;;
    youtube)
        # Estilo YouTube: Blanco con fondo negro semi-transparente
        SUBTITLE_STYLE="FontName=Arial,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H000000,BackColour=&HCC000000,Bold=0,Outline=1,Shadow=0,MarginV=30,Alignment=2"
        echo "Aplicando estilo YouTube (blanco con fondo)"
        ;;
    simple)
        # Estilo simple: Blanco básico
        SUBTITLE_STYLE="FontName=Arial,FontSize=20,PrimaryColour=&H00FFFFFF,OutlineColour=&H000000,BackColour=&H80000000,Bold=0,Outline=2,Shadow=0,MarginV=20,Alignment=2"
        echo "Aplicando estilo simple (blanco básico)"
        ;;
    custom)
        # Personaliza aquí tu estilo
        SUBTITLE_STYLE="FontName=Arial,FontSize=26,PrimaryColour=&H0000FF00,OutlineColour=&H000000,BackColour=&H80000000,Bold=1,Outline=3,Shadow=1,MarginV=45,Alignment=2"
        echo "Aplicando estilo personalizado"
        ;;
    *)
        echo "Error: Estilo '$STYLE' no reconocido"
        echo "Usa: tiktok, instagram, youtube, simple, o custom"
        exit 1
        ;;
esac

echo ""
echo "Procesando video..."

# Escapar la ruta del archivo de subtítulos para ffmpeg
SUBTITLES_ESCAPED="${SUBTITLES//\\/\\\\}"
SUBTITLES_ESCAPED="${SUBTITLES_ESCAPED//:/\\:}"

# Aplicar subtítulos con el estilo seleccionado
ffmpeg -i "$VIDEO" \
    -vf "subtitles='${SUBTITLES_ESCAPED}':force_style='${SUBTITLE_STYLE}'" \
    -c:v libx264 \
    -preset medium \
    -crf 23 \
    -c:a copy \
    -y "$OUTPUT" \
    -loglevel error -stats

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "✓ Subtítulos añadidos exitosamente!"
    echo "========================================"
    echo "Archivo de salida: $OUTPUT"
    
    # Mostrar tamaño del archivo
    SIZE=$(du -h "$OUTPUT" | cut -f1)
    echo "Tamaño: $SIZE"
    
    # Mostrar duración
    DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$OUTPUT")
    echo "Duración: $(printf "%.2f" $DURATION) segundos"
else
    echo ""
    echo "✗ Error al añadir subtítulos"
    exit 1
fi

echo ""
echo "========================================"
echo "¡Listo para subir a redes sociales!"
echo "========================================"

```

---


#### Pasar del archivo de espeak con breaks a srt y quemarlo en el video.

```bash
#!/bin/bash
# Script TODO EN UNO: Convierte script a SRT y lo quema en el video
# Uso: ./auto_subs.sh video.mp4 script.txt [estilo] [duracion_base_ms]

set -e

# Verificar argumentos
if [ $# -lt 2 ]; then
    echo "========================================"
    echo "Video + Script = Video con Subtítulos"
    echo "========================================"
    echo ""
    echo "Uso: $0 <video.mp4> <script.txt> [estilo] [duracion_base_ms]"
    echo ""
    echo "Estilos:"
    echo "  tiktok    - Amarillo, grande, bold (default)"
    echo "  instagram - Blanco con sombra"
    echo "  youtube   - Blanco con fondo negro"
    echo "  simple    - Blanco básico"
    echo ""
    echo "Ejemplos:"
    echo ""
    echo "  # Estilo TikTok, 5370ms por línea"
    echo "  $0 mi_video.mp4 mi_script.txt"
    echo ""
    echo "  # Estilo Instagram, 5370ms por línea"
    echo "  $0 mi_video.mp4 mi_script.txt instagram"
    echo ""
    echo "  # Estilo TikTok, 4000ms por línea"
    echo "  $0 mi_video.mp4 mi_script.txt tiktok 4000"
    echo ""
    exit 1
fi

VIDEO="$1"
SCRIPT_FILE="$2"
STYLE="${3:-tiktok}"
BASE_DURATION="${4:-5370}"

# Verificar archivos
if [ ! -f "$VIDEO" ]; then
    echo "Error: El video '$VIDEO' no existe"
    exit 1
fi

if [ ! -f "$SCRIPT_FILE" ]; then
    echo "Error: El script '$SCRIPT_FILE' no existe"
    exit 1
fi

# Verificar ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "Error: ffmpeg no está instalado"
    exit 1
fi

# Nombres de archivos temporales y finales
TEMP_SRT="temp_subtitles.srt"
OUTPUT_VIDEO="${VIDEO%.*}_con_subs.mp4"

echo "========================================"
echo "🎬 Proceso Automático"
echo "========================================"
echo "Video: $VIDEO"
echo "Script: $SCRIPT_FILE"
echo "Estilo: $STYLE"
echo "Duración base: ${BASE_DURATION}ms"
echo "Salida: $OUTPUT_VIDEO"
echo ""

# PASO 1: Generar SRT desde el script
echo "========================================"
echo "PASO 1: Generando subtítulos SRT..."
echo "========================================"

# Limpiar archivo SRT
> "$TEMP_SRT"

LINE_NUM=0
CURRENT_TIME_MS=0

# Función para convertir milisegundos a formato SRT
ms_to_srt_time() {
    local total_ms=$1
    local hours=$((total_ms / 3600000))
    local minutes=$(((total_ms % 3600000) / 60000))
    local seconds=$(((total_ms % 60000) / 1000))
    local milliseconds=$((total_ms % 1000))
    
    printf "%02d:%02d:%02d,%03d" $hours $minutes $seconds $milliseconds
}

# Procesar cada línea del script
while IFS= read -r line || [ -n "$line" ]; do
    # Ignorar líneas vacías
    if [ -z "$(echo "$line" | tr -d '[:space:]')" ]; then
        continue
    fi
    
    LINE_NUM=$((LINE_NUM + 1))
    
    # Extraer el tiempo del break si existe
    if [[ "$line" =~ \<break\ time=\'([0-9]+)ms\'/\> ]]; then
        BREAK_TIME="${BASH_REMATCH[1]}"
        # Remover el tag de break del texto
        TEXT=$(echo "$line" | sed "s/<break time='[0-9]*ms'\/>.*//g" | sed 's/[[:space:]]*$//')
    else
        BREAK_TIME="$BASE_DURATION"
        TEXT="$line"
    fi
    
    # Calcular tiempos
    START_TIME_MS=$CURRENT_TIME_MS
    END_TIME_MS=$((CURRENT_TIME_MS + BASE_DURATION))
    
    # Convertir a formato SRT
    START_SRT=$(ms_to_srt_time $START_TIME_MS)
    END_SRT=$(ms_to_srt_time $END_TIME_MS)
    
    # Escribir al SRT
    echo "$LINE_NUM" >> "$TEMP_SRT"
    echo "$START_SRT --> $END_SRT" >> "$TEMP_SRT"
    echo "$TEXT" >> "$TEMP_SRT"
    echo "" >> "$TEMP_SRT"
    
    echo "  ✓ Línea $LINE_NUM: $TEXT"
    
    # Actualizar tiempo
    CURRENT_TIME_MS=$((END_TIME_MS + BREAK_TIME))
    
done < "$SCRIPT_FILE"

TOTAL_DURATION_MS=$CURRENT_TIME_MS
TOTAL_DURATION_S=$((TOTAL_DURATION_MS / 1000))

echo ""
echo "✓ SRT generado: $LINE_NUM subtítulos, ${TOTAL_DURATION_S}s totales"
echo ""

# PASO 2: Definir estilo de subtítulos
echo "========================================"
echo "PASO 2: Configurando estilo '$STYLE'..."
echo "========================================"

case "$STYLE" in
    tiktok)
        SUBTITLE_STYLE="FontName=Arial,FontSize=28,PrimaryColour=&H00FFFF,OutlineColour=&H000000,BackColour=&H80000000,Bold=1,Outline=3,Shadow=0,MarginV=40,Alignment=2"
        ;;
    instagram)
        SUBTITLE_STYLE="FontName=Arial,FontSize=24,PrimaryColour=&H00FFFFFF,OutlineColour=&H000000,BackColour=&H80000000,Bold=1,Outline=2,Shadow=1,MarginV=50,Alignment=2"
        ;;
    youtube)
        SUBTITLE_STYLE="FontName=Arial,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H000000,BackColour=&HCC000000,Bold=0,Outline=1,Shadow=0,MarginV=30,Alignment=2"
        ;;
    simple)
        SUBTITLE_STYLE="FontName=Arial,FontSize=20,PrimaryColour=&H00FFFFFF,OutlineColour=&H000000,BackColour=&H80000000,Bold=0,Outline=2,Shadow=0,MarginV=20,Alignment=2"
        ;;
    *)
        echo "Error: Estilo '$STYLE' no reconocido"
        rm -f "$TEMP_SRT"
        exit 1
        ;;
esac

echo "✓ Estilo configurado"
echo ""

# PASO 3: Quemar subtítulos en el video
echo "========================================"
echo "PASO 3: Quemando subtítulos en video..."
echo "========================================"
echo "Esto puede tardar varios minutos..."
echo ""

# Escapar ruta del SRT
TEMP_SRT_ESCAPED="${TEMP_SRT//\\/\\\\}"
TEMP_SRT_ESCAPED="${TEMP_SRT_ESCAPED//:/\\:}"

# Aplicar subtítulos
ffmpeg -i "$VIDEO" \
    -vf "subtitles='${TEMP_SRT_ESCAPED}':force_style='${SUBTITLE_STYLE}'" \
    -c:v libx264 \
    -preset medium \
    -crf 23 \
    -c:a copy \
    -y "$OUTPUT_VIDEO" \
    -loglevel error -stats

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "✓ ¡VIDEO COMPLETADO!"
    echo "========================================"
    echo ""
    echo "📹 Video final: $OUTPUT_VIDEO"
    
    # Información del archivo
    SIZE=$(du -h "$OUTPUT_VIDEO" | cut -f1)
    DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$OUTPUT_VIDEO" 2>/dev/null)
    
    echo "📊 Tamaño: $SIZE"
    if [ -n "$DURATION" ]; then
        MINUTES=$((${DURATION%.*} / 60))
        SECONDS=$((${DURATION%.*} % 60))
        echo "⏱️  Duración: ${MINUTES}m ${SECONDS}s"
    fi
    echo ""
    
    # Preguntar si eliminar SRT temporal
    read -p "¿Eliminar archivo SRT temporal? (s/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[SsYy]$ ]]; then
        rm -f "$TEMP_SRT"
        echo "✓ SRT temporal eliminado"
    else
        echo "📝 SRT guardado como: $TEMP_SRT"
    fi
    
    echo ""
    echo "========================================"
    echo "🎉 ¡Listo para subir a redes sociales!"
    echo "========================================"
else
    echo ""
    echo "✗ Error al quemar subtítulos"
    rm -f "$TEMP_SRT"
    exit 1
fi
```



### Nueva version de slider para que maneje bien la sincronizacion entre las imagenes en diferentes reproductores

```bash
#!/bin/sh

# Give a file with images and timecodes and creates a video slideshow of them.
#
# Timecodes must be in format 00:00:00.
#
# Imagemagick and ffmpeg required.

# Application cache if not stated elsewhere.
cache="${XDG_CACHE_HOME:-$HOME/.cache}/slider"

while getopts "hvrpi:c:a:o:d:f:t:e:x:s:" o; do case "${o}" in
	c) bgc="$OPTARG" ;;
	t) fgc="$OPTARG" ;;
	f) font="$OPTARG" ;;
	i) file="$OPTARG" ;;
	a) audio="$OPTARG" ;;
	o) outfile="$OPTARG" ;;
	d) prepdir="$OPTARG" ;;
	r) redo="$OPTARG" ;;
	s) ppt="$OPTARG" ;;
	e) endtime="$OPTARG" ;;
	x) res="$OPTARG"
		echo "$res" | grep -qv "^[0-9]\+x[0-9]\+$" &&
			echo "Resolution must be dimensions separated by a 'x': 1280x720, etc." &&
			exit 1 ;;
	p) echo "Purge old build files in $cache? [y/N]"
		read -r confirm
		echo "$confirm" | grep -iq "^y$" && rm -rf "$cache" && echo "Done."
		exit ;;
	v) verbose=True ;;
	*) echo "$(basename "$0") usage:
  -i  input timecode list (required)
  -a  audio file
  -c  color of background (use html names, black is default)
  -t  text color for text slides (white is default)
  -s  text font size for text slides (150 is default)
  -f  text font for text slides (sans serif is default)
  -o  output video file
  -e  if no audio given, the time in seconds that the last slide will be shown (5 is default)
  -x  resolution (1920x1080 is default)
  -d  tmp directory
  -r  rerun imagemagick commands even if done previously (in case files or background has changed)
  -p  purge old build files instead of running
  -v  be verbose" && exit 1

esac done

# Check that the input file looks like it should.
{ head -n 1 "$file" 2>/dev/null | grep -q "^00:00:00	" ;} || {
	echo "Give an input file with -i." &&
	echo "The file should look as this example:

00:00:00	first_image.jpg
00:00:03	otherdirectory/next_image.jpg
00:00:09	this_image_starts_at_9_seconds.jpg
etc...

Timecodes and filenames must be separated by Tabs." &&
	exit 1
	}

if [ -n "${audio+x}" ]; then
	# Check that the audio file looks like an actual audio file.
	case "$(file --dereference --brief --mime-type -- "$audio")" in
		audio/*) ;;
		*) echo "That doesn't look like an audio file."; exit 1 ;;
	esac
	totseconds="$(date '+%s' -d $(ffmpeg -i "$audio" 2>&1 | awk '/Duration/ {print $2}' | sed s/,//))"
fi

prepdir="${prepdir:-$cache/$file}"
outfile="${outfile:-$file.mp4}"
prepfile="$prepdir/$file.prep"

[ -n "${verbose+x}" ] && echo "Preparing images... May take a while depending on the number of files."
mkdir -p "$prepdir"

{
while read -r x;
do
	# Get the time from the first column.
	time="${x%%	*}"
	seconds="$(date '+%s' -d "$time")"
	# Duration is not used on the first looped item.
	duration="$((seconds - prevseconds))"

	# Get the filename/text content from the rest.
	content="${x#*	}"
	base="$(basename "$content")"
	base="${base%.*}.jpg"

	if [ -f "$content" ]; then
		# If images have already been made in a previous run, do not recreate
		# them unless -r was given.
		{ [ ! -f "$prepdir/$base" ] || [ -n "${redo+x}" ] ;} &&
			magick -size "${res:-1920x1080}" canvas:"${bgc:-black}" -gravity center "$content" -resize 1920x1080 -composite "$prepdir/$base"
	else
		{ [ ! -f "$prepdir/$base" ] || [ -n "${redo+x}" ] ;} &&
			magick -size "${res:-1920x1080}" -background "${bgc:-black}" -fill "${fgc:-white}" -font "${font:-Sans}" -pointsize "${ppt:-150}" -gravity center label:"$content" "$prepdir/$base"
	fi

	# If the first line, do not write yet.
	[ "$time" = "00:00:00" ] || echo "file '$prevbase'
duration $duration"

	# Keep the information required for the next file.
	prevbase="$base"
	prevtime="$time"
	prevseconds="$(date '+%s' -d "$prevtime")"
done < "$file"
# Do last file which must be given twice as follows
#
# Si el audio dura menos el tiempo que el video el endtime deberia ser 3.

longitud_audio_float=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $audio)
longitud_audio=$(printf "%.0f" $longitud_audio_float)

cantidad_imagenes=$(cat $file | wc -l)

## 3 segundos cada imagen
longitud_video=$((cantidad_imagenes*2))

endtime=""

((longitud_audio >= longitud_video)) && endtime="$((totseconds-seconds))"

((longitud_video > longitud_audio)) && endtime="2"

echo "file '$base'
duration ${endtime:-2}
file '$base'"
} > "$prepfile"
if [ -n "${audio+x}" ]; then
	ffmpeg -hide_banner -y -f concat -safe 0 -i "$prepfile" -i "$audio" -c:a aac -vsync cfr -c:v libx264 -pix_fmt yuv420p "$outfile"
else
	ffmpeg -hide_banner -y -f concat -safe 0 -i "$prepfile" -vsync cfr -c:v libx264 -pix_fmt yuv420p "$outfile"
fi

# Might also try:
# -vf "fps=${fps:-24},format=yuv420p" "$outfile"
# but has given some problems.

```
