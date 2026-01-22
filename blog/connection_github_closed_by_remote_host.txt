---
title: "Connection to github.com closed by remote host."
date: 2024-11-05T01:24:24-03:00
tags: ['github']
---
En el archvo `.config/ssh` agregamos:

```bash
Host *
  ServerAliveInterval 60
  ServerAliveCountMax 60
```

```bash
Host *.github.com
    StrictHostKeyChecking yes
    IdentityFile ~/.ssh/github
    ServerAliveInterval 60
    ServerAliveCountMax 60
```
Esto permitirá 60 minutos de conexión.

Está causado porque se agotá el tiempo de espera de la conexión SSH.

Fuente: [https://stackoverflow.com/questions/60833006/connection-to-github-com-closed-by-remote-host-when-pushing](https://stackoverflow.com/questions/60833006/connection-to-github-com-closed-by-remote-host-when-pushing)

---

I can't explain the long hang time, but the eventual Connection to github.com closed
by remote host message is likely caused by your SSH connection with GitHub timing
out. I recently helped a coworker solve a similar issue where our Husky pre-push
hook was taking a long time to complete on her machine. By the time the hook
finished, she received the same Connection to github.com closed by remote host
message.

We found the solution was keeping her connection alive by setting values for
ServerAliveInterval and ServerAliveCountMax in her `.ssh/config` file. For example,
adding the following settings would send a null packet to the server every 60
seconds (keeping the connection alive) for 30 rounds. This would buy you 30 minutes
of connection.

```bash
Host *
  ServerAliveInterval 60
  ServerAliveCountMax 30
```

You can adjust the the values however you see fit for your use.

