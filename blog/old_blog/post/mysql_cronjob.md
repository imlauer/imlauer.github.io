---
title: "Mysql cronjob"
date: 2024-09-20T19:57:30-03:00
tags: ['mysql']
---

Esto es una pésima forma de hacer backups.

```bash
mkdir -p /home/miusuario/backup/database-backups && cd /home/miusuario/backup/database-backups
touch cron_backup.sh
chmod +x cron_backup.sh
```


Hay muchas mejores formas de hacer esto pero este es el script que lo usé un par de veces.

```bash
#!/bin/sh
#
# @author: Jabran Rafique <hello@jabran.me>
# @link: http://jabran.me/articles/automatic-database-backup-using-git-hosting/

# Set variables
FULLDATE      = $(date +"%Y-%d-%m %H:%M")
NOW           = $(date +"%Y-%m-%d-%H-%M")
# MYSQL_DUMP    = `which mysqldump`
MYSQL_DUMP    = "docker compose -f /home/miusuario/kimkelen/ exec db /usr/bin/mysqldump"
GIT           = `which git`
DB_NAME       = "kimkelen"
CRON_USER     = "root"
CRON_PASSWORD = "xxxx"
TEMP_BACKUP   = "latest_backup.sql"
BACKUP_DIR    = $(date +"%Y/%m")

# Check current Git status and update
${GIT} status
${GIT} pull origin HEAD

# Dump database
${MYSQL_DUMP} -u "$CRON_USER" -p "$CRON_PASSWORD" $DB_NAME > $TEMP_BACKUP 
wait

# Make backup directory if not exists (format: {year}/{month}/)
if [ ! -d "$BACKUP_DIR" ]; then
  mkdir -p $BACKUP_DIR
  fi

  # Compress SQL dump
  tar -cvzf $BACKUP_DIR/$DB_NAME-$NOW-sql.tar.gz $TEMP_BACKUP

  # Remove original SQL dump
  rm -f $TEMP_BACKUP

  # Add to Git and commit
  ${GIT} add -A
  ${GIT} commit -m "Automatic backup - $FULLDATE"
  ${GIT} push origin HEAD
```



---

#### Al final lo terminé dejando así:

Esto es necesario para que find lo ignore:     
`mv cron_backup.sh .cron_backup.sh`

crontab -e 

```bash
@weekly cd /home/xxx/backup/database-backups; /home/xxx/backup/database-backups/.cron_backup.sh > /dev/null 2>&1
```

---

```bash

#!/bin/bash
#
# @author: Jabran Rafique <hello@jabran.me>
# @link: http://jabran.me/articles/automatic-database-backup-using-git-hosting/

# Set variables
FULLDATE=$(date +"%Y-%d-%m %H:%M")
NOW=$(date +"%Y-%m-%d-%H-%M")
# MYSQL_DUMP=`which mysqldump`
DOCKER=`which docker`
DOCKER_COMPOSE="/home/epet36misiones/kimkelen/docker-compose.yml"
DOCKER_DB_SERVICE="db"
GIT=`which git`
DB_NAME="kimkelen"
CRON_USER="root"
CRON_PASSWORD="xx"
TEMP_BACKUP="latest_backup.sql"
BACKUP_DIR=$(date +"%Y/%m")

# Check current Git status and update
${GIT} status
${GIT} pull origin HEAD

# Dump database
$DOCKER compose -f $DOCKER_COMPOSE exec $DOCKER_DB_SERVICE /usr/bin/mysqldump -u "$CRON_USER" --password="$CRON_PASSWORD" $DB_NAME > $TEMP_BACKUP

# Make backup directory if not exists (format: {year}/{month}/)
if [ ! -d "$BACKUP_DIR" ]; then
  mkdir -p $BACKUP_DIR
fi

# Compress SQL dump
tar -cvzf $BACKUP_DIR/$DB_NAME-$NOW-sql.tar.gz $TEMP_BACKUP

# Remove original SQL dump
rm -f $TEMP_BACKUP

# Remove all backups older than 60 days
find /home/epet36misiones/backup/database-backups/ -not -path '*/.*' -type f -mtime +60 -delete

# Add to Git and commit
${GIT} add -A
${GIT} commit -m "Automatic backup - $FULLDATE"
${GIT} push origin HEAD
```
