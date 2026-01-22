---
title: "Como quitar sistema anti-theft de Intel de las netbook"
tags: ['desbloqueo','netbook','binarios','ch341a','pinza programadora']
date: 2023-11-16T20:57:33-03:00
---
### Como desarmarla
En algunas computadoras tenés que sacar el teclado y sacar los tornillos que están debajo para desarmar la tapa de atrás.
En otras tenés que sacar dos gomas que están en la tapa cerca de la pantalla y debajo de cada una tienen dos tornillos.
En las más viejas tenés que desarmar todo desde arriba, sacar la placa madre y darle vuelta para encontrar la BIOS.

##### Requisitos
Vas a necesitar los binarios y la pinza programadora CH341A (lo compré en ML y te trae una pinza con el programador CH341A).
La pinza te viene desarmada hay varios videos que explican como armarla.  


#### BAJAR BINARIOS Y PROGRAMADOR 
Tenés que bajar e instalar el programador CH341A programm v1.34.rar: ([https://drive.google.com/file/d/1W4p-2VgvZbA93FWIWJ7SWmHCuCgd58_f/view](https://drive.google.com/file/d/1W4p-2VgvZbA93FWIWJ7SWmHCuCgd58_f/view) ) , si está caído ese link lo encontrás googleando "CH341A programm v1.34"

Acá están los binarios de las diferentes generaciones de netbooks: [https://drive.google.com/file/d/1KKZFmejxhf8V5m7NlPW7DUnX0mIVopFm/view?usp=sharing](https://drive.google.com/file/d/1KKZFmejxhf8V5m7NlPW7DUnX0mIVopFm/view?usp=sharing)

Y acá hay un backup por si las dudas esos links caen: [https://drive.google.com/file/d/1nxGWSd1SZyQSRJh0pkndBBtWskywZCCH/view?usp=sharing](https://drive.google.com/file/d/1nxGWSd1SZyQSRJh0pkndBBtWskywZCCH/view?usp=sharing)

#### Conectar la pinza al programador
1. Para conectar la pinza al programador, levantá la palanca del programador y ubicá la raya del medio que separa a los dos conectores, yo siempre usé el set de contactos izquierdo.
Esta es la raya que separa los conectores:
![Raya que separa a los conectores del programador](/files/desbloqueo/separacion_conectores.png)

2. Ubicá el cable del color rojo (hace referencia al pin 1) del conector de la pinza.
3. Conectalo de forma de que el cable de color rojo quede del lado de la línea de separación del programador del lado izquierdo.
De la siguiente manera:
![Conectar Pinza al Programador](/files/desbloqueo/conectar_pinza_programador.png)
4. Una vez colocada bajá la palanca.
De la siguiente manera:
![Bajar Palanca de Programador con el cable de pinza conectado](/files/desbloqueo/baja_palanca.png)

#### Luego de desarmarla:
5. Tenés que desconectar la batería y la pila de la BIOS.
**OJO: Fijate bien como está ubicado/conectado el cable negro y el rojo sacale una foto porque si los conectás al revés se puede quemar la pila de la BIOS.**
6. Tenés que sacar la cinta de la memoria RAM y sacar la memoria RAM, debajo está la VERSION de la plata madre. Esto es información que se necesita para saber cual binario hay que flashear en el chip BIOS.
**OJO: Si tenés una netbook de generación antigua no hace falta hacer esto porque solo hay una versión del binario de esa placa madre.**
7. Si sacaste la memoria RAM, volvela a colocar.
8. Con una cinta aislante tapa la patita 8 de la BIOS. La patita 1 está indicada con un circulito en el chip BIOS. La patita de enfrente de la pata 1 es la pata 8.

**Observación: Yo flashee una notebook de generación 5 en donde no tuve que tapar la patita 8 y me funcionó igual.**


9. Volvemos a la placa madre de la netbook ubicamos el chip bios, este chip tiene un punto en una de sus esquinas eso indica el pin 1.

#### Diferentes ubicaciones de BIOS en diferentes modelos:




10.  La pinza tiene un cable rojo que hace referencia al 1er pin(1era patita), el cable rojo tiene que hacer contacto con el pin 1 del CHIP de la BIOS.
Tomamos la pinza y ubicamos el cable rojo, el cable rojo tiene que ir conectado a la pata en donde el chip BIOS tiene un puntito(el puntito indica que es el pin 1), es decir, el cable rojo de la pinza tiene que ir ubicado en la patita 1 del chip de la BIOS.
![Ubicamos CHIP Bios](/files/desbloqueo/chip_bios.png)
**OJO!!!!!: EN ALGUNAS TENÉS QUE TAPAR LA PATITA 8 CON CINTA AISLANTE**
11. Así tendría que quedar la pinza:
![Conectar Pinza al CHIP BIOS](/files/desbloqueo/conectar_pinza_bios.png)
12. Conectamos el programador a la PC.
13. Abrimos el programa "CH341A programm" instalado anteriormente.
14. Apretamos el botón detectar y debería salirnos la información del CHIP bios, si tapas la patita 8 quizás pueda darte "unknown".
15. Luego le damos a "Read"
16. Cuando termina, guardamos el binario.
17. Una vez finalizado, dale al botón Erase/Borrar (esto borrará la bios).
18. Luego dale al botón Blank/Chequear en blanco para asegurarse que está todo en blanco.
19. Luego dale a Abrir/Open y ubicá el archivo binario que descargaste anteriormente de la generación que sea tu netbook y dale a aceptar. Algunos tienen una carpeta en donde dicen con o sin logo, yo siempre elijo sin logo.
20. Ahora dale a programar/write.
21. Al final desconectamos el programador y sacamos la pinza.
22. Le damos la vuelta a la computadora con cuidado y procedemos a encenderla.
Si ya no aparece la advertencia del bloqueo o si ya no aparece el logo de conectar igualdad significa que salió bien.
23. Ahora tenés que conectar la batería y la pila de la BIOS (CUIDADO!! fijate bien el órden de los cables)


Listo!

#### Opcional: Recuperar grub huayra
Luego de hacer todo esto, en algunas computadoras perdés el grub huayra y bootea directamente a Windows. Esto es fácil de solucionar.
Primero podés apretar F7 o F11 (el menu de boot) y acceder a la EFI shell y desde ahí escribí.
```bash
blk0: (suponiendo que esa es la particion efi)
cd EFI
cd huayra
grubx64.efi
```
Y listo botea a el grub de huayra.
**Si querés que el grub de huayra inicie automáticamente hacé** 
1. Instalá EasyUEFI en Windows
2. Agregá una entrada de arranque y ubicá la partición de EFI de Huayra el archivo grubx64.efi algo así era.
3. Ubicala bien arriba.
4. Reiniciá la máquina accedé a la BIOS con el botón suprimir.
5. Cambiá la selección de OS a Linux.


Referencias: [https://youtube.com/watch?v=R1FkJnQwl0g](https://youtube.com/watch?v=R1FkJnQwl0g)
