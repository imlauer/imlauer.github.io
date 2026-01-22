---
title: "Restaurar la base de datos MySQL desde archivos .ibd y .frm"
date: 2024-09-18T14:15:01-03:00
tags: ['sql']
---

https://stackoverflow.com/questions/26868956/restore-table-structure-from-frm-and-ibd-files

https://stackoverflow.com/questions/10934745/restore-the-mysql-database-from-frm-files

https://stackoverflow.com/questions/51997127/restore-mysql-database-using-only-frm-and-ibd-files

https://stackoverflow.com/questions/26868956/restore-table-structure-from-frm-and-ibd-files

Interesante: https://stackoverflow.com/questions/6804397/how-do-i-recreate-an-frm-file-for-an-mysql-innodb-table-with-only-the-ibdata-and

https://stackoverflow.com/questions/75090681/restore-table-from-frm-and-ibd-file

https://community.spiceworks.com/t/recover-mysql-database-from-frm-and-ibd-files/1014394

https://dba.stackexchange.com/questions/282448/recreating-database-from-ibd-files-no-frm

https://dba.stackexchange.com/questions/16875/restore-table-from-frm-and-ibd-file

https://dba.stackexchange.com/questions/316354/restoring-databases-using-only-frm-ibd-files

https://dba.stackexchange.com/questions/71596/restoring-mysql-tables-from-ibd-frm-and-mysqllogbin-files

https://dba.stackexchange.com/questions/241260/mysql-innodb-recover-from-frm-and-ibd

https://www.stellarinfo.com/article/restore-data-from-frm-ibd-files.php

https://serverfault.com/questions/1050154/how-to-restore-mysql-database-from-frm-and-ibd-files-on-localhost

https://serverfault.com/questions/115260/if-i-have-the-mysql-frm-myd-and-myi-files-can-i-recreate-the-db-without-sq

https://serverfault.com/questions/841983/how-to-combine-frm-and-ibd-file-in-mysql

https://serverfault.com/questions/364391/huge-sql-xxxx-xxxx-ibd-files-in-mysql-data-folder

https://serverfault.com/questions/225092/import-from-sql-into-mysql-ibd-files-missing

https://medium.com/@ilhamrisky21/restore-database-from-frm-and-ibd-files-easy-way-using-laragon-mysql-8b8d8cb73ffe

https://learn.microsoft.com/en-us/answers/questions/387106/how-to-recover-sql-just-from-frm-and-ibd-files

https://old.reddit.com/r/mysql/comments/15yzjrf/rebuild_a_broken_mysql_database_using_frm_or_ibd/

https://www.cigatisolutions.com/blog/recover-mysql-database-from-frm-and-ibd-files/

https://gist.github.com/luqmansungkar/a291fa4e9bf4b2b0dd011ad286cbcb13

---

Descargá dbsake:
```bash
curl -s http://get.dbsake.net > dbsake
chmod u+x dbsake
./dbsake --version
```

Extraé la información de la estructura de la tabla del archivo .frm usando dbsake:
`./dbsake frmdump /path/to/file.frm`

Usá la estructura de la tabla extraída para recrear la tabla. También podés recrear múltiples tablas usando el siguiente comando: 
```bash
for tbl in `ls -1 /path/to/*.frm`; do ./dbsake frmdump $tbl | mysql -u [user] -p[password] [database_name]; done;
```

Abrí la consola de mysql y ejecutá `ALTER TABLE [tbl_name] DISCARD TABLESPACE;` 
Este comando eliminará el actual `/var/lib/mysql/[schema_name]/[tbl_name].ibd`

Copiá tu archivo backup .ibd a `/var/lib/mysql/[schema_name]/`   
Necesita copiar los archivos `ib_logfiles` e `ibdata` en su carpeta de datos

Asegurate que el owner sea `mysql:mysql` con el comando `sudo chown -R mysql:mysql /var/lib/mysql` y ponele de permiso 660 con `chmod -R 660 /var/lib/mysql`.

Abrí otra vez la consola de mysql y ejecutá `ALTER TABLE [tbl_name] IMPORT TABLESPACE;`

`tbl_name`: se refiere al nombre de la tabla.

Listo.
