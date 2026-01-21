---
title: "Apache wordpress"
date: 2024-09-22T21:46:26-03:00
tags: ['wordpress','apache']
---
https://www.learnlinux.tv/how-set-up-an-awesome-wordpress-blog-on-ubuntu-22-04/

```bash
sudo apt install apache2
```

En el archivo 

sudo vim `/etc/apache2/sites-available/wordpress.conf` (mejor editá el 000-default.conf) porque cualquier imagen php de docker por defecto lee ese archivo.

```bash
<VirtualHost *:80>
    DocumentRoot /var/www/wordpress
    <Directory /var/www/wordpress>
        Options FollowSymLinks
        AllowOverride Limit Options FileInfo
        DirectoryIndex index.php
        Require all granted
    </Directory>
    <Directory /var/www/wordpress/wp-content>
        Options FollowSymLinks
        Require all granted
    </Directory>
</VirtualHost>
```

Ejecutar:
```bash
sudo a2dissite 000-default.conf
sudo a2ensite wordpress.conf
```

En docker lo hacés con:

```
RUN a2dissite 000-default (sirve para deshablitar es al pedo mejor usa el por defecto en vez de crear un wordpresss.conf usa 000-default)
RUN a2ensite 000-default
```

La mayoría de contenedores de docker ya tienen esto integrado:

```bash
sudo apt install libapache2-mod-php php-curl php-gd php-intl php-mbstring php-mysql php-soap php-xml php-xmlrpc php-zip
```

```bash
sudo a2enmod rewrite
sudo systemctl restart apache2
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --apache
```


