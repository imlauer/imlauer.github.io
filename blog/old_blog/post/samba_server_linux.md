---
title: "Samba server en Linux"
date: 2024-08-15T19:55:28-03:00
tags: ['samba','server','linux']
---
Creo que no hace falta ninguna de esas configuraciones solo tenes que agregar la contraseña.

`sudo smbpasswd -a esotericwarfare`

---

```bash
sudo apt install samba -y
sudo systemctl stop smbd
mkdir linuxshare
vim /etc/samba/smb.conf
```

Agregá lo siguiente:
```
[global]
  server role = standalone server
  map to guest = bad user
  usershare allow guests = yes
  hosts allow = 192.168.0.0/16
  hosts deny = 0.0.0.0/0


[samba]
  comment = Open Linux Share
  path = /home/esotericwarfare/samba
  read only = no
  guest ok = yes
```

Ejecutá: `testparm` para probar la configuración.
```
sudo systemctl enable smbd
sudo systemctl start smbd
```

Permití a samba a través del firewall:    
RHEL/Centos/Fedora
`sudo firewall-cmd --add-service=samba`

Debian/Ubuntu/Mint
`sudo ufw allow Samba`

Ahora en Windows habilitá la funcionalidad (feature): "SMB 1.0" .


---
#### Si no te funcionó de esa forma inténtalo con esto:


```
sudo apt install samba
mkdir /home/esotericwarfare/sambashare/
vim /etc/samba/smb.conf
```

Agregá al final:
```
[sambashare]
	comment = Samba on Kali
	path = /home/esotericwarfare/sambashare/
	read only = no
	browsable = yes
```

Reiniciá samba: `sudo service smbd restart`    
Permití el tráfico de samba a través del firewall: `sudo ufw allow samba`    
Creá una contraseña para samba:   
```
sudo smbpasswd -a esotericwarfare
```

---

En ArchLinux tuve que cargar este archivo de configuración: 
https://wiki.archlinux.org/title/Samba

```bash
sudo pacman -S samba

smbclient --list //192.168.0.204/Users

sudo mount -t cifs //192.168.0.203/Users /mnt/windows

sudo systemctl enable samba smb nmb wsdd avahi-daemon

sudo wget [https://git.samba.org/samba.git/?p=samba.git;a=blob_plain;f=examples/smb.conf.default;hb=HEAD](https://git.samba.org/samba.git/?p=samba.git;a=blob_plain;f=examples/smb.conf.default;hb=HEAD) -O /etc/samba/smb.conf
```





