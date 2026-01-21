---
title: "Lamp server"
date: 2024-09-26T12:39:55-03:00
tags: ['lamp']
---
[lamp_server](/files/upwork_job_desc_lamp_server_a2.pdf)

#### Objective
Configure Linux server. Genrally speaking, this is a LAMP server.
#### Description
* Provided
    * EC2 server with ssh access on AWS with AWS Linux installed with up to date OS. Server will be x86 64 bit.
    * Public IP for ssh and www access
    * A user with ssh access and a key file for ssh
    * Server firewall will be open


* Domain names: clearlight.one, clearlight.app


* Install and configure following software:
    * Amazon utilities: amazon-ec2-utils
    * AWS CLI version 2 version 2.15.17 (current version)
    * Cron: cronie version 1.5.7 (current version)
    * Python 3 3.9.16 (current version)
    * PHP 8.2.9 (current version)
    * Apache HTTPD version 2.4.58 (current version)
    * MySQL 8.4.2 LTS community (current version)
    * Certbot: certbot version 2.6.0 (current version)
    * Python for certbot: python-certbot-apache
    * net-tools.x86_64
    * wget
    * mod_ssl for httpd


* Configure httpd
    * http port 80 redirects to https port 443 for both domains.
    * www.clearlight.one alias for clearlight.one
    * www.clearlight.app alias for clearlight.app

* Install HTTPD module mod_ssl

* Change mysql root password

* Install PHP modules if not already there
    * php-pdo.x86_64
    * php-mbstring.x86_64
    * php-mysql.x86_64
    * php8.1-mysqlnd.x86_64
    * php-common
    * php-process
    * php-xml
    * php-gd
    * php-dba

* Host name is set to clearlight.app

* Use certbot for SSL certificates
    * `sudo certbot -d clearlight.one -d *clearlight.one --apache`
    * `sudo certbot -d clearlight.app -d *clearlight.app --apache`

* Contact will be available to answer questions via email and whatsapp

#### Skills Required
* Unix system administration
* Command line proficiency
* Familiar with above listed software and their configuration

#### Milestones and Payment
* To be discusssed

#### Timeframe
* Build within 48 hours of taking on work

#### Verification
* aws -version shows AWS CLI version 2 and Python 3.
* hostname shows clearlight.app
* HTTPD runs on boot and is accessible from www https and http for domains
    * clearlight.one
    * clearlight.app
* mysqld runs or boot accessible from PHP and shell script
* Cron runs on boot
* SSH runs on boot
* SSL certificate via certbot, https is working with valid certificates from
letsencrypt.org
* Application software is installed on server runs correctly

---

### Español

#### Objetivo
Configurar un servidor Linux. En términos generales, se trata de un servidor LAMP.
#### Descripción
* Proporcionado
    * Servidor EC2 con acceso SSH en AWS con AWS Linux instalado con un sistema operativo actualizado. El servidor será x86 de 64 bits.
    * IP pública para acceso ssh y www
    * Un usuario con acceso ssh y un archivo de clave para ssh
    * El firewall del servidor estará abierto

* Nombres de dominio: clearlight.one, clearlight.app

* Instalar y configurar el siguiente software:
    * Utilidades de Amazon: amazon-ec2-utils
    * AWS CLI versión 2 versión 2.15.17 (versión actual)
    * Cron: cronie versión 1.5.7 (versión actual)
    * Python 3 3.9.16 (versión actual)
    * PHP 8.2.9 (versión actual)
    * Apache HTTPD versión 2.4.58 (versión actual)
    * Comunidad MySQL 8.4.2 LTS (versión actual)
    * Certbot: certbot versión 2.6.0 (versión actual)
    * Python para certbot: python-certbot-apache
    * net-tools.x86_64
    * wget
    * mod_ssl para httpd

* Configurar httpd
    * El puerto http 80 redirige al puerto https 443 para ambos dominios.
    * www.clearlight.one alias para clearlight.one
    * www.clearlight.app alias para clearlight.app

* Instalar módulo HTTPD mod_ssl

* Cambiar contraseña de root de MySQL

* Instalar módulos PHP si aún no están allí
    * php-pdo.x86_64
    * php-mbstring.x86_64
    * php-mysql.x86_64
    * php8.1-mysqlnd.x86_64
    * php-common
    * php-process
    * php-xml
    * php-gd
    * php-dba

* El nombre de host se establece en clearlight.app

* Usar certbot para certificados SSL
    * `sudo certbot -d clearlight.one -d *clearlight.one --apache`
    * `sudo certbot -d clearlight.app -d *clearlight.app --apache`

* El contacto estará disponible para responder preguntas por correo electrónico y whatsapp

#### Habilidades requeridas
* Administración de sistemas Unix
* Dominio de la línea de comandos
* Familiarizado con el software mencionado anteriormente y su configuración

#### Hitos y pago
* A discutir

#### Plazo
* Compilación dentro de las 48 horas posteriores a la aceptación del trabajo

#### Verificación
* aws -version muestra AWS CLI versión 2 y Python 3.
* hostname muestra clearlight.app
* HTTPD se ejecuta en el arranque y es accesible desde www https y http para dominios
* clearlight.one
* clearlight.app
* mysqld se ejecuta o se puede iniciar desde PHP y script de shell
* Cron se ejecuta en el arranque
* SSH se ejecuta en el arranque
* Certificado SSL a través de certbot, https funciona con certificados válidos de letsencrypt.org
* El software de la aplicación está instalado en el servidor y se ejecuta correctamente
