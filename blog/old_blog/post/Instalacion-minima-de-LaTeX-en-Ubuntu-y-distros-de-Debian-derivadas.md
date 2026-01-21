---
title: "Instalacion Minima De LaTeX en Ubuntu Y Distros De Debian Derivadas. Un poquito de Arch."
tags: ['latex','instalacion','debian']
categories: ['linux']
date: 2023-03-07T05:14:57-03:00
---
### Instalacion base

Comenzá instalando texlive-latex-base usando el comando 

```bash
sudo apt install texlive-latex-base
```
### En Arch

```
sudo pacman -S texlive-basic
sudo pacman -S texlive-basic texlive-latex texlive-latexrecommended texlive-fontsrecommended texlive-pictures texlive-luatex

```

Luego intente compilar el archivo latex usando el comando
```bash
pdflatex nombre_archivo.tex
```
Si TeX se queja de que faltan archivos, usa apt-file search para buscar e instalar el archivo faltante, por ejemplo cuando intente compilar mi documento me tiraba un error de este tipo:

```bash
! LaTeX Error: File `xcolor.sty' not found.
```
### Buscando archivos faltantes
Entonces para instalar el archivo faltante primero buscamos en que paquete esta disponible y luego instalamos el paquete con `apt install`
```bash
sudo apt-file search xcolor.sty
```
Este comando me tiro una lista de paquetes en donde estaba disponible ese archivo y procedi a instalar el paquete `texlive-latex-recomended` .

Nota\*: `apt-file` lo instalas con el comando
```bash
sudo apt install apt-file
```

Y así repetis el proceso hasta que logres compilar el archivo de LaTeX con `pdflatex`.

#### Si estas usando ArchLinux

```bash
sudo pacman -S pkgfile
sudo pkgfile --update
pkgfile xcolor.sty
```
