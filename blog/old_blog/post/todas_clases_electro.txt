---
title: "Subtitulo de todas clases de reparación de electrodomésticos"
date: 2024-09-25T14:26:32-03:00
tags: ['electrodomesticos']
---
Acá tienen: [todos subtitulos desde la 2da clase hasta la 12](/subtitulos.tar.gz)
Sirve para buscar más rápido en que minuto habló de tal cosa.
Descomprimí el tar con

```bash
tar xvf subtitulos.tar.gz
grep -i ventilador *
```

### Pueden descargarlas manualmente así (acá están desde la 2 hasta 12):
```bash
yt-dlp --ignore-config --write-auto-sub --write-sub --sub-lang es --skip-download https://www.youtube.com/watch?v=3nJnAqAZQpY  &
yt-dlp --ignore-config --write-auto-sub --write-sub --sub-lang es --skip-download https://www.youtube.com/watch?v=FEQ6iXWc2FQ &
yt-dlp --ignore-config --write-auto-sub --write-sub --sub-lang es --skip-download https://youtu.be/OSlqnhmQsMQ  &
yt-dlp --ignore-config --write-auto-sub --write-sub --sub-lang es --skip-download https://youtu.be/LWxML1Yv3IY &
yt-dlp --ignore-config --write-auto-sub --write-sub --sub-lang es --skip-download https://youtu.be/4LCbuu2Wa_4   &
yt-dlp --ignore-config --write-auto-sub --write-sub --sub-lang es --skip-download https://youtu.be/5RjcuVO6T3I  &
yt-dlp --ignore-config --write-auto-sub --write-sub --sub-lang es --skip-download https://youtu.be/HOFVsSnZ_a4   &
yt-dlp --ignore-config --write-auto-sub --write-sub --sub-lang es --skip-download https://youtu.be/xniJUxh04qI   &
yt-dlp --ignore-config --write-auto-sub --write-sub --sub-lang es --skip-download https://youtu.be/jzlRd4U2xI4   &
yt-dlp --ignore-config --write-auto-sub --write-sub --sub-lang es --skip-download https://www.youtube.com/watch?v=VBKQeiF5XVM   &
yt-dlp --ignore-config --write-auto-sub --write-sub --sub-lang es --skip-download https://youtu.be/kCyNtZ1t94s  &
```

Luego `grep -i ventilador *`
