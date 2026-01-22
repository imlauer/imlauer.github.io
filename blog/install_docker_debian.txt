---
title: "Install docker y docker compose debian 12"
date: 2024-12-17T22:07:21-03:00
tags: ['debian','docker']
---
```bash
$ for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do su  do apt-get remove $pkg; done 
```

# Add Docker's official GPG key:
```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

# Add the repository to Apt sources:
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc]      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

#### Install docker
```bash
$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

#### Verifica que la instalación fue exitosa 
```bash
sudo systemctl start docker.service
sudo usermod -aG docker $USER
```

#### Ahora tenés que cerrar tu sesión y volver a ingresar y ejecutar:
```bash
sudo docker run hello-world
```

Fuente: https://docs.docker.com/engine/install/debian/

