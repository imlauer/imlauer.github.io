---
title: "Claude make short"
date: 2025-12-21T01:06:58-03:00
---

```bash
#!/bin/bash

# Script para dividir video horizontal en 4 cuadros verticales, concatenar segmentos y quemar subtítulos
# Uso: ./concat.sh "persona:inicio:duracion persona:inicio:duracion ..." video.mp4 [subtitulos.srt]

if [ $# -lt 2 ]; then
    echo "Uso: $0 \"segmentos\" video.mp4 [subtitulos.srt]"
    echo ""
    echo "Formato de segmentos: \"persona:inicio:duracion persona:inicio:duracion ...\""
    echo "  persona: 1-4 (de izquierda a derecha)"
    echo "  inicio: segundo de inicio"
    echo "  duracion: duración en segundos del corte"
    echo ""
    echo "Ejemplo SIN subtítulos:"
    echo "  $0 \"1:1140:3 3:1144:2\" video.mp4"
    echo ""
    echo "Ejemplo CON subtítulos:"
    echo "  $0 \"1:1140:3 3:1144:2\" video.mp4 subtitulos.srt"
    exit 1
fi

SEGMENTS="$1"
INPUT_VIDEO="$2"
INPUT_SRT="$3"
OUTPUT_VIDEO="output_vertical_$(date +%s).mp4"
TEMP_DIR="temp_segments_$$"

if [ ! -f "$INPUT_VIDEO" ]; then
    echo "Error: El archivo '$INPUT_VIDEO' no existe"
    exit 1
fi

USE_SUBTITLES=0
if [ -n "$INPUT_SRT" ]; then
    if [ ! -f "$INPUT_SRT" ]; then
        echo "Error: El archivo de subtítulos '$INPUT_SRT' no existe"
        exit 1
    fi
    USE_SUBTITLES=1
    echo "✓ Se quemarán subtítulos desde: $INPUT_SRT"
fi

# Verificar ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "Error: ffmpeg no está instalado"
    exit 1
fi

# Verificar bc
if ! command -v bc &> /dev/null; then
    echo "Error: bc no está instalado (necesario para cálculos)"
    exit 1
fi

echo "========================================"
echo "Cortador y Concatenador de Videos"
echo "========================================"
echo "Video: $INPUT_VIDEO"
echo "Segmentos: $SEGMENTS"
echo ""

# Crear directorio temporal
mkdir -p "$TEMP_DIR"

# Obtener dimensiones del video
echo "Analizando video..."
VIDEO_INFO=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "$INPUT_VIDEO")
WIDTH=$(echo "$VIDEO_INFO" | cut -d'x' -f1)
HEIGHT=$(echo "$VIDEO_INFO" | cut -d'x' -f2)

echo "Dimensiones originales: ${WIDTH}x${HEIGHT}"

# Calcular dimensiones de cada cuadro
QUAD_WIDTH=$((WIDTH / 4))
echo "Ancho de cada cuadro: ${QUAD_WIDTH}px"

# Dimensiones verticales para redes sociales (9:16)
VERTICAL_WIDTH=1080
VERTICAL_HEIGHT=1920

echo ""
echo "Formato de salida: ${VERTICAL_WIDTH}x${VERTICAL_HEIGHT} (9:16 - vertical)"
echo ""

# Función para convertir timestamp SRT a segundos
timestamp_to_seconds() {
    local timestamp="$1"
    local hours=$(echo "$timestamp" | cut -d':' -f1 | sed 's/^0*//')
    local minutes=$(echo "$timestamp" | cut -d':' -f2 | sed 's/^0*//')
    local seconds=$(echo "$timestamp" | cut -d':' -f3 | cut -d',' -f1 | sed 's/^0*//')
    local milliseconds=$(echo "$timestamp" | cut -d',' -f2 | sed 's/^0*//')
    
    [ -z "$hours" ] && hours=0
    [ -z "$minutes" ] && minutes=0
    [ -z "$seconds" ] && seconds=0
    [ -z "$milliseconds" ] && milliseconds=0
    
    echo "$hours * 3600 + $minutes * 60 + $seconds + $milliseconds / 1000" | bc -l
}

# Función para convertir segundos a timestamp SRT
seconds_to_timestamp() {
    local total_seconds="$1"
    
    if (( $(echo "$total_seconds < 0" | bc -l) )); then
        echo "00:00:00,000"
        return
    fi
    
    local hours=$(printf "%.0f" $(echo "$total_seconds / 3600" | bc -l))
    local remainder=$(echo "$total_seconds - ($hours * 3600)" | bc -l)
    local minutes=$(printf "%.0f" $(echo "$remainder / 60" | bc -l))
    local seconds_decimal=$(echo "$remainder - ($minutes * 60)" | bc -l)
    local secs_int=$(printf "%.0f" $(echo "$seconds_decimal" | bc -l))
    local milliseconds=$(printf "%.0f" $(echo "($seconds_decimal - $secs_int) * 1000" | bc -l))
    
    printf "%02d:%02d:%02d,%03d" "$hours" "$minutes" "$secs_int" "$milliseconds"
}

# Procesar segmentos y crear SRT ajustado si es necesario
segment_num=0
concat_file="$TEMP_DIR/concat_list.txt"
> "$concat_file"

if [ $USE_SUBTITLES -eq 1 ]; then
    ADJUSTED_SRT="$TEMP_DIR/adjusted_subtitles.srt"
    > "$ADJUSTED_SRT"
    subtitle_counter=1
    
    echo "Procesando subtítulos globalmente..."
    
    # Parsear todos los segmentos primero
    declare -a seg_starts
    declare -a seg_durations
    seg_count=0
    for seg in $SEGMENTS; do
        IFS=':' read -r p s d <<< "$seg"
        seg_starts[$seg_count]=$s
        seg_durations[$seg_count]=$d
        ((seg_count++))
    done
    
    # Procesar el SRT UNA SOLA VEZ y ELIMINAR SOLAPAMIENTOS
    in_subtitle=0
    current_offset=0
    current_text=""
    last_end_time=0
    
    while IFS= read -r line; do
        if [[ $line =~ ([0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3})\ --\>\ ([0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}) ]]; then
            start_ts="${BASH_REMATCH[1]}"
            end_ts="${BASH_REMATCH[2]}"
            
            start_sec=$(timestamp_to_seconds "$start_ts")
            end_sec=$(timestamp_to_seconds "$end_ts")
            
            # Buscar en qué segmento(s) cae este subtítulo
            current_offset=0
            found=0
            for ((i=0; i<seg_count; i++)); do
                seg_start=${seg_starts[$i]}
                seg_dur=${seg_durations[$i]}
                seg_end=$(echo "$seg_start + $seg_dur" | bc)
                
                # Si el subtítulo cruza este segmento
                if (( $(echo "$start_sec < $seg_end && $end_sec > $seg_start" | bc -l) )); then
                    new_start=$(echo "$start_sec - $seg_start + $current_offset" | bc -l)
                    new_end=$(echo "$end_sec - $seg_start + $current_offset" | bc -l)
                    
                    if (( $(echo "$new_start < $current_offset" | bc -l) )); then
                        new_start=$current_offset
                    fi
                    
                    # EVITAR SOLAPAMIENTO: Si empieza antes de que termine el anterior, ajustar
                    if (( $(echo "$new_start < $last_end_time" | bc -l) )); then
                        new_start=$last_end_time
                    fi
                    
                    if (( $(echo "$new_end > $new_start + 0.1" | bc -l) )); then
                        new_start_ts=$(seconds_to_timestamp "$new_start")
                        new_end_ts=$(seconds_to_timestamp "$new_end")
                        in_subtitle=1
                        found=1
                        current_text="$subtitle_counter
$new_start_ts --> $new_end_ts
"
                        ((subtitle_counter++))
                        last_end_time=$new_end
                        break
                    fi
                fi
                current_offset=$(echo "$current_offset + $seg_dur" | bc -l)
            done
            
            if [ $found -eq 0 ]; then
                in_subtitle=0
                current_text=""
            fi
        elif [ -n "$line" ]; then
            if [ $in_subtitle -eq 1 ] && [[ ! $line =~ ^[0-9]+$ ]]; then
                current_text="${current_text}${line}
"
            fi
        elif [ -z "$line" ] && [ $in_subtitle -eq 1 ]; then
            echo -n "$current_text" >> "$ADJUSTED_SRT"
            echo "" >> "$ADJUSTED_SRT"
            in_subtitle=0
            current_text=""
        fi
    done < "$INPUT_SRT"
    
    echo "✓ Subtítulos procesados (sin solapamientos)"
fi

# Arrays para guardar info de segmentos
declare -a segment_starts
declare -a segment_durations

for segment in $SEGMENTS; do
    IFS=':' read -r person start_time duration <<< "$segment"
    
    if [ "$person" -lt 1 ] || [ "$person" -gt 4 ]; then
        echo "Error: Persona debe estar entre 1 y 4"
        exit 1
    fi
    
    if [ "$duration" -le 0 ]; then
        echo "Error: Duración debe ser positiva (segmento: $segment)"
        exit 1
    fi
    
    segment_starts[$segment_num]=$start_time
    segment_durations[$segment_num]=$duration
    
    end_time=$(echo "$start_time + $duration" | bc)
    
    case $person in
        1) crop_x=0 ;;
        2) crop_x=$QUAD_WIDTH ;;
        3) crop_x=$((QUAD_WIDTH * 2)) ;;
        4) crop_x=$((QUAD_WIDTH * 3)) ;;
    esac
    
    output_segment="$TEMP_DIR/segment_${segment_num}.mp4"
    
    echo "----------------------------------------"
    echo "Segmento $((segment_num + 1)):"
    echo "  Persona: $person"
    echo "  Inicio: ${start_time}s | Duración: ${duration}s | Fin: ${end_time}s"
    echo "  Crop X: $crop_x"
    echo "  Procesando video..."
    
    # Construir filtro de video
    vf_filter="crop=${QUAD_WIDTH}:${HEIGHT}:${crop_x}:0,scale=${VERTICAL_WIDTH}:${VERTICAL_HEIGHT}:force_original_aspect_ratio=decrease,pad=${VERTICAL_WIDTH}:${VERTICAL_HEIGHT}:(ow-iw)/2:(oh-ih)/2:black,setsar=1"
    
    ffmpeg -y -ss "$start_time" -t "$duration" -i "$INPUT_VIDEO" \
        -vf "$vf_filter" \
        -c:v libx264 -preset fast -crf 18 \
        -c:a aac -b:a 192k \
        -movflags +faststart \
        "$output_segment" 2>&1 | grep -E "(time=|Duration|error|Error)" | tail -3 || true
    
    if [ $? -eq 0 ] && [ -f "$output_segment" ]; then
        file_size=$(stat -c%s "$output_segment" 2>/dev/null || stat -f%z "$output_segment" 2>/dev/null)
        if [ "$file_size" -gt 1000 ]; then
            echo "  ✓ Segmento creado (${file_size} bytes)"
            echo "file '$(basename "$output_segment")'" >> "$concat_file"
        else
            echo "  ✗ Error: Segmento vacío"
            exit 1
        fi
    else
        echo "  ✗ Error al crear segmento"
        exit 1
    fi
    
    ((segment_num++))
done

echo ""
echo "========================================"
echo "Concatenando $segment_num segmentos..."
echo "========================================"

if [ ! -s "$concat_file" ]; then
    echo "✗ Error: No hay segmentos para concatenar"
    exit 1
fi

# Concatenar segmentos
TEMP_OUTPUT="$TEMP_DIR/temp_concatenated.mp4"
cd "$TEMP_DIR"
ffmpeg -y -f concat -safe 0 -i "concat_list.txt" \
    -c copy \
    -movflags +faststart \
    "temp_concatenated.mp4" 2>&1 | grep -E "(time=|Duration|error|Error)" | tail -3 || true
cd ..

if [ ! -f "$TEMP_OUTPUT" ]; then
    echo "✗ Error al concatenar segmentos"
    exit 1
fi

# Quemar subtítulos si existen
if [ $USE_SUBTITLES -eq 1 ] && [ -f "$ADJUSTED_SRT" ]; then
    echo ""
    echo "========================================"
    echo "Quemando subtítulos..."
    echo "========================================"
    
    # Escapar ruta del SRT para ffmpeg
    ESCAPED_SRT=$(echo "$ADJUSTED_SRT" | sed 's/\\/\\\\/g; s/:/\\:/g; s/'\''/'\'\\\\\\\'\''/g')
    
    ffmpeg -y -i "$TEMP_OUTPUT" \
        -vf "subtitles='$ESCAPED_SRT':force_style='FontName=Arial,FontSize=11,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BackColour=&H99000000,BorderStyle=4,Outline=1,Shadow=0,MarginV=50,Alignment=2'" \
        -c:v libx264 -preset medium -crf 18 \
        -c:a copy \
        -movflags +faststart \
        "$OUTPUT_VIDEO" 2>&1 | grep -E "(time=|Duration|error|Error)" | tail -5 || true
else
    # Sin subtítulos, solo mover el archivo
    mv "$TEMP_OUTPUT" "$OUTPUT_VIDEO"
fi

if [ -f "$OUTPUT_VIDEO" ]; then
    echo ""
    echo "✓✓✓ VIDEO COMPLETADO ✓✓✓"
    echo "========================================"
    echo "Archivo: $OUTPUT_VIDEO"
    
    TOTAL_DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$OUTPUT_VIDEO" 2>/dev/null | cut -d'.' -f1)
    [ -n "$TOTAL_DURATION" ] && echo "Duración total: ${TOTAL_DURATION}s"
    
    FILE_SIZE=$(du -h "$OUTPUT_VIDEO" | cut -f1)
    echo "Tamaño: $FILE_SIZE"
    
    if [ $USE_SUBTITLES -eq 1 ]; then
        echo "✓ Subtítulos quemados en el video"
    fi
    
    echo ""
    echo "¿Eliminar archivos temporales? (S/n)"
    read -t 5 -r response || response="s"
    if [[ "$response" != "n" && "$response" != "N" ]]; then
        rm -rf "$TEMP_DIR"
        echo "✓ Archivos temporales eliminados"
    else
        echo "→ Temporales en: $TEMP_DIR"
        [ -f "$ADJUSTED_SRT" ] && echo "→ SRT ajustado: $ADJUSTED_SRT"
    fi
else
    echo "✗ Error al crear video final"
    exit 1
fi

echo ""
echo "¡Listo para subir a las redes! 🚀🔥"
```
