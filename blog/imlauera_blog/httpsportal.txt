---
title: "Httpsportal"
date: 2024-09-23T00:05:18-03:00
---

https://josejuansanchez.org/iaw/practica-https-docker/index.html

#### ¿Qué es HTTPS-PORTAL?
HTTPS-PORTAL es una imagen Docker que contiene un servidor HTTPS totalmente automatizado que hace uso de las tecnologías Nginx y Let’s Enctrypt. Los certificados SSL se obtienen y renuevan de Let’s Encrypt automáticamente.

Esta imagen está preparada para permitir que cualquier aplicación web pueda ejecutarse a través de HTTPS con una configuración muy sencilla.

Puede encontrar más información sobre HTTPS-PORTAL en la web oficial de Docker Hub.

```bash
version: '3.4'

services:
  mysql:
    image: mysql
    command: --default-authentication-plugin=mysql_native_password
    ports: 
      - 3306:3306
    environment: 
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
      - MYSQL_DATABASE=${MYSQL_DATABASE}
      - MYSQL_USER=${MYSQL_USER}
      - MYSQL_PASSWORD=${MYSQL_PASSWORD}
    volumes: 
      - mysql_data:/var/lib/mysql
    networks: 
      - backend-network
    restart: always
  
  phpmyadmin:
    image: phpmyadmin
    ports:
      - 8080:80
    environment: 
      - PMA_ARBITRARY=1
    networks: 
      - backend-network
      - frontend-network
    restart: always
    depends_on: 
      - mysql

  prestashop:
    image: prestashop/prestashop
    environment: 
      - DB_SERVER=mysql
    volumes:
      - prestashop_data:/var/www/html
    networks: 
      - backend-network
      - frontend-network
    restart: always
    depends_on: 
      - mysql

  https-portal:
    image: steveltn/https-portal:1
    ports:
      - 80:80
      - 443:443
    restart: always
    environment:
      DOMAINS: 'practicahttps.ml -> http://prestashop:80'
      STAGE: 'production' # Don't use production until staging works
      # FORCE_RENEW: 'true'
    networks:
      - frontend-network

volumes:
  mysql_data:
  prestashop_data:

networks: 
  backend-network:
  frontend-network:
```


.env
```
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=prestashop
MYSQL_USER=ps_user
MYSQL_PASSWORD=ps_password
```


Luego de esto tenés que abrir los puertos en la VPS obtener la dirección IP y asignarle los registros DNS: A y cname (www).


Una vez llegado a este punto, sólo queda desplegar los servicios con Docker Compose y ya tendríamos nuestro sitio web con HTTPS habilitado y todo configurado para que el certificado se vaya renovando automáticamente.


Mezclalo con este docker-compose.yml: y geenerá la imágen de la app con este: https://github.com/jjcosgrove/docker-apache-php/tree/master

```bash
version: '2'
volumes:
  db:
services:
  app:
    restart: always
    image: orbitmedia/php:5.4-apache
    ports:
    - 80:80
    volumes:
    - /home/esotericwarfare/mcg:/var/www/html
    - ./cloudflare:/etc/cloudflare/
  db:
    restart: always
    image: hsheth2/mysql-low-memory:5.6
    environment:
      MYSQL_DATABASE: midb
      MYSQL_ROOT_PASSWORD: root
    volumes:
    - db:/var/lib/mysql
```

