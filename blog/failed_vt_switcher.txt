---
title: "Failed VT switcher"
date: 2024-11-04T13:11:26-03:00
tags: ['archlinux']
---
```bash
[vo/gpu/drm] VT_GETMODE failed: Inappropriate ioctl for device
[vo/gpu/drm] Failed to set up VT switcher. Terminal switching will be unavailable.
```

[https://github.com/mpv-player/mpv/issues/9773](https://github.com/mpv-player/mpv/issues/9773)

#### Solución en arch:

* Reinstalar libxpresent:

`sudo pacman -S libxpresent`
