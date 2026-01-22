---
title: "Generadores de sitios estaticos"
date: 2024-08-06T04:44:55-03:00
tags: ['generador','sitios','estaticos']
---
WordPress es el demonio. Todos los generadores de sitios webs estáticos son superiores.
Actualmente para este blog estoy usando **Hugo** y funciona bastante bien, pero lo ideal sería simplemente generar la página usando un makefile.

Un sitio creado usando un simple `makefile`: https://pablo.rauzy.name/
>Mi sitio web personal (`https://pablo.rauzy.name/`) solía generarse mediante un simple Makefile. Luego agregué funciones como noticias y un canal RSS, una forma de enumerar automáticamente mis publicaciones de investigación y materiales de cursos, una lista de libros filtrables con etiquetas, etc. Así que ahora sigue siendo un Makefile, pero el Makefile en sí es un poco más simple que antes. solía serlo, pero llama a algunos scripts Bash que en particular hacen uso de las increíbles utilidades `xml2` y `2xml` para poder manipular HTML de manera orientada a líneas usando las utilidades principales (grep y sed principalmente). Además de eso, tengo algunos ganchos de git que llaman a make automáticamente cuando es necesario, en particular en el servidor remoto donde está alojado el sitio web para que la versión pública se reconstruya cuando envío actualizaciones al repositorio allí. ¡Ha estado funcionando a las mil maravillas durante años! Mi historial de git se remonta a 2009.    

Fuente: https://news.ycombinator.com/item?id=37454853

Astro, es un nuevo generador de sitios webs estáticos pero parece otro framework de javascript que lo complica todo.


NextJS otro generador de sitios web estáticos que se está haciendo popular.


Otro generador de sitios estáticos muy conocido es Jekyll a mi no me gusta porque usa Ruby.

Nunca usé este pero debería probarlo, no usa ningún framework de javascript: https://www.11ty.dev/ y Nuxt

El mejor de todos en mi opinión: https://romanzolotarev.com/ssg.html

https://jamstack.org/generators/

Generadores de sitios estáticos en bash:
https://jamstack.org/generators/expose/   
https://jamstack.org/generators/bashblog/

Generadores de sitios estáticos en lisp:
https://jamstack.org/generators/coleslaw/


Generadores de sitios estáticos en C:
https://jamstack.org/generators/blogc/   
https://jamstack.org/generators/sblg/     

