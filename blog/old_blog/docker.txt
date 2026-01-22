---
title: "Docker: Instalar una distro e iniciarla"
date: 2024-09-21T12:10:49-03:00
---
```bash
docker run debian
docker run -it debian
```

### Instalando en debian
#### eliminar paquetes en conflicto
`for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done`

#### Métodos de instalación
* Docker Engine viene incluido con [Docker Desktop para Linux](https://docs.docker.com/desktop/install/linux/). Esta es la forma más fácil y rápida de empezar.
* Configure e instale Docker Engine desde el repositorio apto de Docker.
* Instálelo manualmente y administre las actualizaciones manualmente.
* Utilice un script de conveniencia. Sólo recomendado para entornos de prueba y desarrollo.

#### Usando `apt` repositorio (este es el que yo uso siempre)
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get updatebash
```

Si usa una distribución derivada, como Kali Linux, es posible que deba sustituir la parte de este comando que se espera que imprima el nombre en clave de la versión:

`$(. /etc/os-release && echo "$VERSION_CODENAME")`

Reemplace esta parte con el nombre en clave de la versión de Debian correspondiente, como bookworm.

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
###### Verificá que la instalación fue exitosa:
```bash
sudo docker run hello-world
```

### Instalar docker desde un paquete
Tenés que bajarte el deb 

Si no puede utilizar el repositorio apt de Docker para instalar Docker Engine, puede descargar el archivo deb para su versión e instalarlo manualmente. Debe descargar un archivo nuevo cada vez que desee actualizar Docker Engine.


Descargá el deb: https://download.docker.com/linux/debian/dists/.
Seleccioná tu versión de debian.

En `pool/stable/` seleccioná tu arquitectura (amd64, armhf, arm64, or s390x).

Descarga los siguientes archivos deb para docker, cli, containerd y docker compose:

```bash
containerd.io_<version>_<arch>.deb
docker-ce_<version>_<arch>.deb
docker-ce-cli_<version>_<arch>.deb
docker-buildx-plugin_<version>_<arch>.deb
docker-compose-plugin_<version>_<arch>.deb
```

Instalá todos esos paquetes deb. 
Install the .deb packages. Actualice las rutas en el siguiente ejemplo donde descargó los paquetes de Docker.


```bash
sudo dpkg -i ./containerd.io_<version>_<arch>.deb \
./docker-ce_<version>_<arch>.deb \
./docker-ce-cli_<version>_<arch>.deb \
./docker-buildx-plugin_<version>_<arch>.deb \
./docker-compose-plugin_<version>_<arch>.deb
```
El demonio de docker empezará automáticamente.

```bash
sudo service docker start
sudo docker run hello-world
```

#### Agregá tu usuario a docker y salí de la cuenta y volvé a ingresar.
```bash
sudo usermod -aG docker $USER
```

### Usando un script de conveniencia:

https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script

https://get.docker.com/

* El script requiere privilegios de root o sudo para ejecutarse.
* El script intenta detectar su distribución y versión de Linux y configurar su sistema de administración de paquetes por usted.
* El script no le permite personalizar la mayoría de los parámetros de instalación.
* El script instala dependencias y recomendaciones sin pedir confirmación. Esto puede instalar una gran cantidad de paquetes, dependiendo de la configuración actual de su máquina host.
* De forma predeterminada, el script instala la última versión estable de Docker, containerd y runc. Cuando se utiliza este script para aprovisionar una máquina, esto puede dar como resultado actualizaciones importantes inesperadas de la versión de Docker. Pruebe siempre las actualizaciones en un entorno de prueba antes de implementarlas en sus sistemas de producción.
* El script no está diseñado para actualizar una instalación de Docker existente. Cuando se utiliza el script para actualizar una instalación existente, es posible que las dependencias no se actualicen a la versión esperada, lo que da como resultado versiones obsoletas.

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
```

Este ejemplo descarga el script de https://get.docker.com/ y lo ejecuta para instalar la última versión estable de Docker en Linux:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
Executing docker install script, commit: 7cae5f8b0decc17d6571f9f52eb840fbc13b2737
<...>
```

Ahora ha instalado e iniciado Docker Engine con éxito. El servicio Docker se inicia automáticamente en distribuciones basadas en Debian. En distribuciones basadas en RPM, como CentOS, Fedora, RHEL o SLES, debe iniciarlo manualmente usando el comando systemctl o service apropiado. Como indica el mensaje, los usuarios que no son root no pueden ejecutar comandos de Docker de forma predeterminada.

### Instalar pre-lanzamientos (releases)
```bash
curl -fsSL https://test.docker.com -o test-docker.sh
sudo sh test-docker.sh
```

### Borrar docker
https://docs.docker.com/engine/install/debian/#uninstall-docker-engine

```
sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras

sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd

sudo rm /etc/apt/sources.list.d/docker.list
sudo rm /etc/apt/keyrings/docker.asc
```


### Pasos luego de la instalación
```bash
sudo usermod -aG docker $USER
### si el grupo no existe crealo
sudo groupadd docker
### agregalo al grupo
sudo usermod -aG docker $USER
### activa los cambios a los grupos con el comando
newgrp docker
docker run hello-world
```

```bash
sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
sudo chmod g+rwx "$HOME/.docker" -R
```


### Configurar docker para que arranque al inicio
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

