---
title: "Thumbnail imagemagick"
date: 2025-12-20T03:00:15-03:00
---
```bash
¡Excelente idea! Te voy a mostrar cómo crear un thumbnail atractivo para YouTube usando solo herramientas de línea de comandos. Voy a darte ejemplos con **ImageMagick** (convert/magick) que es perfecto para esto.

## Ejemplo 1: Thumbnail con múltiples imágenes y texto impactante

```bash
# Crear un collage de 2x2 con tus imágenes
magick montage imagen1.jpg imagen2.jpg imagen3.jpg imagen4.jpg \
  -tile 2x2 -geometry +5+5 -background black collage.jpg

# Añadir texto grande y llamativo
magick collage.jpg \
  -gravity north -pointsize 80 -font Arial-Bold \
  -stroke black -strokewidth 4 -fill yellow \
  -annotate +0+50 "¡INCREÍBLE!" \
  -gravity south -pointsize 60 -font Arial-Bold \
  -stroke white -strokewidth 3 -fill red \
  -annotate +0+50 "NO VAS A CREER ESTO" \
  thumbnail_final.jpg
```

## Ejemplo 2: Thumbnail estilo "reacción" con imagen principal y texto

```bash
# Redimensionar imagen principal a 1280x720 (tamaño YouTube)
magick imagen_principal.jpg -resize 1280x720^ -gravity center -extent 1280x720 base.jpg

# Añadir borde/viñeta dramático
magick base.jpg -vignette 0x20 base_vignette.jpg

# Añadir texto con sombra y efectos
magick base_vignette.jpg \
  -gravity center -pointsize 100 -font Impact \
  -stroke black -strokewidth 8 -fill white \
  -annotate +0-150 "¿QUÉ PASÓ?" \
  -pointsize 70 \
  -stroke navy -strokewidth 5 -fill cyan \
  -annotate +0+100 "😱 MIRA HASTA EL FINAL" \
  thumbnail_youtube.jpg
```

## Ejemplo 3: Thumbnail con imagen de fondo, foto pequeña y texto

```bash
# Crear fondo degradado
magick -size 1280x720 gradient:blue-purple fondo.jpg

# Añadir tu foto en una esquina (circular)
magick tu_foto.jpg -resize 300x300^ -gravity center -extent 300x300 \
  \( +clone -threshold -1 -negate -fill white -draw "circle 150,150 150,0" \) \
  -alpha off -compose copy_opacity -composite foto_circular.png

# Combinar todo
magick fondo.jpg \
  foto_circular.png -geometry +950+50 -composite \
  -gravity west -pointsize 90 -font Impact \
  -stroke black -strokewidth 6 -fill yellow \
  -annotate +50+0 "TOP 10\nMOMENTOS" \
  thumbnail_completo.jpg
```

## Ejemplo 4: Estilo "antes y después"

```bash
# Combinar dos imágenes lado a lado con flecha
magick \( antes.jpg -resize 600x720^ -extent 600x720 \) \
  \( despues.jpg -resize 600x720^ -extent 600x720 \) \
  +append temporal.jpg

# Añadir flecha y textos
magick temporal.jpg \
  -gravity northwest -pointsize 60 -fill white -stroke black -strokewidth 3 \
  -annotate +50+50 "ANTES" \
  -gravity northeast -pointsize 60 -fill lime -stroke black -strokewidth 3 \
  -annotate +50+50 "DESPUÉS" \
  -gravity center -pointsize 120 -fill red \
  -annotate +0+0 "➜" \
  antes_despues.jpg
```

## Consejos para texto llamativo:

**Fuentes populares para thumbnails:**
- Impact (clásica de memes)
- Arial-Bold
- Bebas (si la tienes instalada)

**Efectos de texto que funcionan:**
```bash
# Texto con borde grueso
-stroke black -strokewidth 8 -fill white

# Texto con sombra
-shadow 80x3+5+5

# Texto con degradado (requiere más pasos)
magick -size 800x200 gradient:red-yellow -font Impact -pointsize 100 \
  -gravity center -annotate +0+0 "TEXTO" texto_degradado.png
```

## Verificar las fuentes disponibles:

```bash
magick -list font | grep -i "font:"
```

## Tamaño ideal para YouTube:
- **1280x720 píxeles** (16:9)
- Mantén el texto en la zona segura (centro 80%)

¿Qué tipo de contenido es tu video? Te puedo dar un ejemplo más específico según tu temática (gaming, tutoriales, vlogs, etc.)
```

---

```bash
#!/bin/bash

# Generador de Thumbnails para YouTube
# Requiere ImageMagick instalado

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para mostrar el banner
show_banner() {
    echo -e "${BLUE}"
    echo "╔═══════════════════════════════════════════╗"
    echo "║   GENERADOR DE THUMBNAILS PARA YOUTUBE   ║"
    echo "╚═══════════════════════════════════════════╝"
    echo -e "${NC}"
}

# Verificar que ImageMagick esté instalado
check_imagemagick() {
    if ! command -v magick &> /dev/null && ! command -v convert &> /dev/null; then
        echo -e "${RED}Error: ImageMagick no está instalado.${NC}"
        echo "Instálalo con: sudo pacman -S imagemagick"
        exit 1
    fi
    
    # Usar 'magick' si está disponible, sino 'convert'
    if command -v magick &> /dev/null; then
        MAGICK="magick"
    else
        MAGICK="convert"
    fi
}

# Detectar fuente disponible para usar
detect_font() {
    # Lista de fuentes a probar en orden de preferencia
    local fonts=("Impact" "Arial-Bold" "Liberation-Sans-Bold" "DejaVu-Sans-Bold" "Roboto-Bold" "FreeSans-Bold")
    
    for font in "${fonts[@]}"; do
        if $MAGICK -list font | grep -qi "$font"; then
            FONT_BOLD="$font"
            echo -e "${GREEN}✓ Usando fuente: $FONT_BOLD${NC}"
            return 0
        fi
    done
    
    # Si no encuentra ninguna, usar la fuente por defecto
    echo -e "${YELLOW}⚠ No se encontró ninguna fuente preferida, usando fuente por defecto${NC}"
    FONT_BOLD=""
}

# Función para mostrar menú de estilos
show_styles() {
    echo -e "${YELLOW}Selecciona el estilo de thumbnail:${NC}"
    echo "1) Collage 2x2 con texto grande"
    echo "2) Imagen principal + texto central impactante"
    echo "3) Antes y después (2 imágenes lado a lado)"
    echo "4) Imagen de fondo + foto pequeña + texto"
    echo "5) Miniaturas múltiples en fila + texto"
    echo ""
    echo -e "${RED}═══ ESTILOS CLICKBAIT ═══${NC}"
    echo "6) 🔴 Círculo rojo + flecha señalando"
    echo "7) 😱 Cara de shock + texto exagerado"
    echo "8) ⚡ Comparación dramática con VS"
    echo "9) 🎯 Múltiples flechas y círculos"
    echo "10) 💥 Explosión de texto con efectos"
    echo ""
    read -p "Opción (1-10): " STYLE
}

# Función para crear collage 2x2
style_collage() {
    if [ ${#IMAGES[@]} -lt 4 ]; then
        echo -e "${RED}Error: Este estilo necesita al menos 4 imágenes${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Creando collage 2x2...${NC}"
    
    # Crear collage
    $MAGICK montage "${IMAGES[0]}" "${IMAGES[1]}" "${IMAGES[2]}" "${IMAGES[3]}" \
        -tile 2x2 -geometry 640x360+5+5 -background black temp_collage.jpg
    
    # Redimensionar a tamaño YouTube
    $MAGICK temp_collage.jpg -resize 1280x720! temp_base.jpg
    
    # Añadir texto
    $MAGICK temp_base.jpg \
        -gravity north -pointsize 90 ${FONT_BOLD:+-font "$FONT_BOLD"} \
        -stroke black -strokewidth 6 -fill "$TEXT_COLOR" \
        -annotate +0+30 "$TEXT_TOP" \
        -gravity south -pointsize 70 ${FONT_BOLD:+-font "$FONT_BOLD"} \
        -stroke black -strokewidth 5 -fill yellow \
        -annotate +0+30 "$TEXT_BOTTOM" \
        "$OUTPUT"
    
    rm temp_collage.jpg temp_base.jpg
}

# Función para imagen principal + texto
style_main_image() {
    if [ ${#IMAGES[@]} -lt 1 ]; then
        echo -e "${RED}Error: Este estilo necesita al menos 1 imagen${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Creando thumbnail con imagen principal...${NC}"
    
    # Preparar imagen base
    $MAGICK "${IMAGES[0]}" -resize 1280x720^ -gravity center -extent 1280x720 temp_base.jpg
    
    # Añadir viñeta
    $MAGICK temp_base.jpg -vignette 0x20 temp_vignette.jpg
    
    # Añadir textos
    $MAGICK temp_vignette.jpg \
        -gravity center -pointsize 110 ${FONT_BOLD:+-font "$FONT_BOLD"} \
        -stroke black -strokewidth 8 -fill "$TEXT_COLOR" \
        -annotate +0-150 "$TEXT_TOP" \
        -pointsize 80 -fill yellow -stroke black -strokewidth 6 \
        -annotate +0+100 "$TEXT_BOTTOM" \
        "$OUTPUT"
    
    rm temp_base.jpg temp_vignette.jpg
}

# Función para antes y después
style_before_after() {
    if [ ${#IMAGES[@]} -lt 2 ]; then
        echo -e "${RED}Error: Este estilo necesita al menos 2 imágenes${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Creando thumbnail antes/después...${NC}"
    
    # Preparar imágenes
    $MAGICK "${IMAGES[0]}" -resize 600x720^ -gravity center -extent 600x720 temp_antes.jpg
    $MAGICK "${IMAGES[1]}" -resize 600x720^ -gravity center -extent 600x720 temp_despues.jpg
    
    # Combinar lado a lado
    $MAGICK temp_antes.jpg temp_despues.jpg +append temp_combined.jpg
    
    # Añadir textos y flecha
    $MAGICK temp_combined.jpg \
        -gravity northwest -pointsize 70 ${FONT_BOLD:+-font "$FONT_BOLD"} \
        -stroke black -strokewidth 4 -fill white \
        -annotate +30+30 "ANTES" \
        -gravity northeast -pointsize 70 ${FONT_BOLD:+-font "$FONT_BOLD"} \
        -stroke black -strokewidth 4 -fill lime \
        -annotate +30+30 "DESPUÉS" \
        -gravity center -pointsize 150 -fill red -stroke black -strokewidth 5 \
        -annotate +0+0 "→" \
        -gravity north -pointsize 90 -fill yellow -stroke black -strokewidth 6 \
        -annotate +0+600 "$TEXT_TOP" \
        "$OUTPUT"
    
    rm temp_antes.jpg temp_despues.jpg temp_combined.jpg
}

# Función para fondo + foto pequeña
style_background_photo() {
    if [ ${#IMAGES[@]} -lt 2 ]; then
        echo -e "${RED}Error: Este estilo necesita al menos 2 imágenes (fondo + foto)${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Creando thumbnail con fondo y foto...${NC}"
    
    # Preparar fondo
    $MAGICK "${IMAGES[0]}" -resize 1280x720^ -gravity center -extent 1280x720 temp_fondo.jpg
    
    # Oscurecer fondo un poco
    $MAGICK temp_fondo.jpg -brightness-contrast -20x10 temp_fondo_dark.jpg
    
    # Preparar foto circular
    $MAGICK "${IMAGES[1]}" -resize 350x350^ -gravity center -extent 350x350 temp_foto.jpg
    $MAGICK temp_foto.jpg \
        \( +clone -threshold -1 -negate -fill white -draw "circle 175,175 175,0" \) \
        -alpha off -compose copy_opacity -composite \
        -bordercolor white -border 8 \
        temp_foto_circular.png
    
    # Combinar todo
    $MAGICK temp_fondo_dark.jpg \
        temp_foto_circular.png -geometry +900+50 -composite \
        -gravity west -pointsize 100 ${FONT_BOLD:+-font "$FONT_BOLD"} \
        -stroke black -strokewidth 7 -fill "$TEXT_COLOR" \
        -annotate +40+0 "$TEXT_TOP" \
        -gravity southwest -pointsize 70 -fill yellow -stroke black -strokewidth 5 \
        -annotate +40+40 "$TEXT_BOTTOM" \
        "$OUTPUT"
    
    rm temp_fondo.jpg temp_fondo_dark.jpg temp_foto.jpg temp_foto_circular.png
}

# Función para miniaturas en fila
style_thumbnails_row() {
    if [ ${#IMAGES[@]} -lt 3 ]; then
        echo -e "${RED}Error: Este estilo necesita al menos 3 imágenes${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Creando thumbnail con miniaturas en fila...${NC}"
    
    # Crear fondo degradado
    $MAGICK -size 1280x720 gradient:blue-purple temp_fondo.jpg
    
    # Preparar miniaturas (máximo 4)
    NUM_IMAGES=$(( ${#IMAGES[@]} < 4 ? ${#IMAGES[@]} : 4 ))
    THUMB_WIDTH=$((1200 / NUM_IMAGES))
    
    for i in $(seq 0 $(($NUM_IMAGES - 1))); do
        $MAGICK "${IMAGES[$i]}" -resize ${THUMB_WIDTH}x400^ -gravity center -extent ${THUMB_WIDTH}x400 \
            -bordercolor white -border 5 temp_thumb_$i.jpg
    done
    
    # Combinar miniaturas horizontalmente
    $MAGICK temp_thumb_*.jpg +append temp_row.jpg
    
    # Combinar con fondo y añadir texto
    $MAGICK temp_fondo.jpg \
        temp_row.jpg -geometry +40+250 -composite \
        -gravity north -pointsize 110 ${FONT_BOLD:+-font "$FONT_BOLD"} \
        -stroke black -strokewidth 8 -fill "$TEXT_COLOR" \
        -annotate +0+30 "$TEXT_TOP" \
        -gravity south -pointsize 70 -fill yellow -stroke black -strokewidth 6 \
        -annotate +0+30 "$TEXT_BOTTOM" \
        "$OUTPUT"
    
    rm temp_fondo.jpg temp_row.jpg temp_thumb_*.jpg
}

# ESTILOS CLICKBAIT

# Función para círculo rojo + flecha
style_red_circle_arrow() {
    if [ ${#IMAGES[@]} -lt 1 ]; then
        echo -e "${RED}Error: Este estilo necesita al menos 1 imagen${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Creando thumbnail CLICKBAIT con círculo rojo...${NC}"
    
    # Preparar imagen base
    $MAGICK "${IMAGES[0]}" -resize 1280x720^ -gravity center -extent 1280x720 temp_base.jpg
    
    # Posición del círculo
    echo -e "${YELLOW}¿Dónde poner el círculo? (izquierda/derecha/centro) [derecha]:${NC}"
    read -p "> " CIRCLE_POS
    CIRCLE_POS=${CIRCLE_POS:-derecha}
    
    case ${CIRCLE_POS,,} in
        izquierda) CIRCLE_X=250; ARROW_START=450; ARROW_END=350 ;;
        centro) CIRCLE_X=640; ARROW_START=440; ARROW_END=640 ;;
        *) CIRCLE_X=1000; ARROW_START=800; ARROW_END=950 ;;
    esac
    
    # Añadir círculo rojo grueso + flecha + texto
    $MAGICK temp_base.jpg \
        -fill none -stroke red -strokewidth 12 \
        -draw "circle $CIRCLE_X,360 $((CIRCLE_X+100)),360" \
        -fill none -stroke yellow -strokewidth 15 \
        -draw "line $ARROW_START,200 $ARROW_END,320" \
        -draw "line $ARROW_END,320 $((ARROW_END-30)),280" \
        -draw "line $ARROW_END,320 $((ARROW_END-30)),360" \
        -gravity north -pointsize 100 ${FONT_BOLD:+-font "$FONT_BOLD"} \
        -stroke black -strokewidth 8 -fill red \
        -annotate +0+30 "$TEXT_TOP" \
        -gravity south -pointsize 80 -fill yellow -stroke black -strokewidth 6 \
        -annotate +0+30 "$TEXT_BOTTOM" \
        -gravity northeast -pointsize 60 -fill white -stroke red -strokewidth 4 \
        -annotate +20+20 "¡MIRA ESTO!" \
        "$OUTPUT"
    
    rm temp_base.jpg
}

# Función para cara de shock
style_shocked_face() {
    if [ ${#IMAGES[@]} -lt 2 ]; then
        echo -e "${RED}Error: Este estilo necesita 2 imágenes (fondo + tu cara)${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Creando thumbnail con CARA DE SHOCK...${NC}"
    
    # Preparar fondo
    $MAGICK "${IMAGES[0]}" -resize 1280x720^ -gravity center -extent 1280x720 temp_fondo.jpg
    
    # Oscurecer y saturar el fondo para más drama
    $MAGICK temp_fondo.jpg -brightness-contrast -30x20 -modulate 100,150,100 temp_fondo_dramatic.jpg
    
    # Preparar foto de cara (grande y circular)
    $MAGICK "${IMAGES[1]}" -resize 450x450^ -gravity center -extent 450x450 temp_cara.jpg
    $MAGICK temp_cara.jpg \
        \( +clone -threshold -1 -negate -fill white -draw "circle 225,225 225,0" \) \
        -alpha off -compose copy_opacity -composite \
        -bordercolor yellow -border 10 \
        temp_cara_circular.png
    
    # Añadir cara + texto exagerado + elementos clickbait
    $MAGICK temp_fondo_dramatic.jpg \
        temp_cara_circular.png -geometry +50+120 -composite \
        -gravity northeast -pointsize 120 ${FONT_BOLD:+-font "$FONT_BOLD"} \
        -stroke black -strokewidth 10 -fill red \
        -annotate +30+50 "$TEXT_TOP" \
        -gravity east -pointsize 90 -fill yellow -stroke black -strokewidth 7 \
        -annotate +30+200 "$TEXT_BOTTOM" \
        -gravity southeast -pointsize 70 -fill white -stroke red -strokewidth 5 \
        -annotate +30+30 "😱 NO LO VAS\nA CREER" \
        -fill none -stroke red -strokewidth 15 \
        -draw "circle 950,300 1050,300" \
        "$OUTPUT"
    
    rm temp_fondo.jpg temp_fondo_dramatic.jpg temp_cara.jpg temp_cara_circular.png
}

# Función para VS dramático
style_dramatic_vs() {
    if [ ${#IMAGES[@]} -lt 2 ]; then
        echo -e "${RED}Error: Este estilo necesita 2 imágenes${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Creando thumbnail VS DRAMÁTICO...${NC}"
    
    # Preparar imágenes con efectos diferentes
    $MAGICK "${IMAGES[0]}" -resize 580x720^ -gravity center -extent 580x720 \
        -modulate 100,80,100 temp_lado1.jpg
    $MAGICK "${IMAGES[1]}" -resize 580x720^ -gravity center -extent 580x720 \
        -modulate 100,120,100 temp_lado2.jpg
    
    # Crear rayo divisor
    $MAGICK -size 120x720 plasma:fractal temp_lightning.jpg
    $MAGICK temp_lightning.jpg -colorspace gray -brightness-contrast 30x50 \
        -fill yellow -tint 100 temp_lightning_yellow.jpg
    
    # Combinar con el rayo en medio
    $MAGICK temp_lado1.jpg temp_lightning_yellow.jpg temp_lado2.jpg +append temp_combined.jpg
    
    # Añadir VS gigante y textos
    $MAGICK temp_combined.jpg \
        -gravity center -pointsize 200 ${FONT_BOLD:+-font "$FONT_BOLD"} \
        -stroke black -strokewidth 15 -fill red \
        -annotate +0+0 "VS" \
        -gravity northwest -pointsize 80 -fill yellow -stroke black -strokewidth 6 \
        -annotate +30+30 "ESTO" \
        -gravity northeast -pointsize 80 -fill cyan -stroke black -strokewidth 6 \
        -annotate +30+30 "vs ESTO" \
        -gravity north -pointsize 90 -fill white -stroke red -strokewidth 7 \
        -annotate +0+600 "$TEXT_TOP" \
        -gravity south -pointsize 70 -fill lime -stroke black -strokewidth 5 \
        -annotate +0+30 "¿CUÁL ES MEJOR?" \
        "$OUTPUT"
    
    rm temp_lado1.jpg temp_lado2.jpg temp_lightning.jpg temp_lightning_yellow.jpg temp_combined.jpg
}

# Función para múltiples flechas y círculos
style_multiple_arrows() {
    if [ ${#IMAGES[@]} -lt 1 ]; then
        echo -e "${RED}Error: Este estilo necesita al menos 1 imagen${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Creando thumbnail con MÚLTIPLES INDICADORES...${NC}"
    
    # Preparar imagen base
    $MAGICK "${IMAGES[0]}" -resize 1280x720^ -gravity center -extent 1280x720 temp_base.jpg
    
    # Aumentar saturación para más impacto
    $MAGICK temp_base.jpg -modulate 100,140,100 temp_saturated.jpg
    
    # Añadir múltiples círculos rojos, flechas y efectos
    $MAGICK temp_saturated.jpg \
        -fill none -stroke red -strokewidth 12 \
        -draw "circle 300,250 380,250" \
        -draw "circle 950,400 1030,400" \
        -draw "circle 640,500 700,500" \
        -stroke yellow -strokewidth 15 \
        -draw "line 500,150 350,220" \
        -draw "line 350,220 380,190" \
        -draw "line 350,220 380,250" \
        -draw "line 800,250 920,370" \
        -draw "line 920,370 890,350" \
        -draw "line 920,370 900,400" \
        -gravity north -pointsize 110 ${FONT_BOLD:+-font "$FONT_BOLD"} \
        -stroke black -strokewidth 10 -fill red \
        -annotate +0+20 "$TEXT_TOP" \
        -gravity south -pointsize 80 -fill yellow -stroke black -strokewidth 7 \
        -annotate +0+30 "$TEXT_BOTTOM" \
        -gravity northwest -pointsize 50 -fill white -stroke red -strokewidth 3 \
        -annotate +20+20 "🔥 VIRAL" \
        -gravity northeast -pointsize 50 -fill lime -stroke black -strokewidth 3 \
        -annotate +20+20 "¡WOW!" \
        "$OUTPUT"
    
    rm temp_base.jpg temp_saturated.jpg
}

# Función para explosión de texto
style_text_explosion() {
    if [ ${#IMAGES[@]} -lt 1 ]; then
        echo -e "${RED}Error: Este estilo necesita al menos 1 imagen${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Creando thumbnail con EXPLOSIÓN DE TEXTO...${NC}"
    
    # Preparar imagen base oscurecida
    $MAGICK "${IMAGES[0]}" -resize 1280x720^ -gravity center -extent 1280x720 temp_base.jpg
    $MAGICK temp_base.jpg -brightness-contrast -35x15 temp_dark.jpg
    
    # Crear efecto de explosión con formas
    $MAGICK temp_dark.jpg \
        -fill "rgba(255,255,0,0.3)" -stroke yellow -strokewidth 5 \
        -draw "polygon 640,100 680,200 780,220 700,300 720,400 640,350 560,400 580,300 500,220 600,200" \
        temp_explosion.jpg
    
    # Añadir textos en múltiples ángulos para efecto dinámico
    $MAGICK temp_explosion.jpg \
        -gravity center -pointsize 130 ${FONT_BOLD:+-font "$FONT_BOLD"} \
        -stroke black -strokewidth 12 -fill red \
        -annotate +0-100 "$TEXT_TOP" \
        -pointsize 90 -fill yellow -stroke black -strokewidth 8 \
        -annotate +0+100 "$TEXT_BOTTOM" \
        -gravity northwest -pointsize 60 -fill white -stroke red -strokewidth 4 \
        -annotate +30+30 "😱" \
        -gravity northeast -pointsize 60 -fill lime -stroke black -strokewidth 4 \
        -annotate +30+30 "🔥" \
        -gravity southwest -pointsize 70 -fill cyan -stroke black -strokewidth 5 \
        -annotate +30+30 "¡ÉPICO!" \
        -gravity southeast -pointsize 70 -fill magenta -stroke black -strokewidth 5 \
        -annotate +30+30 "100% REAL" \
        -gravity north -pointsize 50 -fill white -stroke red -strokewidth 3 \
        -annotate +0+20 "⚠️ ADVERTENCIA ⚠️" \
        "$OUTPUT"
    
    rm temp_base.jpg temp_dark.jpg temp_explosion.jpg
}

# Función principal
main() {
    show_banner
    check_imagemagick
    detect_font
    
    # Solicitar imágenes
    echo -e "${YELLOW}Ingresa las rutas de las imágenes (separadas por espacio):${NC}"
    read -p "> " -a IMAGES
    
    # Verificar que existan las imágenes
    for img in "${IMAGES[@]}"; do
        if [ ! -f "$img" ]; then
            echo -e "${RED}Error: No se encuentra la imagen: $img${NC}"
            exit 1
        fi
    done
    
    echo -e "${GREEN}✓ ${#IMAGES[@]} imagen(es) cargada(s)${NC}"
    echo ""
    
    # Seleccionar estilo
    show_styles
    
    # Solicitar textos
    echo ""
    echo -e "${YELLOW}Texto superior (línea principal):${NC}"
    read -p "> " TEXT_TOP
    
    echo -e "${YELLOW}Texto inferior (opcional, presiona Enter para omitir):${NC}"
    read -p "> " TEXT_BOTTOM
    
    # Color del texto principal
    echo -e "${YELLOW}Color del texto principal (rojo/azul/verde/blanco/amarillo) [blanco]:${NC}"
    read -p "> " COLOR_INPUT
    case ${COLOR_INPUT,,} in
        rojo) TEXT_COLOR="red" ;;
        azul) TEXT_COLOR="blue" ;;
        verde) TEXT_COLOR="lime" ;;
        amarillo) TEXT_COLOR="yellow" ;;
        *) TEXT_COLOR="white" ;;
    esac
    
    # Nombre del archivo de salida
    echo -e "${YELLOW}Nombre del archivo de salida [thumbnail.jpg]:${NC}"
    read -p "> " OUTPUT
    OUTPUT=${OUTPUT:-thumbnail.jpg}
    
    echo ""
    echo -e "${BLUE}Generando thumbnail...${NC}"
    
    # Ejecutar el estilo seleccionado
    case $STYLE in
        1) style_collage ;;
        2) style_main_image ;;
        3) style_before_after ;;
        4) style_background_photo ;;
        5) style_thumbnails_row ;;
        6) style_red_circle_arrow ;;
        7) style_shocked_face ;;
        8) style_dramatic_vs ;;
        9) style_multiple_arrows ;;
        10) style_text_explosion ;;
        *) echo -e "${RED}Opción inválida${NC}"; exit 1 ;;
    esac
    
    echo ""
    echo -e "${GREEN}✓ ¡Thumbnail generado exitosamente!${NC}"
    echo -e "${BLUE}Archivo: $OUTPUT${NC}"
    echo -e "${BLUE}Tamaño: 1280x720 (ideal para YouTube)${NC}"
}

# Ejecutar script
main
```
