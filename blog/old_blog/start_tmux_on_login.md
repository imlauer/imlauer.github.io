---
title: "Iniciar TMUX en el login en la TTY"
date: 2024-11-19T07:31:32-03:00
tags: ['linux']
---
Agregando esta linea a tu `bashrc`.

`[ -z "$TMUX"  ] && { tmux attach || exec tmux new-session && exit;}`

Fijate que esta línea cerrará el ssh o el login en la tty cuando termines tu session de TMUX. Si no te gusta esta configuración eliminá el "exit" del final.

`[ -z "$TMUX"  ] && { tmux attach || exec tmux new-session;}`

No deberías envolver a tmux con exec, esto causará que la conexión se cierre cuando no haya sessiones de tmux para unir (attach).

---

### Así lo terminé configurando en fish: `.config/fish/config.fish`:

```console
if test -z "$TMUX" -a $XDG_VTNR = 1
  tmux attach || exec tmux new-session
end
```
Con el `$XDG_VTNR` hago que solo me abra TMUX en la 1er TTY.


## Esto funciona pero me dió este problema: `sessions should be nested with care, unset $TMUX to force`

#### Con fish
En el `.config/fish/fish.conf` agregá:

```bash
if status --is-login
  if test -z "$DISPLAY" -a $XDG_VTNR = 1
    tmux attach-session -t mysession 2>/dev/null || tmux new-session -s mysession
  end
end
```

#### Con bash
```
if [ -z "$TMUX" ] && [ -n "$SSH_TTY" ] && [[ $- =~ i ]]; then
  tmux attach-session -t mysession 2>/dev/null || tmux new-session -s mysession
fi
```

### Al final terminé agregando `mbsync -a` para que descargue mis nuevos correos cuando estoy usando neomutt.
```bash
if test -z "$TMUX" -a $XDG_VTNR = 1
  mbsync -a > /dev/null &
  tmux attach || exec tmux new-session
end
```

Para hacer que inicie programas al arrancar tmux:
```bash
if test -z "$TMUX" -a $XDG_VTNR = 1
  tmux attach-session -t mysession || tmux new-session -d -s mysession
  tmux send-keys -t mysession "falkon" Enter
  tmux send-keys -t mysession "duolingo" Enter
  tmux send-keys -t mysession "upwork" Enter
end
```


Saludos

