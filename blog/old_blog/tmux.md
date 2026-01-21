---
title: "Tmux"
date: 2024-11-10T03:00:45-03:00
tags: ['tmux']
---

Cambiar el prefijo Control+B a F12

```console
run '~/.tmux/plugins/tpm/tpm'

set -g prefix F12
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-cpu'

bind '"' split-window -c "#{pane_current_path}"
bind % split-window -h -c "#{pane_current_path}"
bind c new-window -c "#{pane_current_path}"
```

Y cargalo con `tmux source .tmux.conf`

```console
F12 + "
F12 + %
F12 + z
F12 + z
F12 + Up
F12 + Down
F12 + o - Intercambia entre diferentes ventanas 
F12 + L - (Control Tab)
```

Lo estoy usando actualmente con fish, porque bash con oh-my-bash y tmux no rompe los colores pero rompe el clear.


### dark theme
```bash
set -g default-terminal "screen-256color"
set -g bell-action none

set -g pane-active-border-style fg=white
set -g pane-border-style fg=black

set -g status-style bg=black,fg=white
set -g status-left-length 20
set -g status-left '#[fg=yellow]#H'
set -g status-right '#[fg=green]%Y-%m-%d #[fg=cyan]%H:%M:%S'

set -g window-status-format '#[fg=black]#[bg=black] #I #[fg=white]#W '
set -g window-status-current-format '#[fg=white]#[bg=black] #I #[fg=white]#W '
```
