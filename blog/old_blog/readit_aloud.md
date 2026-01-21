---
title: "Hack para leer texto desde w3m (Readit aloud)"
date: 2025-11-17T01:28:20-03:00
tags: ['cli']
---
```bash
links -dump -width 512 $1 | tr "\n\ r" " " | sed "s/^.*, consoomer version//g" | espeak -s 180 -p 30  &
#links -dump -width 512 $1 | tr "\n\ r" " " | espeak -s 180 -p 30  &
# Español
#links -dump -width 512 $1 | tr "\n\ r" " " | sed "s/^.*, consoomer version//g" | espeak-ng -v es  &
#links -dump -width 512 $1 | tr "\n\ r" " " | sed "s/^.*, consoomer version//g" | piper-tts --model /usr/share/piper-voices/en/en_US/ryan/high/en_US-ryan-high.onnx --output_raw 2> /dev/null  | aplay -f S16_LE -r 22050 &
# To file
#links -dump -width 512 $1 | tr "\n\ r" " " | sed "s/^.*, consoomer version//g" | piper-tts --model /usr/share/piper-voices/en/en_US/ryan/high/en_US-ryan-high.onnx --output .
```
