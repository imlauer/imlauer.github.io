---
title: "Evil twin ESP32"
date: 2025-01-12T08:31:41-03:00
tags: ['hacking']
---
https://github.com/y0xhz/ESP32-EvilTwin/blob/master/Evil-Twin%20and%20Deauther%20esp32.ino


https://github.com/aadesh0706/IOT-ESP32-Evil-Twin-WiFi-Hacking-Deauthentication-Captive-Portal/blob/main/NetworkDeAuth.ino


https://github.com/risinek/esp32-wifi-penetration-tool


https://www.youtube.com/watch?v=uYTu98j_STY&t=37s


Binarios del ESP32 WiFi Penetration Tool:

https://github.com/risinek/esp32-wifi-penetration-tool/releases

Herramienta que se usa para flashear el binario: 
```bash
esptool.py -p /dev/ttyS5 -b 115200 --after hard_reset write_flash --flash_mode dio --flash_freq 40m --flash_size detect 0x8000 build/partition_table/partition-table.bin 0x1000 build/bootloader/bootloader.bin 0x10000 build/esp32-wifi-penetration-tool.bin
```
https://github.com/espressif/esptool
