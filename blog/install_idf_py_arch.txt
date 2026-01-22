---
title: "Install idf py en Arch"
date: 2025-01-22T05:56:03-03:00
tags: ['arch']
---
```bash
yay -S esp-py
/opt/esp-idf/install.sh
/opt/esp-idf/install.fish
. /opt/esp-idf/export.fish
idf build
```
A partir de ahora cada vez que lo quieras usar tendrás que ejecutar . /opt/esp-idf/export.fish

Ejemplos
https://github.com/espressif/esp-idf/tree/v4.3/examples/get-started/hello_world

git clone https://github.com/espressif/esp-idf/


