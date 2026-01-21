---
title: "Agregar un servicio a Systemd"
date: 2024-09-25T19:48:04-03:00
tags: ['systemd']
---

https://www.youtube.com/watch?v=2gyKkgguyxE  
https://www.youtube.com/watch?v=fYQBvjYQ63U  
https://www.youtube.com/watch?v=6Cz6A8P0B2U  


En este tutorial se habló del video: https://www.youtube.com/watch?v=xvDXSIcl3vc  

Un archivo UNIT simple en `/etc/systemd/system` proporcionará un servicio compatible con `systemd` en un sistema Linux.

Creá un archivo llamado :

```bash
vim helloworldd.service`
cp helloworld.service /etc/systemd/system
```

```bash
[Unit]
Description=Hello World Service
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/local/sbin/helloworldd start
ExecStop=/usr/local/sbin/helloworldd stop
TimeoutStopSec=infinity

[Install]
WantedBy=multi-user.target
```

**Para que el script funcione** creamos un demonio llamado `helloworldd`:

```bash
#!/bin/bash

function hellostart(){
  while [ 1 ]
    do
      echo Hello World $(date)
      sleep 10
    done
}
function hellostop(){
  killall $(basename $0)
}

case "$1" in
  start)
    hellostart
  ;;
  stop)
    hellostop
  ;;
esac
```

---

```bash
cp helloworldd /usr/local/bin
```


**After**:  
`After=multi-user.target` significa que el servicio iniciará después que el `multi-user.target` esté listo.   
Otras posibilidades de **target** es por ejemplo `network`.

Tenés que definir que tipo de servicio.
#### **Type**:
* `simple`: que no inicia otro servicio más
* `forking`: si mi script inicia otro programa

#### [Install]
Al final **[Install]** es para poder usar el comando: **`systemctl enable` y `systemctl disable`**

Lo iniciamos con: systemctl start helloworldd ;  systemctl daemon-reload; systemctl stop helloworldd

Si ejecutás `journalctl -u helloworldd` -n 10
### Para ver si falló
`systemctl status helloworldd`

---

`systemctl enable helloworld`

`systemctl disable helloworld`

`systemctl restart helloworld`

`systemctl status helloworld`
