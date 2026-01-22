---
title: "Compilar vim"
date: 2023-05-18T22:10:51-03:00
tags: ['vim','compile']
categories: ['editor']
---

#### Como compilar la utima version de VIM
##### Ver la version actual de vim
`vim`

##### Deshazte del Vim existente
```bash
sudo apt autoremove vim vim-runtime gvim
```

##### Deshágase del obsoleto python 2.x
```bash
sudo apt autoremove python2*
```

Agregar paquetes de compilación
```console
sudo apt install -y git \
                 libatk1.0-dev \
                 libcairo2-dev \
                 libgtk2.0-dev \
                 liblua5.1-0-dev \
                 libncurses5-dev \
                 libperl-dev \
                 libx11-dev \
                 libxpm-dev \
                 libxt-dev \
                 lua5.1 \
                 python3-dev \
                 ruby-dev 
```


Clonamos el repositorio y lo configuramos  
```bash
cd
git clone https://github.com/vim/vim.git
cd ~/vim
python3-config --configdir
```

Agregar la configuracion
```bash
./configure --with-features=huge \
--enable-multibyte \
--enable-rubyinterp=yes \
--enable-python3interp=yes \
--with-python3-command=$PYTHON_VER \
--with-python3-config-dir=$(python3-config --configdir) \
--enable-perlinterp=yes \
--enable-gui=gtk2 \
--enable-cscope \
--prefix=/usr/local
```
##### Compilar la fuente e instalar
```bash
make && sudo make install
```
##### Confirme la configuración de Vim y grep en la compatibilidad con Python3 (es decir, +Python3)
```bash
vim --version | grep +python3
```


O pueden bajar el appimage desde aca: [https://github.com/vim/vim-appimage](https://github.com/vim/vim-appimage)

Si quieren aprender como usar VIM recomiendo el curso de ThePrimeagen en YouTube aunque el ahora recomienda usuar neovim que es escencialmente lo mismo pero usa LUA como lenguaje de programacion para la configuracion, VIM tiene su propio lenguaje de programacion.
