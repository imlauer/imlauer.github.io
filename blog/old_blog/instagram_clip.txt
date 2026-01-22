---
title: "Make Instagram clip"
date: 2025-12-28T01:45:04-03:00
---

```bash
#!/bin/bash

# Script para editar videos de streaming al estilo Instagram/TikTok
# Uso: ./edit_video.sh input.mp4 [inicio] [duracion]

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificar que ffmpeg esté instalado
if ! command -v ffmpeg &> /dev/null; then
    echo -e "${RED}Error: ffmpeg no está instalado${NC}"
    echo "Instala con: sudo pacman -S ffmpeg"
    exit 1
fi

# Función de ayuda
show_help() {
    echo "Uso: $0 <input.mp4> [inicio] [duracion] [opciones]"
    echo ""
    echo "Argumentos posicionales:"
    echo "  input.mp4    Video de entrada"
    echo "  inicio       Tiempo de inicio (formato: 00:05:30 o 330)"
    echo "  duracion     Duración del clip (formato: 00:00:30 o 30)"
    echo ""
    echo "Opciones:"
    echo "  -o, --output <nombre>     Nombre del archivo de salida"
    echo "  -r, --ratio <aspect>      Aspect ratio: 9:16 (vertical), 1:1 (cuadrado), 16:9 (horizontal)"
    echo "  -s, --speed <velocidad>   Velocidad: 0.5 (lento), 1.0 (normal), 2.0 (rápido)"
    echo "  -z, --zoom <factor>       Factor de zoom: 1.0-2.0"
    echo "  -b, --blur                Añadir blur en los bordes (letterbox)"
    echo "  -t, --text <texto>        Añadir texto/subtítulo"
    echo "  -f, --fade                Añadir fade in/out"
    echo "  -q, --quality <preset>    Preset de calidad: ultrafast, fast, medium, slow"
    echo "  -c, --compress            Comprimir para redes sociales"
    echo "  --vertical                Formato vertical (9:16) - shortcut"
    echo "  --square                  Formato cuadrado (1:1) - shortcut"
    echo "  -h, --help                Mostrar esta ayuda"
    echo ""
    echo "Ejemplos:"
    echo "  $0 stream.mp4 00:05:30 30 --vertical"
    echo "  $0 stream.mp4 330 30 -r 9:16 -s 1.5 -z 1.2 -f"
    echo "  $0 stream.mp4 0 60 --square -t \"Mi clip\" -b"
}

# Valores por defecto
INPUT=""
START_TIME="0"
DURATION=""
OUTPUT=""
ASPECT_RATIO="9:16"
SPEED="1.0"
ZOOM="1.0"
ADD_BLUR=false
TEXT=""
ADD_FADE=false
QUALITY="medium"
COMPRESS=false

# Parsear argumentos
POSITIONAL_ARGS=()
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -o|--output)
            OUTPUT="$2"
            shift 2
            ;;
        -r|--ratio)
            ASPECT_RATIO="$2"
            shift 2
            ;;
        -s|--speed)
            SPEED="$2"
            shift 2
            ;;
        -z|--zoom)
            ZOOM="$2"
            shift 2
            ;;
        -b|--blur)
            ADD_BLUR=true
            shift
            ;;
        -t|--text)
            TEXT="$2"
            shift 2
            ;;
        -f|--fade)
            ADD_FADE=true
            shift
            ;;
        -q|--quality)
            QUALITY="$2"
            shift 2
            ;;
        -c|--compress)
            COMPRESS=true
            shift
            ;;
        --vertical)
            ASPECT_RATIO="9:16"
            shift
            ;;
        --square)
            ASPECT_RATIO="1:1"
            shift
            ;;
        *)
            POSITIONAL_ARGS+=("$1")
            shift
            ;;
    esac
done

# Restaurar argumentos posicionales
set -- "${POSITIONAL_ARGS[@]}"

# Validar argumentos requeridos
if [ $# -lt 1 ]; then
    echo -e "${RED}Error: Se requiere al menos el archivo de entrada${NC}"
    show_help
    exit 1
fi

INPUT="$1"
[ $# -ge 2 ] && START_TIME="$2"
[ $# -ge 3 ] && DURATION="$3"

# Validar que el archivo existe
if [ ! -f "$INPUT" ]; then
    echo -e "${RED}Error: El archivo '$INPUT' no existe${NC}"
    exit 1
fi

# Generar nombre de salida si no se especificó
if [ -z "$OUTPUT" ]; then
    BASENAME=$(basename "$INPUT" | sed 's/\.[^.]*$//')
    OUTPUT="${BASENAME}_edited_$(date +%Y%m%d_%H%M%S).mp4"
fi

echo -e "${GREEN}=== Editor de Video FFmpeg ===${NC}"
echo "Input: $INPUT"
echo "Inicio: $START_TIME"
echo "Duración: ${DURATION:-"hasta el final"}"
echo "Output: $OUTPUT"
echo "Aspect Ratio: $ASPECT_RATIO"
echo "Velocidad: ${SPEED}x"
echo "Zoom: ${ZOOM}x"
echo ""

# Calcular dimensiones según aspect ratio
case $ASPECT_RATIO in
    9:16|vertical)
        WIDTH=1080
        HEIGHT=1920
        ;;
    1:1|square)
        WIDTH=1080
        HEIGHT=1080
        ;;
    16:9|horizontal)
        WIDTH=1920
        HEIGHT=1080
        ;;
    *)
        echo -e "${YELLOW}Advertencia: Aspect ratio no reconocido, usando 9:16${NC}"
        WIDTH=1080
        HEIGHT=1920
        ;;
esac

# Construir filtros de video
FILTERS=""

# 1. Ajustar velocidad si es necesario
if [ "$SPEED" != "1.0" ]; then
    FILTERS="${FILTERS}setpts=PTS/${SPEED},"
fi

# 2. Aplicar zoom si es necesario
if [ "$ZOOM" != "1.0" ]; then
    FILTERS="${FILTERS}scale=iw*${ZOOM}:ih*${ZOOM},crop=iw/${ZOOM}:ih/${ZOOM},"
fi

# 3. Blur en los bordes (efecto letterbox popular en Instagram)
if [ "$ADD_BLUR" = true ]; then
    FILTERS="${FILTERS}split[main][blur];[blur]scale=${WIDTH}:${HEIGHT}:force_original_aspect_ratio=increase,crop=${WIDTH}:${HEIGHT},boxblur=20:5[blurred];[blurred][main]overlay=(W-w)/2:(H-h)/2,"
else
    # Solo escalar y hacer crop
    FILTERS="${FILTERS}scale=${WIDTH}:${HEIGHT}:force_original_aspect_ratio=increase,crop=${WIDTH}:${HEIGHT},"
fi

# 4. Añadir fade in/out
if [ "$ADD_FADE" = true ]; then
    FADE_DURATION=1
    if [ -n "$DURATION" ]; then
        # Calcular duración en segundos si está en formato HH:MM:SS
        if [[ $DURATION =~ : ]]; then
            DUR_SEC=$(echo "$DURATION" | awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }')
        else
            DUR_SEC=$DURATION
        fi
        FILTERS="${FILTERS}fade=t=in:st=0:d=${FADE_DURATION},fade=t=out:st=$((DUR_SEC - FADE_DURATION)):d=${FADE_DURATION},"
    else
        FILTERS="${FILTERS}fade=t=in:st=0:d=${FADE_DURATION},"
    fi
fi

# 5. Añadir texto si se especificó
if [ -n "$TEXT" ]; then
    # Escapar caracteres especiales
    TEXT_ESCAPED=$(echo "$TEXT" | sed "s/:/\\\\:/g" | sed "s/'/\\\\'/g")
    FILTERS="${FILTERS}drawtext=fontfile=/usr/share/fonts/TTF/DejaVuSans-Bold.ttf:text='${TEXT_ESCAPED}':fontcolor=white:fontsize=48:box=1:boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/2:y=h-th-50,"
fi

# Remover la última coma
FILTERS="${FILTERS%,}"

# Construir comando ffmpeg
FFMPEG_CMD="ffmpeg -i \"$INPUT\""

# Añadir tiempo de inicio
if [ "$START_TIME" != "0" ]; then
    FFMPEG_CMD="$FFMPEG_CMD -ss $START_TIME"
fi

# Añadir duración
if [ -n "$DURATION" ]; then
    FFMPEG_CMD="$FFMPEG_CMD -t $DURATION"
fi

# Añadir filtros de video
if [ -n "$FILTERS" ]; then
    FFMPEG_CMD="$FFMPEG_CMD -vf \"$FILTERS\""
fi

# Ajustar audio a la velocidad
if [ "$SPEED" != "1.0" ]; then
    FFMPEG_CMD="$FFMPEG_CMD -af \"atempo=$SPEED\""
fi

# Configuración de encoding
if [ "$COMPRESS" = true ]; then
    # Optimizado para redes sociales
    FFMPEG_CMD="$FFMPEG_CMD -c:v libx264 -preset $QUALITY -crf 23 -c:a aac -b:a 128k -movflags +faststart"
else
    # Calidad alta
    FFMPEG_CMD="$FFMPEG_CMD -c:v libx264 -preset $QUALITY -crf 18 -c:a aac -b:a 192k -movflags +faststart"
fi

# Forzar framerate
FFMPEG_CMD="$FFMPEG_CMD -r 30"

# Output
FFMPEG_CMD="$FFMPEG_CMD \"$OUTPUT\""

# Mostrar comando
echo -e "${YELLOW}Ejecutando:${NC}"
echo "$FFMPEG_CMD" | sed 's/ -/\n  -/g'
echo ""

# Ejecutar
eval $FFMPEG_CMD

# Verificar resultado
if [ $? -eq 0 ]; then
    FILE_SIZE=$(du -h "$OUTPUT" | cut -f1)
    echo ""
    echo -e "${GREEN}✓ Video editado exitosamente!${NC}"
    echo "Archivo: $OUTPUT"
    echo "Tamaño: $FILE_SIZE"
    echo ""
    echo "Para ver el resultado:"
    echo "  mpv \"$OUTPUT\""
else
    echo -e "${RED}✗ Error al procesar el video${NC}"
    exit 1
fi
```
