---
title: "Libreboot Static Site Generator(Lbssg) con pandoc."
date: 2025-07-14T09:43:10-03:00
tags: ['static','website','generator']
---
Usa pandoc como dependencia.   

Cree este sitio: https://cursoelectricidad.github.io
   
Reposotorio: https://codeberg.org/libreboot/lbssg   
Documentación: https://libreboot.org/docs/sitegen/   
   
Yo uso el sistema de blog de noticias al inicio de la página, borro el index.md   
```bash   
cp www-example/bunnies www # Tenes que copiar con el nombre la carpeta a www   
cd www/bunnies/site   
rm index.md   
cd news   
mv * ..   
cd ..   
```   
   
Editá el archivo `news.cfg` y agrega una descripción a tu blog, en mi caso hice un blog de electricidad.   
```bash   
BLOGTITLE="cursos"   
BLOGDESCRIPTION="Electricista"   
```   
   
Borré la publicación `bunny` que tiene por defecto y renombré `resignations.md` para usarla como bienvenido.   
```bash   
rm bunny202104xx.md   
mv resignations.md bienvenido.md   
```   
   
Ahora editá el archivo bienvenido.md con vim, nano, emacs tu editor de preferencia.   
   
En el archivo `MANIFEST` borrá todo y agregá tu primera publicación: `bienvenido.md`   
En el archivo `sitemap.md` borrá las entradas que hacían referencia a `bunny` y a `resignations`, renombré la primera por `bienvenido.md` y borré todas las entradas que no necesitaba.   
   
El `site.cfg` lo dejé así:   
```bash   
TITLE="Curso Electricidad"   
CSS="/global.css"   
DOMAIN="https://cursoelectricidad.github.io/"   
BLOGDIR="" # leave as empty string if you want the blog to be the homepage   
DEFAULTLANG="es"   
```   
En el archivo `lang/en/strings.cfg` traduje el mensaje `"Return to Index"` a `"Volver al índice"` porque faltaba traducir eso.
   
Ahora construímos el sitio desde la raíz del proyecto    
```bash   
cd ../../../   
./build   
```   
   
El binario `./clean` borra los `html`   
   
##### Importante:   
Debemos crear un repositorio para el directorio `www` (se crea usando `git init && git add origin git@github.com... && git add . && git commit -m first && git push`) que debe tener de nombre `tudominio.github.io` y tenes que crear una nueva organización en GitHub para poder tener ese dominio.   
Todo lo que está anterior a ese directorio será ignorado y la configuración `site.cfg` no estará en el repositorio.   
```bash   
cd www/bunnies/site   
git init    
git add ...    
git commit -m first   
git push ..... # etc, etc, etc   
```   
   
El archivo `template.include` contiene los links del `navbar` ahí eliminá todos los links que no quieras también eliminá los links que no necesitás del `sitemap.md`

##### Archivo `MANIFEST`
Place this file in the root of the directory where you want there to be a news section.
The order of the file names dictate what order the links will appear in, on the news index that is automatically generated (see below).


### Como tengo los repositorios configurados
```bash
[I] esotericwarfare@arch ~> cd projects/cursoelectricidad/
[I] esotericwarfare@arch ~/p/cursoelectricidad (master)> git remote -vv
origin	git@github.com:imlauera/lbssg.git (fetch)
origin	git@github.com:imlauera/lbssg.git (push)
[I] esotericwarfare@arch ~/p/c/www (master)> cd www/bunnies/site/
[I] esotericwarfare@arch ~/p/c/w/b/site (master)> git remote -vv
origin	git@github.com:cursoelectricidad/cursoelectricidad.github.io.git (fetch)
origin	git@github.com:cursoelectricidad/cursoelectricidad.github.io.git (push)
[I] esotericwarfare@arch ~/p/c/w/b/site (master)> 
```

##### Si queres crear un nuevo sitio:
```bash
[I] esotericwarfare@arch ~/p/c (master)> cd www/
[I] esotericwarfare@arch ~/p/c/www (master)> cp -R bunnies new_site
[I] esotericwarfare@arch ~/p/c/www (master)> cd new_site
[I] esotericwarfare@arch ~/p/c/www (master)> rm -rf .git
[I] esotericwarfare@arch ~/p/c/www/new_site (master)> git remote add origin git@github.com:curso2/curso2.github.io.git
```

#### Lo terminé dejando así

```bash
[I] esotericwarfare@arch ~/p/lbssg (master)> ls www/
electricidad  electrodomesticos
[I] esotericwarfare@arch ~/p/lbssg (master)>
```
