---
title: "How to add dwm to xsessions"
date: 2024-07-13T18:00:21-03:00
tags: ['linux']
---
Crea un bash script llamado startdwm:
```
$ cat /usr/bin/startdwm
while true ; do xsetroot -name "$(cat /sys/class/thermal/thermal_zone4/temp) | `date`"; sleep 2
0; done &
keynav &
brightnessctl s 30% &
mbsync -a &
st -e neomutt &
exec dwm
```

Guardalo en `/usr/bin`
Ahora andá a `/usr/share/xsessions/`, copiá una existente y pone Exec=startdwm o podés usar esta:
```bash
$ cat /usr/share/xsessions/dwm.desktop
[Desktop Entry]
Version=1.0
Name=DWM
Comment=Use this session to run DWM as your desktop environment
Exec=startdwm
Icon=
Type=Application
```

Esto es todo
