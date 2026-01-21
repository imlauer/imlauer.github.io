---
title: "CISCO ios port forwarding y dynamic dns(DDNS)"
date: 2023-11-10T04:52:04-03:00
tags: ['CISCO','iOS','port','forwarding','ddns']
---
Basic Configuration: [https://youtube.com/watch?v=3wuFFYVWnbc](https://youtube.com/watch?v=3wuFFYVWnbc)

Port Forwarding: [https://youtube.com/watch?v=8WVWoW86Uhw](https://youtube.com/watch?v=8WVWoW86Uhw)

Dynamic DNS: [https://youtube.com/watch?v=Zh39hgRJwGE](https://youtube.com/watch?v=Zh39hgRJwGE)

[https://content.cisco.com/chapter.sjs?uri=/searchable/chapter/content/en/us/td/docs/ios-xml/ios/ipaddr_dns/configuration/15-sy/dns-15-sy-book/Dynamic-DNS-Support.html.xml](https://content.cisco.com/chapter.sjs?uri=/searchable/chapter/content/en/us/td/docs/ios-xml/ios/ipaddr_dns/configuration/15-sy/dns-15-sy-book/Dynamic-DNS-Support.html.xml) 

[https://ipwithease.com/how-to-configure-ddns-in-a-cisco-router/](https://ipwithease.com/how-to-configure-ddns-in-a-cisco-router/)

DDNS y NoIP: [https://www.firewall.cx/cisco/cisco-routers/cisco-router-ddns.html](https://www.firewall.cx/cisco/cisco-routers/cisco-router-ddns.html)

Setup DNNS on a Cisco IOS Router: [https://www.bytesolutions.com/setup-ddns-dynamic-dns-cisco-ios-router/](https://www.bytesolutions.com/setup-ddns-dynamic-dns-cisco-ios-router/)



```console
=================================
Basic Router Commands
=================================
Router(greater than sign)        ---User EXEC mode               exit
Router(greater than sign) ?
Router(greater than sign) enable     
---------------
Router#                          ---Privileged EXEC mode         disable, exit
Router# ?
-----------------
Router# configure terminal
Router(config)#                  ---Global Config mode           exit, end, Ctrl+c, Ctrl+z
Router(config)# ?
-----------------
Router(config)# line vty 0 15
Router(config)# line console 0
Router(config-line)#             ---Line configuration mode      exit, end, Ctrl+c, Ctrl+z
Router(config-line)# ?
----------------------------
Router(config)# interface gigabitEthernet 0/0/0
Router(config-if)#               ---Interface configuration mode exit, end, Ctrl+c, Ctrl+z
Router(config-if)# ?
----------------------------
Router#
Router# configure terminal
Router# show ?
Router# show running-config
Router# copy running-config startup-config
Router# ping 192.168.1.100
Router# traceroute 192.168.1.100
Router# ssh 192.168.1.100 
Router# telnet 192.168.1.100
Router# debug ?
Router# clock set 07:14:00 October 15 2019
Router# reload
---------------------------------
Router(conf)#
Router(conf)# hostname R1
Router(conf)# banner motd "No unauthorized access allowed!"
Router(conf)# enable password class
Router(conf)# enable secret class
Router(conf)# service password-encryption
Router(config)# line vty 0 15
Router(config)# line console 0
Router(config)# interface gigabitEthernet 0/0/0
----------------------------------------------------
Router(config-line)# 
Router(config-line)# password cisco
Router(config-line)# login
Router(config-line)# transport input all   (line vty)
----------------------------------------------------
Router(config-if)# 
Router(config-if)# interface gigabitEthernet 0/0/0
Router(config-if)# int g0/0                              //command abbreviation
Router(config-if)# ip address 192.168.1.1 255.255.255.0 
Router(config-if)# no shutdown


=================================
Basic Switch Commands
=================================
Switch(greater than sign)        ---User EXEC mode               exit
Switch(greater than sign) enable     
---------------
Switch#                          ---Privileged EXEC mode         disable, exit
-----------------
Switch# configure terminal
Switch(config)#                  ---Global Config mode           exit, end, Ctrl+c, Ctrl+z
-----------------
Switch(config)# line vty 0 15
Switch(config)# line console 0
Switch(config-line)#             ---Line configuration mode      exit, end, Ctrl+c, Ctrl+z
----------------------------
Switch(config)# interface vlan 1
Switch(config-if)#               ---Interface configuration mode exit, end, Ctrl+c, Ctrl+z
----------------------------
Switch#
Switch# configure terminal
Switch# show ?                
Switch# show running-config
Switch# copy running-config startup-config
Switch# ping 192.168.1.100
Switch# traceroute 192.168.1.100
Switch# ssh 192.168.1.100 
Switch# telnet 192.168.1.100
Switch# debug ?
Switch# clock set 07:14:00 October 15 2019
Switch# reload
---------------------------------
Switch(conf)#
Switch(conf)# hostname R1
Switch(conf)# banner motd "No unauthorized access allowed!"
Switch(conf)# enable password class
Switch(conf)# enable secret class
Switch(conf)# service password-encryption
Switch(config)# line vty 0 15
Switch(config)# line console 0
Switch(config)# interface vlan 1
----------------------------------------------------
Switch(config-line)# 
Switch(config-line)# password cisco
Switch(config-line)# login
Switch(config-line)# transport input all   (line vty)
----------------------------------------------------
Switch(config-if)# 
Switch(config-if)# interface vlan 1
Switch(config-if)# ip address 192.168.1.2 255.255.255.0 
Switch(config-if)# no shutdown
Switch(config-if)# exit
Switch(config)# ip default-gateway 192.168.1.1

```
