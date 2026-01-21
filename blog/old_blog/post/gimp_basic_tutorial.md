---
title: "Básico: Crear un thumbnail en GIMP"
date: 2023-12-04T11:56:18-03:00
tags: ['gimp','thumbnail']
---
Cuando abrís GIMP las barras de estado están en diferentes ventanas, si querés tenerlas todas en una ventana, abrís GIMP y en el menú principal buscá Windows -> Single Window Mode
Si accidentalmente cerraste alguna de estas barras podés recuperarlas yendo a Windows -> Recently closed docks, o andá a dockable dialogs y buscá la que habías cerrado.


`Ctrl + n` para crear un nuevo archivo/imagen

Si querés crear un thumbnail para youtube dejalo en 1920x1080p
z para hacer zoom y + - para acercarse o click izquierdo y control click izquierod para alejarse

Por defecto el fondo va a ser el color secundario de GIMP, podés cambiar el fondo secundario y al crear un nuevo archivo ese será el nuevo color de fondo.


`B o shift b` te selecciona automáticamente la herramienta del balde, y ahora en el menú izquierdo inferior llamada tool options podés seleccionar Foreground(FG) o Background(BG).
Foreground : principal , background: secundario, son los colores que tenés seteados más arriba.
O podés seleccionar pattern fill (patrón relleno)

`ctrl alt o` para abrir una nueva imagen en una nueva capa
`control o` abre una nueva imagen como un nuevo archivo

si apretás `m` podés mover la imágen importada como capa
para agregar texto apretá `t` introducí el texto

ahora para agregarle sombra, podes seleccionar la layer 
en donde tenés el texto dale botón derecho y alpha to selection y sólo seleccionará el área de esa capa en donde haya algo que tiene algo que no sea transparente.
ahora creá una nueva capa dándo botón derecho en el menú de capaz y dale a new layer
Ahora andá al top menu a la opción select  y dale a grow
ahora apretá shift b o B para seleccionar la herramienta del balde y pintá de negro la selección, luego mové la capa que creaste abajo de la capa del texto eso creará un efecto de resaltado.

`t` para acceder al modo texto

`ctrl z` y `ctrl y` (undo y redo)
podés cambiar el color de letra seleccionando el texto

ctrl a para seleccionar todo (no es recomendable copiar y pegar imágenes porque quedan como una capa flotante, mejor guarda la imagen y abrila con `ctrl alt o` )

si estás usando el balde y vez que no agrega el color fijate en el menú de opciones en donde dice "area afectada o affected area " tiene que estar seleccionado fill whole selection


formato al texto:
dale botón derecho a la capa en donde tenés el texto y dale a alpha to selection o en este caso para agergar drop shadow no es necesario, sólo con tener la capa selecionada es suficiente.

filters -> light and shadow drop shadow y aumenta el opacity
`ctrl f` para repetir el comando anterior


### resize image gimp
seleccioná la imágen, andá al menú layer dale a scale layer y cambiá el ancho
o podés usar shift s al seleccionar la imágen


#### cuando copiás y pegas una imagen passa esto:
Cuando pegas algo en GIMP, se convierte en una selección flotante. Es una especie de pseudocapa temporal que contiene el contenido pegado y le permite moverlo (y editarlo de otras maneras) antes de fusionarlo en la imagen de destino. Sin embargo, tener una selección flotante activa también le impide realizar ediciones en cualquier cosa que no sea la selección flotante.

Para ver si tiene una selección flotante, eche un vistazo al cuadro de diálogo Capas, donde aparece como una capa especial. Además, cuando el puntero del mouse está fuera de la selección flotante (pero dentro de la ventana de la imagen), se muestra un símbolo de ancla junto a él.

Hay dos formas principales de deshacerse de una selección flotante:

Puede anclarlo a la capa actual con el comando Capa → Anclar capa (Ctrl+H), o haciendo clic en el icono de ancla en el cuadro de diálogo Capas, o simplemente haciendo clic en cualquier lugar de la imagen fuera de la selección flotante. Esto fusiona la selección flotante en la capa actual, sobrescribiendo cualquier otra cosa que pueda haber debajo de la selección.

Alternativamente, puede convertir la selección flotante en una nueva capa usando el comando Capa → Nueva capa (Ctrl+Shift+N), o el botón Nueva capa en el cuadro de diálogo Capas, mientras la selección flotante está activa. Esto convierte la selección flotante en una capa real que puedes editar cuando quieras.


### Remove background (transparencia)
Abrí la imágen  
Desde el menú -> Layer -> New Layer  
Fill with: Transparency  
Image-> Merge Visible Layer(Control+M) -> Merge  
Bucket Fill (Shift b)  
En Tool Options Bucket Fiil mode -> Erase y abajo de Affected Area poné Fill similar colors en vez de fill whole selection
Edit -> Copy  
Edit -> Paste As -> New Layer  



