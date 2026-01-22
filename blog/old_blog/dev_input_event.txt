---
title: "Permiso chmod 666 /dev/input/event* permanente"
date: 2025-10-27T13:19:45-03:00
tags: ['linux']
---
```bash
[N] esotericwarfare@arch /e/u/rules.d> sudo vim 99-input-event-permissions.rules

[I] esotericwarfare@arch /e/u/rules.d> cat 99-input-event-permissions.rules
KERNEL=="event[0-9]*", MODE="0666"
[I] esotericwarfare@arch /e/u/rules.d>

```
