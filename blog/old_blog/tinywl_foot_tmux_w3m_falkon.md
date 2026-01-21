---
title: "Como usando un navegador de consola puedo ver videos e Instagram. WAYLAND: Tinywl o DWL, Foot, Tmux w3m, QuteBrowser, Konqueror y Falkon(Ex-QupZilla)"
date: 2024-12-20T05:26:21-03:00
tags: ['wayland']
---
El setup mas minimalista que encontre:

En `.bashrc` o `.zshrc` o `.config/fish/config.fish`:

###### Usá w3m con `-sixel` para ver imágenes con foot.
```bash
if status is-interactive
    # Commands to run in interactive sessions can go here
end


set -U fish_greeting
export QT_QPA_PLATFORM=wayland
alias dgg 'w3m -sixel dgg.gg'
alias f1 'bash scripts/f1exposure.sh'
alias google 'cha -V google.com'
alias 3dgames 'cha -V foros.3dgames.com.ar'
alias wgoogle 'w3m -sixel google.com'
alias tdgg 'w3m -sixel dgg.gg'
alias imlauera 'w3m -sixel imlauera.github.io'
alias cimlauera 'cha -V imlauera.github.io'
alias invidious 'w3m -sixel https://inv.nadeko.net/feed/subscriptions'
alias cinvidious 'cha -V https://inv.nadeko.net/feed/subscriptions'
```

### Si vas a usar linuxfb en algunos casos tenes que agregar esta bandera para que funcionen falkon, qutebrowser y angelfish.

```bash
export QTWEBENGINE_CHROMIUM_FLAGS="--ignore-gpu-blacklist --disable-gpu"
```

```bash
alias upwork="falkon upwork.com"
alias linkedin="falkon linkedin.com"
alias freelancer="falkon freelancer.com"
alias hackernews="w3m news.ycombinator.com"
alias drudgereport="w3m drudgereport.com"
alias argentina="w3m old.reddit.com/r/argentina"
alias rcommandline="w3m old.reddit.com/r/commandline"
alias buenosaires="w3m old.reddit.com/r/BuenosAires"
alias duolingo="falkon https://duolingo.com/learn"
alias f1="echo 'Los tiempos están en UTC. Coordinated Universal Time está 3 horas adelantado a Buenos Aires'; bash $HOME/scripts/f1exposure.sh | jq ."
alias chatgpt="falkon chatgpt.com"
alias telegram="falkon web.telegram.org"


export QT_QPA_PLATFORM=linuxfb:offset=0x0:size=1038x700
#export QT_QPA_PLATFORM=linuxfb:offset=0x0
#export QT_QPA_PLATFORM=
#export QT_QPA_PLATFORM=eglfs:offset=900x130:size=768x600

#export QT_QPA_PLATFORM=eglfs
#export QT_QPA_EGLFS_INTEGRATION=eglfs_kms
#export QT_QPA_EGLFS_WIDTH=400
#export QT_QPA_EGLFS_HEIGHT=420
#export QT_QPA_EGLFS_PHYSICAL_HEIGHT=109.62
#export QT_QPA_EGLFS_PHYSICAL_WIDTH=292.32
#export QT_QPA_EGLFS_NO_LIBINPUT=1
#export QT_QPA_FONTDIR=/lib/Fonts
#export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/plugins/platforms

#export TERM=xterm-256color
# Start X at login
#
#if status --is-login
#  if test -z "$DISPLAY" -a $XDG_VTNR = 1
#    # tmux attach-session -t mysession 2>/dev/null || tmux new-session -s mysession
#    tmux new-session
#  end
##end
#if status --is-login
#  if test -z "$DISPLAY" -a $XDG_VTNR = 1
#    exec dvtm
#  end
#end



if test -z "$TMUX" -a $XDG_VTNR = 1
  #mbsync -a > /dev/null &
  #exec dvtm
  #tinywl -s foot
  tmux attach || exec tmux new-session
end
```

`sudo pacman -S tinywl foot tmux w3m qutebrowser` y `yay -S falkon`

```bash
qutebrowser --qt-flag disable-gpu --qt-flag disable-software-rasterizer
```


##### Como bloquear publicidad en Falkon no es tan eficiente como Firefox con uBlock pero corre en el framebuffer:

Essentially, you need to do three things:

 1. Goto AdBlock settings, and add all non-regional lists (EasyPrivacy, NoCoin List,
    Anti-Adblock Killer, Peter Lowe's List etc).

 2. Go to Settings -> Extensions, and check the box for GreaseMonkey.

 3. Go to https://greasyfork.org/en/scripts/459541-youtube� � � -youtube-ad-blocker,
    and click Install this script, then click install anyway. This is the Youtube
    Adblocker.

Now your Falkon should be able to block all the ads.

Test its abilities here: https://d3ward.github.io/toolz/adblock



**Cambiar el tamaño de la letra en foot, descomentá las lineas:**

```bash
cp /etc/xdg/foot/foot.ini .config/foot/foot.ini
```
foot.ini:
```bash
# -*- conf -*-

# shell=$SHELL (if set, otherwise user's default shell from /etc/passwd)
# term=foot (or xterm-256color if built with -Dterminfo=disabled)
# login-shell=no

# app-id=foot # globally set wayland app-id. Default values are "foot" and "footclient" for desktop and server mode
# title=foot
# locked-title=no

# font=monospace:size=8
# font-bold=<bold variant of regular font>
# font-italic=<italic variant of regular font>
# font-bold-italic=<bold+italic variant of regular font>
# font-size-adjustment=0.5
# line-height=<font metrics>
# letter-spacing=0
# horizontal-letter-offset=0
# vertical-letter-offset=0
# underline-offset=<font metrics>
# underline-thickness=<font underline thickness>
# strikeout-thickness=<font strikeout thickness>
# box-drawings-uses-font-glyphs=no
# dpi-aware=no

# initial-window-size-pixels=700x500  # Or,
# initial-window-size-chars=<COLSxROWS>
# initial-window-mode=windowed
# pad=0x0                             # optionally append 'center'
# resize-by-cells=yes
# resize-keep-grid=yes
# resize-delay-ms=100

# bold-text-in-bright=no
# word-delimiters=,│`|:"'()[]{}<>
# selection-target=primary
# workers=<number of logical CPUs>
# utmp-helper=/usr/lib/utempter/utempter  # When utmp backend is ‘libutempter’ (Linux)
# utmp-helper=/usr/libexec/ulog-helper    # When utmp backend is ‘ulog’ (FreeBSD)

[environment]
# name=value

[security]
# osc52=enabled  # disabled|copy-enabled|paste-enabled|enabled

[bell]
# urgent=no
# notify=no
# visual=no
# command=
# command-focused=no

[desktop-notifications]
# command=notify-send --wait --app-name ${app-id} --icon ${app-id} --category ${category} --urgency ${urgency} --expire-time ${expire-time} --hint STRING:image-path:${icon} --hint BOOLEAN:suppress-sound:${muted} --hint STRING:sound-name:${sound-name} --replace-id ${replace-id} ${action-argument} --print-id -- ${title} ${body}
# command-action-argument=--action ${action-name}=${action-label}
# close=""
# inhibit-when-focused=yes


[scrollback]
# lines=1000
# multiplier=3.0
# indicator-position=relative
# indicator-format=""

[url]
# launch=xdg-open ${url}
# label-letters=sadfjklewcmpgh
# osc8-underline=url-mode
# protocols=http, https, ftp, ftps, file, gemini, gopher
# uri-characters=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.,~:;/?#@!$&%*+="'()[]

[cursor]
# style=block
# color=<inverse foreground/background>
# blink=no
# blink-rate=500
# beam-thickness=1.5
# underline-thickness=<font underline thickness>

[mouse]
# hide-when-typing=no
# alternate-scroll-mode=yes

[touch]
# long-press-delay=400

[colors]
# alpha=1.0
# background=242424
# foreground=ffffff
# flash=7f7f00
# flash-alpha=0.5

## Normal/regular colors (color palette 0-7)
# regular0=242424  # black
# regular1=f62b5a  # red
# regular2=47b413  # green
# regular3=e3c401  # yellow
# regular4=24acd4  # blue
# regular5=f2affd  # magenta
# regular6=13c299  # cyan
# regular7=e6e6e6  # white

## Bright colors (color palette 8-15)
# bright0=616161   # bright black
# bright1=ff4d51   # bright red
# bright2=35d450   # bright green
# bright3=e9e836   # bright yellow
# bright4=5dc5f8   # bright blue
# bright5=feabf2   # bright magenta
# bright6=24dfc4   # bright cyan
# bright7=ffffff   # bright white

## dimmed colors (see foot.ini(5) man page)
# dim0=<not set>
# ...
# dim7=<not-set>

## The remaining 256-color palette
# 16 = <256-color palette #16>
# ...
# 255 = <256-color palette #255>

## Sixel colors
# sixel0 =  000000
# sixel1 =  3333cc
# sixel2 =  cc2121
# sixel3 =  33cc33
# sixel4 =  cc33cc
# sixel5 =  33cccc
# sixel6 =  cccc33
# sixel7 =  878787
# sixel8 =  424242
# sixel9 =  545499
# sixel10 = 994242
# sixel11 = 549954
# sixel12 = 995499
# sixel13 = 549999
# sixel14 = 999954
# sixel15 = cccccc

## Misc colors
# selection-foreground=<inverse foreground/background>
# selection-background=<inverse foreground/background>
# jump-labels=<regular0> <regular3>          # black-on-yellow
# scrollback-indicator=<regular0> <bright4>  # black-on-bright-blue
# search-box-no-match=<regular0> <regular1>  # black-on-red
# search-box-match=<regular0> <regular3>     # black-on-yellow
# urls=<regular3>

[csd]
# preferred=server
# size=26
# font=<primary font>
# color=<foreground color>
# hide-when-maximized=no
# double-click-to-maximize=yes
# border-width=0
# border-color=<csd.color>
# button-width=26
# button-color=<background color>
# button-minimize-color=<regular4>
# button-maximize-color=<regular2>
# button-close-color=<regular1>

[key-bindings]
# scrollback-up-page=Shift+Page_Up
# scrollback-up-half-page=none
# scrollback-up-line=none
# scrollback-down-page=Shift+Page_Down
# scrollback-down-half-page=none
# scrollback-down-line=none
# scrollback-home=none
# scrollback-end=none
# clipboard-copy=Control+Shift+c XF86Copy
# clipboard-paste=Control+Shift+v XF86Paste
# primary-paste=Shift+Insert
# search-start=Control+Shift+r
# font-increase=Control+plus Control+equal Control+KP_Add
# font-decrease=Control+minus Control+KP_Subtract
# font-reset=Control+0 Control+KP_0
# spawn-terminal=Control+Shift+n
# minimize=none
# maximize=none
# fullscreen=none
# pipe-visible=[sh -c "xurls | fuzzel | xargs -r firefox"] none
# pipe-scrollback=[sh -c "xurls | fuzzel | xargs -r firefox"] none
# pipe-selected=[xargs -r firefox] none
# pipe-command-output=[wl-copy] none # Copy last command's output to the clipboard
# show-urls-launch=Control+Shift+o
# show-urls-copy=none
# show-urls-persistent=none
# prompt-prev=Control+Shift+z
# prompt-next=Control+Shift+x
# unicode-input=Control+Shift+u
# noop=none
# quit=none

[search-bindings]
# cancel=Control+g Control+c Escape
# commit=Return
# find-prev=Control+r
# find-next=Control+s
# cursor-left=Left Control+b
# cursor-left-word=Control+Left Mod1+b
# cursor-right=Right Control+f
# cursor-right-word=Control+Right Mod1+f
# cursor-home=Home Control+a
# cursor-end=End Control+e
# delete-prev=BackSpace
# delete-prev-word=Mod1+BackSpace Control+BackSpace
# delete-next=Delete
# delete-next-word=Mod1+d Control+Delete
# extend-char=Shift+Right
# extend-to-word-boundary=Control+w Control+Shift+Right
# extend-to-next-whitespace=Control+Shift+w
# extend-line-down=Shift+Down
# extend-backward-char=Shift+Left
# extend-backward-to-word-boundary=Control+Shift+Left
# extend-backward-to-next-whitespace=none
# extend-line-up=Shift+Up
# clipboard-paste=Control+v Control+Shift+v Control+y XF86Paste
# primary-paste=Shift+Insert
# unicode-input=none
# scrollback-up-page=Shift+Page_Up
# scrollback-up-half-page=none
# scrollback-up-line=none
# scrollback-down-page=Shift+Page_Down
# scrollback-down-half-page=none
# scrollback-down-line=none
# scrollback-home=none
# scrollback-end=none

[url-bindings]
# cancel=Control+g Control+c Control+d Escape
# toggle-url-visible=t

[text-bindings]
# \x03=Mod4+c  # Map Super+c -> Ctrl+c

[mouse-bindings]
# scrollback-up-mouse=BTN_WHEEL_BACK
# scrollback-down-mouse=BTN_WHEEL_FORWARD
# font-increase=Control+BTN_WHEEL_BACK
# font-decrease=Control+BTN_WHEEL_FORWARD
# selection-override-modifiers=Shift
# primary-paste=BTN_MIDDLE
# select-begin=BTN_LEFT
# select-begin-block=Control+BTN_LEFT
# select-extend=BTN_RIGHT
# select-extend-character-wise=Control+BTN_RIGHT
# select-word=BTN_LEFT-2
# select-word-whitespace=Control+BTN_LEFT-2
# select-quote = BTN_LEFT-3
# select-row=BTN_LEFT-4

# vim: ft=dosini
```

Iniciá tinywl o dwl ejecutando:  `tinywl -s foot` (no tiene soporte para ver videos en MPV XD) o `dwl` (que si lo tiene)    

Si usas `dwl` tenes que instalar foot y yay -S wmenu` para instalar dwl clona el repo de dwl y compilalo. Con tecla Windows+p abre el menu para ejecutar un programa con tecla Windows+Shift+Enter abre foot, los demas comandos los podes leer en config.h al clonar el repo de `dwl`.

**dwl cambiar el keyboard layout:**

Para cambiar el keyboard layout tenés que exportar la variable `XKB_DEFAULT_LAYOUT`.
o agregando .layout = "es" in the keyboard section in the `config.h` file and recompiled. 

#### Qué es wayland?

To expand slightly on the above, wayland isn't a real thing; it's a protocol, an idea, or a concept.  There is no implementation other than your compositor.  With X11
you had the Xorg server and a window manager as separated bits of software - and questions about the keymap would be addressed at the level of the Xorg server, so it is
meaningful to ask a question like "How do I change my keymap in X11" (or really that should be Xorg not X11, but for better or worse the two are used interchangeably
now).  But "How do I change my keymap in Wayland" makes no sense; you have to change it in your compositor - in your case in dwl's settings which are commented on above.

And how you do this in dwl is completely different than how you'd do it in sway, or weston, or any other wayland compositor.  There may be some vague similarity as they
all use similar protocols to talk to clients, so some convergence in how you specific some configuration is likely - but this is mostly just coincidence: different
compositors *can* handle such things completely differently, and some will not handle it at all.

All that said, *many* compositors use xkbcommon, and those that do can be influenced by the same environment variables.  As I'm pretty sure this is the case for dwl, you
can see here for the answer for another compositor that uses xkbcommon.  In short, set (and export) XKB_DEFAULT_LAYOUT before starting dwl.  It can be set to the
two-letter abbreviation for the Swedish locale (which I don't know off hand).  This should be easier and will not require a recompile.


#### Navegador consola

En `w3m` apretá o y poné como navegadores por defecto: `mpv`, `qutebrowser`, `yt-dlp -f134+140`, `netsurf-fb -f sdl -w 1366 -h 768`, `gallery-dl --cookies-from-browser firefox`, `falkon`, `konqueror`.


#### Para copiar y pegar en vim usando wayland:
```bash
sudo pacman -S wl-clipboard
vim .vimrc
xnoremap <silent> <C-@> :w !wl-copy<CR><CR>
```
Seleccioná las líneas a copiar y apretá `Control+@` y lo pegás con `Control+Shift+V`. 


#### Para correr chrome necesitás ejecutarlo con el siguiente argumento:

```bash
chromium --ozone-platform=wayland
```

##### O configuralo de forma permanente en chrome.
* Go to chrome://flags
* Search "Preferred Ozone platform"
* Set it to "Wayland"

https://www.reddit.com/r/Fedora/comments/rkzp78/make_chrome_run_on_wayland_permanently/
