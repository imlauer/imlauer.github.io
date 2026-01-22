---
title: "Configurar tu Android para que automáticamente prenda al conectar al cargador"
date: 2024-09-01T23:25:34-03:00
---
Tenés que encenderlo aprentando el botón de la placa una vez que lograste encenderlo, habilitá developer options: abrí settings andá a la última opción: `acerca del teléfono` y apretá `build number` varias veces hasta habilitar modo desarrollo.   
   
Ahora en opciones del programador (developer options) habilitá `usb-debugging, oem unlock, stay awake` instalá platform-tools adb y fastboot, ejecutá `adb devices` conectá el celular a la PC con USB, te saldrá una notificación que te pedirá autorización en tu celular, a veces no sale tenés que habilitar y deshabilitar usb debugging hasta que funcione. Ahora ejecutá `adb devices` en la consola y deberías poder ver el celular luego `adb reboot bootloader` ahora `sudo fastboot devices` deberías poder ver el celular si no lo ves desconectá el cable rapido y volvelo a conectar hasta que aparezca, ahora ejecutá:   
`sudo fastboot oem off-mode-charge 0` listo , el celular se debería encender al conectar el USB.   
   
   
https://m.youtube.com/watch?v=Zp9G6A6EFlA   
https://android.stackexchange.com/questions/20021/automatically-power-on-android-when-the-charger-is-connected   
