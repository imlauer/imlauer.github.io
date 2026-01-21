---
title: "Configurando un servidor proxy: squid"
date: 2024-09-20T17:08:21-03:00
tags: ['proxy','server','squid']
---
Instalamos squid:

```bash
sudo apt install -y squid
systemctl start squid
systemctl enable squid
systemctl status squid
ss -antpl | grep 3128 
```

Abrimos el siguiente archivo:

```
sudo vim /etc/squid/squid.conf
```

Cambiá la siguiente línea con el puerto deseado `http_port 3128`

### Configurá squid para permitir todo el tráfico:
Comenta la línea `http_access deny all` y añadí el `http_access allow all` como se muestra más abajo:

También bloqueá algunos sitios
```bash
acl backlist1 dstdomain facebook.com
acl backlist2 dstdomain yahoo.com
http_access deny backlist1
http_access deny backlist2

http_access allow all
http_access deny all
```

Guardá y reiniciá el servicio de Squid: `systemctl restart squid`

### Configurá el navegador del cliente para usar el servidor proxy

En firefox: Preferencias > configuración de red (network settings) > configuración (settings) > manual proxy configuration > en http proxy agregá la ip del proxy y el puerto (la-ip-de-tu-proxy:3128) y marcá `use this proxy for all proocols`.
En chrome lo tenés que configurar con el comando `chromium --proxy-server="http://127.0.0.1:8080`

### Probá el proxy.
Ingresá a https://whatismyipaddress.com/ 

Si intentás ingresar a facebook.com o yahoo.com te dirá acceso denegado.



