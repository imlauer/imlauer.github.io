---
layout: post
title: 'Wordpress: Lo básico y buscando vulnerabilidades con WPScan'
date: 2024-09-22T17:49:51-03:00
tags: ['wordpress']
---
https://m.youtube.com/watch?v=lD6vQBDHkqU

https://www.youtube.com/watch?v=1Haj2D_WTCY

https://www.youtube.com/watch?v=Wv3uogmRFBU

https://www.youtube.com/watch?v=pOESHd1G-HI

https://www.youtube.com/watch?v=PsMhopODLTY

https://m.youtube.com/watch?v=gy2wy9VlSWs

https://m.youtube.com/watch?v=G3CoIv3MQH0

https://www.youtube.com/watch?v=a4m8D02U8W8

### Vulnerabilidades escaneo con WPScan

https://www.youtube.com/watch?v=9gwyj4frqwc

https://www.youtube.com/watch?v=bVSrlDtTBdI



https://www.youtube.com/watch?v=V6COUeJeqjw

https://www.youtube.com/watch?v=Inn0RXSF00g

https://www.youtube.com/watch?v=ulDZnlURIc0

https://www.youtube.com/watch?v=oYk3-oM2Tz4

---

```bash
sudo apt update && sudo apt upgrade -y 
sudo apt install apache2 -y
hostname -I (lo mismo que ifconfig te tira tu ip lan, en el caso de ser un servidor tu ip publica)

sudo apt install -y libapache2-mod-php php-mysql
```
instalar base de datos: (esto también lo expliqué en wordpress howto)
```bash
sudo apt install -y mysql-server (o mariadb explicado en wordpress howto)
sudo mysql_secure_installation (ahora se usa sudo mariadb-install-db)
sudo mysql -u root -p
CREATE DATABASE wpdb DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
CREATE USER 'wpuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON wpdb.* TO 'wpuser'@'localhost';
```

### Instalá wordpress
```bash
cd /var/www/html
sudo rm *
sudo wget https://wordpress.org/latest.tar.gz
sudo tar xzf latest.tar.gz
sudo mv wordpress/* .
sudo chown -R www-data .
```

### Port forwarding
```bash
80,445
```

### Domain
Comprá el dominio, si es un colegio el `.edu.ar` lo tenés gratis ;)

### HTTPS
```bash
sudo apt install -y python-certbot-apache
sudo certbot --apache -d <domain> -d <www.domain>
```


---
### Atacando wordpress
```bash
wpscan --url 10.129.178.192 -e u,vp --api-token
```

-e: enumerar
u: user
vp: plugins vulnerables
ap: todos los plugins
ahora se necesita un api-token XDD, tenés que ir a https://wpscan.com y obtener uno y crearte una cuenta gratis XDD y pegarlo luego del `--api-token`


Para hacer un bruteforce podés usar hydra pero no es recomendable, quedan miles de logs y es muy fácil de detectar ese ataque y es tonto.

