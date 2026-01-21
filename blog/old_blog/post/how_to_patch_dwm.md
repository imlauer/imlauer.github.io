---
title: "Parchear DWM"
date: 2023-12-02T16:56:28-03:00
tags: ['dwm','patch']
---

[https://suckless.org/hacking/](https://suckless.org/hacking/)


#### Hacking
## Copia/licencia
Solo aceptamos contribuciones de individuos, no de entidades corporativas. Vea el archivo de LICENCIA del proyecto al que está contribuyendo.

### Debugging
Si encuentra algún fallo, envíe un seguimiento completo a la lista de correo dedicada. Puedes crear rastros de retroceso con gdb:

Antes de iniciar un programa, es posible que deba permitir la creación de archivos principales. Te recomendamos que pongas esto en tu perfil:

```console
$ ulimit -c unlimited
```
Luego inicie el programa como de costumbre.

Después de que el programa falle, haga lo siguiente:

```console
$ gdb -q `which program` /path/to/core
gdb> bt full
```
Si encuentra congelaciones (sin ningún bloqueo) del programa, puede depurarlo de la siguiente manera:

```bash
$ gdb -q `which program` --attach `pgrep -o programa`
gdb> bt full
```
Envíe el resultado de ese comando a la lista de correo junto con el resultado del programa -v! ¡Gracias!

### Parches
Hay dos tipos de parches: los que se ajustan a tu gusto personal y los que crees que deberían incluirse en la línea principal.

Para parches que se ajusten a sus gustos personales y desee compartir con la comunidad, siga las instrucciones en la página wiki sobre cómo editar las páginas que ve aquí.

Para los parches que deberían incluirse en la línea principal, consulte la página de la comunidad y la lista de correo hackers@. Tenga en cuenta que solo los parches que se incluirán en los repositorios principales deben enviarse a esta lista, ¡los parches de personalización deben enviarse a la wiki!

Proporcione un "mensaje de confirmación" claro y conciso para sus parches.

Las siguientes instrucciones son una guía general sobre cómo generar y aplicar parches publicados en esta wiki:

formato de nombre de archivo de parche
El formato esperado para los parches es:

##### Para revisiones de git:

```bash
toolname-patchname-YYYYMMDD-SHORTHASH.diff
dwm-allyourbase-20160617-3465bed.diff
```

La fecha AAAAMMDD debe corresponder a la última vez que se modificó el parche. El SHORTHASH aquí son los siete caracteres del hash corto de git commit correspondientes a la última confirmación de la herramienta en la que se puede aplicar correctamente el parche y con la que se está trabajando. Puedes obtenerlo tomando los primeros siete caracteres del hash completo o por ejemplo:

```bash
git rev-parse --short <commit-id> (with commit-id: HEAD, commit hash, etc.)
```

Para versiones de lanzamiento:

toolname-patchname-RELEASE.diff
dwm-allyourbase-6.1.diff

La VERSIÓN debe corresponder a la versión de lanzamiento de la herramienta, es decir, 6.1 para dwm-6.1.

#### generación de diferencias
Para usuarios de git:

```bash
cd program-directory
git add filechanges...
git commit (write a clear patch description)
git format-patch --stdout HEAD^ > toolname-patchname-YYYYMMDD-SHORTHASH.diff

```
Para archivos comprimidos:

```bash
cd modified-program-directory/..
diff -up original-program-directory modified-program-directory > \
           toolname-patchname-RELEASE.diff
```

No envíe múltiples conjuntos de parches de confirmación. Un único parche debería aplicar todos los cambios usando el parche -p1.

#### programa de parche
Para usuarios de git, use -3 para solucionar el conflicto fácilmente:

```bash
cd program-directory
git apply path/to/patch.diff
```

Para parches formateados con git format-patch:

```bash
cd program-directory
git am path/to/patch.diff
```

Para archivos comprimidos:

```bash
cd program-directory
patch -p1 < path/to/patch.diff
```

#### Sacar el patch si no funcionó
patch -Rp1 < patch.diff


