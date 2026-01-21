---
title: "Creando una billetera bitcoin para aceptar donaciones"
date: 2023-06-08T00:38:13-03:00
tags: ['bitcoin','billetera']
---

### Creando una billetera Bitcoin
Ahora obtengamos una billetera Bitcoin y podamos recibir fondos o donaciones de Bitcoin.

### Billeteras
Una de las opciones clásicas para una billetera Bitcoin es Electrum. Vaya a https://electrum.org para descargarlo e instalarlo, o si es un usuario de Linux, probablemente esté incluido en el repositorio de paquetes de su distribución.

##### ¿Version móvil?
Tenga en cuenta también que hay versiones de Electrum para teléfonos móviles/celulares para Android e iOS. Por lo general, recomiendo no usar una billetera en un teléfono celular por razones de seguridad, pero si lo desea, puede hacerlo.

Si está de acuerdo con una billetera móvil, le recomiendo que obtenga Cake Wallet, que puede usar billeteras Bitcoin estilo Electrum, pero también Monero y Litecoin.

### Generación de una billetera
Una vez que abra Electrum (o Cake Wallet), puede elegir crear una nueva billetera. Ponle el nombre que quieras y elige la opción "Monedero estándar".

También señalaré que si eres paranoico, es perfectamente posible generar una billetera sin conexión a Internet.

#### Tu Semilla es tu dinero.
Ahora elija la opción "Crear una nueva semilla" al crear la billetera. Eso producirá aleatoriamente una "semilla" de 12 palabras.
![https://landchad.net/pix/bitcoin-01.png](https://landchad.net/pix/bitcoin-01.png)

**Estas palabras son tu dinero**. Una vez que se los muestren, escríbalos inmediatamente en papel físico, y los almacenará en algún lugar donde no se pierda ni se encuentre. Puedes memorizar estas doce palabras si confías en tu memoria.

Estas doce palabras desbloquean todos los fondos/direcciones que tendrá en esta billetera. Quien tiene tu semilla tiene la capacidad de gastar tu dinero.

Tenga en cuenta, obviamente, que he incluido una imagen de una frase semilla arriba en este tutorial. Yo o cualquier otra persona sería estúpido si alguna vez enviara Bitcoin a las siguientes direcciones, ya que las frases semilla ahora son públicas.

Una vez que haya escrito su semilla, haga clic en "Siguiente" y Electrum le pedirá que ingrese esa semilla nuevamente para asegurarse de que la haya escrito.

También se le pedirá que proporcione una contraseña. Esta contraseña simplemente encripta su archivo de billetera en esta computadora para que no tenga que volver a escribir su frase inicial cada vez que abra Electrum. Tenga en cuenta que cualquier persona con su frase inicial aún puede obtener sus fondos. Esta contraseña es solo protección en su computadora aquí.

#### Administrando su billetera
Una vez que se genere y abra su billetera, estará en la página de la billetera. Primero, recomiendo abrir el menú "Ver" y mostrar todas las pestañas diferentes.
![https://landchad.net/pix/bitcoin-02.png](https://landchad.net/pix/bitcoin-02.png)

#### Direcciones
La pestaña de direcciones contiene todas las direcciones de Bitcoin generadas por su frase semilla. De hecho, a medida que los use, la billetera agregará automáticamente más.

Estas direcciones (que se generarán todas con bc1 al principio) pueden ser utilizadas por otras personas para enviarle Bitcoins. Alguien puede simplemente copiar y pegar la dirección en su billetera para enviarle fondos.
![https://landchad.net/pix/bitcoin-03.png](https://landchad.net/pix/bitcoin-03.png)

### Recibir
Haga clic en la pestaña "Recibir" y luego haga clic en "Nueva dirección". Eso elegirá su primera dirección no utilizada que aparecerá en el lado derecho. Puede copiar esto desde la pestaña "Direcciones", pero esta pestaña también genera un código QR que también aparecerá a la derecha si hace clic en la subpestaña "Código QR".


#### ¿Para qué sirve el código QR?
En caso de que no lo sepa, un código QR es una forma de almacenar información de texto en un formato que puede escanearse con un teléfono. Si alguien tiene un programa de billetera en un teléfono, puede escanear fácilmente el código QR en otra pantalla para evitar tener que copiar su dirección o, peor aún, escribirlo manualmente.

#### Recibamos donaciones en nuestro sitio web.
Guarde el código QR y la dirección de la billetera a la que corresponde (a partir de bc1). Ahora simplemente colóquelos en su sitio web y cualquiera puede enviarles Bitcoin. Los usuarios de Bitcoin sabrán cómo escanearlos y usarlos.
