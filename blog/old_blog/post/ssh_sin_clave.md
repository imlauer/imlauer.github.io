---
title: "Ssh sin clave"
date: 2024-09-24T12:17:39-03:00
tags: ['ssh']
---

```bash
sudo service sshd start
sudo systemtcl start sshd
sudo service sshd status
ssh remote_username@remote_server_ip_address
ssh-keygen -t ed25519 -C "your_email@gmail.com"
ssh-copy-id remote_username@remote_server_ip_address
```
Ahora podés ingresar a tu servidor sin contraseña: 

```bash
$ ssh remote_username@remote_server_ip_address
```
`
