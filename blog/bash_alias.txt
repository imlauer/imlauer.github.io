---
title: "Bash: alias que uso"
date: 2024-11-15T14:42:32-03:00
tags: ['alias']
---

Para mirar rápidamente mi blog y algunas otras páginas tengo configurado estos alias en mi `.config/fish/config.fish`, también los podés agregar a `.bashrc`

```bash
alias blog 'w3m imlauer.blogspot.com'
alias dgg 'w3m dgg.gg'
alias edgg 'elinks dgg.gg'
alias ldgg 'lynx dgg.gg'
alias imlauera 'w3m imlauera.github.io'
alias invidious 'w3m https://inv.nadeko.net/feed/subscriptions'
```


```
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
