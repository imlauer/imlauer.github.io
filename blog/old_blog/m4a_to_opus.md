---
title: "Audio: m4a to opus"
date: 2025-02-25T06:06:32-03:00
tags: ['audio']
---

```bash
for i in *.m4a; do echo $i; ffmpeg -i "$i" -ar 16000 -b:a 32000 -ac 1 "${i%.*}".opus; done
```

https://medium.com/@nadirapovey/ffmpeg-compress-audio-files-97cfb3eecd
