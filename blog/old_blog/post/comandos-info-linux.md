---
title: "Comandos de consola para obtener informacion del hardware en Linux"
tags: ['comandos','consola','hardware']
categories: ['linux','hardware']
date: 2023-03-03T19:40:57-03:00
---

### lshw
lshw es una pequeña herramienta para extraer información detallada sobre la configuración de hardware de la máquina, puede informar la memoria exacta, configuración de memoria, versión de firmware, configuración de placa base, versión y velocidad de CPU, configuración de caché, velocidad de bus, etc.

```
sudo lshw 
```

### lscpu
Muestra informacion sobre la arquitectura del CPU.
```
sudo lscpu
```


### inxi
Muestra informacion sobre la CPU, placa madre, placa de video, de audio, de red, bluetooth, bateria.
```
sudo inxi -F
```

### lspci
Obtener lista sobre dispositivos PCI
```
sudo lspci
```


