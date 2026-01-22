---
title: "MySQL consultas"
date: 2024-10-13T15:47:16-03:00
tags: ['mysql']
---
```mysql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```


DATE = NOW();

#### ¿Cómo acceder a un servicio web de base de datos MySQL a través de LAN? [cerrado]

```bash
sudo vim mariadb.conf.d/50-server.cnf
```
En vez de 127.0.0.1 cambialo por
```bash
bind-address            = 0.0.0.0
```


Luego: `sudo systemctl restart mariadb`

Ahora ya deberías poder acceder de la siguiente manera: `mysql -u admin -p -h 192.168.0.146`
