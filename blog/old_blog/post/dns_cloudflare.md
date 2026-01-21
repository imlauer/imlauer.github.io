---
title: "Dns cloudflare"
date: 2024-09-23T16:46:13-03:00
---
https://www.youtube.com/watch?v=XQKkb84EjNQ

https://www.youtube.com/watch?v=IXpvUD5SDzA

https://www.youtube.com/watch?v=9vaiZQtL9lQ

https://www.youtube.com/watch?v=M-wxorxYVNs

Ingresá cloudflare, add site, ingresa dominio, free, determina tu registrar con whois, entrá a la cuenta de administrador de tu dominio, eliminá los servidores de dns que tiene, y reemplazalos por el de cloudflare.
Con .edu.ar lo tuve que hacer en riu.edu.ar, luego dale a done check nameservers.

get started > desactivá automatic https rewrites y al resto dejá como está, ahora dale next y check dns

Ahora te dirá que todo funciona bien, en DNS add record A @ y de IP poné la IP de tu servidor, agregá CNAME www y target: @

Eso es todo
