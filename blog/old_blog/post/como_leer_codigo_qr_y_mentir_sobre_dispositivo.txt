---
title: "Como leer codigo qr desde la PC y engañar sobre el dispositivo"
date: 2024-08-23T16:54:49-03:00
---
Podemos engañar a una página web haciéndole creer que estamos accediendo desde un celular, cuando estamos ingresando de una computadora. Esto tiene muchos usos como por ejemplo: las páginas son más ligeras cuando ingresás desde el celular, o algunos te piden que ingreses del celular para hacer algún tipo de verificación.
Esto se puede hacer apretando 
```
F12 -> Network (Red) -> More network conditions (más condiciones de red) tiene un ícono como de una red wifi -> abajo en donde dice user agent demarcá "Usar el navegador por defecto" y cambialo a Chrome Android
```

Para leer QR desde la consola sacá la captura del qr y usá el comando zbarimg que está en el paquete zbar-tools.
