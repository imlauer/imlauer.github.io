---
title: "Usando tinywl o alternativa a DWM para wayland: DWL"
date: 2024-11-19T22:04:57-03:00
tags: ['tinywl']
---
Primero de todo: en wayland no existe `startx` XD.

Por ejemplo tinywl se inicia desde la TTY con el siguiente comando: `tinywl -s chromium`
Podés probar con los siguientes navegadores que son ligeros:

Cualquier navegador que esté basado(que sea un fork) en una vieja versión de firefox o una vieja versión de chrome.

Actualmente estoy probando:
* Midori: Hasta ahora en mi opinión el más rápido, está basado en Firefox.
* Konqueror.
* Vivaldi.
* SeaMonkey.
* Falkon.
* NetSurf. No tiene soporte javascript.
* Qutebrowser: escrito en python con vim keybindings.
* Throrium: fork de chromium
* Mercury: fork de Firefox.

```console
$ yay -Ss mercury
aur/mercury-browser-sse4-bin 129.0.2-1 (+2 0.23)
    Compiler optimized, private Firefox fork
aur/mercury-browser-avx2-bin 129.0.2-1 (+7 1.88)
```
Como ves acá hay una versión para sse4 y otra para avx2, ¿qué corno es eso? Lo podés googlear o preguntarle a ChatGPT, Claude AI o Perplexity o con el aichat que te enseñé a instalar antes.

En resumen: 

**SSE4**(Streaming SIMD Extensions 4)  se centra principalmente en optimizar aplicaciones multimedia y de procesamiento de imágenes.   
**AVX2** (Advanced Vector Extensions 2) es otra extensión de instrucciones para microprocesadores que proporciona un mayor ancho de banda de datos y capacidades de procesamiento en paralelo. AVX2 puede manejar datos de 256 bits en lugar de 128 bits, lo que permite a los programas manipular más
datos en una sola instrucción, lo que resulta en un mayor rendimiento en tareas como la codificación de video y la inteligencia artificial.

Lo que nos interesa acá es saber si tu microprocesador soporta o no eso y lo hacemos de la siguiente manera:
```bash
grep -E --color 'se4_1|sse4_2|avx|avx2' /proc/cpuinfo
```



There's no such thing as "start Wayland", as there's no such program as "Wayland". Wayland is a
protocol, and there are multiple Wayland-compatible compositors out there, Plasma's KWin being
one of them. You can start a KWin-on-Wayland session with startplasmacompositor, but keep in
mind it's not fully fleshed out yet, so expect it to be less stable and feature-complete than X.


Si estás usando una computadora lenta mi recomendación es NO usar el entorno gráfico, hay demasiadas aplicaciones y podés usar la inteligencia artificial para programar aplicaciones en python que interactúen con las APIs de páginas como mercadolibre, apis para saber los horarios para ver la fórmula 1, o cualquier cosa.

Necesitas usar el mouse con GPM, leer pdfs con fbpdf, mirar imagenes con fbi, mirar videos con mpv --vo=drm (usando el framebuffer), escuchando música con mpv, mirando youtube con invidious o con ytfzf (expliqué anteriormente los alias que usaba uno de ellos era: w3m inv.nadeko.net/feed/subscriptions), mirando twitch o kick con mpv, etc.


Los navegadores que uso: w3m, lynx, elinks, todavía probé **links 2** y al parecer tiene un mejor soporte de javascript, mi recomendación es instalar todos.

elinks y lynx tienen un mínimo soporte de javascript y se puede ver imágenes como expliqué acá: [https://imlauera.github.io/elinks_add_image_viewer/](https://imlauera.github.io/elinks_add_image_viewer/)

w3m soporta imágenes directamente desde la consola sin modificar nada.


Pero si por ALGUNA razón necesitás si o si por una URGENCIA usar el entorno gráfico podés usar tinywl lo instalás así en archlinux: `yay -S tinywl` si estás en otras distros quizás las vayas a tener que compilar manualmente.

`Control+Alt+Escape` para salir de tinywl.

En tu `.xinitrc` agregá al final `tinywl -s chromium` o el navegador que uses.
