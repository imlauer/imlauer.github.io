---
title: "Burp_suite"
date: 2024-08-03T06:17:58-03:00
draft: true
---
Abrí burp suite, dejá la configuración por defecto, andá a la pestaña proxy, intercept -> insercept is off.
Entrá a http://localhost:8080 en el menú dale a CA-certificate , descargalo e importalo en chrome : `settings->privacy and security->security->manage certificates->authorities->import->all files->cacert.der`
Abrí `firefox settings->manual proxy configuration->localhost 8080 -> also use this for https`

O en chrome: `chromium --proxy-server="http://127.0.0.1:8080"`

