---
title: "Publicar audio como video a youtube desde la terminal"
date: 2024-11-16T13:28:41-03:00
tags: ['linux']
---
1. Generá el thumbnail usando el script publicado [acá](https://imlauera.github.io/bash_script_generate_youtube_thumbnail/).
2. Transformá el audio a mp4 usando el comando publicado [acá](https://imlauera.github.io/post/ffmpeg_audio_to_mp4/).
3. Subí el video a YouTube usando el comando publicado [acá](https://imlauera.github.io/post/upload_videos_from_terminal/
).

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
  --credentials-file="my_credentials.json" \
  --playlist="My favorite music" \
  --embeddable=True|False \
  anne_sophie_mutter.flv

--privacy (public | unlisted | private)
--publish-at (YYYY-MM-DDThh:mm:ss.sZ)
--location (latitude=VAL,longitude=VAL[,altitude=VAL])
--thumbnail (string)
```
