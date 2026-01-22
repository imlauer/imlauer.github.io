---
title: "Bash: Cómo chequear multiples condiciones en un IF"
date: 2025-01-30T11:25:06-03:00
tags: ['scripting']
---
```
#!/bin/bash
if [[ -z $1 || -z $2 || -z $3 ]]; then
        echo "Uso: youtube_upload_hide titulo descripcion archivo"
        exit;
fi


youtube-upload --title=$1 --description=$2 --category="Science" --privacy unlisted --recording-date="2011-03-10T15:32:17.0Z" --default-language="es" --default-audio-language="es" --embeddable=True --client-secrets="my_client_secrets.json" "$3"
```
