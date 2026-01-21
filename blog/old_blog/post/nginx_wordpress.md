---
title: "Nginx_wordpress"
date: 2024-09-22T18:04:38-03:00
tags: ['nginx']
---

https://www.youtube.com/watch?v=Wv3uogmRFBU

```bash
sudo apt install -y ngnix
systemctl status ngnix
```
La instalación de la base de datos es todo lo mismo que explicamos en el antiguo tutorial
```bash
sudo apt install -y mysql-server (no se usa más ahora se usa mariadb salvo que tengas una aplicación con una base de datos que usaba mysql ahi vas a tener que usar docker)
sudo mysql -u root
CREATE DATABASE wordpress_db;
CREATE USER 'zack'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON wordpress_db.* TO 'sam'@'localhost';
FLUSH PRIVILEGES;
EXIT;
sudo apt install -y php8.1 php8.1-cli php8.1-fpm php8.1-mysql # es importante fpm porque es el socket de comunicacion
```

```bash
ls /var/run/php
```
Ahí encontraremos un archivo `php8.1-fpm.sock` que es usado para la comunicación entre php y el servidor web.

```bash
wget https://wordpress.org/latest.zip
sudo apt install -y unzip
unzip latest.zip
sudo mv wordpress/* /var/www/html
rm -rf wordpress
sudo chown -R www-data:www-data /var/www/html/*
cd /var/www/html
sudo rm index.html index.nginx-debian.html
sudo mv wp-config-sample.php wp-config.php
sudo vim wp-config.php
```
Adaptá ahí dentro a los datos de tu base de datos `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`.

Si no existe ese archivo wordpress creará un archivo de configuración para vos tenés que copiar el que te dá en el proceso de instalación y ponerlo ahí.

```bash
sudo vim /etc/nginx/sites-available/default
```
Borrá todo con rm
```bash
sudo rm /etc/nginx/sites-enabled/default
```

Y copiá lo siguiente:

https://zacs-tech.com/how-to-install-and-configure-wordpress-in-ubuntu-24-04/

```bash
server {
 listen 80;
 server_name your_domain.com www.your_domain.com;

 root /var/www/html/;
 index index.php;

 location / {
   try_files $uri $uri/ /index.php?$args;
 }
 location ~ \.php$ {
   include snippets/fastcgi-php.conf;
   # Acá va el archivo sock que está en /var/run/php
   fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
 }
 location ~ /\.ht {
   deny all;
 }
}
```
```bash
sudo nginx -t
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/
sudo systemctl restart nginx.service
```

Ahora ingresá a localhost y hacé la instalación hasta que te dé la configuración del archivo `wp-config.php` que lo tenés que crear en `/var/www/html` (explicado anteriormente)

