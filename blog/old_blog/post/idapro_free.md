---
title: "Ida PRO Free"
date: 2024-09-06T05:37:11-03:00
tags: ['reversing']
---
```
magnet:?xt=urn:btih:6903c417f24b595fc8831933fa454e42e53bd132&dn=IDA%20Pro%209.0%20Beta&tr=http%3A%2F%2Fbt.t-ru.org%2Fann%3Fmagnet
```

Para instalarlo, abrí la carpeta en donde se descargó. 

Ubicate en la carpeta de `installers original`
Ahora ejecutá
```
chmod +x idapro_90_x64linux.run
./idapro_90_x64linux.run
```
Se instalará en `~/idapro-9.0`

Ahora ubicate en la carpeta `crack` copiá `crack_ida90_beta.py` a donde se instaló el IDAPro: `~/idapro-9.0` ejecutalo con `python crack_ida90_beta.py` esto generará los archivos libida.so.patched y libida64.so.patched ahora renombralos a libida.so y libida64.so con el siguiente comando:
```bash
mv libida.so.patched libida.so
mv libida64.so.patched libida64.so
```

Listo ya debería funcionar, podés agregarlo al path ejecutando
```bash
cd /usr/bin
sudo ln -s /home/tu_usuario/idapro-9.0/ida64 .
```

Ahora podés ejecutar `ida64`.
