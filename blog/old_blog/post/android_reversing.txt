---
title: "Android App Reverse Engineering"
date: 2024-09-17T13:56:22-03:00
tags: ['reversing','android']
---
https://redirect.invidious.io/playlist?list=PL3jdfxUyXxoyG6qEkaTMq0iWaaVps2SLa

https://odysee.com/@jadebayo:6/reverse-engineering-an-android-app:e

https://redirect.invidious.io/watch?v=UwFXndJH_34&list=PLhjZWEsxrYGpxhiSsVgyPM0kLn6EV_GXt&index=12

```bash
sudo apt install -y jadx
jadx-gui
```
Cargá el APK, podés bajar cualquier apk de la fdroid

https://github.com/pxb1988/dex2jar/releases

https://java-decompiler.github.io

```console
adb shell pm list packages | grep virtualmic  
package: tech....

adb shell pm path tech.smallwonder.androidvirtualmic

adb shell pull /date/app/tech....==/base.apk pulled.apk

unzip pulled.apk

cd pulled

cd Downloads/dex-tools-2.2-SNAPSHOT

./d2j-dex2jar.sh classes.dex classes2.dex
Generará dos archivos .jar

Que los cargaremos dentro de este programa (java-decompiler):
java -jar Downloads/jd-gui-1.6.6.jar

y en classes2-dex2jar estaba todo el código.
```

