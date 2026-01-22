---
title: "Lets Encrypt Docker"
date: 2023-09-20T08:59:37-03:00
tags: ['docker']
---
##### Configurar que el servicio de docker inicie automáticamente en caso de caída o reseteo por mantenimiento
[https://stackoverflow.com/questions/43671482/how-to-run-docker-compose-up-d-at-system-start-up](https://stackoverflow.com/questions/43671482/how-to-run-docker-compose-up-d-at-system-start-up)
#### Usando systemd:
Creá un archivo en /etc/systemd/system/docker-compose-app.service con el siguiente contenido:

```bash
# /etc/systemd/system/docker-compose-app.service

[Unit]
Description=Docker Compose Application Service
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/home/test/docker
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
```
Cambie el parámetro WorkingDirectory con la ruta de su proyecto docker. Y habilite el servicio para que se inicie automáticamente:
```bash
systemctl enable docker-compose-app
```
### Usando restart:always
Utilice `restart: always` en su archivo `docker-compose.yaml` a cada servicio que desee reiniciar en el archivo docker-compose.yml.
`docker-compose up -d` volverá a iniciar el contenedor desde las imágenes. 
```bash
nginx:   
    restart: always   
    image: nginx   
    ports:
      - "80:80"
      - "443:443"
    links:
      - other_container:other_container
```
Ahora si reinicías la máquina o si apagás y prendés la VPS, el servicio se levantará sólo. 
**Observación: Esto sólo funciona si tenés el docker.service habilitado al iniciar el sistema**
Eso se hace con el siguiente comando:
```bash
$ sudo systemctl enable docker
```

## Instalar certbot de LetsEncrypt
```console
sudo apt update
sudo apt install -y certbot
```
Ahora podemos ejecutar Certbot para obtener nuestro certificado. Usaremos la opción --standalone para decirle a Certbot que maneje el desafío usando su propio servidor web integrado. La opción --preferred-challenges le indica a Certbot que use el puerto 80 o el puerto 443. Si está usando el puerto 80, querrá --preferred-challenges http. Para el puerto 443 sería --preferred-challenges tls-sni. Finalmente, el indicador -d se usa para especificar el dominio para el que solicita un certificado. Puede agregar varias opciones -d para cubrir varios dominios en un solo certificado.
```bash
# http
sudo certbot certonly --standalone --preferred-challenges http -d example.com
```
[https://www.digitalocean.com/community/tutorials/how-to-use-certbot-standalone-mode-to-retrieve-let-s-encrypt-ssl-certificates-on-ubuntu-16-04](https://www.digitalocean.com/community/tutorials/how-to-use-certbot-standalone-mode-to-retrieve-let-s-encrypt-ssl-certificates-on-ubuntu-16-04)
>Los certificados de Let's Encrypt solo son válidos por noventa días. Esto es para alentar a los usuarios a automatizar su proceso de renovación de certificados. El paquete certbot que instalamos se encarga de esto agregando un script de renovación a /etc/cron.d. Este script se ejecuta dos veces al día y renovará cualquier certificado que se encuentre dentro de los treinta días posteriores a su vencimiento.

>Dado que nuestros certificados se renuevan automáticamente, todavía necesitamos una forma de ejecutar otras tareas después de una renovación. Necesitamos al menos reiniciar o recargar nuestro servidor para recoger los nuevos certificados y, como se mencionó en el Paso 3, es posible que necesitemos manipular los archivos de certificados de alguna manera para que funcionen con el software que estamos usando. Este es el propósito de la opción renew\_hook de Certbot.

>Para agregar un renew\_hook, actualizamos el archivo de configuración de renovación de Certbot. Certbot recuerda todos los detalles de cómo obtuvo el certificado por primera vez y se ejecutará con las mismas opciones al renovarlo. Sólo necesitamos agregar nuestro gancho. Abra el archivo de configuración con su editor favorito:

[https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71](https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71)

##### Luego de que se renueva el certificado automáticamente hay que reiniciar el servidor Apache para que cargue el nuevo certificado para ello usaremos renew-hooks

## Una forma de hacerlo (la segunda es mejor)
#### LetsEncrypt certbot con multiples renew-hooks
[https://stackoverflow.com/questions/42300579/letsencrypt-certbot-multiple-renew-hooks](https://stackoverflow.com/questions/42300579/letsencrypt-certbot-multiple-renew-hooks)
Si coloca algún script en la carpeta "post", se ejecutará automáticamente después de la renovación. No olvide hacerlo ejecutable agregando +x al script.

Estoy usando solo un "001-restart-nginx.sh" con el siguiente contenido:
```console
#!/bin/bash
echo "ssl certs updated" && service nginx restart
```
Eso va en `/etc/letsencrypt/renewal-hooks/post/001-restart-nginx.sh`


De esta manera, no es necesario proporcionar manualmente los parámetros --post-hook con ciertas instrucciones.

En el proceso de renovación real verá algo como esto:

```console
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Congratulations, all renewals succeeded. The following certs have been renewed:
  /etc/letsencrypt/live/<your-domain-name>/fullchain.pem (success)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Running post-hook command: /etc/letsencrypt/renewal-hooks/post/001-restart-nginx.sh
Output from post-hook command 001-restart-nginx.sh:
ssl certs updated
```


## Otra forma
También puedes configurar hooks (y otras opciones si lo deseas) como opciones globales en el archivo `/etc/letsencrypt/cli.ini` (ver documentación) de esta manera:

```console
# Global config for letsencrypt runs
#
# Note that these options apply automatically to all use of Certbot for
# obtaining or renewing certificates, so options specific to a single
# certificate on a system with several certificates should not be placed
# here.

renew-hook = service postfix reload
#post-hook = service nginx reload
post-hook = docker compose -f /home/test/docker/docker-compose.yml restart app
```
Primero debe crear el archivo en la mayoría de los sistemas. Letsencrypt viene sin.
También puede crear una versión específica del certificado en cada carpeta de `renewal` si no desea globalizarse.
