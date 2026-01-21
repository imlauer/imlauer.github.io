---
title: "Software y consejos al usar una PC de hace 20 años"
tags: ['informatica']
---
* Comprate cualquier teclado mecánico barato, es impresionante la diferencia que hace, te hace creer que la computadora es más rápida.
* Instalá ArchLinux con [sway](https://imlauera.github.io/sway/) o con dwm o AntiX Linux. [ArchLinux guía de instalación](https://imlauera.github.io/post/instalacion_arch_basica/)    
* Usá Perplexity desde Telegram-Desktop desde el navegador es demasiado lento: https://t.me/askplexbot    
* Usá thunderbird o [neomutt](https://imlauera.github.io/post/neomutt/) para leer el correo.    
* Whatsie para WhatsApp y la aplicación de discord (`sudo pacman -S discord`)    
* Para mirar YouTube usá smtube (`yay -S smtube`) con mpv y yt-dlp o `https://inv.nadeko.net` (invidious) si no carga el video en Invidious abrilo en EMBED que es el 1er ícono a la derecha debajo del titulo del video.    
* Para subir videos a YouTube usá: `youtube-upload` no subas videos desde el navegador.    
Ejemplo: 
```bash
[I] esotericwarfare@arch ~/p/blog (master)> source $HOME/youtube-upload/bin/activate.fish
[I] (youtube-upload) esotericwarfare@arch ~/p/blog (master)> $HOME/youtube-upload/youtube-upload/bin/youtube-upload --title="arreglo cocina valvula de la hornalla" --default-language="es" --default-audio-language="es" --privacy="unlisted" --embeddable=True ~/samba/imlauernews/VID_20250915_115540.mp4
```



* Para ingresar a Google Drive usá `rclone`.    
* No uses `google docs` en su lugar podes usar `latex con vim` o `libreoffice`.    
