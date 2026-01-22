---
title: "Hostear tu sitio en AWS"
date: 2024-09-18T15:26:33-03:00
tags: ['ec2','aws']
---
https://www.youtube.com/watch?v=_LIuNAu5Ktc

https://www.youtube.com/watch?v=gWVIIU1ev0Y

https://www.youtube.com/watch?v=lHgxFfioaR4

1. Logueate en la consola AWS.
1. Crea una máquina `ec2`.
1. Configurá security group(ssh -22 admin only)(80 - for normal traffic)
1. Conectate a la máquina ec2.
1. Instalá el servidor web `httpd`(apache) o podés instalar ngnix para correr la aplicación web.
```bash
sudo su
yum update -y
yum install httpd -y
cd /var/www/html
service httpd start
```
6. Creá tu página en ese directorio.
7. Acedé a tu página desde el navegador usando la IP pública de la máquina ec2 o del DNS.
