---
title: "Saber que aplicación corre en X puerto"
date: 2024-07-22T15:46:57-03:00
---
Cualquiera de los siguientes comandos funciona:

`# ss -tanp | grep 6379`

`sudo netstat -nlp`

`lsof -i tcp:8080`

`netstat -ano | find "1234" | find "LISTEN"`

