---
title: "Cambiar DNS de forma permanente en Debian"
tags: ['dns','cambiar dns','debian']
categories: ['linux','networking']
date: 2023-03-09T18:37:44-03:00
---
### Una forma que NetworkManager deje de agregar servidores DNS automaticamente
Una forma de detener que Network Manager agregue servidores DNS al archivo `/etc/resolv.conf` es hacer lo siguiente:

Primero abra el archivo de configuración de nm `/etc/NetworkManager/NetworkManager.conf`:

`sudo vim /etc/NetworkManager/NetworkManager.conf`
Luego, agregue lo siguiente a la sección [main]:

```bash
dns=none
rc-manager=unmanaged
Guarde y salga.
```

### Una forma de cambiar los DNS de forma permanente
`/etc/resolv.conf` es un enlace simbólico a `/run/resolvconf/resolv.conf`.
NetworkManager no actualiza directamente `/etc/resolv.conf` (solo actualiza `/run/resolvconf/resolv.conf`).
Entonces:

* elimina el enlace simbólico (`rm /etc/resolv.conf`)
* escribí tu propia versión de `/etc/resolv.conf`

Luego recibirás este error XD:
```
Error: ipv4: Address already assigned.
/etc/resolvconf/update.d/libc: Warning: /etc/resolv.conf is not a symbolic link to /
run/resolvconf/resolv.conf
```


### Usando resolvconf para agregar DNS en `/etc/resolv.conf`
```bash
sudo apt update
sudo apt install resolvconf
```

```bash
sudo vim /etc/resolvconf/resolv.conf.d/head
```

Agrega las DNS de Google por ejemplo
```bash
nameserver 8.8.8.8 
nameserver 8.8.4.4
```

Si usas systemd:
```bash
sudo systemctl restart resolvconf.service
sudo systemctl restart systemd-resolved.service
```

Y por ultimo
```bash
sudo resolvconf -u
```



Eso es todo.
