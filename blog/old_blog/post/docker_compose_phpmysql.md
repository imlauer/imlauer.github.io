---

title: "Docker compose con php y mysql"
date: 2024-09-22T13:52:06-03:00
---
https://alysivji.github.io/php-mysql-docker-containers.html


```bash
mkdir lamp-stack && cd lamp-stack
mkdir php
```
Creá un docker-compose.yml con el siguiente contenido:

```bash
# ./docker-compose.yml

version: '3'

services:
  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: my_secret_pw_shh
      MYSQL_DATABASE: test_db
      MYSQL_USER: devuser
      MYSQL_PASSWORD: devpass
    ports:
      - "9906:3306"
  web:
    image: php:7.2.2-apache
    container_name: php_web
    depends_on:
      - db
    volumes:
      - ./php/:/var/www/html/
    ports:
      - "8100:80"
    stdin_open: true
    tty: true
```

Dentro de la carpeta `php` creada anteriormente pone

```php
<!-- ./php/index.php -->

<html>
    <head>
        <title>Hello World</title>
    </head>

    <body>
        <?php
            echo "Hello, World!";
        ?>
    </body>
</html>
```

Levantalo con `docker-compose up`

Aunque en el `docker-compose` de **Kimkelen** usan link para que puedas ver la base de datos desde el otro contenedor, es decir te podés conectar a la base de datos con mysql -h db -u user -p (db es el host que se le asignó desde el docker-compose).

```bash
version: '2'
volumes:
  kimkelen-db:
services:
  app: &php-app
    build:
      context: ..
      dockerfile: docker/Dockerfile
    environment:
      MEMCACHE_HOST: memcache
      MEMCACHE_PORT: 11211
      DB_NAME: kimkelen
      DB_HOST: db
      DB_USERNAME: root
      DB_PASSWORD: root
      DEBUG: 'true'
      APACHE_RUN_GROUP: $APACHE_RUN_GROUP
      APACHE_RUN_USER: $APACHE_RUN_USER
      #    entrypoint: tail -f /dev/null
    ports:
      - "80:80"
    links:
      - memcache
      - db
    volumes:
      - ../:/app
      - /etc/passwd:/etc/passwd:ro
      - /etc/group:/etc/group:ro
  memcache:
    image: memcached:1.4
    command: -m 256
  db:
    image: mysql:5.6
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: kimkelen
    volumes:
      - kimkelen-db:/var/lib/mysql
    restart: unless-stopped
  phpmyadmin:
    image: phpmyadmin/phpmyadmin:latest
    environment:
      PMA_HOST: db
      PMA_USER: root
      PMA_PASSWORD: root
    ports:
      - "8071:80"
```


#### Montá el /etc/ directorio en el servidor (necesitás para cambiar la configuración de apache)
https://stackoverflow.com/questions/39176561/copying-files-to-a-container-with-docker-compose
