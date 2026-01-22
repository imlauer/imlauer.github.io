#!/bin/sh
# Este script genera el index.html y lo sube a w10.site 

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
sed -i '1i <a href="../index.html">⬆️  Up</a><br><hr>' index.html

tree -r  -H '' -o index.html

sed -i 's|</head>|<link rel="stylesheet" href="../../style.css">\n</head>|' index.html

# =========================
# SUBCARPETAS
# =========================
## boton subir
#sed -i '1i <a href="../index.html">⬆️  Up</a><br><hr>' index.html
#
#find . -type d ! -path '*/.*' ! -path '.' | while read dir; do
#  (
#    cd "$dir" || exit
#    #tree -r -I '*.md' -H '' -o index.html
#    tree -r  -H '' -o index.html
#
#    # link a style.css (un nivel arriba)
#    sed -i 's|</head>|<link rel="stylesheet" href="../../style.css">\n</head>|' index.html
#
#    # boton subir
#    sed -i '1i <a href="../index.html">⬆️  Up</a><br><hr>' index.html
#  )
#done


NAME="MI_BLOG$(date +%s-$$)"
echo "https://archive.org/details/$NAME" | tee -a BACKUPS.txt
mv ZZZALL_FILES.zip /tmp
zip -r ZZZALL_FILES.zip . &&
source $HOME/internetarchive/bin/activate &&
ia upload "$NAME" ZZZALL_FILES.zip &&
cd $HOME/projects/imlauer.github.io && bash up.sh $1
cp * $HOME/projects/imlauer.w10.site/
cd $HOME/projects/ && bash subir_w10.sh


