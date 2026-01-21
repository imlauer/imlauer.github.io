---
title: "Bash autosuggestions: FZF"
date: 2025-06-21T16:21:54-03:00
tags: ['linux']
---
Usando `Control+R` y fzf se puede lograr. 

On Arch, after installing fzf with `pacman -S fzf`, you just need to add this line to your `~/.bashrc` for `autosuggestions and keybindings`:

```bash
eval "$(fzf --bash)"
```


Alternatively, you can source the scripts directly:

```bash
source /usr/share/fzf/key-bindings.bash
source /usr/share/fzf/completion.bash
```


Then restart your terminal or run source `~/.bashrc`. Now you'll have fuzzy completion and handy shortcuts like `Ctrl+T`, `Ctrl+R`, and Alt+C in Bash! 


```bash
#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias ..="cd .."
alias dgg='w3m -sixel dgg.gg'
alias news='w3m https://news.ycombinator.com'
alias f1='torsocks bash scripts/f1exposure.sh'
alias google='cha -V google.com'
alias 3dgames='cha -V https://foros.3dgames.com.ar'
alias wgoogle='w3m -sixel https://google.com'
alias tdgg='w3m -sixel https://dgg.gg'
alias imlauera='w3m -sixel https://imlauera.github.io'
alias cimlauera='cha -V https://imlauera.github.io'
alias yewtube='cha -V https://yewtu.be'
alias invidious='w3m -sixel https://inv.nadeko.net/feed/subscriptions'
alias cinvidious='cha -V https://inv.nadeko.net/feed/subscriptions'

PS1='[\u@\h \W]\$ '
source /usr/share/bash-completion/bash_completion
eval "$(fzf --bash)"
```

### Para limpiar la terminal cuando tenés seteado el set -o vi
Esto va en el archivo .inputrc
```bash
set editing-mode vi
$if mode=vi

set keymap vi-command
# these are for vi-command mode
Control-l: clear-screen

set keymap vi-insert
# these are for vi-insert mode
Control-l: clear-screen 
$endif
```
