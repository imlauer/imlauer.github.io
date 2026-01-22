---
title: "Como configurar tu proyecto HUGO en una nueva PC"
date: 2024-07-06T11:17:21-03:00
tags: ['hugo']
---
Lo más importante es no pushear imágenes porque quedan en el historial.

Themes de hugo: https://demo.gethugothemes.com/

Es recomendable tener 3 repositorios.

1 fork del hugo theme que vayas a usar, 1 repositorio para la pagina (tunombre.github.io) que lo vas a alojar en la carpeta `public` y otro repositorio base que debería ser privado en mi opinión.

Clono el repositorio usando SSH.  
Clono usando `--recurse-submodules -j8`  

**Si hacés esto clonás public** cuando no es necesario clonarlo, ¿quizás hay que poner public dentro de .gitignore?

```bash
git clone --recurse-submodules -j8 git@github.com:imlauera/blog.git
cd blog

```
`-j8` es para optimizar el rendimiento.

O si ya lo había clonado ejecuto

```bash
git submodule init update --init --recursive
```
 
Luego ejecuto   
```bash
cd blog
hugo
hugo serve
```
Y ya estoy listo para empezar a escribir mi nuevo artículo en cualquier computadora.  

##### Ojo
Hay un problema si empezaste a hacer el proyecto en Linux y te pasás a Windows. Ambos sistemas operativos tienen diferentes caracteres para representar el fin de línea.
Windows y Linux utilizan diferentes caracteres para marcar el final de una línea o carácter de fin de línea (EOL):
Windows: utiliza el modelo CR/LF, que consta de dos caracteres, \r\n, donde \r representa un retorno de carro y \n representa una nueva línea.
Linux: utiliza el modelo \n, que es un solo carácter.


```bash
cd public
git checkout master
git push
```
O `git pull`

```bash
git config pull.rebase false # merge
git config pull.rebase true # rebase
git config pull.ff only # fast-forward only
```

#### Instalando un nuevo theme a tu sitio.
```
hugo new site
cd newsite
git submodule add https://github.com/halogenica/beautifulhugo.git themes/beautifulhugo
```
Ahora tenés que copiar los archivos de exampleSite al directorio base del proyecto. `cp -r themes/beautifulhugo/exampleSite/* . -iv`


#### Otra cosa importantísima:
la carpeta `public` siempre tiene que estar apuntado a tu repositorio `tunombre.github.io` para hacer esto podés clonar tu repo en la carpeta `public` así:

```bash
git clone git@github.com:imlauerindex/imlauerindex.github.io.git public
```

Es decir el repositorio base tiene que apuntar a un repositorio privado(o publico) y el public al repositorio con el nombre de la pagina de github `tunombre.github.io`


### A veces instalar un nuevo theme a tu sitio no funciona.
No sé por qué carajo, pero mi solucion es directamente clonar el theme y montarlo desde ahí, una vez me pasó que tenía un archivo llamado hugo.toml y ese archivo me probocaba el fallo y no podía compilar el sitio, es decir si lo clonaste lo pusiste en una carpeta de themes/ y no te funcionó intentá clonarlo y tomar el theme como si fuera todo un sitio completo, no como un theme, eso me funcionó.

O si es sólo el theme:
```bash
 git clone --recurse-submodules -j8 https://github.com/imlauera/bare-hugo-theme themes/bare
cd themes/bare
 git submodule update --force --recursive --init --remote

```
### Para agregar un theme
```bash
git submodule add https://github.com/orf/bare-hugo-theme.git themes/bare
# This is required:
git submodule update --init --recursive
```


#### Error de mierda clonando el theme
```bash

└─$ git submodule add git@github.com:imlauera/bare-hugo-theme.git bare
fatal: A git directory for 'imlauera/themes/bare' is found locally with remote(s):
  origin        https://github.com/orf/bare-hugo-theme.git
If you want to reuse this local git directory instead of cloning again from
  git@github.com:imlauera/bare-hugo-theme.git
use the '--force' option. If the local git directory is not the correct repo
or you are unsure what this means choose another name with the '--name' option.
```
https://stackoverflow.com/questions/20929336/git-submodule-add-a-git-directory-is-found-locally-issue

Tenés que borrar la caché :
```bash
git rm --cached path_to_submodule (no trailing slash) as well as
rm -rf path_to_submodule
```
Y fijate en `.gitmodules` que no haya ninguna referencia a ese repositorio, si las hay borralo.
```bash
rm -rf .git/modules/path_to_submodule
```

Después de todo eso podés intentar ejecutar otra vez:

```bash
git submodule add https://github.com/path_to_submodule
```


### Como solucione este problema de mierda que estuve horas que no descargaba assets/css/bulma ni los iconos.
```bash
$ git clone --recurse-submodules -j8 git@github.com:imlauera/blog.git

...
Resolving deltas: 100% (37994/37994), done.
fatal: remote error: upload-pack: not our ref 5b0902b2797a51ab224f34717ba233e6bb6f070a
fatal: Fetched in submodule path 'imlauera/themes/bare/assets/css/bulma', but it did not contain 5b0902b2797a51ab224f34717ba233e6bb6f070a. Direct fetching of that commit failed.
fatal: Failed to recurse into submodule path 'imlauera/themes/bare'

```

Borrá el themes/bare y cloná el original:
```bash
rm -rf themes/bare
git clone https://github.com/orf/bare-hugo-theme themes/bare
cd themes/bare
git remote set-url origin git@github.com:imlauera/bare-hugo-theme.git
git pull --force
```

Por qué carajo paso esto todavía no lo entiendo.
