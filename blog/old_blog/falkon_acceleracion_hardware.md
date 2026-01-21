---
title: "Falkon acceleración Hardware"
date: 2025-03-06T10:41:23-03:00
tags: ['falkon']
---
https://trac.gateworks.com/wiki/qt


##### User Agent Android:
Uso este pero agrego excepciones para chatgpt, gemini.google.com, grok.com, entre otras.

```bash    
Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36
```

Pero agrego excepciones con este `User-Agent` a páginas como ChatGPT:

```bash
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/6.9.2 Chrome/130.0.0.0 Safari/537.36
```


Para cambiar el user-agent de falkon en Preferencias en la última opción ofrece para cambiar el user agent yo uso el User-Agent de Android asi Twitch carga mas rapido:
```bash

Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36
```

### Con linuxfb (framebuffer) no funcionó
```bash
export QT_QPA_PLATFORM=linuxfb:size=1000x1000 
export QT_QPA_FB_DRM=1
```

#### Si no aparece el mouse ejecutá:
```bash
sudo chmod 666 /dev/input/event*
```

Ejecuté este comando y rompí pipewire-pulse XDD porque buscaba la carpeta /pulse en lotro lado. Lo borré.
```bash
export XDG_RUNTIME_DIR=/tmp
```

#### Con eglfs
```bash
export QT_QPA_EGLFS_INTEGRATION=eglfs_kms
export QT_QPA_FONTDIR=/lib/Fonts
export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/plugins/platforms
export QT_QPA_PLATFORM=eglfs
#export QT_QPA_EGLFS_PHYSICAL_WIDTH=155
#export QT_QPA_EGLFS_PHYSICAL_HEIGHT=86
#export QT_QPA_EGLFS_WIDTH=1024
#export QT_QPA_EGLFS_HEIGHT=614
#export QT_QPA_EVDEV_KEYBOARD_PARAMETERS=grab=1
#export QT_QPA_EVDEV_MOUSE_PARAMETERS=grab=1
export QT_QPA_EGLFS_NO_LIBINPUT=0

export QT_QPA_EGLFS_KEYBOARD_LAYOUT='es'
export QT_QPA_EGLFS_KBD_MAP='es'
#
#
#export XKB_LOG_LEVEL=50
#export XKB_LOG_VERBOSITY=10
#
#export XKB_DEFAULT_MODEL=logicd
export XKB_DEFAULT_LAYOUT=es
##export XKB_DEFAULT_VARIANT=abnt2
#export XKB_DEFAULT_OPTIONS=lv3:ralt_switch

export QTWEBENGINE_CHROMIUM_FLAGS="--ignore-gpu-blacklist --enable-gpu-rasterization --enable-native-gpu-buffers"
```

Esto sirve para tomar el mouse y el teclado en vez de que escriba en la consola, pero es una mala idea porque si se te traba la aplicación no se puede cerrar y tenés que apagar la computadora.
##### NO lo uses
```bash
#export QT_QPA_EVDEV_KEYBOARD_PARAMETERS=grab=1
#export QT_QPA_EVDEV_MOUSE_PARAMETERS=grab=1
```
