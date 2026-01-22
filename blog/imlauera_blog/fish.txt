---
title: "Instalar shell fish con VIM keybindings, iniciar dvtm en el login."
date: 2024-11-03T21:29:15-03:00
tags: ['fish']
---
Ya no uso más fish porque es bloated, ahora solo uso bash.

````bash
#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

# Only run in interactive shells
[[ $- != *i* ]] && return

# -----------------------------
# TTY / TMUX logic
# -----------------------------

if [[ -z "$TMUX" && "$XDG_VTNR" == "1" ]]; then
  tmux attach || exec tmux new-session
fi

if [[ -z "$TMUX" && "$XDG_VTNR" == "5" ]]; then
  sudo pacman --noconfirm -Syu
fi

if [[ -z "$TMUX" && "$XDG_VTNR" == "2" ]]; then
  irssi
fi

if [[ -z "$TMUX" && "$XDG_VTNR" == "6" ]]; then
  mbsync -a
  neomutt
fi

# -----------------------------
# Environment variables
# -----------------------------

export WWW_BROWSER=w3m
export BROWSER=w3m

export QT_QPA_PLATFORM=eglfs
export QTWEBENGINE_CHROMIUM_FLAGS="--ignore-gpu-blacklist"
export QT_QPA_EGLFS_INTEGRATION=eglfs_kms
export QT_QPA_EGLFS_FULLSCREEN=1

export XKB_DEFAULT_LAYOUT=es
export XKB_DEFAULT_VARIANT=nodeadkeys

# -----------------------------
# Aliases
# -----------------------------

alias doom="cd doom && bash play_doom.sh"
alias wiby="w3m http://wiby.org"
alias geohot="netsurf-fb -f sdl -w 1366 -h 768 https://geohot.github.io/blog"
alias ..="cd .."
alias nadeko="w3m https://nadeko.net"
alias ce="netsurf-fb -f sdl -w 1366 -h 768 http://cursoelectricidad.github.io"
alias el="netsurf-fb -f sdl -w 1366 -h 768 http://cursoelectrodomesticos.github.io"
alias mc="w3m https://sotwe.com/marianocrosetti"
alias in="netsurf-fb -f sdl -w 1366 -h 768 https://imlauernews.github.io"
alias im="netsurf-fb -f sdl -w 1366 -h 768 https://imlauer.github.io"
alias imlauer="netsurf-fb -f sdl -w 1366 -h 768 http://imlauera.github.io"
alias hp="netsurf-fb -f sdl -w 1366 -h 768 http://hyperphysics.phy-astr.gsu.edu/hbasees/hframe.html"
alias news="lynx news.ycombinator.com"

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias ..='cd ..'

alias drudgereport="w3m drudgereport.com"
alias dgg="w3m dgg.gg"
alias mojeek="w3m https://www.mojeek.com/search?q=hola"
alias google="w3m https://leta.mullvad.net/search?q=google&engine=google"
alias images2="w3m https://www.ecosia.org/images?q=ecosia"
alias ecosia="w3m https://www.ecosia.org/search?q=ecosia"
alias blog="w3m imlauer.blogspot.com"
alias tdgg="w3m dgg.gg"
alias imlauera="cha -V imlauera.github.io"
alias analisismatematico2="netsurf-fb -f sdl -w 1366 -h 768 analisismatematico2.github.io"
alias wimlauera="w3m imlauera.github.io"
alias invidious="w3m https://inv.nadeko.net/feed/subscriptions"
alias cinvidious="cha -V https://inv.nadeko.net/feed/subscriptions"

alias upwork="falkon upwork.com"
alias linkedin="falkon linkedin.com"
alias freelancer="falkon freelancer.com"
alias duolingo="falkon https://duolingo.com/learn"
alias notebooklm="falkon https://notebooklm.google.com"
alias telegram="falkon web.telegram.org"

alias home="w3m $HOME/samba/offline_tastyfish/startpage.html"
alias images="w3m https://pinterest.lurkmore.com/"
alias lyrics="w3m https://genius.lurkmore.com/"
alias rightdao="w3m https://rightdao.com"
alias ttt="torsocks w3m ~/projects/imlauer.github.io/index.html"
alias focus="sudo systemctl stop NetworkManager"

alias f1="bash $HOME/scripts/f1exposure.sh"

# -----------------------------
# PATH
# -----------------------------

export PATH="$HOME/.local/bin:$PATH"

set -o vi

export HISTSIZE=1000000
export HISTFILESIZE=1000000

````



---



```bash
pacman -S fish
fish_vi_key_bindings
set -U fish_greeting # deshabilita mensaje de bienvenida

```

Si querés modificar más tu fish podés ejecutar `fish_TAB`


En `.config/fish/config.fish` agregá:

# Start X at login
if status --is-login
  if test -z "$DISPLAY" -a $XDG_VTNR = 1
    exec dvtm
  end
end


**Mis alias actuales**:

```bash
if status is-interactive
    # Commands to run in interactive sessions can go here
end

set -U fish_greeting
#export QT_QPA_PLATFORM=wayland
#alias dgg 'w3m -sixel dgg.gg'
#alias f1 'bash scripts/f1exposure.sh'
#alias google 'cha -V google.com'
#alias wgoogle 'w3m -sixel google.com'
#alias tdgg 'w3m -sixel dgg.gg'
#alias imlauera 'w3m -sixel imlauera.github.io'
#alias cimlauera 'cha -V imlauera.github.io'
#alias invidious 'w3m -sixel https://inv.nadeko.net/feed/subscriptions'
#alias cinvidious 'cha -V https://inv.nadeko.net/feed/subscriptions'
#alias upwork="falkon upwork.com"
#alias linkedin="falkon linkedin.com"
#alias freelancer="falkon freelancer.com"
#alias rcommandline="w3m old.reddit.com/r/commandline"
#alias buenosaires="w3m old.reddit.com/r/BuenosAires"
#alias duolingo="falkon https://duolingo.com/learn"
#alias f1="echo 'Los tiempos están en UTC. Coordinated Universal Time está 3 horas adelantado a Buenos Aires'; bash $HOME/scripts/f1exposure.sh | jq ."
#alias chatgpt="falkon chatgpt.com"
#alias telegram="falkon web.telegram.org"

alias wiby="netsurf-fb -f sdl -w 1366 -h 768 http://wiby.org/surprise"
alias ce="netsurf-fb -f sdl -w 1366 -h 768 http://cursoelectricidad.github.io"
alias imlauer="netsurf-fb -f sdl -w 1366 -h 768 http://imlauera.github.io"
alias hp="netsurf-fb -f sdl -w 1366 -h 768 http://hyperphysics.phy-astr.gsu.edu/hbasees/hframe.html"
alias 3dgames="netsurf-fb -f sdl -w 1366 -h 768 https://foros.3dgames.com.ar"
alias news="netsurf-fb -f sdl -w 1366 -h 768 news.ycombinator.com"
alias argentina="netsurf-fb -f sdl -w 1366 -h 768 old.reddit.com/r/argentina"

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias ..="cd .."
#export QT_QPA_PLATFORM=wayland
export QT_QPA_PLATFORM=eglfs
#export QTWEBENGINE_CHROMIUM_FLAGS="--ignore-gpu-blacklist --disable-gpu"
export QTWEBENGINE_CHROMIUM_FLAGS="--ignore-gpu-blacklist"


export QT_QPA_EGLFS_INTEGRATION=eglfs_kms
export QT_QPA_FONTDIR=/lib/Fonts
export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/plugins/platforms
export QT_QPA_EGLFS_PHYSICAL_WIDTH=155
export QT_QPA_EGLFS_PHYSICAL_HEIGHT=86
export QT_QPA_EGLFS_WIDTH=1024
export QT_QPA_EGLFS_HEIGHT=614
export QT_QPA_EGLFS_NO_LIBINPUT=0

#export QT_QPA_EGLFS_KEYBOARD_LAYOUT='es'
#export QT_QPA_EGLFS_KBD_MAP='es'

#export QT_QPA_EGLFS_FULLSCREEN=1
export XKB_DEFAULT_LAYOUT=es

alias drudgereport="netsurf-fb -f sdl -w 1366 -h 768 drudgereport.com"
alias dgg='w3m  dgg.gg'
alias google='cha -V google.com'
alias wgoogle='w3m  google.com'
alias blog='w3m imlauer.blogspot.com'
alias tdgg='w3m  dgg.gg'
alias imlauera='cha -V imlauera.github.io'
alias analisismatematico2='netsurf-fb -f sdl -w 1366 -h 768 analisismatematico2.github.io'
alias wimlauera='w3m imlauera.github.io'
alias invidious='w3m  https://inv.nadeko.net/feed/subscriptions'
alias cinvidious='cha -V https://inv.nadeko.net/feed/subscriptions'
alias upwork="falkon upwork.com"
alias linkedin="falkon linkedin.com"
alias freelancer="falkon freelancer.com"
alias rcommandline="w3m old.reddit.com/r/commandline"
alias buenosaires="w3m old.reddit.com/r/BuenosAires"
alias duolingo="falkon https://duolingo.com/learn"
alias f1="bash $HOME/scripts/f1exposure.sh"
alias chatgpt="falkon chatgpt.com"
alias telegram="falkon web.telegram.org"

export BROWSER=w3m

```


```console
if status is-interactive
    # Commands to run in interactive sessions can go here
end

#if status --is-login
#    if test -z "$DISPLAY" -a $XDG_VTNR = 2
#        exec tmux
#    end
#end

if test -z "$TMUX" -a $XDG_VTNR = 1
  tmux attach || exec tmux new-session
end
if test -z "$TMUX" -a $XDG_VTNR = 5
  sudo pacman --noconfirm -Syu
end
if test -z "$TMUX" -a $XDG_VTNR = 6
  mbsync -a
  neomutt
end

#sudo loadkeys /home/esotericwarfare/mi_mapa.kmap

set -xg WWW_BROWSER w3m
set BROWSER w3m
set -U fish_greeting
export BROWSER=w3m

#export QT_QPA_PLATFORM=wayland
#alias dgg 'w3m -sixel dgg.gg'
#alias f1 'bash scripts/f1exposure.sh'
#alias wgoogle 'cha -V google.com'
#alias wgoogle 'w3m -sixel google.com'
#alias tdgg 'w3m -sixel dgg.gg'
#alias imlauera 'w3m -sixel imlauera.github.io'
#alias cimlauera 'cha -V imlauera.github.io'
#alias invidious 'w3m -sixel https://inv.nadeko.net/feed/subscriptions'
#alias cinvidious 'cha -V https://inv.nadeko.net/feed/subscriptions'
#alias upwork="falkon upwork.com"
#alias linkedin="falkon linkedin.com"
#alias freelancer="falkon freelancer.com"
#alias rcommandline="w3m old.reddit.com/r/commandline"
#alias buenosaires="w3m old.reddit.com/r/BuenosAires"
#alias duolingo="falkon https://duolingo.com/learn"
#alias f1="echo 'Los tiempos están en UTC. Coordinated Universal Time está 3 horas adelantado a Buenos Aires'; bash $HOME/scripts/f1exposure.sh | jq ."
#alias telegram="falkon web.telegram.org"

alias doom="cd doom; bash play_doom.sh;"
alias wiby="w3m http://wiby.org"
alias geohot="netsurf-fb -f sdl -w 1366 -h 768 https://geohot.github.io/blog"
alias ce="netsurf-fb -f sdl -w 1366 -h 768 http://cursoelectricidad.github.io"
#alias google="netsurf-fb -f sdl -w 1366 -h 768 http://google.com"
alias el="netsurf-fb -f sdl -w 1366 -h 768 http://cursoelectrodomesticos.github.io"
alias mc="w3m https://sotwe.com/marianocrosetti"
alias in="netsurf-fb -f sdl -w 1366 -h 768 https://imlauernews.github.io"
alias im="netsurf-fb -f sdl -w 1366 -h 768 https://imlauer.github.io"
alias imlauer="netsurf-fb -f sdl -w 1366 -h 768 http://imlauera.github.io"
alias hp="netsurf-fb -f sdl -w 1366 -h 768 http://hyperphysics.phy-astr.gsu.edu/hbasees/hframe.html"
# alias 3dgames="netsurf-fb -f sdl -w 1366 -h 768 https://foros.3dgames.com.ar"
alias 3dgames="w3m https://foros.3dgames.com.ar"
alias news="netsurf-fb -f sdl -w 1366 -h 768 news.ycombinator.com"
alias argentina="netsurf-fb -f sdl -w 1366 -h 768 old.reddit.com/r/argentina"

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias ..="cd .."
#export QT_QPA_PLATFORM=wayland
export QT_QPA_PLATFORM=eglfs
#export QT_QPA_PLATFORM=linuxfb
#export QTWEBENGINE_CHROMIUM_FLAGS="--ignore-gpu-blacklist --disable-gpu"
export QTWEBENGINE_CHROMIUM_FLAGS="--ignore-gpu-blacklist"


export QT_QPA_EGLFS_INTEGRATION=eglfs_kms
#export QT_QPA_FONTDIR=/lib/Fonts
#export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/plugins/platforms
#export QT_QPA_EGLFS_PHYSICAL_WIDTH=155
#export QT_QPA_EGLFS_PHYSICAL_HEIGHT=86
#export QT_QPA_EGLFS_WIDTH=1024
#export QT_QPA_EGLFS_HEIGHT=614
#export QT_QPA_EGLFS_NO_LIBINPUT=0

#export QT_QPA_EGLFS_KEYBOARD_LAYOUT='es'
#export QT_QPA_EGLFS_KBD_MAP='es'

export QT_QPA_EGLFS_FULLSCREEN=1

export XKB_DEFAULT_LAYOUT=es
export XKB_DEFAULT_VARIANT=nodeadkeys

alias drudgereport="w3m drudgereport.com"
alias dgg='w3m  dgg.gg'
#alias google='cha -V google.com'
alias mojeek "w3m https://www.mojeek.com/search?q=hola"
alias google "w3m https://leta.mullvad.net/search?q=google&engine=google"
alias blog='w3m imlauera.blogspot.com'
alias blog='w3m imlauer.blogspot.com'
alias tdgg='w3m  dgg.gg'
alias imlauera='cha -V imlauera.github.io'
alias analisismatematico2='netsurf-fb -f sdl -w 1366 -h 768 analisismatematico2.github.io'
alias wimlauera='w3m imlauera.github.io'
alias invidious='w3m  https://inv.nadeko.net/feed/subscriptions'
alias cinvidious='cha -V https://inv.nadeko.net/feed/subscriptions'
alias upwork="falkon upwork.com"
alias linkedin="falkon linkedin.com"
alias home="w3m www.tastyfish.cz/startpage.html"
alias freelancer="falkon freelancer.com"
alias rcommandline="w3m old.reddit.com/r/commandline"
alias buenosaires="w3m old.reddit.com/r/BuenosAires"
alias duolingo="falkon https://duolingo.com/learn"
alias f1="bash $HOME/scripts/f1exposure.sh"
alias notebooklm="falkon https://notebooklm.google.com"
alias telegram="falkon web.telegram.org"
alias images="w3m https://pinterest.lurkmore.com/"
alias lyrics="w3m https://genius.lurkmore.com/"
alias rightdao="w3m https://rightdao.com"
alias ttt="torsocks w3m ~/projects/imlauer.github.io/index.html"



fish_add_path $HOME/.local/bin
set -gx ANDROID_HOME ~/Android/Sdk
set -gx PATH $PATH $ANDROID_HOME/cmdline-tools/bin $ANDROID_HOME/platform-tools
```

```bash
#!/bin/bash
sudo chmod 666 /dev/input/event*
amixer set 'Internal Mic Boost' 50%-

ttyd --port 2020 --writable bash &
angelfish "https://chatgpt.com" "http://127.0.0.1:2020"
```


