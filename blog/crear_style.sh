#!/bin/sh

if [[ -z "$1" ]]; then
  echo "Uso: $0 commit_msg"
  exit
fi

# =========================
# ROOT: solo carpetas
# =========================
tree -H '' -d -o index.html

# agrega style.css al index root
sed -i 's|</head>|<link rel="stylesheet" href="../style.css">\n</head>|' index.html
sed -i '1i <a href="../index.html">⬆️ Subir</a><br><hr>' index.html

# =========================
# SUBCARPETAS
# =========================
find . -type d ! -path '*/.*' ! -path '.' | while read dir; do
  (
    cd "$dir" || exit
    tree -r -I '*.md' -H '' -o index.html

    # link a style.css (un nivel arriba)
    sed -i 's|</head>|<link rel="stylesheet" href="../../style.css">\n</head>|' index.html

    # boton subir
    sed -i '1i <a href="../index.html">⬆️ Subir</a><br><hr>' index.html
  )
done

