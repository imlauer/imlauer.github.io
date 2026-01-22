---
title: "Wordpress: HowTo"
date: 2024-09-13T17:17:52-03:00
tags: ['wordpress']
---
Primero instalamos mariadb (alternativa open-source a mysql) la configuramos y creamos una base de datos y tabla prueba.

```
sudo apt update
sudo apt install -y mariadb-server
sudo systemctl start mariadb
sudo systemctl enable mariadb
sudo systemctl status mariadb

// sudo mysql_secure_installation (comando deprecado)
sudo mariadb-install-db

sudo mysql
grant all on *.* to 'admin'@'%' identified by 'myawesomepass' with grant option;

// O en vez de '%' podés usar 'localhost'
grant all on *.* to 'admin'@'localhost' identified by 'myawesomepass' with grant option;

```
Luego desde tu usuario normal:
```
mysql -u admin@localhost -p
show databases;
create database db1;
use db1;
show tables;
create table names (id int primary key, name varchar(100) not null);
show tables;
quit
```

#### Diferentes formas de configurar el usuario creado:

https://phoenixnap.com/kb/how-to-create-mariadb-user-grant-privileges

#### Descargue wordpress:

https://wordpress.org/download/

#### Descomprimilo e instalalo.

`unzip wordpress*.zip`

#### Corré wordpress

```
cd wordpress
sudo php -S localhost:80 -t .
```

Luego de conectarte a http://localhost ingresá los datos de tu base de datos y procedé a instalar wordpress, estableciendo el nombre del sitio, el usuario del administrador del wordpress, contraseña, email, y si querés que los motores de búsqueda no te sigan.

##### Ahora procederemos a instalar los plugins.
