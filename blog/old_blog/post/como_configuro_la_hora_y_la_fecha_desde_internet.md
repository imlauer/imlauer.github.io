---
title: "Configurar la hora y la fecha desde Internet en Arch"
date: 2024-08-11T18:15:20-03:00
tags: ['configurar','hora','fecha','arch']
---

```
sudo pacman -S ntp
timedatectl set-ntp true
sudo vim /etc/ntp.conf
server pool.ntp.org
sudo ntpdate pool.ntp.org
sudo systemctl enable ntpd
sudo systemctl start ntpd
```


```
sudo ntpd -qg; sudo hwclock -w
```

