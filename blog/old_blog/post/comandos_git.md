---
title: "Comandos git"
date: 2024-07-06T11:18:47-03:00
tags: ['git']
---
## COMANDOS COMUNES DE LA CLI DE GIT:

**`git --version`** Muestra la version de git instalada.


### GIT ADD

**`git add .`** Agrega los cambios de todos los archivos al area de preparacion (antes del commit).

**`git add -A`** (Otra opción) Genera el mismo efecto que **`git add .`**, la **-A** significa **--all**.


### GIT BLAME

**`git blame -c blogpost.html`** Muestra quien ha hecho cambios en dicho archivo, indentado.

**`git blame --help`** Muestra en el navegador el uso del comando (en este caso blame).

**`git blame archivo -L 35, 60 -c`** Muestra quien escribio el codigo con informacion de la linea 35 a la 60, EJ: git blame css/estilos.css -L 35, 60 -c


### GIT BRANCH

**`git branch`** Muestra las ramas disponibles y en cual estamos.

**`git branch [NewBranch-name]`** Crea una nueva rama.

**`git branch -d [branch-name]`** Borra una rama que ya fue pusheada y mergeada con su repositorio remoto.

**`git branch -D [branch-name]`** Borra una rama local aunque no haya sido pusheada y mergeada con su repositorio remoto.

**`git branch [nombre rama] [codigo commit]`** Crea una rama a partir de un commit. Es otra opción para guardar cambios hechos desde un detached HEAD en una rama nueva.

**`git branch -r`** Muestra las ramas remotas del repositorio.

**`git branch -a`** Muestra todas las ramas del repositorio, locales y remotas.

**`git branch [branch_name] -u [remote_repo/branch_name]`** Establece un upstream remoto para la rama local (**-u** significa **--set-upstream**).

**`git branch -vv`** Verifica que ramas locales siguen a una remote tracking branch, y muestra el commit mas reciente de dichas ramas. En las ramas locales que sigan ramas remotas se verá un **[remote-repo/tracking-branch-name]**, las que no sigan ramas remotas carecerán de dicha info.

**`git branch -m [old-branch_name] [new-branch_name]`**


### GIT CHECKOUT

**`git checkout -- [path del archivo]`** Elimina un archivo del working tree. (No funciona si es un archivo untracked, ver `git clean`).

**`git checkout [branch-name]`** (Otra opción) Cambiar de rama.

**`git checkout [codigo del commit]`** (Detached HEAD) Volver al estado de un commit anterior y revisar el codigo o hacer cambios experimentales (también se puede lograr con el nuevo comando **git switch -d [codigo del commit]**).

**`git checkout --orphan [new-branch-name]`** Crea una nueva rama huérfana. Se mantendrán todos los archivos en el index tree, en caso de que no se necesiten se recomienda el uso de `git rm -rf .` para eliminarlos. NOTA: la rama no figurará en la lista de ramas `git branch -l` hasta no poseer commits.


### GIT CHERRY-PICK

**`git cherry-pick [commit reference]`** Toma un commit de una rama y lo aplica a otra. Útil para team collaboration, hotfixes, deshacer cambios erroneos y restaurar commmits perdidos.

**`git cherry-pick [commit reference] -n`** Es un cherry-pick común pero en lugar de realizar un nuevo commit, moverá el contenido del commit de origen al working directory de la rama actual.

**`git cherry-pick [commit reference] -e`** Hará que git solicite un mensaje de commit antes de aplicar la operación cherry-pick.


### GIT CLEAN

**`git clean [path del archivo] -f`** Elimina un archivo untracked del working tree. (Si la variable de configuración clean.requireForce se establece en false no hace falta el -f).


### GIT CLONE

**`git clone [link del repositorio a clonar]`** Clona un repositorio remoto a local.


### GIT COMMIT

**`git commit -m "mensaje descriptivo"`** Crea un commit (Una version del proyecto).

**`git commit --amend`** Reescribe el commit anterior (ejemplo: si se olvidó agregar algún archivo o error en el msj del commit).

**`git commit -am "mensaje descriptivo"`** Crea un commit (Una version del proyecto) agregando previamente todos los cambios a stage, es un conjunto de **git add -A + git commit - m**.


### GIT CONFIG

**`git config --global user.name "nombre"`** Configura el usuario de forma global.

**`git config --global user.email "email@email.com"`** Configura el email de forma global.

**`git config --global user.password "password/PAT"`** Configura el password o personal access token de forma global.

**`git config --global --replace-all core.pager "less -iXFR"`** Evita que desaparezca el resultado de git log (paginación) al cerrar less (paginador).

**`git config --global pager.branch false`** Muestra el resultado de comandos como git branch por terminal y no en el editor (vim).

**`git config --global alias.stats “shortlog -sn --all --no-merges”`** Configura el comando “shortlog -sn --all --no-merges” en un alias (en este caso stats) en las configuraciones globales de git del pc.

**`git config -l`** Muestra las configuraciones del sistema, globales y (si está dentro de un repositorio) locales de git en el pc. Agregar los argumentos **--global** **--local** o **--system** para ver las configuraciones por separado.

**`git config --global pull.rebase false`** Evita que el comando **git pull** efectúe un rebase por default.

**`git config --global pull.ff only`** Setea el comportamiento del comando **git pull** para que solo se efectúe si el merge es de tipo fast-fordware únicamente, de lo contrario arrojará error.

**NOTA:** El argumento **--global** ejecuta dicha config globalmente, **--system** lo hace a nivel de sistema y **--local** lo hace solo en el repositorio actual (es el default en la mayoría de los casos con excepciones como **git config -l**).


### GIT FETCH

**`git fetch [nombre-remoto]`** Descarga todos los datos del proyecto remoto que no estén en el local.


### GIT GREP

**`git grep "palabra"`** Muestra en donde se usó la palabra.

**`git grep -n "palabra"`** Muestra en que líneas de que archivos se usó la palabra.

**`git grep -c "etiqueta html"`** Muestra cuantas veces y en qué archivos se usó la etiqueta [etiqueta html].


### GIT INIT

**`git init`** Crea un repositorio local. Sólo se requiere una vez por proyecto.


### GIT LOG

**`git log`** Muestra el historial de commits del repositorio.

**`git log --oneline`** Muestra el historial de commits en una sola linea (mas limpio que git log).

**`git log -S “palabra”`** Muestra cuantas veces se usó la palabra en todos los commits.


### GIT MERGE

**`git merge [nombreRama]`** Combina una rama con otra (ejemplo: se debe estar en la master para combinar una rama a la master).

**`git merge --ff`** Siempre que sea posible, realiza el merge como un fast-forward (solo actualiza el puntero de la rama para que coincida con la rama combinada; no crea un merge commit). Cuando no sea posible (cuando el historial a mergear no sea descendiente del historial actual), crea un merge commit.

**`git merge --no-ff`** Siempre genera un merge commit incluso cuando el merge podría resolverse como un fast-forward, con el fin de mantener un registro de cada merge.

**`git merge --ff-only`** Realiza el merge como un fast-forward cuando sea posible. Cuando no sea posible, se rehúsa a efectuar el merge y sale con un estado distinto de cero.

**`git merge --no-commit`** Realiza el merge y se detiene justo antes de crear el merge commit, para darle al usuario la oportunidad de inspeccionar y modificar aún más el resultado del merge antes de realizar el commit. Tener en cuenta que los fast-forward merges no crean un merge commit, por lo tanto, no hay forma de detener esas fusiones con --no-commit. Para asegurar que la rama actual no sea modificada o actualizada por el comando merge, usar --no-ff con --no-commit

**`git merge --abort`** Para abortar el merge y volver al estado anterior.


### GIT PULL

**`git pull [nombre-remoto] [rama]`** Combina un git fetch y git merge en un solo comando.

**`git pull --allow-unrelated-histories [nombre-remoto] [rama]`** Es un git fetch y git merge juntos cuando no permite hacer un git pull común debido al error: unrelated histories (diferencias en el historial del repo local con el remoto).

**`git pull --no-commit [nombre-remoto] [rama]`** Similar al pull común pero no genera el commit del merge dejando los cambios en el working tree. Si el merge se resuelve con fast-forward no se detendrá ya que no generará un merge commit, sera necesario el uso de --no-ff (Mismo comportamiento de git merge).

**`git pull --rebase [nombre-remoto] [rama]`** Similar al pull común pero en lugar de usar git merge para integrar los cambios del remoto al local, utiliza git rebase.

**`git pull --verbose [nombre-remoto] [rama]`** Proporciona una salida detallada que muestra el contenido que se descarga y los detalles del merge.


### GIT PUSH

**`git push -u [nombre-remoto] [rama]`** Sube el estado del repositorio local al repositorio remoto. Al usar push por primera vez se agrega "-u", el cual significa upstring. Le indica al sistema que estaremos subiendo todos los bytes necesarios para vincular ambos repositorios, el local y el remoto.

**`git push [nombre-remoto] [rama] -f`** Forzar un push si el repositorio remoto va por delante del repositorio local. (Esto puede tener efectos destructivos como perder los commits que van por delante del repositorio local, por eso git por default no permite un push si no es un fast-forward merge.

**`git push origin --delete [branch_name]`** Borra una rama de un repositorio remoto.

**`git push origin :[branch_name]:`** (Otra opción) Borra una rama de un repositorio remoto.

**`git push [nombre-remoto] --all`** Sube todas las ramas del repo local al remoto.


### GIT REBASE

**`git rebase [rama]`** Reorganiza los commits de forma que los de la rama actual queden sobre los de la rama de origen. (Reescribe el historial de los commits de la rama actual y no genera un merge commit).

**`git rebase --abort`** Para abortar y volver al estado anterior a "git rebase".


### GIT REFLOG

**`git reflog show`** Muestra el historial incluyendo los cambios revertidos con [git reset --hard] y [git commit --amend]. A diferencia de git log, git reflog muestra todo el historial de cambios que se han efectuado. Es útil para conocer exactamente que cambios se hicieron, quien y cuando.


### GIT REMOTE

**`git remote add [name] [url]`** Vincula un nuevo repositorio remoto al proyecto local.

**`git remote -v`** Muestra los repositorios remotos configurados en el proyecto en modo `--verbose`.

**`git remote rename [old-name] [new-name]`** Cambia el nombre del repositorio remoto (por default suele ser **origin**).

**`git remote set-url [name] [new-url]`** Cambia la url del repositorio remoto.

**`git remote remove [name]`** Elimina el repositorio remoto del proyecto local.


### GIT RESET

**`git reset`** Saca todos los archivos del index tree(ó staging area) y vuelven a working tree (ó working directory).

**`git reset [path del archivo]`** Sacar el archivo del index tree.

**`git reset HEAD [path del archivo]`** (Otra opción) Saca el archivo del index tree.

**`git reset --hard HEAD`** Regresa al estado del commit HEAD borrando los cambios en el index y working tree.

**`git reset --hard`** (otra opción) Deshace todos los cambios de todos los archivos en seguimiento, volviendo al estado del commit HEAD.

**`git reset HEAD~1`** Deshace el último commit extrayendo los cambios del mismo al working tree. Implicitamente aplica el argumento `--soft` ya que es el default.

**`git reset --soft HEAD~1`** Deshace el último commit extrayendo los cambios del mismo al index (staging area). No confundir con el comando anterior que extrae los cambios al working tree.

**`git reset --merge HEAD`** La referencia HEAD apuntará al commit original de antes del merge. La opción --merge no tiene nada que ver con el comando `git merge`, es como `git reset --hard HEAD`, pero más segura ya que no toca los cambios en el working tree ni index tree.

**`git reset --hard HEAD^`** Regresa 1 commit antes de HEAD. Deshace 1 commit borrando todos los cambios hechos en el.

**`git reset --hard HEAD~1`** Otra forma de escribir `git reset --hard HEAD^`. El número representa la cantidad de commits que regresaré desde HEAD (Deshace n commits borrando todos los cambios hechos en ellos).

**`git reset --keep HEAD@{1}`** Vuelve al ultimo estado de head.


### GIT RESTORE 
https://git-scm.com/docs/git-restore

**`git restore [file]`** Para descartar cambios en el working directory / working tree (Implícitamente se ejecuta con el argumento `--worktree`/`-W` ya que es el default).

**`git restore --staged [file]`** Descarta los cambios del staging area / index tree y los retorna al working directory / working tree (Unstage).

**`git restore [path-file-with-extension] --source [commit-hash]`** Restaura el archivo al estado que tenía en dicho commit.


### GIT SHORTLOG

**`git shortlog`** Muestra cuantos commits han hecho los miembros del equipo.

**`git shortlog -sn`** Muestra las personas que han hecho ciertos commits.

**`git shortlog -sn --all`** Muestra todos los commits (también los borrados).

**`git shortlog -sn --all --no-merges`** Muestra las estadísticas de los commits del repositorio actual (excluye los merges commits).


### GIT STASH

**`git stash`** Almacena en memoria temporal los archivos en staging area y working directory que están siendo trackeados (que en algn momento estuvieron en stagin area) limpiando el working tree para hacer cambios de rama o trabajar en algo mas.

**`git stash pop`** Recupera los archivos almacenados en el stash volviendolos a su estado anterior (y los elimina del stash).

**`git stash apply`** Recupera los archivos almacenados en el stash volviendolos a su estado anterior (no los elimina del stash, ejem: se pueden extraer de nuevo del stash en otros lugares).

**`git stash -u`** Modifica el comportamiento default almacenando en el stash los archivos untracked también.

**`git stash -a`** Modifica el comportamiento default almacenando en el stash los archivos ignored también.

**`git stash --keep-index`** Posee el mismo comportamiento del comando `git stash`, pero a su vez deja todos los archivos del index disponibles en el index (útil para generar un stash de los archivos en el index).

**`git stash list`** Debido a que se puede ejecutar git stash varias veces, puedes tener varios stashes, con este comando los listas todos en consola.

**`git stash pop stash@{n}`** De esta forma se aplica un pop a un stash específico cuando se tienen varios.

**`git stash push -m "message"`** De esta forma se agrega un msj descriptivo al stash para no tener el default WIP (work in progress).

**`git stash -p`** Iterará sobre cada cambio consultando si queremos almacenarlo en un stash con las siguientes opciones `Stash this hunk [y,n,q,a,d,/,e,?]?`, `y` es si, `n` es no, `q` es salir (se mantiene en stash lo que ya se haya seleccionado con `y` ) y `?` para consultar mas detalles sobre las opciones disponibles.

**`git stash branch [name] stash@{n}`** Crea una rama nueva basada en el commit a partir del cual se creó el stash y, después, se hace pop en ella con los cambios del stash seleccionado.

**`git stash drop stash@{n}`** Elimina un stash.

**`git stash clear`** Elimina todos los stashes.


### GIT STATUS

**`git status`** Muestra el status del repositorio.


### GIT SWITCH

**`git switch [branch-name]`** Se mueve hacia la rama especificada.

**`git switch -`** Vuelve a la ultima rama visitada (diferente a la actual).

**`git switch -c [new-branch-name]`** Crea una rama y se cambia a ella (atajo para `git branch nombre-rama` y `git switch nombre-rama`). A su vez permite guardar cambios hechos desde un detached HEAD en una nueva rama.

**`git switch -d [commit-hash]`** (Detached HEAD) Volver al estado de un commit anterior y revisar el codigo o hacer cambios experimentales (Es la versión moderna del **git checkout commitHash**).

**`git switch --orphan [new-branch-name]`** Crea una nueva rama huérfana. Se eliminan todos los tracked files. En dicha nueva rama quedarán todos los untracked files (incluídos en el .gitignore), en caso de que no se necesiten se recomienda el uso de `git add -A` y `git rm -rf .` para eliminarlos. NOTA: la rama no figurará en la lista de ramas `git branch -l` hasta no poseer commits.


## INFO EXTRA

### Diferencia entre `reset`, `revert` y `checkout`

| Command       | Scope         | Common use cases                                                     |
| ------------- | ------------- | -------------------------------------------------------------------- |
| git reset     | Commit-level  | Discard commits in a private branch or throw away uncommited changes |
| git reset     | File-level    | Unstage a file                                                       |
| git checkout  | Commit-level  | Switch between branches or inspect old snapshots                     |
| git checkout  | File-level    | Discard changes in the working directory                             |
| git revert    | Commit-level  | Undo commits in a public branch                                      |
| git revert    | File-level    | (N/A)                                                                |



Ignorar archivos: Se crea un archivo llamado **.gitignore** y adentro se mencionan todos los archivos y carpetas que deseo que git ignore ( ***.a** ) ( **/folder** ).

Si aparece el editor de texto vim en la terminal de git presiono **i** para insertar texto, **esc** para volver a la línea de comandos y **:wq** para aplicar el cambio ("w" de write y "q" de quit).

En caso de que dos personas hayan modificado un mismo archivo, o una elimine un archivo que otra modificó en distintas ramas se generará un conflicto, los veremos en nuestros archivos de la siguiente manera:

    Contenido no afectado por el conflicto
    <<<<<<< master
    Contenido en conflicto dentro de master (rama actual)
    =======
    Contenido en conflicto dentro de feature (rama entrante)
    >>>>>>> feature branch;
