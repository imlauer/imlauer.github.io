---
title: "SFTP setup"
date: 2024-09-18T21:05:46-03:00
tags: ['sftp']
---
https://www.youtube.com/watch?v=pS_mY4Rfsg8

https://m.youtube.com/watch?v=XhnqJ4S7C10

```bash
sudo apt install -y ssh
sudo systemctl enable ssh
sudo systemctl start ssh
sudo addgroup sftp
sudo adduser walu
sudo usermod -a -G sftp walu
sudo mkdir -p /var/sftp/files
sudo chown root:root /var/sftp
sudo chmod 755 /var/sftp
sudo chown walu:walu /var/sftp/files
```
Dentro de `sudo vim /etc/ssh/sshd_config` al final insertar:
```bash
Match User walu
ChrootDirectory /var/sftp
X11Forwarding no
AllowTcpForwarding no
ForceCommand internal-sftp
```

```bash
sudo systemctl restart ssh
```

Eso es todo, la conexión se realiza por el puerto 22.
