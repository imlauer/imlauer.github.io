---
title: "El diseño de YouTube es demasiado lento. Tips para que cargue más rapido"
date: 2024-08-11T18:43:12-03:00
tags: ['offtopic']
---
Podés usar alguna instancia de invidious: https://redirect.invidious.io es lo mismo que youtube pero un diseño más ligero y respetuoso con el usuario o https://piped.video (que no siempre funciona bien)

#### Otra opción: 
Bajate una extensión [User-Agent Switcher](https://chromewebstore.google.com/detail/user-agent-switcher-and-m/bhchdcejhohfmigjafbampogmaanbfkg) permití la extensión en modo privado y en las opciones de la extensión en Custom Mode agregá:

```
{
"youtube.com": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.154 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"twitch.tv":"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.154 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"twitch.com":"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.154 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
}
```

Guardalo, ahora YouTube y Twitch creerá que visitás la página desde un Android.

Ahora instalá yt-dlp y mpv y cuando quieras ver un video, no lo veas en la página miralo desde mpv.

[Ya escribí un artículo de esto](https://imlauera.github.io/post/2022-07-12-usando-mpv-para-mirar-videos-en-pc-s-de-bajos-recursos/) pero hay una pequeña modificación en la configuración.

/etc/mpv/mpv.conf:
```bash
--ytdl-raw-options="format=bestvideo[height<=?360]+bestaudio/best[height<=?360]/bestvideo[height<=?480]+bestaudio/best[height<=?480],write-auto-sub=,sub-lang=[en,ru],write-sub="
```
Con j activás los subtitulos.
