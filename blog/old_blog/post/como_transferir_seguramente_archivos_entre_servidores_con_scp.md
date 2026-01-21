---
title: "Como transferir seguramente archivos entre servidores con scp"
date: 2023-10-01T11:41:54-03:00
tags: ['transferir','archivos','scp']
---
#### Copie un solo archivo de la máquina local a una máquina remota:
El comando scp necesita un origen y un destino para copiar archivos de una ubicación a otra. Este es el patrón que utilizamos:

```console
scp máquina local/ruta_al_archivo nombre de usuario@ip_servidor:/ruta_al_directorio_remoto
```

En el siguiente ejemplo, estoy copiando un archivo local a mi vps de Linux.
```console
scp /home/imlauera/Downloads/slackware.iso blogger@111.111.111.111:/home/blogger/isos/
```

Aquí, "blogger" es el usuario en el servidor y 111.111.111.111 es la IP del servidor. Le pedirá que proporcione la contraseña de ese usuario y luego copie el archivo de forma segura.

##### Copie una carpeta/directorio local a un servidor remoto:
Si desea copiar todo el directorio local al servidor, puede agregar el indicador -r al comando:

```console
scp -r máquina local/ruta_al_directorio nombre_usuario@ip_servidor:/ruta_al_directorio_remoto/
```
Asegúrese de que el directorio de origen no tenga una barra diagonal al final de la ruta; al mismo tiempo, la ruta de destino *debe* tener una barra diagonal. O se puede comprimir el directorio en un tar y subir el archivo tar, con el comando anterior.

### Copiar archivos del servidor remoto a la máquina local
##### Copie un solo archivo:
```console
scp nombre de usuario@ip_servidor:/ruta_al_directorio_remoto máquina_local/ruta_al_archivo
```
##### Copie un directorio remoto a una máquina local:
```console
scp -r nombre de usuario@ip_servidor:/ruta_al_directorio_remoto máquina-local/ruta_al_directorio/
```
Asegúrese de que el directorio de origen no tenga una barra diagonal al final de la ruta; al mismo tiempo, la ruta de destino *debe* tener una barra diagonal.

### Copie archivos de un servidor remoto a otro servidor remoto desde una máquina local
Por lo general, ingreso a esa máquina y luego uso el comando rsync para realizar el trabajo, pero con SCP, puedo hacerlo fácilmente sin tener que iniciar sesión en el servidor remoto.
##### Copie un solo archivo:
```bash
scp nombre de usuario@ip_servidor1:/ruta_al_archivo_remoto nombre de usuario@ip_servidor2:/ ruta_al_directorio_destino/
```
##### Copie un directorio desde una ubicación en un servidor remoto a una ubicación diferente en el mismo servidor:
```console
scp nombre de usuario@ip_servidor1:/ruta_al_archivo_remoto nombre de usuario@ip_servidor2:/ ruta_al_directorio_destino/
```
