---
title: "Cómo hacer un backup de mysql y restaurarlo usando un volumen de docker"
date: 2023-09-26T07:13:42-03:00
tags: ['mysql','backup','docker']
---
Ejecutá esto desde la máquina host:
```bash
docker exec CONTAINER /usr/bin/mysqldump -u root --password=root DATABASE > backup.sql   
```
Para recuperarlo:
```bash
cat backup.sql | docker exec -i CONTAINER /usr/bin/mysql -u root --password=root DATABASE
```
