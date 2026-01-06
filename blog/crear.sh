#!/bin/sh
if [[ -z "$1" ]]; then
  echo "Uso: $0 commit_msg"
  exit;
fi

# Solo carpetas
tree -H '' -d -o index.html 

# Busca carpetas, ignora la carpeta actual, las carpetas ocultas 
find . -type d ! -path '*/.*' ! -path '.' | while read dir; do 
  (cd "$dir" && tree -r -I '*.md' -H '' -o index.html && sed -i '1i <a href="../index.html">⬆️ Subir</a><br><hr>' index.html)
done

#git add . && git commit -m "$1" && git push
