---
title: "Montar SAMBA Windows"
date: 2025-11-03T17:26:34-03:00
tags: ['linux']
---
Montar servidor directorio de SAMBA de Linux en Windows.

Abrí `cmd` como administrador y ejecuta estos comandos:

```bash
net use * /delete /y
net session /delete /y
```

Luego como **NO ADMINISTRADOR**:

```bash
net use Z: \\192.168.0.48\samba /user:esotericwarfare
```

Ahora podras ver el "disco" Z: en This PC.

Luego para limpiar las conexiones:

```bash
net use * /delete /y
net session /delete /y
```
