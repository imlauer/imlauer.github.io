---
title: "Setup on Access Point on ArchLinux."
date: 2025-11-27T02:32:30-03:00
tags: ['cli','networking']
---

### No uso más esto. Funciona pero es lento, quizás algo de mi configuración está mal. Levanto un Hotspot desde mi Android y me conecto desde la PC y uso SAMBA.

Uso esto para transferir archivos de SAMBA (Bluetooth con OBEX funciona mal).

```console
sudo pacman --needed --noconfirm -S hostapd dnsmasq
sudo systemctl stop NetworkManager
iwconfig # (para saber nombre interfaz en mi caso wlp1s0)
sudo ifconfig wlp1s0 192.168.0.1/24
sudo ifconfig wlp1s0 192.168.0.1 netmask 255.255.255.0
route -n
sudo route add default gw 192.168.0.1 # gw hace referencia a gateway
```

Necesitás crear los siguientes archivos: `dnsmasq.conf` y `hostapd.conf`.

### ¡Ojo!

**El rango de DHCP** debe coincidir con la configuración de `/etc/samba/smb.conf` en mi caso tenía `hosts allow =  192.168.0.0/16` (si queres ver mi configuración completa buscá con control+f en mi índice de mi página por samba).
 
#### Mi dnsmasq.conf

```console
#Set the wifi interface
interface=wlp1s0

#Set the IP range that can be given to clients
dhcp-range=192.168.0.10,192.168.0.100,8h

#Set the gateway IP address
dhcp-option=3,192.168.0.1

#Set dns server address
dhcp-option=6,192.168.0.1

#Redirect all requests to 192.168.0.1
address=/#/192.168.0.1
```

#### hostapd.conf

```console
#Set wifi interface
interface=wlp1s0

#Set network name
ssid=iot-lab

#Set channel
channel=1

#Set driver
driver=nl80211
```

#### Ahora.

```bash
sudo dnsmasq -C dnsmasq.conf
sudo hostapd hostapd.conf
```

Para ver puertos abiertos: `ss -tanp` (para asegurate que SAMBA esté corriendo).

Listo, como configurar servidor SAMBA lo expliqué en otra publicación en esta misma página.
