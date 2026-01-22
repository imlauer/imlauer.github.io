---
title: "Abrir grandes archivos: dividirlos en varios."
date: 2025-02-28T20:49:44-03:00
tags: ['big','files']
---
Intenté abrir archivos de 2GBs con less, vim y ed pero todos tardan demasiado, así que la solución real es dividirlo en varios archivos.

```bash
sed -e 's/oldstuff/newstuff/g' inputFileName > outputFileName
```


Another method is to use split. Split the file into 8 pieces and manipulate the
files with a editor. After that, you reassemble the files again.

```bash
split -b 53750k <your-file>
cat xa* > <your-file>
```



