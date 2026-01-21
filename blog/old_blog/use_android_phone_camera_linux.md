---
title: "Use android phone camera Linux"
date: 2025-02-28T21:32:14-03:00
tags: ['android']
---
You can use any Android phone as a webcam for your Ubuntu PC by using DroidCam.

```bash
mpv IP/video 
```
Pero no podés transmitir la cámara a través de internet porque de esa forma es muy lento.

1. First download the DroidCam app on your android device via the Play Store.
2. Next install adb on your Ubuntu PC:
```bash
sudo apt install adb
```

3. Follow the instructions to install the DroidCam Linux client.
4. On your android phone, enable USB debugging (you need to enable developer mode to do this).

5. Find the drivers for your device:
* This page provides links to most manufacturers websites: http:// developer.android.com/tools/extras/oem-usb.html#Drivers.
* You can also search Google “ADB Drivers for \_\_\_"

6. Plug the device back into computer over USB. If you get a dialog asking Allow USB Debugging, you need to tap OK.

7. Open DroidCam and select the USB option. On the phone you may get a dialog asking Allow USB Debugging, you need to tap OK. Sometimes you need to open USB Options from the notification area on the device and pick PTP mode for that to show up.

For more information on how to set up DroidCam, click here.

---

To use your android phone as a microphone, check out WO Mic.

To install the Linux client see this.

You will also need to download the WO Mic app from the PlayStore.

Theoretically you can use both WO Mic and DroidCam in conjunction to turn your
Android device into a webcam with a microphone.


