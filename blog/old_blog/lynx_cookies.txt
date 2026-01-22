---
title: "Accept Lynx cookies always"
date: 2025-11-01T10:53:19-03:00
---

https://old.reddit.com/r/commandline/comments/1c0qgm3/using_lynx_browser_drop_your_tips_here/

Podes agregarlo todo al final del /etc/lynx.cfg

**Lynx tiene una configuración retrasada.**

Primero podes cambiar la configuración presionando `O` dentro del navegador pero esa configuración nunca se guarda porque apropósito en `/etc/lynx.cfg` están comentadas las líneas que habilitan esa configuración por lo menos en ArchLinux. 

Tenes 2 opciones descomentar todo eso y luego editar la configuración desde el menú de `lynx` o escribir la configuración en ese mismo archivo.

```bas
#ENABLE_LYNXRC:ACCEPT_ALL_COOKIES:ON
#ENABLE_LYNXRC:ASSUME_CHARSET:OFF
#ENABLE_LYNXRC:AUTO_SESSION:OFF
#ENABLE_LYNXRC:BOOKMARK_FILE:ON
#ENABLE_LYNXRC:CASE_SENSITIVE_SEARCHING:ON
#ENABLE_LYNXRC:CHARACTER_SET:ON
#ENABLE_LYNXRC:COLLAPSE_BR_TAGS:ON
#ENABLE_LYNXRC:COOKIE_ACCEPT_DOMAINS:ON
#ENABLE_LYNXRC:COOKIE_FILE:ON
#ENABLE_LYNXRC:COOKIE_LOOSE_INVALID_DOMAINS:ON
#ENABLE_LYNXRC:COOKIE_QUERY_INVALID_DOMAINS:ON
#ENABLE_LYNXRC:COOKIE_REJECT_DOMAINS:ON
#ENABLE_LYNXRC:COOKIE_STRICT_INVALID_DOMAIN:ON
#ENABLE_LYNXRC:DIR_LIST_STYLE:ON
#ENABLE_LYNXRC:DISPLAY:OFF
#ENABLE_LYNXRC:EMACS_KEYS:ON
#ENABLE_LYNXRC:FILE_EDITOR:ON
#ENABLE_LYNXRC:FILE_SORTING_METHOD:ON
#ENABLE_LYNXRC:FORCE_COOKIE_PROMPT:OFF
#ENABLE_LYNXRC:FORCE_SSL_PROMPT:OFF
#ENABLE_LYNXRC:FTP_PASSIVE:OFF
#ENABLE_LYNXRC:HTML5_CHARSETS:OFF
#ENABLE_LYNXRC:HTTP_PROTOCOL:1.0
#ENABLE_LYNXRC:IDNA_MODE:TR46
#ENABLE_LYNXRC:KBLAYOUT:ON
#ENABLE_LYNXRC:KEYPAD_MODE:ON
#ENABLE_LYNXRC:LINEEDIT_MODE:ON
#ENABLE_LYNXRC:LOCALE_CHARSET:ON
#ENABLE_LYNXRC:MAKE_LINKS_FOR_ALL_IMAGES:OFF
#ENABLE_LYNXRC:MAKE_PSEUDO_ALTS_FOR_INLINES:OFF
#ENABLE_LYNXRC:MULTI_BOOKMARK:ON
#ENABLE_LYNXRC:NO_PAUSE:OFF
#ENABLE_LYNXRC:PERSONAL_MAIL_ADDRESS:ON
...
...
```



Estoy usando w3m, lynx, links, elinks, chawan, simultaneamente, y a veces Falkon cuando necesito preguntar algo a ChatGPT. Es molesto cuando me pregunta si quiero o no aceptar cookies y para poder ver los acentos cambiar `Display character set` a UNICODE debes marcar la opción SAVE TO DISK.

Y también podes habilitar las VIM keybindings, habilitar el HTML5 charset, underline links, y show images as links así se puede abrir las imágenes y poné a w3m como navegador por defecto o mpv para ver la imagen (acordate que tenes que marcar Save options to disk y guardar), sino no se guarda cuando reinicias el navegador.

```bash

EXTERNAL:http:mpv %s:TRUE
EXTERNAL:http:w3m %s:TRUE
EXTERNAL:http:cha %s:TRUE
EXTERNAL:http:netsurf-fb -f sdl -w 1366 -h 768 %s:TRUE
EXTERNAL:http:falkon %s:TRUE
EXTERNAL:http:angelfish %s:TRUE


KEYMAP:,:EXTERN_PAGE            # Run external program with current page
KEYMAP:.:EXTERN_LINK            # Run external program with current link
```

`TEXTFIELDS_NEED_ACTIVATION` así no se traba cuando usas vi mode

Con el punto (.) abrira la pagina en w3m.

### Lo ideal es editar /etc/lynx.conf porque a veces no te toma la configuración por más que marques SAVE TO DISK.

Por ejemplo esta opción no me la tomaba tuve que como root descomentarla y asignarle TRUE.

```bash
MAKE_LINKS_FOR_ALL_IMAGES:TRUE
```

Aún así hay una configuración que no la pude guardar que es la de SHOW TRANSFER RATE: quería cambiarlo de Show KiB/sec rate a Show progressbar y no pude



### Como aceptar cookies

#### Option 1: Through interactive menu

1. Run Lynx:

   ```bash
   lynx
   ```
2. Press `O` (capital letter O) to open **Options**.
3. Scroll down to **Cookies** settings.
4. Set:

   * `Save options to disk: [X]`
   * `accept all cookies` → **Yes**
   * `ask user about cookies` → **No**
5. Press `→` (right arrow key) on **Accept Changes** to save.

---

#### Option 2: Modify config file

Edit your Lynx configuration file, usually at:

```
~/.lynxrc
```

or globally in `/etc/lynx.cfg`.

Add or modify these lines:

#### A veces lynx ignora la configuración del .lynxrc

```
accept_all_cookies=TRUE
ask_user_about_cookies=FALSE
preferred_charset=utf-8
vi_keys=on
```

You can also check `COOKIE_ACCEPT_PROMPT` in `/etc/lynx.cfg`:

```
COOKIE_ACCEPT_PROMPT:FALSE
SET_COOKIES:TRUE
ACCEPT_ALL_COOKIES:TRUE
ASSUME_CHARSET:utf-8
CHARACTER_SET:utf-8

```


Controles para editar texto en lynx Control+G:
```bash
Control+p va para atras
Control+o cancela
Control+g cancela
Control+´ cancela
control+u borra
control+t mayúscula
control+a comienzo
control+d borra letra adelante
control+h borra letra atras
control+f borra palabra adelante
control+j te lleva a pages.github.com
control+x salta adonde estaba el cursor antes.
control+b borra palabra hacia atras. (Si estas en TMUX tenes que ejecutar control+b+control+b)
control+n mueve cursor palabra hacia adelante
control+- borra hacia atras
control+- borra hacia atras
alt+k borra todo
alt+d borra palabra hacia adelante
alt+a va al inicio
alt+t mueve cursor hacia atras
alt+r va a la url

alt+q top
alt+w al fondo
```

