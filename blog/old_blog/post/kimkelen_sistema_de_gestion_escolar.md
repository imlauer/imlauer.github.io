---
title: "Kimkelen: sistema de gestion escolar GRATUITO"
date: 2024-06-25T23:45:45-03:00
tags: ['kimkelen','sistema','escolar','gratis']
---
Si estás buscando un sistema de gestión escolar gratis Argentino. Esta es una de las mejores opciones.

[https://github.com/desarrollo-cespi/kimkelen](https://github.com/desarrollo-cespi/kimkelen)

Existen otros sitemas como RosarioSIS, pero aún no la he probado profesionalmente, Kimkelen sí aunque tiene algunos problemas funciona bastante bien.

Funcionalidades que faltan implementar:
· Equivalencias.

---

### Como instalarlo y configurarlo:

Instalá docker, agregá tu usuario como parte de ese grupo y deslogueate y volvé a ingresar:
```bash
sudo pacman -S docker docker-compose
sudo systemctl start docker.service
sudo usermod -aG docker $USER
```

Seguí este readme: https://github.com/desarrollo-cespi/kimkelen
#### el docker-compose.yml que está en su readme está mal escrito

Es ideal quitar el puerto 80 acá por cuestiones de seguridad.
Acá **monté un volumen llamado cloudflare**. Los volumenes son directorios(carpetas) compartidas entre docker y el host(tu PC), en este caso lo usé para compartir los archivos de configuración del ssl.

### Usá este.
```bash
version: '2'
volumes:
  db:
  disciplinary-sanction-documents:
  justification-documents:
  persons-photos:
services:
  app:
    restart: always
    image: registry.gitlab.com/kimkelen/kimkelen:latest
    #image: my-web-app
    environment:
      DB_HOST: db
      DB_NAME: kimkelen
      DB_USERNAME: root
      DB_ENCODING: utf8
      DB_PASSWORD: root
      DB_PORT: 3306
      DEBUG: 'false'
      FLAVOR: elflavordetuescuela
      MEMCACHE_HOST: memcache
      MEMCACHE_PORT: '11211'
      TESTING: 'false'
      MAIL_PORT: 25
      MAIL_HOST: localhost
      FACEBOOK_ID: 'demo'
      FACEBOOK_SECRET: 'demo'
    ports:
    - 80:80
    - 443:443
    volumes:
    - disciplinary-sanction-documents:/app/data/disciplinary-sanction-documents
    - justification-documents:/app/data/justification-documents
    - persons-photos:/app/data/persons-photos
    - ./cloudflare:/etc/cloudflare/
  memcache:
    restart: always
    image: memcached:1.4
    command:
    - -m
    - '256'
  db:
    restart: always
    image: hsheth2/mysql-low-memory:5.6
    environment:
      MYSQL_DATABASE: kimkelen
      MYSQL_ROOT_PASSWORD: root
    volumes:
    - db:/var/lib/mysql

```
Lo levantás con `docker-compose up` o `docker compose up`

#### Para poder reconstruir la imágen cada vez que hacemos un cambio del repositorio kimkelen tenemos que cambiar el FROM del `docker/Dockerfile` porque está mal:
Cambia el from por:
```
FROM registry.gitlab.com/kimkelen/kimkelen:base-latest
```

---

#### Creá un flavor(sabor) copiando el flavor de otra carpeta y cambiando los logos, esto esta explicado mejor en un archivo que tengo aparte.
**Como crear un nuevo sabor:**

Tenes que copiar algun otro sabor ya existente y ingresar a la carpeta del sabor lib y ahi cambiar todos los nombres del antiguo sabor al nuevo.

Por ejemplo:

```bash
cp -R agropecuaria nombredemiescuela  
cd nombredemiescuela/lib/behavior
```

Ahora si te copiaste el flavor de Anexa los archivos se llamaran por ejemplo `AnexaEvaluatorBehaviour.class.php`. Tenes que reemplazar Anexa por el nuevo nombre del sabor por ejemplo `nombredemiescuela`, esto se hace con el siguiente comando:
Reemplazar el nombre de los archivos:
```
for i in *; do mv "$i" "`echo $i | sed "s/Agropecuaria/Nombredemiescuela/"`"; done
```
**Movete a los subdirectorios y ejecutá ese mismo comando**: Es decir
```
cd factory
for i in *; do mv "$i" "`echo $i | sed "s/Agropecuaria/Nombredemiescuela/"`"; done
cd ..
cd filter
for i in *; do mv "$i" "`echo $i | sed "s/Agropecuaria/Nombredemiescuela/"`"; done
etc
```

Se puede usar `find` para que recorra todos los subdirectorios en vez de moverte.  
Por ejemplo: 

```
for i in $(find . -type f -print); do mv "$i" "`echo $i | sed "s/Agropecuaria/Nombredemiescuela/"`";  done
```
**(No lo probé)**

---

Luego tenes que reemplazar el nombre de la clase adentro de cada archivo , con el siguiente comando, dentro de la misma carpeta:
```
find ./ -type f -exec sed -i -e 's/Agropecuaria/Nombredemiescuela/g' {} \;
```

Y listo, ahora podemos cambiar cosas como el logo del boletin etc.

Para cambiar el logo podemos ir a `flavors/nombredemiescuela/web/images/` y buscar y reemplazar por cada logo de otra escuela por el nuestro.


Cambiá todas las ocurrencias del nombre de la escuela vieja, usando `grep` situado en flavors en que archivos aparece y reemplazalos: `grep -i agropecuaria -r *`

Por ejemplo acá hay un archivo: `flavors/nombredemiescuela/modules/examination_subject/templates/printStudentsSuccess.php` que tiene un nombre de colegio.

Otro: `flavors/nombredemiescuela/lib/behaviour/NombredemiescuelaSchoolBehaviour.class.php`

---

### Creá un archivo de configuración extra, hice esto porque no te deja pisar la configuración de apache hay una forma pero yo lo hice así:
`cp config/extra.conf /etc/apache2/conf.d/extra.conf` (esto lo puse en el entrypoint para que copie cada vez que recompilo la imágen que no era necesario porque lo agregué también al Dockerfile) 
```
ServerName miescuelanombre.edu.ar

<LocationMatch /uploads/.*>
     php_flag engine off
</LocationMatch>

<Directory /app/web >
      RewriteEngine On
      # uncomment the following line, if you are having trouble
      # getting no_script_name to work
      #RewriteBase /

      # we skip all files with .something
      #RewriteCond %{REQUEST_URI} \..+$
      #RewriteCond %{REQUEST_URI} !\.html$
      #RewriteRule .* - [L]

      # we check if the .html version is here (caching)
      RewriteRule ^$ index.html [QSA]
      RewriteRule ^([^.]+)$ $1.html [QSA]
      RewriteCond %{REQUEST_FILENAME} !-f

      # no, so we redirect to our front web controller
      RewriteRule ^(.*)$ index.php [QSA,L]
</Directory>

<VirtualHost *:80>
  DocumentRoot "/app/web/"
  ServerAdmin admin@miescuelanombre.edu.ar
  <Directory "/app/web">
      Options -Indexes +FollowSymLinks -MultiViews
      AllowOverride None
      Order allow,deny
      allow from all
  </Directory>
  #Redirect permanent / https://miescuelanombre.edu.ar
</VirtualHost>
```
Es recomendable redirigir todo el trafico del puerto 80 a https(443) para comentá todo dentro VirtualHost menos la directiva Redirect.


#### Borrá web/.htaccess
##### docker/entrypoint
```
#!/bin/sh
 set -eo pipefail

source /usr/local/bin/setenvdefaults

echo -e "expose_php = Off\n"\
	"date.timezone = $TIMEZONE\n"\
        "memory_limit = $MEMORY_LIMIT\n"\
        "max_execution_time = $MAX_EXECUTION_TIME\n" > /usr/local/etc/php/conf.d/php.ini

envsubst '${DB_NAME} ${DB_HOST} ${DB_USERNAME} ${DB_PASSWORD}' < /app/config/propel.ini.docker > /app/config/propel.ini

cp config/extra.conf /etc/apache2/conf.d/extra.conf
#cp config/ssl.conf /etc/apache2/conf.d/ssl.conf
#cp config/apache2-foreground /usr/local/bin/apache2-foreground

echo 'SetEnvIf Request_URI "^/robots.txt$" dontlog' > /etc/apache2/conf.d/docker.conf
echo 'CustomLog logs/access.log combined env=!dontlog' >> /etc/apache2/conf.d/docker.conf 
echo 'ServerTokens Prod' >> /etc/apache2/conf.d/docker.conf 
echo 'ServerSignature Off' >> /etc/apache2/conf.d/docker.conf 
echo 'TraceEnable Off' >> /etc/apache2/conf.d/docker.conf 



CMD='cd /app && rm -fr cache/* && ./symfony propel:build-all --classes-only && ./symfony plugin:publish && ./symfony fix-perms && ./symfony kimkelen:flavor $FLAVOR'

if [ -z "$APACHE_RUN_USER" ]; then
  sh -c "$CMD"
else
  su $APACHE_RUN_USER -c "$CMD"
fi

exec /usr/local/bin/original-docker-php-entrypoint "$@"
```

---

#### Importante

**Tenés que arreglar los permisos a apache a las carpetas, esto lo hice modificando el `Dockerfile`, y tenés que instalar `apache2-ssl` para que funcione el ssl.**

```bash
FROM registry.gitlab.com/kimkelen/kimkelen:base-latest

RUN mv /usr/local/bin/docker-php-entrypoint /usr/local/bin/original-docker-php-entrypoint
ADD docker/entrypoint /usr/local/bin/docker-php-entrypoint
ADD docker/setenvdefaults /usr/local/bin/setenvdefaults
ADD . /app
RUN rm /app/web/*_dev.php
ENV APACHE_DOCUMENT_ROOT=/app/web/ \
    DB_ENCODING=utf8
ARG REVISION
ENV VERSION=$REVISION
WORKDIR /app
RUN chown -R apache /app/data
COPY config/extra.conf /etc/apache2/conf.d/extra.conf
RUN apk add -U --no-cache apache2-ssl
COPY config/ssl.conf /etc/apache2/conf.d/ssl.conf
```


#### config/ssl.conf
```bash
#
# This is the Apache server configuration file providing SSL support.
# It contains the configuration directives to instruct the server how to
# serve pages over an https connection. For detailed information about these 
# directives see <URL:http://httpd.apache.org/docs/2.4/mod/mod_ssl.html>
# 
# Do NOT simply read the instructions in here without understanding
# what they do.  They're here only as hints or reminders.  If you are unsure
# consult the online docs. You have been warned.  
#
# Required modules: mod_log_config, mod_setenvif, mod_ssl,
#          socache_shmcb_module (for default value of SSLSessionCache)
LoadModule ssl_module modules/mod_ssl.so
LoadModule socache_shmcb_module modules/mod_socache_shmcb.so

#
# Pseudo Random Number Generator (PRNG):
# Configure one or more sources to seed the PRNG of the SSL library.
# The seed data should be of good random quality.
# WARNING! On some platforms /dev/random blocks if not enough entropy
# is available. This means you then cannot use the /dev/random device
# because it would lead to very long connection times (as long as
# it requires to make more entropy available). But usually those
# platforms additionally provide a /dev/urandom device which doesn't
# block. So, if available, use this one instead. Read the mod_ssl User
# Manual for more details.
#
#SSLRandomSeed startup file:/dev/random  512
SSLRandomSeed startup file:/dev/urandom 512
SSLRandomSeed connect builtin
#SSLRandomSeed connect file:/dev/random  512
#SSLRandomSeed connect file:/dev/urandom 512


#
# When we also provide SSL we have to listen to the 
# standard HTTP port (see above) and to the HTTPS port
#
Listen 443

##
##  SSL Global Context
##
##  All SSL configuration in this context applies both to
##  the main server and all SSL-enabled virtual hosts.
##

#   SSL Cipher Suite:
#   List the ciphers that the client is permitted to negotiate,
#   and that httpd will negotiate as the client of a proxied server.
#   See the OpenSSL documentation for a complete list of ciphers, and
#   ensure these follow appropriate best practices for this deployment.
#   httpd 2.2.30, 2.4.13 and later force-disable aNULL, eNULL and EXP ciphers,
#   while OpenSSL disabled these by default in 0.9.8zf/1.0.0r/1.0.1m/1.0.2a.
SSLCipherSuite HIGH:MEDIUM:!MD5:!RC4:!3DES:!ADH
SSLProxyCipherSuite HIGH:MEDIUM:!MD5:!RC4:!3DES:!ADH

#  By the end of 2016, only TLSv1.2 ciphers should remain in use.
#  Older ciphers should be disallowed as soon as possible, while the
#  kRSA ciphers do not offer forward secrecy.  These changes inhibit
#  older clients (such as IE6 SP2 or IE8 on Windows XP, or other legacy
#  non-browser tooling) from successfully connecting.  
#
#  To restrict mod_ssl to use only TLSv1.2 ciphers, and disable
#  those protocols which do not support forward secrecy, replace
#  the SSLCipherSuite and SSLProxyCipherSuite directives above with
#  the following two directives, as soon as practical.
# SSLCipherSuite HIGH:MEDIUM:!SSLv3:!kRSA
# SSLProxyCipherSuite HIGH:MEDIUM:!SSLv3:!kRSA

#   User agents such as web browsers are not configured for the user's
#   own preference of either security or performance, therefore this
#   must be the prerogative of the web server administrator who manages
#   cpu load versus confidentiality, so enforce the server's cipher order.
SSLHonorCipherOrder on 

#   SSL Protocol support:
#   List the protocol versions which clients are allowed to connect with.
#   Disable SSLv3 by default (cf. RFC 7525 3.1.1).  TLSv1 (1.0) should be
#   disabled as quickly as practical.  By the end of 2016, only the TLSv1.2
#   protocol or later should remain in use.
SSLProtocol all -SSLv3
SSLProxyProtocol all -SSLv3

#   Pass Phrase Dialog:
#   Configure the pass phrase gathering process.
#   The filtering dialog program (`builtin' is an internal
#   terminal dialog) has to provide the pass phrase on stdout.
SSLPassPhraseDialog  builtin

#   Inter-Process Session Cache:
#   Configure the SSL Session Cache: First the mechanism 
#   to use and second the expiring timeout (in seconds).
#SSLSessionCache         "dbm:/run/apache2/ssl_scache"
SSLSessionCache        "shmcb:/var/cache/mod_ssl/scache(512000)"
SSLSessionCacheTimeout  300

#   OCSP Stapling (requires OpenSSL 0.9.8h or later)
#
#   This feature is disabled by default and requires at least
#   the two directives SSLUseStapling and SSLStaplingCache.
#   Refer to the documentation on OCSP Stapling in the SSL/TLS
#   How-To for more information.
#
#   Enable stapling for all SSL-enabled servers:
#SSLUseStapling On

#   Define a relatively small cache for OCSP Stapling using
#   the same mechanism that is used for the SSL session cache
#   above.  If stapling is used with more than a few certificates,
#   the size may need to be increased.  (AH01929 will be logged.)
#SSLStaplingCache "shmcb:/run/apache2/ssl_stapling(32768)"

#   Seconds before valid OCSP responses are expired from the cache
#SSLStaplingStandardCacheTimeout 3600

#   Seconds before invalid OCSP responses are expired from the cache
#SSLStaplingErrorCacheTimeout 600

##
## SSL Virtual Host Context
##

<VirtualHost _default_:443>
DocumentRoot "/app/web/"
ServerAdmin admin@miescuelanombre.edu.ar
ServerAlias www.miescuelanombre.edu.ar:443
<Directory "/app/web">
    Options -Indexes +FollowSymLinks -MultiViews
    AllowOverride None
    Order allow,deny
    allow from all
</Directory>
#DocumentRoot "/var/www/localhost/htdocs"
#ServerName www.example.com:443
#ServerAlias www.miescuelanombre.edu.ar:443
#ServerAdmin you@example.com
#ErrorLog logs/ssl_error.log
ErrorLog logs/error.log
TransferLog logs/access.log

#   SSL Engine Switch:
#   Enable/Disable SSL for this virtual host.
SSLEngine on

#   Server Certificate:
#   Point SSLCertificateFile at a PEM encoded certificate.  If
#   the certificate is encrypted, then you will be prompted for a
#   pass phrase.  Note that a kill -HUP will prompt again.  Keep
#   in mind that if you have both an RSA and a DSA certificate you
#   can configure both in parallel (to also allow the use of DSA
#   ciphers, etc.)
#   Some ECC cipher suites (http://www.ietf.org/rfc/rfc4492.txt)
#   require an ECC certificate which can also be configured in
#   parallel.
SSLCertificateFile /etc/cloudflare/server.pem
#SSLCertificateFile /etc/ssl/apache2/server-dsa.pem
#SSLCertificateFile /etc/ssl/apache2/server-ecc.pem

#   Server Private Key:
#   If the key is not combined with the certificate, use this
#   directive to point at the key file.  Keep in mind that if
#   you've both a RSA and a DSA private key you can configure
#   both in parallel (to also allow the use of DSA ciphers, etc.)
#   ECC keys, when in use, can also be configured in parallel
SSLCertificateKeyFile /etc/cloudflare/server.key
#SSLCertificateKeyFile /etc/ssl/apache2/server-dsa.key
#SSLCertificateKeyFile /etc/ssl/apache2/server-ecc.key

#   Server Certificate Chain:
#   Point SSLCertificateChainFile at a file containing the
#   concatenation of PEM encoded CA certificates which form the
#   certificate chain for the server certificate. Alternatively
#   the referenced file can be the same as SSLCertificateFile
#   when the CA certificates are directly appended to the server
#   certificate for convenience.
#SSLCertificateChainFile /etc/ssl/apache2/server-ca.pem

#   Certificate Authority (CA):
#   Set the CA certificate verification path where to find CA
#   certificates for client authentication or alternatively one
#   huge file containing all of them (file must be PEM encoded)
#   Note: Inside SSLCACertificatePath you need hash symlinks
#         to point to the certificate files. Use the provided
#         Makefile to update the hash symlinks after changes.
#SSLCACertificatePath /etc/ssl/apache2/ssl.crt
#SSLCACertificateFile /etc/ssl/apache2/ssl.crt/ca-bundle.pem

#   Certificate Revocation Lists (CRL):
#   Set the CA revocation path where to find CA CRLs for client
#   authentication or alternatively one huge file containing all
#   of them (file must be PEM encoded).
#   The CRL checking mode needs to be configured explicitly
#   through SSLCARevocationCheck (defaults to "none" otherwise).
#   Note: Inside SSLCARevocationPath you need hash symlinks
#         to point to the certificate files. Use the provided
#         Makefile to update the hash symlinks after changes.
#SSLCARevocationPath /etc/ssl/apache2/ssl.crl
#SSLCARevocationFile /etc/ssl/apache2/ssl.crl/ca-bundle.crl
#SSLCARevocationCheck chain

#   Client Authentication (Type):
#   Client certificate verification type and depth.  Types are
#   none, optional, require and optional_no_ca.  Depth is a
#   number which specifies how deeply to verify the certificate
#   issuer chain before deciding the certificate is not valid.
#SSLVerifyClient require
#SSLVerifyDepth  10

#   TLS-SRP mutual authentication:
#   Enable TLS-SRP and set the path to the OpenSSL SRP verifier
#   file (containing login information for SRP user accounts). 
#   Requires OpenSSL 1.0.1 or newer. See the mod_ssl FAQ for
#   detailed instructions on creating this file. Example:
#   "openssl srp -srpvfile /etc/apache2/passwd.srpv -add username"
#SSLSRPVerifierFile "/etc/apache2/passwd.srpv"

#   Access Control:
#   With SSLRequire you can do per-directory access control based
#   on arbitrary complex boolean expressions containing server
#   variable checks and other lookup directives.  The syntax is a
#   mixture between C and Perl.  See the mod_ssl documentation
#   for more details.
#<Location />
#SSLRequire (    %{SSL_CIPHER} !~ m/^(EXP|NULL)/ \
#            and %{SSL_CLIENT_S_DN_O} eq "Snake Oil, Ltd." \
#            and %{SSL_CLIENT_S_DN_OU} in {"Staff", "CA", "Dev"} \
#            and %{TIME_WDAY} >= 1 and %{TIME_WDAY} <= 5 \
#            and %{TIME_HOUR} >= 8 and %{TIME_HOUR} <= 20       ) \
#           or %{REMOTE_ADDR} =~ m/^192\.76\.162\.[0-9]+$/
#</Location>

#   SSL Engine Options:
#   Set various options for the SSL engine.
#   o FakeBasicAuth:
#     Translate the client X.509 into a Basic Authorisation.  This means that
#     the standard Auth/DBMAuth methods can be used for access control.  The
#     user name is the `one line' version of the client's X.509 certificate.
#     Note that no password is obtained from the user. Every entry in the user
#     file needs this password: `xxj31ZMTZzkVA'.
#   o ExportCertData:
#     This exports two additional environment variables: SSL_CLIENT_CERT and
#     SSL_SERVER_CERT. These contain the PEM-encoded certificates of the
#     server (always existing) and the client (only existing when client
#     authentication is used). This can be used to import the certificates
#     into CGI scripts.
#   o StdEnvVars:
#     This exports the standard SSL/TLS related `SSL_*' environment variables.
#     Per default this exportation is switched off for performance reasons,
#     because the extraction step is an expensive operation and is usually
#     useless for serving static content. So one usually enables the
#     exportation for CGI and SSI requests only.
#   o StrictRequire:
#     This denies access when "SSLRequireSSL" or "SSLRequire" applied even
#     under a "Satisfy any" situation, i.e. when it applies access is denied
#     and no other module can change it.
#   o OptRenegotiate:
#     This enables optimized SSL connection renegotiation handling when SSL
#     directives are used in per-directory context. 
#SSLOptions +FakeBasicAuth +ExportCertData +StrictRequire
<FilesMatch "\.(cgi|shtml|phtml|php)$">
    SSLOptions +StdEnvVars
</FilesMatch>
#<Directory "/var/www/localhost/cgi-bin">
#    SSLOptions +StdEnvVars
#</Directory>

#   SSL Protocol Adjustments:
#   The safe and default but still SSL/TLS standard compliant shutdown
#   approach is that mod_ssl sends the close notify alert but doesn't wait for
#   the close notify alert from client. When you need a different shutdown
#   approach you can use one of the following variables:
#   o ssl-unclean-shutdown:
#     This forces an unclean shutdown when the connection is closed, i.e. no
#     SSL close notify alert is sent or allowed to be received.  This violates
#     the SSL/TLS standard but is needed for some brain-dead browsers. Use
#     this when you receive I/O errors because of the standard approach where
#     mod_ssl sends the close notify alert.
#   o ssl-accurate-shutdown:
#     This forces an accurate shutdown when the connection is closed, i.e. a
#     SSL close notify alert is send and mod_ssl waits for the close notify
#     alert of the client. This is 100% SSL/TLS standard compliant, but in
#     practice often causes hanging connections with brain-dead browsers. Use
#     this only for browsers where you know that their SSL implementation
#     works correctly. 
#   Notice: Most problems of broken clients are also related to the HTTP
#   keep-alive facility, so you usually additionally want to disable
#   keep-alive for those clients, too. Use variable "nokeepalive" for this.
#   Similarly, one has to force some clients to use HTTP/1.0 to workaround
#   their broken HTTP/1.1 implementation. Use variables "downgrade-1.0" and
#   "force-response-1.0" for this.
BrowserMatch "MSIE [2-5]" \
         nokeepalive ssl-unclean-shutdown \
         downgrade-1.0 force-response-1.0

#   Per-Server Logging:
#   The home of a custom SSL log file. Use this when you want a
#   compact non-error SSL logfile on a virtual host basis.
#CustomLog logs/ssl_request.log \
CustomLog logs/access.log \
          "%t %h %{SSL_PROTOCOL}x %{SSL_CIPHER}x \"%r\" %b"

</VirtualHost>                                  

```

Todos los archivos por defecto toman la configuración de los archivos que están en /lib/ salvo que estén presentes en el flavor si el mismo nombre de archivo está presente en el flavor pisa el archivo por defecto que está en /lib/.


Podés cambiar por ejemplo:
`flavors/miescuelanombre/lib/behavior/MiescuelanombreEvaluatorBehaviour.class.php`    
```
    self::DECEMBER => 'Diciembre',
    self::FEBRUARY => 'Febrero',
```
Lo cambiamos por
```
    self::DECEMBER => 'PEEE-dic',
    self::FEBRUARY => 'PEEE-feb',
```

Después tenés que cambiar los mensajes en por ejemplo `flavors/miescuelanombre/i18n/messages.es.xml`
`La Plata` cambialo por la ciudad de tu colegio.

`flavors/miescuelanombre/config/view.yml`:
```
title:         Liceo Víctor Mercante - UNLP
description:   Liceo Víctor Mercante - UNLP
keywords:      liceo, victor, mercante, unlp
```
**Cambiala por el nombre de tu colegio.**

Cambiá también el nombre de la otra escuela en todos los documentos: `flavors/minombreescuela/modules/student/templates/_analytical_header_text.php` y `flavors/minombreescuela/modules/student/templates/_certificate_regular_text.php` `flavors/minombreescuela/modules/student/templates/_analytical_footer_signatures.php` y en todas las demás ocurrencias buscalas con `grep -i agropecuaria -r *` y editá los nombres del director del colegio y de la vice. Cambiá todos los logos.

```
flavors/miescuelanombre/modules/student/templates/_analytical_header.php
```

---

# Algunos problemas en el código 
#### Hay que aplicar parches para que los preceptores puedan imprimir el boletín.
El nombre del parche no recuerdo pero si te ubicás en `patch` y ejecutás `grep "preceptores" -r *`.

#### Que se puedan agregar notas con decimal: `lib/form/CourseSubjectMarksForm.class.php`:


Cambiá `sfValidatorInteger` por `sfValidatorNumber`


#### Cierre de ciclo (tenés que hacerlo cada año o poner una variable):        

Tenés que cambiar esta variable en `lib/model/SchoolYear.php`
```php
    $lastYear = (int)2023;
```

Por

```php
    $lastYear = (int)(date('Y'))-1;
```

Cambia en `lib/model/SchoolYear.php` y `lib/school_behaviour/base/BaseAnalyticalBehaviour.class.php` busca con `grep 2021 -r *` diferentes años y cambia `lastYear` y un array.


```php
    if (count(ExaminationPeer::retrieveForSchoolYearAndExaminationNumber($this, SchoolBehaviourFactory::getEvaluatorInstance()->getFebruaryExaminationNumber())) == 0 && $this->year != 2022)
```

Por

```php
    $lastYear = (int)(date('Y'))-1;
    if (count(ExaminationPeer::retrieveForSchoolYearAndExaminationNumber($this, SchoolBehaviourFactory::getEvaluatorInstance()->getFebruaryExaminationNumber())) == 0 && $this->year != $lastYear)
```

Tenés que ir agregando los años en `$years  = array(2023,2024,2025,...);`


--- 

#### Agregar observaciones al boletín

Se hace modificando el archivo `flavors/miescuelanombre/modules/report_card/templates/_footer.php`:


```php
<p><?php echo $student->getPerson()->getObservations(); ?> </p>
```

---

**Si tenés dudas sobre los pasos de como generar la imagen, hacer el backup y comprobar si todo funciona bien mandame un correo y te envío los pasos.**

##### Cada vez que hacés un cambio hay que generar la imágen 
```bash
docker build . -t my-web-app -f docker/Dockerfile
```

#### Eliminá contenedores e imágenes viejas
```bash
docker rm -vf $(docker ps -aq) && docker rmi -f $(docker images -aq)
```

Si todo funciona bien subí la imagen a dockerhub para posteriormente bajarla desde el servidor, podés usar el mismo nombre o cambiar el nombre si cambias el nombre tendrás que cambiar el nombre en el `docker-compose.yml image:` y borrar la imagen vieja.

```bash
docker login  
docker images  
docker tag my-web-app:latest dresuer/kimkelen-notasdecimal_fix  
docker push dresuer/kimkelen-notasdecimal_fix  
```

`docker compose stop` y automáticamente se borraran los contenedores en uso y luego `docker compose up -d`

No te debería crear una imágen nueva de la base de datos ni tampoco te debería tirar un error de 500. Si te pasa esto es porque tu `docker-compose.yml` está mal configurado. Al comienzo `volume: db:` tiene que tener el mismo nombre que `db: volume: db:/var/lib/mysql`

### Quizás tengas que borrar la imagen vieja.
```bash
docker image prune --all --filter "until=4320h" # delete images older than 6 months ago; 4320h = 24 hour/day * 30 days/month * 6 months

# the following command will delete images older than 48 hours.
docker image prune --all --filter until=48h
```

O `docker rmi -f <Image>`

Acordate que la opción `-f` fuerza la eliminación.




#### Como hacer un cambio en el código:
Agregamos la firma.

```bash
cp firma_director.png ~/projects/kimkelen/flavors/epet36/web/images/
vim ~/projects/kimkelen/flavors/epet36/modules/report_card/templates/_footer.php
```
Debajo del `<div class="rowfirm_authority">` agregá `<img src="/images/firma_directo.png" width="82%" height="82%"/>`

Agregá en el `.gitignore` una línea para que no pushee la firma del director (`/flavors/epet36/web/images/firma_director.png`).

Pushea los cambios al repositorio `git add . && git commit -m "agregué firma" && git push`

Ahora tenés que reconstruir la imagen con el comando:
```bash
docker build . -t my-web-app -f docker/Dockerfile
```

y tagearla y subirla a docker hub
```bash
docker login  
docker tag my-web-app:latest dresuer/kimkelen-epet36-observations
docker push dresuer/kimkelen-epet36-observations 
```

Luego conectarte a la VPS y descargar la imagen (poné el mismo nombre así no hay tanto lío)

Ahora ingresá a la VPN ejecutá `docker compose stop` y luego `docker compose up -d`
O si así no funciona podés usar `docker-compose pull  && docker-compose up -d`

