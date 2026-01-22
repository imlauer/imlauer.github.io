---
title: "Ejecutar qutebrowser en framebuffer"
date: 2024-12-08T18:39:44-03:00
tags: ['framebuffer']
---
```bash
export QT_QPA_PLATFORM=linuxfb
export QT_QPA_PLATFORM=linuxfb:offset=900x130:size=768x600
qutebrowser
```
O usando también: `export QT_QPA_PLATFORM=eglfs`

**Cambiar el keymap:**

```bash
sudo pacman -S ckbcomp  
ckbcomp -layout xx > xx.kmap
O tomá un keymap desde acá: /usr/share/kbd/keymaps/i386/qwertz
kmap2qmap xx.kmap xx.qmap
QWS_KEYBOARD="TTY:keymap=xx.qmap"
```
**Compilá kmap2qmap desde acá:**:
```bash
git clone https://github.com/qt/qttools
cd qttools
mkdir build
cmake ..
```
 
Y agregá en `.bashrc` o en `.config/fish/config.fish`:
```bash
export QT_QPA_PLATFORM=linuxfb:offset=900x130:size=768x600:keymap=es.qmap
```
### OJOO!!!

Asegurarte de bajar el qttools para la versión de tu QT.
Ejemplo de error:
```bash
Version 6.8.2 of package Qt6 was requested but an incompatible version was found: 6.8.1.  You can pass -DQT_NO_PACKAGE_VERSION_CHECK=TRUE to disable
```
Tenés que entrar a la página de qttools bajo Release encontrarás TAGS. Ahí buscá la vresión indicada para vos: en mi caso 6.8.1

**ESO NO ES TODO!!!** Ahora cuando bajes el zip o el tar.gz de tu versión (en mi caso 6.8.1) y lo compiles te va a putear porque te falta `src/assistant/qlitehtml` porque es un submódulo que no lo baja. Tenés que clonar este repo en `/tmp` ejecutá: 

#### ESO NO ES TODO
No te va a compilar el kmap2qmap, tenés que abrir `configure.cmake` y descomentar:
```bash
qt_configure_add_summary_entry(ARGS "kmap2qmap")
```

```bash
git clone --recurse-submodules -j8 "https://github.com/PyQt5/QLiteHtml"`
cd QLiteHtml
cp -R qlitehtml /home/usuario/Downloads/qttools-6.8.1/src/assistant
vim /home/usuario/Downloads/qttools-6.8.1/configure.cmake
Descomentá qt_configure_add_summary_entry(ARGS "kmap2qmap")
cd /home/usuario/Downloads/qttools-6.8.1
mkdir build
cd build
cmake ..
make
sudo make install
```
**Y ahora sí compila, pero no aparece kmap2qmap en mi caso no sé por qué**    

Olvidate de todo esto si no te funcionó cloná este repo:

```bash
git clone https://github.com/neochapay/kmap2qmap
cd kmap2qmap
qmake .
./kmap2qmap
```

Todo esto para tener la utilidad `kmap2qmap` y poder tener el teclado en español XDD, amo el framebuffer.


## FIN: TODO ESTO NO SIRVE PARA NADA... SOLO ESTO ME SIRVIO
https://forum.qt.io/topic/107443/how-to-configure-keyboard-layout-when-running-qt-on-eglfs-without-x

```bash
export XKB_DEFAULT_LAYOUT=es
```


Si querés copiar y pegar un texto podés clonar privatebin

```bash
git clone https://github.com/PrivateBin/PrivateBin
cd PrivateBin
php -S 127.0.0.1:1111
```

Copiar desde qutebrowser y pegar a ahí entrar a la URL y darle a guardar archivo

##### Agregá para usar a Android como user-agent así las páginas cargan más rápido en `.config/qutebrowser/config.py`:

```bash
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36"
)
config.load_autoconfig()
```
