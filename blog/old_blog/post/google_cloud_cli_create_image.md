---
title: "Google cloud CLI creamos borramos imágenes de maquinas virtuales"
date: 2024-09-21T22:30:06-03:00
tags: ['google','cloud','cli']
---

https://invidious.materialio.us/search?q=google+cloud+cli+create+image

https://youtube.com/watch?v=RPYFbMXc-1Q

https://youtube.com/watch?v=LxHiCZCKwa8

https://youtube.com/watch?v=JW5YB0lOypY

https://youtube.com/watch?v=7CvD6oHmYxU

https://youtube.com/watch?v=KpYO6Ru8MOI

https://youtube.com/watch?v=jlLE157HCR4

https://youtube.com/watch?v=rpmOM5jJJfY

https://youtube.com/watch?v=dtKM8MJqI48

https://youtube.com/watch?v=AA7Dpyjic64

---
### Creamos una compute engine disk image
Para empezar tenemos una máquina virtual que hemos configurado, la usaremos como template para la nueva imagen, el primer paso es eliminar la máquina virtual pero guardaremos el disco persistente del boot(arranque).
Así que usamos el siguiente comando:
```bash
gcloud compute instances delete gold-template --keep-disks boot
```
en donde gold-template es el nombre de la máquina virtual.

Ahora crearemos una imagen de ese disco con el siguiente comando:
```bash
gcloud compute images create gold-image --source-disk gold-template
```
Ahora que tenemos las imágenes, podemos crear nuevas máquinas virtuales a partir de ellas con el siguiente comando:
```bash
gcloud compute instances create --image gold-image new-vm # new-vm es el nombre de la nueva maquina virtual
```

Ahora podemos ingresar a la VM a través del SSH con el comando: `gcloud compute ssh new-vm`

Y podemos ver que nuestra nueva máquina virtual tiene la misma configuración que el "template" original de la máquina virtual.

---
### Gcloud CLI
Buscá gcloud cli download, descargalo e instalalo.

### Inicializar gcloud cli.
Ejecutá `gcloud init`, te pedirá que ingreses a tu cuenta de google.

Alternativas a `gcloud init` pero usaremos `gcloud init`:

```bash
gcloud auth login 
gcloud auth activate-service-account
```

Si no tenés acceso a Xorg.
```bash
gcloud init --no-launch-browser
```

Ahora luego de ejecutar `gcloud init` te pedirá que selecciones el proyecto o crees uno nuevo o que entres un ID de algún proyecto.

### Creando imagen custom de una instancia de una máquina virtual en GCP usando gcloud CLI

```
gcloud version
gcloud compute instances list
gcloud compute machine-images create demo-image --source-instance=demo-instance --source-instance-zone=us-central1-c 
gcloud compute instances create demo-instance-1 --zone=us-central1-c --source-machine-image=demo-image
gcloud compute instances list
gcloud compute instances delete demo-instance-1 --zone=us-central1-c
gcloud compute instances list
gcloud compute machine-images delete demo-image
```

### Creando y eliminando repositorios en GCP registro artifact usando gcloud cli
```
gcloud version
gcloud config list
gcloud artifacts repositories create scenery --repository-format=docker --location=us-central1
gcloud artifacts repositories list
gcloud artifacts repositories describe scenery --location=us-central1
gcloud auth configure-docker us-central1-docker.pkg.dev
cat Dockerfile
docker build -t scenery .
docker tag scenery us-central1-docker.pkg.dev/civil-keyword-395016/scenery/scenery:v1
### Pushear al repositorio gcp artifact
docker push scenery us-central1-docker.pkg.dev/civil-keyword-395016/scenery/scenery:v1
### Para chequear
gcloud artifacts repositories describe scenery --location=us-central1
### borramos
gcloud artifacts repositories delete scenery --location=us-central1
gcloud artifacts repositories list
```

Expliqué lo que era artifacs en la publicación de gitlab runner.


---

#### GCLOUD comandos
```bash
### list out the regions available for you
gcloud compute regions list
### set regions
gcloud config set compute/region REGION
### unset the regions
gcloud config unset compute/region
### Build Command
--zone us-central1-c
```
### Sistema operativo
```bash
### select image from list
gcloud compute images list
Descubrí los valores de los parametros: --image-family --image-project
```
### build command
```bash
--image-family centos-6 --image-project centros-cloud
```
#### instance type
```bash
gcloud compute machine-types list
```

Cambia el hardware a tu necesidad
```bash
--custom-memory 4GiB --custom-cpu 2vCPU
```

### build command
```bash
--machine-type=f1-micro / --custom-memory 4GiB --custom-cpu 2vCPU
```

## agregar descripción
```bash
gcloud compute instances -h
--description="testing for the command line"
```

### más opciones
```bash 
--no-restart-on-failure by default on
--metadata @ add ssh keys if you want
Hay un link a un tutorial de como manejar ssh-key en GCP(google cloud platform)
gcloud compute instance-templates create
```

### crear una maquina
```bash
gcloud compute instances create secops --zone us-central1-c --image-family centos-6 --image-project centos-cloud --machine-type f1-micro --description 'testing for the command line'
```

### iniciar y detener una instancia
```bash
gcloud compute instances stop secops --zone us-central1-c
gcloud compute instances start secops --zone us-central1-c
```

### borrar una instancia
```bash
gcloud compute instances delete secops --zone us-central1-c
```



