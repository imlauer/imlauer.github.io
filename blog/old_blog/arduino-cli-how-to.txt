---
title: "ESP32 con Arduino Cli How To"
date: 2023-07-12T02:26:15-03:00
tags: ['esp32','arduino','cli']
---
#### Instalacion
```bash
git clone https://github.com/arduino/arduino-cli    
cd arduino-cli
bash install.sh  
cd bin/  
sudo mv arduino-cli /usr/bin  
```
**Agregar y descargar un indice adicional**:
```bash
arduino-cli core update-index --additional-urls https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
```
**Iniciar la configuracion:**
```bash
arduino-cli config init
arduino-cli config dump --verbose 
```
Cuando inicias la configuracion te crea un archivo en `~/.arduino/arduino-cli.yaml` podes editar ese archivo y agregar la URL del indice en ese archivo en vez de usar --additional-urls como se demostro en el paso 1.
#### Configurando arduino-cli para usarlo con ESP32
**Buscar core**:
```bash
arduino-cli core search esp32
```
**Instala el ESP32 Core**:
```bash
arduino-cli core install esp32:esp32
```
Podes buscar el FQBN (necesario para compilar) usando el comando
```bash
arduino-cli board search esp32
arduino-cli board details -b esp32:esp32:esp32wrover
arduino-cli board details -b <Tu FQBN>
```

**Crea un nuevo sketch**:
```
arduino-cli sketch new ejemplo
cd ejemplo
```
No hace falta si ya tenes un archivo ino. Directamente pasa al siguiente paso.

**Para compilar el sketch**:
```bash
arduino-cli compile --fqbn esp32:esp32:esp32 .
o
arduino-cli compile --fqbn esp32:esp32:esp32wrover .
```

**Para subirlo al esp32**:
```bash
arduino-cli upload -p /dev/ttyUSB0 --fqbn esp32:esp32:esp32 .
o 
arduino-cli upload -p /dev/ttyUSB9 --fqbn esp32:esp32:esp32wrover .
```

**Para monitorearlo**:
```bash
screen /dev/ttyUSB0 115200
```

**Buscar librerias**:
```bash
arduino-cli lib search DH11
```

**Instalando librerias**:
```bash
arduino-cli lib install "DHT sensor library"
```

**Para compilar y subir**:
```bash
arduino-cli compile --fqbn esp32:esp32:esp32 -u -p /dev/ttyUSB0
arduino-cli compile --fqbn esp32:esp32:esp32wrover -u -p /dev/ttyUSB0
```
