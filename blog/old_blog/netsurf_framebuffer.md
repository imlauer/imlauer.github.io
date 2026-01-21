---
title: "Netsurf en framebuffer"
date: 2024-11-28T00:33:15-03:00
tags: ['framebuffer']
---
https://askubuntu.com/questions/817937/how-to-run-netsurf-fb-fails-with-unable-to-set-console-s


I had a similar problem getting netsurf to run, but managed to fix it thanks to
persistence and blind luck.

Problem 1: init mouse failed Solution: Add myself to the input group (the group that
owns /dev/input/mice

Problem 2: Unable to set video: Could not set console screen info fbdev Solution:
Install the xserver-xorg-video-fbdev and fbset packages

Problem 3: Running netsurf causes the screen to go blank and the system to hang,
requiring a hard reboot Solution: I ran it in verbose mode and redirected standard
error to a file, and I saw that netsurf was complaining about not being able to find
DejaVuSans.ttf. I copied the file from /usr/share/fonts/truetype/dejavu to /usr/
share/netsurf


```bash
netsurf-fb -f sdl -w 1366 -h 768 "https://imlauera.github.io"
```

Probá luakit, qutebrowser, otter-browser.
