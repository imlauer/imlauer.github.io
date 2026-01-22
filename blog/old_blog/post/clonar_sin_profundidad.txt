---
title: "Clonar un repositorio sin profundidad"
date: 2023-09-24T13:11:37-03:00
tags: ['clonar','repositorio','profundidad']
---

Un clonado sin profundidad, te permite clonar un repositorio manteniendo sólo las últimas confirmaciones del historial.

Es un problema común que algunos repositorios crezcan en tamaño después de mucho tiempo trabajando en ellos.

Hay principalmente dos razones que hacen que un repositorio GIT crezca masivamente:

- Acumulación con el tiempo de un largo historial.
- Inclusión de ficheros binarios de gran tamaño.

Por lo que un repositorio puede crecer debido al aumento de la carpeta de trabajo y a su historial acumulado, que encima puede agravarse si el repositorio contiene versiones con ficheros que están en desuso.

#### Clonado normal:
```bash
$ git clone https://github.com/symfony/symfony.git
Cloning into 'symfony'...
remote: Counting objects: 329770, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 329770 (delta 1), reused 1 (delta 1), pack-reused 329766
Receiving objects: 100% (329770/329770), 72.03 MiB | 2.23 MiB/s, done.
Resolving deltas: 100% (212113/212113), done.
Checking connectivity... done.
```

#### Clonado sin profundidad:
```bash
$ git clone --depth 1 https://github.com/symfony/symfony.git 
Cloning into 'prueba'...
remote: Counting objects: 6129, done.
remote: Compressing objects: 100% (5252/5252), done.
remote: Total 6129 (delta 1700), reused 2984 (delta 523), pack-reused 0
Receiving objects: 100% (6129/6129), 4.84 MiB | 1.25 MiB/s, done.
Resolving deltas: 100% (1700/1700), done.
Checking connectivity... done.
```

#### Clonar solo una rama:
Desde Git 1.7.10, es posible limitar el historial mediante la clonación de una sola rama:

```bash
git clone --depth [num confirmaciones] [url repositorio] --branch [rama remota] --single-branch [carpeta destino]
git clone --depth 1 https://github.com/imlauera/imlauera.github.io.git --branch master --single-branch prueba 
```
