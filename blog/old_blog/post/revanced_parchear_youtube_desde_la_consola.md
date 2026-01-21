---
title: "YouTube Revanced: Parchear youtube desde la consola"
date: 2023-10-16T08:24:29-03:00
tags: ['youtube','revanced','patch']
---
Anteriormente explique como parchear youtube usando revanced-manager desde android directamente, el problema es que para dispositivos con armv7 no esta bien soportado, entonces podés parchearlo desde la computadora con la siguiente guía:

#### OJO: ESTE GENERADOR YA NO SE USA MAS PORQUE TODOS LOS PARCHES SON APLICADOS AUTOMATICAMENTE 

Guía:
[https://thismoon.github.io/revanced-helper/](https://thismoon.github.io/revanced-helper/)

Bajate el jar de   
https://github.com/ReVanced/revanced-cli/releases   
y los apk de    
https://github.com/ReVanced/revanced-integrations/releases  
https://github.com/ReVanced/revanced-patches/releases  
Services MicroG: https://github.com/revanced/gmscore/releases/tag/v0.3.1.4.240913 (signed-apk)

Hay que desactivar la optimización para servicios microg


Necesitás java jdk 17.
Necesitás entrar al github de revanced y bajar el jar de revanced cli, el jar de revanced patches, el apk de revanced integrations y el apk de youtube desde apkmirror, tenés que ver que versión es compatible generalmente están en los releases de revanced patches (no tiene que ser -dev). Tenés que tener microG instalado en tu celular lo podés bajar desde la página oficial o desde el github de vanced microg.


El comando que te genera la página mencionada anteriormente tiene algunos parámetros viejos todos los parches son automaticamente aplicados asi que no necesitas listarlos uno por uno, este fue el comando que usé para generar el patch :
```console
java -jar revanced-cli-4.0.2-all.jar patch  --patch-bundle revanced-patches-2.193.0.jar  --out patched-app.apk -m revanced-integrations.apk youtube.apk
```


#### Actualización 2025

Ahora se hace así (creo que no se usa más el revanced-integrations).
```bash
java -jar revanced-cli-5.0.1-all.jar patch --patches patches-5.33.0.rvp  --out patched-app.apk com.google.android.youtube_20.13.41-1553731008_minAPI26\(arm64-v8a,armeabi-v7a,x86,x86_64\)\(nodpi\)_apkmirror.com.apk
```

Cualquier versión de YouTube Music funciona, bajate el último APK.
