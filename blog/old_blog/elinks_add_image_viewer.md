---
title: "Elinks add image viewer in TTY using framebuffer"
date: 2024-11-19T19:38:04-03:00
tags: ['elinks']
---
Instalar fbida que viene con un set de comandos: fbi, ida. Y tenemos que configurar elinks para que abra las imágenes usando esos programas.

Elinks tiene un básico soporte de javascript, alcanza hasta el javascript de 4chan XD. 

A diferencia de w3m que no tiene soporte de javascript pero se pueden ver imágenes directamente en la consola sin una herramienta adicional. Antes existía w3m-js pero al parecer está obsoleto.


[https://www.linuxquestions.org/questions/blog/uxrs75-534818/viewing-images-with-elinks-3057/](https://www.linuxquestions.org/questions/blog/uxrs75-534818/viewing-images-with-elinks-3057/)


Podés usar lynx y elinks simultáneamente para ver imágenes.


Si usas lynx tenés que cambiar el archivo `sudo vim /etc/lynx.cfg` para que acepte todas la cookies por defecto, descomentá la línea 1359 y ponelo a TRUE: `ACCEPT_ALL_COOKIES:TRUE`


#### Para configurar elinks 
```bash
Escape - Setup - Terminal Options

Frame handling: [X] Linux frames with fbterm colors.  
Colors: [X] true color   

[X] Switch fonts for line drawing
[X] Restrict frames in cp850/852   
[X] Block cursor                
[X] Italic                      
[X] Transparency                
[X] Underline                   
[X] Strikethrough               
[X] UTF-8 I/O            
```

### o pueden usar esta configuración

```bash
set mime.extension.jpg="image/jpeg"
set mime.extension.jpeg="image/jpeg"
set mime.extension.png="image/png"
set mime.extension.gif="image/gif"
set mime.extension.bmp="image/bmp"

set mime.handler.image_viewer.unix.ask = 0
set mime.handler.image_viewer.unix-xwin.ask = 0

set mime.handler.image_viewer.unix.block = 1
set mime.handler.image_viewer.unix-xwin.block = 0

set mime.handler.image_viewer.unix.program = "fbi %"
set mime.handler.image_viewer.unix-xwin.program = "ida %"


set mime.type.image.jpg = "image_viewer"
set mime.type.image.jpeg = "image_viewer"
set mime.type.image.png = "image_viewer"
set mime.type.image.gif = "image_viewer"
set mime.type.image.bmp = "image_viewer"


set mime.extension.mp4="video/mp4"
set mime.extension.webm="video/webm"

set mime.handler.video_viewer.unix.ask = 0
set mime.handler.video_viewer.unix-xwin.ask = 0

set mime.handler.video_viewer.unix.block = 1
set mime.handler.video_viewer.unix-xwin.block = 0

set mime.handler.video_viewer.unix.program = "mpv %"
set mime.handler.video_viewer.unix-xwin.program = "mpv %"


set mime.type.video.mp4 =  "video_viewer"
set mime.type.video.webm = "video_viewer"




##############################
# Automatically saved options
#

## config 
#  Configuration handling options.

  ## config.saving_style_w [0|1]
  #  This is internal option used when displaying a warning about obsolete
  #  config.saving_style. You shouldn't touch it.
  set config.saving_style_w = 1


## terminal 
#  Terminal options.

  ## terminal.tmux-256color 
  #  Options specific to this terminal type (according to $TERM value).

    ## terminal.tmux-256color.underline [0|1]
    set terminal.tmux-256color.underline = 1
    ## terminal.tmux-256color.strike [0|1]
    set terminal.tmux-256color.strike = 1
    ## terminal.tmux-256color.italic [0|1]
    set terminal.tmux-256color.italic = 1
    ## terminal.tmux-256color.transparency [0|1]
    set terminal.tmux-256color.transparency = 1
    ## terminal.tmux-256color.colors <num>
    set terminal.tmux-256color.colors = 4
    ## terminal.tmux-256color.block_cursor [0|1]
    set terminal.tmux-256color.block_cursor = 1
    ## terminal.tmux-256color.restrict_852 [0|1]
    set terminal.tmux-256color.restrict_852 = 1
    ## terminal.tmux-256color.utf_8_io [0|1]
    set terminal.tmux-256color.utf_8_io = 1
    ## terminal.tmux-256color.m11_hack [0|1]
    set terminal.tmux-256color.m11_hack = 1
    ## terminal.tmux-256color.type <num>
    set terminal.tmux-256color.type = 5


## ui 
#  User interface options.

  ## ui.language <language>
  #  Language of user interface. 'System' means that the language will be
  #  extracted from the environment dynamically.
  set ui.language = "System"
```

Se usa v para ver las imágenes.

### Luego me dí cuenta que es mejor poner elinks en 16 bits de colores en Setup - Terminal Options - Color mode.


### Agregá soporte javascript a elinks:

https://www.cnx-software.com/2014/02/09/building-elinks-text-based-web-browser-with-some-sort-of-javascript-support/

