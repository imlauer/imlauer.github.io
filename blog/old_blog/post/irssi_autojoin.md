---
title: "Conectarse automáticamente a una red y a un canal de IRC usando Irssi y guardar logs"
date: 2023-09-08T20:00:49-03:00
tags: ['irssi']
---

### Habilite la conexión automática en un servidor:
```
/SERVER MODIFY -auto irc.libera.chat
```

Para desactivarlo nuevamente, use `-noauto`.

#### Unirse automáticamente a canales
```
/CHANNEL ADD -auto #channelname NetworkName
```

(Ver tus redes configuradas con: /NETWORK)

Agregue todos los canales actualmente abiertos como canales de unión automática
```
/ADDALLCHANS
```
(Este es un alias predeterminado que ejecuta un script Perl para ejecutar en masa comandos /CHANNEL ADD)

### Inicio de sesión automático en NickServ
Muchas redes admiten el inicio de sesión SASL (consulte el sitio web de la red o el canal de ayuda para obtener más detalles). En tal caso, utilícelo:

```
/NETWORK ADD -sasl_username yourname -sasl_password yourpassword -sasl_mechanism PLAIN liberachat
```

Se aplican algunos casos especiales. Para la red OFTC, puede utilizar este script: [https://unit193.net/dump/holdjoin.pl](https://unit193.net/dump/holdjoin.pl) en combinación con CertFP.

Otra posibilidad es usar el comando WAIT dentro de autosendcmd para agregar un retraso después de que se envió el comando de identificación y antes de unir canales automáticamente (pero tenga en cuenta que esto no es confiable).

```
/NETWORK MODIFY -autosendcmd "^msg NickServ identify YOURPASSWORD YOURNICK;wait -OFTC 2000" OFTC

```

### Registro de mensajes
Bajá el script de acá: [queryresume](/files/queryresume.pl)
```bash
mkdir -p .irssi/scripts/autorun
cd .irssi/scripts/autorun
wget http://scripts.irssi.org/scripts/queryresume.pl
o cd /usr/share/irssi/scripts/
irssi
/SET autolog ON
/script load script.pl
```
Y en el script vas a tener que comentar `return unless (ref $witem && $witem->{type} eq 'QUERY');` a `#return unless (ref $witem && $witem->{type} eq 'QUERY');` 
Con eso ya tenemos autologs en el 2024 XD.

