---
title: "Lftp"
date: 2026-01-21T11:46:15-03:00
---

```bash
sudo pacman -S lftp
lftp -u username,pass w10.host -e "mirror --reverse --verbose /home/esotericwarfare/projects/web.github.io/ .; quit"
```
