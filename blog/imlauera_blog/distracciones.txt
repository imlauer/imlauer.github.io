---
title: "Disminuir distracciones"
date: 2025-11-13T21:32:37-03:00
tags: ['offtopic']
---
1. Usa solo la TTY en Linux.
2. Bloqueá el malware, las páginas de apuestas, la publicidad, la pornografía, etc con el archivo [/etc/hosts](/etc_hosts).
3. Configurá estos alias para desconectar tu Internet:

```bash
alias focus='sudo systemctl stop NetworkManager; echo "Modo offline activado"'
alias unfocus='sudo systemctl start NetworkManager'
```


