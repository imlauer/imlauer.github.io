---
title: "Imgsearch: buscar imágenes desde la consola más rápido"
date: 2025-12-28T13:04:19-03:00
---
# Cortecía de Claude AI

```bash
#!/bin/bash
# img-search - Buscador simple de imágenes que SIEMPRE funciona
# Soporta múltiples motores sin JavaScript

set -e

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# Configuración
CACHE_DIR="$HOME/.cache/img-search"
mkdir -p "$CACHE_DIR"
W3M="w3m -o display_image=1 -o auto_image=1"

# Ayuda
show_help() {
    cat << EOF
${CYAN}img-search - Buscador universal de imágenes para consola${NC}

${GREEN}USO:${NC}
    img-search MOTOR "búsqueda" [opciones]

${GREEN}MOTORES:${NC}
    searx     - SearXNG local (localhost:8888)
    ddg       - DuckDuckGo Images (sin JS)
    ecosia    - Ecosia Images (sin JS)
    bing      - Bing Images (sin JS)
    qwant     - Qwant Images (sin JS)

${GREEN}OPCIONES:${NC}
    --list|-l       Listar URLs encontradas
    --download|-d   Descargar imágenes
    --urls|-u       Solo mostrar URLs (para pipes)
    --open|-o       Abrir en navegador (default)

${GREEN}EJEMPLOS:${NC}
    img-search ddg "gatos"
    img-search searx "wallpapers" --list
    img-search bing "linux logos" --download
    img-search ecosia "nature" --urls > urls.txt

${YELLOW}DEPENDENCIAS:${NC}
    w3m curl wget (opcional: jq para SearXNG)

EOF
}

# Función para extraer URLs de HTML
extract_urls_from_html() {
    local html="$1"
    
    # Múltiples patrones para capturar diferentes formatos
    grep -oE '(src|data-src|href)="https?://[^"]+\.(jpg|jpeg|png|gif|webp|svg)(\?[^"]*)?[^"]*"' "$html" | \
        sed 's/.*="\(.*\)"/\1/' | \
        grep -v '^//' | \
        grep -v 'data:image' | \
        sort -u || true
    
    # También buscar URLs sin comillas
    grep -oE 'https?://[^\s"<>()]+\.(jpg|jpeg|png|gif|webp)(\?[^\s"<>()]+)?' "$html" | \
        grep -v 'data:image' | \
        sort -u || true
}

# Validar argumentos
if [ $# -lt 2 ]; then
    show_help
    exit 1
fi

MOTOR="$1"
QUERY="$2"
MODE="${3:-open}"

# Validar motor
case "$MOTOR" in
    searx|ddg|ecosia|bing|qwant) ;;
    -h|--help|help)
        show_help
        exit 0
        ;;
    *)
        echo -e "${RED}Motor desconocido: $MOTOR${NC}"
        echo -e "${YELLOW}Usa: searx, ddg, ecosia, bing o qwant${NC}"
        exit 1
        ;;
esac

# Encode query
ENCODED=$(echo "$QUERY" | sed 's/ /%20/g' | sed 's/+/%2B/g')

# Construir URL según motor
case "$MOTOR" in
    searx)
        URL="http://localhost:8888/search?q=${ENCODED}&categories=images&format=json"
        USE_JSON=true
        ;;
    ddg)
        URL="https://duckduckgo.com/?q=${ENCODED}&iax=images&ia=images"
        USE_JSON=false
        ;;
    ecosia)
        URL="https://www.ecosia.org/images?q=${ENCODED}"
        USE_JSON=false
        ;;
    bing)
        URL="https://www.bing.com/images/search?q=${ENCODED}"
        USE_JSON=false
        ;;
    qwant)
        URL="https://www.qwant.com/?q=${ENCODED}&t=images"
        USE_JSON=false
        ;;
esac

# Banner
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}  Buscador de Imágenes - ${MOTOR^^}${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}Búsqueda:${NC} $QUERY"
echo -e "${GREEN}Motor:${NC}    $MOTOR"
echo -e ""

# Descargar resultados
CACHE_FILE="${CACHE_DIR}/${MOTOR}_$(echo $QUERY | tr ' ' '_').cache"

echo -e "${YELLOW}Descargando resultados...${NC}"
if $USE_JSON; then
    curl -s "$URL" > "$CACHE_FILE"
else
    curl -s -A "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0" "$URL" > "$CACHE_FILE"
fi

if [ ! -s "$CACHE_FILE" ]; then
    echo -e "${RED}Error: No se pudo descargar resultados${NC}"
    exit 1
fi

# Extraer URLs según el tipo
echo -e "${YELLOW}Extrayendo URLs...${NC}"

if $USE_JSON; then
    # SearXNG JSON
    if command -v jq &> /dev/null; then
        URLS=$(jq -r '.results[]? | select(.img_src != null) | .img_src' "$CACHE_FILE" 2>/dev/null | head -30)
        [ -z "$URLS" ] && URLS=$(jq -r '.results[]? | select(.thumbnail != null) | .thumbnail' "$CACHE_FILE" 2>/dev/null | head -30)
    else
        echo -e "${RED}Error: jq no está instalado (necesario para SearXNG)${NC}"
        echo -e "${YELLOW}Instala con: sudo pacman -S jq${NC}"
        exit 1
    fi
else
    # HTML parsing
    URLS=$(extract_urls_from_html "$CACHE_FILE")
fi

# Verificar si hay URLs
if [ -z "$URLS" ]; then
    echo -e "${RED}No se encontraron URLs de imágenes${NC}"
    echo -e "${YELLOW}Tip: Prueba con otro motor${NC}"
    echo -e "${YELLOW}Debug: cat $CACHE_FILE${NC}"
    exit 1
fi

NUM_URLS=$(echo "$URLS" | wc -l)
echo -e "${GREEN}✓ Encontradas $NUM_URLS URLs${NC}\n"

# Procesar según modo
case "$MODE" in
    --list|-l)
        echo -e "${CYAN}URLs encontradas:${NC}\n"
        echo "$URLS" | nl -w2 -s'. '
        ;;
    
    --urls|-u)
        echo "$URLS"
        ;;
    
    --download|-d)
        DOWNLOAD_DIR="${CACHE_DIR}/downloads/$(date +%Y%m%d_%H%M%S)_${QUERY// /_}"
        mkdir -p "$DOWNLOAD_DIR"
        
        echo -e "${CYAN}Descargando a: $DOWNLOAD_DIR${NC}\n"
        
        counter=1
        echo "$URLS" | while read url; do
            [ -z "$url" ] && continue
            
            ext="${url##*.}"
            ext="${ext%%\?*}"
            ext="${ext%%&*}"
            case "$ext" in
                jpg|jpeg|png|gif|webp|svg) ;;
                *) ext="jpg" ;;
            esac
            
            filename="${counter}.${ext}"
            echo -n "[$counter/$NUM_URLS] $filename ... "
            
            if timeout 10 wget -q --max-redirect=3 -U "Mozilla/5.0" \
                -O "${DOWNLOAD_DIR}/${filename}" "$url" 2>/dev/null; then
                
                # Verificar que sea imagen
                if file "${DOWNLOAD_DIR}/${filename}" 2>/dev/null | grep -qE "image|JPEG|PNG|GIF|WebP|SVG"; then
                    echo -e "${GREEN}✓${NC}"
                else
                    rm -f "${DOWNLOAD_DIR}/${filename}"
                    echo -e "${YELLOW}✗${NC}"
                fi
            else
                echo -e "${RED}✗${NC}"
            fi
            
            ((counter++))
        done
        
        DOWNLOADED=$(find "$DOWNLOAD_DIR" -type f 2>/dev/null | wc -l)
        echo -e "\n${GREEN}Descargadas: $DOWNLOADED imágenes${NC}"
        echo -e "${GREEN}Ubicación: $DOWNLOAD_DIR${NC}"
        
        if [ "$DOWNLOADED" -gt 0 ]; then
            echo -e "${YELLOW}Ver con: feh $DOWNLOAD_DIR/${NC}"
        else
            rmdir "$DOWNLOAD_DIR" 2>/dev/null
        fi
        ;;
    
    --open|-o|*)
        echo -e "${YELLOW}Abriendo en w3m... (Presiona 'q' para salir)${NC}\n"
        sleep 1
        $W3M "$URL"
        ;;
esac
```
