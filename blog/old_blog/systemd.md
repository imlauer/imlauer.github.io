---
title: "Systemd"
date: 2025-06-13T22:35:11-03:00
tags: ['linux']
---
```bash
systemd-analyze time
systemctl list-unit-files --type=service --state=enabled 
systemd-analyze blame 
systemd-analyze plot > boot.svg 
cd /etc/systemd/system/
ls -ltr # Últimos servicios agregados.
```
