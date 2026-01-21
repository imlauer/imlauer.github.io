---
title: "Leer correos desde la terminal: Neomutt y mutt-wizard"
date: 2024-07-10T03:12:27-03:00
tags: ['neomutt','correo','terminal','mutt-wizard']
---
NeoMutt por defecto usa `POP` es decir que descarga todo tu correo a tu disco duro, si queres que tu correo no se descargue y quede en el servidor tenes que usar `IMAP`.

Para usar IMAP en NeoMutt y evitar que descargue todos tus correos como hace POP, solo tienes que configurar tu archivo de configuración (~/.neomuttrc o similar) con tu servidor IMAP. Ejemplo básico:

```bash
set folder = "imaps://usuario@imap.tuservidor.com/"
set spoolfile = "+INBOX"
set imap_user = "usuario"
set imap_pass = "tu_contraseña"
```
Así NeoMutt solo sincroniza los correos y carpetas que ves, **sin descargarlos todos localmente.**

---

```bash
sudo apt install -y neomutt
sudo apt install -y lynx notmuch abook urlview cronie curl isync msmtp pass ca-certificates gettext libpam0g-dev mpop
git clone https://github.com/cruegge/pam-gnupg
cd pam-gnupg
mkdir m4
aclocal && autoheader && autoconf && automake --add-missing
autoreconf --install --force
./autogen.sh
./configure
make
make install
```

Aca vamos a usar mutt wizard de Luke Smith pero no es necesario podes hacerlo manual preguntale a chatgpt xD o mira mi otra publicacion.

```bash
git clone https://github.com/LukeSmithxyz/mutt-wizard
cd mutt-wizard
sudo make install
pass init imlauerandres@gmail.com
gpg --full-generate-key
mw -a imlauerandres@gmail.com
```
Ahora vas a tener que habilitar doble factor de autenticación en tu cuenta de Google, entrá a tu gmail apretá el avatar de tu cuenta, gestionar tu cuenta y entrá a Seguridad y luego de habilitar doble factor de autenticacion, apretá esa opción y agregá una contraseña de aplicación para neomutt copiar y pegar el código.
Y cuando ejecutás 
mw -a tucorreo@asdf.com
tenés que ingresar la contraseña de aplicación que generaste en el paso anterior no tu contraseña real.
Ejecutá mbsync -a para bajar los correos o 
la tecla: o

```bash
/usr/local/share/mutt-wizard/mutt-wizard.muttrc:12: Option smtp_authenticators: gssapi is not a valid authenticator
/home/esotericwarfare/.config/mutt/muttrc:2: source: file /usr/local/share/mutt-wizard/mutt-wizard.muttrc could not be sour
ced
source: errors in /home/esotericwarfare/.config/mutt/muttrc
```
Se soluciona reemplazando 
```bash
set smtp_authenticators = 'gssapi:login'
```
por
```bash
set smtp_authenticators = 'login'
```

en `/usr/local/share/mutt-wizard/mutt-wizawrd.muttrc
Si tenés varios correos los alternas usando i1 i2 o si querés cambiar el atajo de teclaod los podés editarlos en `.config/mutt/muttrc``


Luego cambiá en mbsyncrc Master por Far y Slave por Near.

Y ejecutá `mbsync -a` para bajar tus correos.



Abrir archivos HTML en falkon: `BROWSER=falkon neomutt`


Genera una contraseña para tu neomutt desde aca ( lo mejor seria que dejes de usar Gmail ).

https://myaccount.google.com/apppasswords
