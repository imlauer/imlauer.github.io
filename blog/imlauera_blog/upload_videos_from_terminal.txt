---
title: "Subí videos a YouTube desde la consola"
date: 2024-09-27T04:30:50-03:00
tags: ['terminal','youtube']
---

https://github.com/tokland/youtube-upload


```bash
$HOME/youtube-upload/youtube-upload/bin/youtube-upload --title="Trafo Sí o Trafo No？ Para tableros de bombas" --recording-date="2011-03-10T15:32:17.0Z" --default-language="es" --default-audio-language="es" --privacy="unlisted" --embeddable=True trafo.mp4
```

Hay también otra alternativa pero no hablaremos de esa en este tutorial: **Otra Alternativa: https://github.com/porjo/youtubeuploader**

Desde el readme.md: `sudo pip install --upgrade google-api-python-client oauth2client progressbar2`

```bash
wget https://github.com/tokland/youtube-upload/archive/master.zip
unzip master.zip
cd youtube-upload-master
sudo python setup.py install
cd youtube-upload-master
PYTHONPATH=. python bin/youtube-upload ...
```

O en arch: `yay -S youtube-upload`

---

### Ahora tenés que crear una aplicación de tipo Desktop, no funciona más crearla como Web Application y no hace falta agregar authorized redirect URI. Solo necesitás `client_secrets.txt` no el archivo de credentials.

```bash
Create an account on the Google Developers Console
Create a new project for this app
Enable the Youtube API (APIs & Services -> Enable APIs and Services -> Click 'ENABLE APIS AND SERVICES' top right). Select 'YouTube Data API v3'
Create OAuth consent screen (APIs & Services -> OAuth Consent Screen)
Add a test user. This can be any Google User account but it should correspond with the Youtube account where videos will be uploaded.
NOOOOOOOOO (No tenés que crear una aplicación web sino un Desktop app): Create Credentials (APIs & Services -> Credentials -> click 'CREATE CREDENTIALS'), select 'OAuth client ID', select 'Web application'
No hace falta agregar URI de callback en un Desktop App: Add an 'Authorized redirect URI' of 'http://localhost:8080/oauth2callback'
Download the client secrets JSON file (click download icon next to newly created client ID) and save it as file client_secrets.json in the same directory as the utility e.g.
```


### Está bien la parte de agregar test users pero no existe más OAuth 2.0  -> Other  tenés que agregar un OAuth client pero de aplicación de escritorio (Desktop App)

* Abrí la [consola](https://console.cloud.google.com/apis/dashboard) de Google.
* Creá un proyecto.
* Ingresá a APIs & auth -> APIs
* En menú de arriba: Activá (Enabled) API(s): Enable all Youtube APIs.
* APIs & auth -> Credentials.
* Configurá OAuth consent screen 
* Creá un Client ID: Agregá credentials -> OAuth 2.0 Client ID -> Other -> Name: youtube-upload -> Crear -> OK
* Andá a OAuth consent screen (o en Publico si estas en español abajo agrega tu cuenta como test user) y debajo de **Test users** dale a **agregar usuarios**. 
* Descargá el JSON desde "OAuth 2.0 client IDs". Guardá el archivo.
* Usá ese JSON como tu archivo de credenciales:

### Ojo: si ya tenias una cuenta antes y queres cambiarla tenes que borrar `.youtube-upload-credentials.json`

```bash
$ youtube-upload \
  --title="A.S. Mutter" \
  --description="A.S. Mutter plays Beethoven" \
  --category="Music" \
  --tags="mutter, beethoven" \
  --recording-date="2011-03-10T15:32:17.0Z" \
  --default-language="en" \
  --default-audio-language="en" \
  --client-secrets="my_client_secrets.json" \
  --playlist="My favorite music" \
  --embeddable=True|False \
  anne_sophie_mutter.flv
tx2Zb-145Yz
```

```bash
--privacy (public | unlisted | private)  
--publish-at (YYYY-MM-DDThh:mm:ss.sZ)  
--location (latitude=VAL,longitude=VAL[,altitude=VAL])  
--thumbnail (string)  
```

### Subir video pasale titulo descripcion y path del video (por defecto puse oculto).


```bash
#!/bin/bash

# Descargá los subtitulos para pasarlos a chatgpt.

# yt-dlp --ignore-config --write-subs --write-auto-sub
--sub-lang en --sub-format "srt" --skip-download https://www.youtube.com/watch?v=ID

# sed -E '/^[0-9]+$|^$/d; /^[0-9]{2}:/d' video.en.srt > subtitles.txt

if [ $# -lt 3 ]; then
    echo "Uso: $0 <titulo> <desc> <path video.mp4>"
    exit 1
fi


source $HOME/youtube-upload/bin/activate
$HOME/youtube-upload/youtube-upload/bin/youtube-upload \
  --title="$1" \
  --description="$2" \
  --recording-date="2011-03-10T15:32:17.0Z" \
  --privacy="unlisted" \
  --embeddable=True \
  $3
``` 
