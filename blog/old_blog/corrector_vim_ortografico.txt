---
title: "Corrector vim ortografico"
date: 2023-12-13T18:57:14-03:00
tags: ['vim']
---
[https://archive.is/v4tU9](https://archive.is/v4tU9)

[https://web.archive.org/web/20230129193216/https://atareao.es/tutorial/vim/el-corrector-ortografico-en-vim/](https://web.archive.org/web/20230129193216/https://atareao.es/tutorial/vim/el-corrector-ortografico-en-vim/)


```
mkdir -p ~/.vim/spell
cd ~/.vim/spell


wget --no-check-certificate https://ftp.nluug.nl/vim/runtime/spell/es.latin1.spl
wget --no-check-certificate https://ftp.nluug.nl/vim/runtime/spell/es.latin1.sug
wget --no-check-certificate https://ftp.nluug.nl/vim/runtime/spell/es.utf-8.spl
wget --no-check-certificate https://ftp.nluug.nl/vim/runtime/spell/es.utf-8.sug
```

Agregá a `.vimrc`
```bash
:setlocal spell spelllang=es

```
