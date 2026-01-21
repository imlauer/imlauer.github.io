---
title: "Vulnerabilidades en el router TP Link WR841N"
date: 2024-08-16T19:35:21-03:00
tags: ['vulnerabilidades','tp','link','hacking']
---
Se puede acceder a toda la configuración y ejecutar cualquier comando remotamente.

https://www.exploit-db.com/exploits/45064
https://www.exploit-db.com/exploits/45168
https://www.exploit-db.com/exploits/45203
https://www.exploit-db.com/exploits/46882

Usando burp-suite podés repetir la consulta agregandole `'Referer: http://192.168.0.1/mainFrame.htm'`

#### Authentication Bypass:
https://www.exploit-db.com/exploits/44781

#### Emulador TL-WR841N

https://emulator.tp-link.com/TL-WR841ND_V8/Index.htm

#### Listar Virtual Servers:
```
curl 'https://emulator.tp-link.com/TL-WR841ND_V8/userRpm/VirtualServerRpm.htm' \
  -H 'Referer: https://emulator.tp-link.com/TL-WR841ND_V8/userRpm/MenuRpm.htm' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```


