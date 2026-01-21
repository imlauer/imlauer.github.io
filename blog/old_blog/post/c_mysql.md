---
title: "Consultas MySQL en C y un simple servidor web"
date: 2024-10-03T12:19:50-03:00
tags: ['c']
---

Para entender por qué se usan lenguajes de alto nivel aprender primero a entender todos los problemas que trae programar en un lenguaje de bajo nivel.

Hay que aprender lenguaje ensamblador para saber por qué existe C, hay que aprender C para entender por qué existe C++, rust, python, php, etc. y cuales son los problemas que estos lenguajes intentan solucionar.

https://www.youtube.com/watch?v=jACHG6tZakw

https://www.ucl.ac.uk/isd/services/websites-apps/databases/mysql/calling-mysql-c

https://github.com/bloominstituteoftechnology/C-Web-Server

#### Archivo `mysql.c`:
```c
// sudo apt install -y libmariadb-dev-compat libmariadb-dev
// Compile: gcc -o mysql-test mysql.c $(mysql_config --libs)

#include <stdio.h>
#include <mysql/mysql.h>

int main() {
   MYSQL *conn;
   MYSQL_RES *res;
   MYSQL_ROW row;

   char *server = "localhost";
   char *user = "admin";
   char *password = "myawesomepass";
   char *database = "db1";
   
   conn = mysql_init(NULL);
   
   /* Connect to database */
   if (!mysql_real_connect(conn, server,
         user, password, database, 0, NULL, 0)) {
      fprintf(stderr, "%s\n", mysql_error(conn));
      return(0);
   }

   /* send SQL query */
   if (mysql_query(conn, "SELECT * FROM wp_users WHERE id = 1")) {
      fprintf(stderr, "%s\n", mysql_error(conn));
      return(0);
   }

   res = mysql_use_result(conn);
   
   /* output fields 1 and 2 of each row */
   while ((row = mysql_fetch_row(res)) != NULL)
      printf("%s %s\n", row[1], row[2]);

   /* Release memory used to store results and close connection */
   mysql_free_result(res);
   mysql_close(conn);
}
```
