---
title: "Millones de aplicaciones vulneradas: como ejecutar código remoto sobre millones de personas y cientas aplicaciones."
date: 2025-03-01T22:31:57-03:00
tags: ['hacking']
---
Fuente: 
w3m https://kibty.town/blog/todesktop/

**Traducción**:    

Esto empezó cuando estaba mirando cursor, un editor con inteligencia artificial. Yo uso lulu por visión de objetos en mi laptop, así que cuando descargué el instalador de cursor obtuve este pop-up:

![lulu](https://kibty.town/files/img/posts/todesktop/lulu-alert.png)

Una alerta de LuLu, mostrando que "Install Cursor" estaba intentando conectarse a "[https://download.todesktop.com](https://download.todesktop.com)"

Ahora, ¿qué es todesktop? Pensé que estaba descargando cursor. Mirando en su sitio aparenta ser un servicio bundler[1] además de proveer un SDK[2] para aplicaciones de electron. Así que aparentemente el instalador que descargué está en realidad controlado por **todesktop**, no cursor.

Esto me despertó la curiosidad y me cree una cuenta en **todesktop** para investigar, y cuando apreté el botón de login de GitHub, vi mi llamada a Firebase.

##### basic firebase recon[3]

Cuando me dí cuenta que la aplicación usaba firestore (es una base de datos no-sql de firebase que es frecuentemente usada en frontend), rápidamente abrí mi devtools(F12 o Control+Shift+i en cualquier navegador) y empecé a hacer basic recon[3] en el firebase.

Me dí cuenta que el sitio tenía sourcemaps, que hicieron que la búsqueda de todos las rutas de firestore usadas en aplicación sea más fácil (sigue siendo fácil sin los sourcemaps)

Luego encontré una colección insegura, temporaryApplications, que parecía darme una lista de nombres de algunas aplicaciones (edito: **todesktop** aclaró que esta colección no tiene información sensible y no fue actualizada desde el 2022), pero no encontré más que eso, todo parecía seguro en el firebase salvo de eso.

Me dí cuenta de que la mayoría del deployment y la lógica general pasa en la terminal con el paquete de npm llamado: `@todesktop/cli`, así que lo instalé y comencé a investigarlo.

El cli (command line interface) administra deployments, subida de código de fuente, y mucho más. La página parece ser una shell para crear aplicaciones, ver deployments, etc etc.

Yo fui otra vez suertudo que el cli también tenía sourcemaps, así que usé el [sourcemapper](https://github.com/denandz/sourcemapper) para extraerlos en un árbol source.

Observando ahí, encontré una vulnerabilidad arbitraria s3 a través de una función de firebase llamada `getSignedURL`, pero no tenía una clave s3 (ruta de archivo) para subir a eso haría algo interesante, así que seguí buscando.

##### hijacking[4] la tubería de deployment a través de un script post-install

Quería obtener acceso a la máquina en donde la aplicación se construye y la forma más fácil de hacerlo es a través de un script postinstall en el `package.json`, así que hice eso con un `simple reverse shell payload`.

Esto funcionó. Navegando a través del contenedor, descubrí donde estaba vivía el código de compilación de la aplicación y encontré esto:

![configprodjsonencrypted](https://kibty.town/files/img/posts/todesktop/config-encrypted.png)

Encontré el código para descifrar este archivo, y esto es lo que obtuve luego de descifrarlo:

![config-json](https://kibty.town/files/img/posts/todesktop/config-json.png)

Un archivo llamado "config.json" con 2 id de apple, firma remota y credenciales hsm. Este contenedor guarda los secretos.

Investigando más en el contenedor, encontré una clave de administrador de firebase hardcodeada (que estaba completa).

##### post-exploitation

Rápidamente me dí cuenta que con las credenciales que tengo, puedo deployar una actualización automática a cualquier aplicación que quiera, y que los clientes reciban la actualización inmediatamente al reiniciar la aplicación.

Luego hice un código para usar mis credenciales para deployar una actualización a mi aplicación, y funcionó. Inmediatamente recibí la actualización en mi cliente de mi aplicación y obtuve un **Remote Code Execution**.

##### Hablemos sobre el impacto 

Con esto podría publicar actualizaciones automáticas a todas las aplicaciones que usan **todesktop**, como por ejemplo:

* clickup (https://clickup.com)
* cursor (https://cursor.com) (update: cursor has now switched off of todesktop to
* their own build system)
* linear (https://linear.app)
* notion calendar (https://calendar.notion.so)

(Por favor no acoses a esas empresas o hacerlo ver como si fuera su culpa, ellos no la tienen, si alguien acá tiene la culpa es **todesktop**.)

Si hago una estimación probablemente está en el rango de miles de millones de personas en el entorno de tecnología, otros hackers, programadores, ejecutivos, etc. **Haciendo que este exploit sea mortal si es usado**.

##### El arreglo

Usé mis contactos para comunicarme con el creador de **todesktop**, chateamos por signal y el arreglo llegó de inmediato, ellos fueron lo suficientemente amables para compensarme por mis esfuerzos y fueron muy amables.

El contenedor build ahora tiene un privilegiado "sidecar"(acompañante)[5] que hace el firmado, y la subida y todo lo demás **en vez de que esta lógica esté en el código de usuario del contenedor principal**.

Los incidentes de seguridad pasan todo el tiempo, es natural. Lo que impora es la respuesta de la empresa, y la respuesta de **todesktop** fue buenísima.

Mirá el reporte de **todesktop** acá: https://www.todesktop.com/blog/posts/security-incident-at-todesktop

---

##### Definiciones y referencias:

1. En Electron, un servicio bundler se refiere a una herramienta que ayuda a empaquetar y preparar una aplicación Electron para su distribución. Un bundler es responsable de recopilar todos los archivos y recursos necesarios para ejecutar la aplicación, como el código JavaScript, los archivos de recursos, las bibliotecas y las dependencias, y empaquetarlos en un formato que pueda ser ejecutado en diferentes plataformas.
2. Un SDK (Kit de Desarrollo de Software) es un conjunto de herramientas de desarrollo que permite a los programadores crear aplicaciones en este caso para Electron. Un SDK proporciona un conjunto de bibliotecas, frameworks, herramientas y documentación que facilitan la creación, prueba y depuración de aplicaciones Android.
3. Basic Firebase Recon es un conjunto de técnicas y herramientas utilizadas para realizar una investigación y análisis inicial de la configuración y seguridad de un proyecto de Firebase. Firebase es una plataforma de Google que ofrece una variedad de servicios para el desarrollo de aplicaciones web y móviles, incluyendo bases de datos, almacenamiento de archivos, autenticación de usuarios y más. El objetivo de un Basic Firebase Recon es identificar posibles vulnerabilidades y debilidades en la configuración de seguridad de un proyecto de Firebase, lo que puede incluir:
4. "Hijacking" es un término que se utiliza en varios contextos para describir la toma ilegal o no autorizada del control de algo.
5.  **Build Container**:
Un Build Container es un contenedor que se ejecuta durante el proceso de creación de una imagen de Docker. Su propósito es compilar y construir el código fuente de una aplicación, creando así la imagen de Docker final que se puede ejecutar en producción. El Build Container tiene acceso a todos los archivos y recursos necesarios para compilar y construir la aplicación, incluyendo el código fuente, las dependencias y las herramientas de compilación.

**Privileged Sidecar**:
Un Privileged Sidecar es un tipo de contenedor que se ejecuta con privilegios de root (o con permisos elevados) en el host que lo ejecuta. 
