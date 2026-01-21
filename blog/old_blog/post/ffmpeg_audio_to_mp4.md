---
title: "Audio to mp4 rápido (para subir audios a youtube)"
date: 2024-07-13T22:04:45-03:00
tags: ['audio','youtube']
---
Here is a full explanation:

```bash
ffmpeg -i image.jpg -i audio.mp3 -c:v libx264 -tune stillimage -c:a copy out.mp4 
```

- `c:v libx264`: use x264 to encode video.

- `tune stillimage`: x264 setting to optimize video for still image encoding

- `c:a copy`: copies the codec used for the input audio. You may change this if you want a different audio codec.

I did not use `-loop 1` or `-shortest`. `-loop 1` drastically slows down the encoding and creates a larger file. -shortest should not be used without `-loop 1` since then the video will be one frame long. However YouTube does not like videos with one frame (see PJ Brunet's answer) so then both options should be used.



