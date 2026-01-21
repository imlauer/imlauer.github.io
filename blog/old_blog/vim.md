---
title: "Como copiar y pegar en VIM:"
date: 2024-11-08T05:49:20-03:00
tags: ['vim']
---

##### Potente comando.
Podes seleccionar cualquier linea con **Shift+V**, y guardarla en otro archivo con: `:w /tmp/prueba.txt`. 

### Como copiar y pegar gráficamente en VIM:
#### Copiar: 
```bash
"+y
```

#### Pegar: 
```bash
Ctrl+Shift+V
Shift+Insert
"+gp
```

### Copiar y pegar dentro de VIM:
```bash
yy - Copia la línea
p - pega
P - pega para atrás
```bash

`Shift+V` seleccionás las líneas que quieras y con `y` las copías
