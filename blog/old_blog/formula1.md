---
title: "Formula1: horarios desde la terminal"
tags: ['bash']
---
Guardá el siguiente script en scripts/f1exposure.sh luego agregá un alias f1 'bash scripts/f1exposure.sh' y gualá.

OJO! Si estás en Linux el encoding no debe ser DOS, si te tira \r: command not found es porque estás usando el encoding de windows, usualmente se soluciona creando un archivo nuevo.

Podés chequearlo con bash -x `scripts/f1exposure.sh`

```bash
#!/usr/bin/sh
echo "Los tiempos están en UTC. Coordinated Universal Time está 3 horas adelantado a Buenos Aires"
curl "https://f1exposure.com/f1exposure/countdown?mode=0" -H "Accept: application/json, text/plain, */*" -H 'Accept-Language: en-US,en;q=0.8' -H 'Client: 36aed15c-f2ca-40a0-ae6d-96d82091df99' -H 'Connection: keep-alive' -H 'Content-Type: application/json' -H 'Cookie: _ga=GA1.1.185284743.1738591811; _ga_7SC6WMLXPL=GS1.1.1738591810.1.1.1738592298.0.0.0' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-origin' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/6.8.1 Chrome/122.0.6261.171 Safari/537.36' -H 'sec-ch-ua: "Not(A:Brand";v="24", "Chromium";v="122"' -H 'sec-ch-ua-mobile: ?0' -H 'sec-ch-ua-platform: "Linux"'| jq .
```
