---
title: "Mattermost"
date: 2024-09-24T17:11:22-03:00
tags: ['mattermost']
---
https://www.youtube.com/watch?v=9BgVRShk00Y  
https://www.youtube.com/watch?v=zL9mjKrEuKY  
https://www.youtube.com/watch?v=z4yPSEMm22g  
https://www.youtube.com/watch?v=aT1HG8EHMDA  
https://www.youtube.com/watch?v=6TJH2p1HcwA  
https://www.youtube.com/watch?v=HySOrcCBhUs  
https://www.youtube.com/watch?v=H_2i7j1MU-0  
https://www.youtube.com/watch?v=OAAfe500Gc4  



```bash
sudo su
### Instalá docker, habilitá docker para que inicie al boot.
systemctl enable docker systemctl start docker
Instalá docker-compose

#NO: docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview
git clone https://github.com/mattermost/docker && cd docker
cp env.example.env
vim .env 

Buscá el nombre DOMAIN borrá lo que está escrito y poné el subdominio: mattermost.example.org

Cambiá la contraseña POSTGRES_PASSWORD en .env

mkdir -p ./volumes/app/mattermost/{config,data,logs,plugins,client/plugins,bleve-indexes} && sudo chown -R 2000:2000 ./volumes/app/mattermost

## Ahora ahora andate a home como root y creá una carpeta llamada mattermost y ejecutá:
mkdir mattermost
cd mattermost

wget https://dl.smallstep.com/cli/docs-cli-install/latest/step-cli_amd64.deb
sudo dpkg -i step-cli_amd64.deb

step ca certificate mattermost.example.org mattermost.example.org.crt mattermost.example.org.key ingresá una contraseña y guardala en tu bitwarden por las dudas.

scp * mattermost.example.org:
logout

mkdir -p ./volumes/web/cert/
mv /root/mattermost.example.org.crt ./volumes/web/cert/cert.pem
mv /root/mattermost.example.org.key ./volumes/web/cert/key-no-password.key


# docker compose -f docker-compose.yml -f docker-compose.nginx.yml up -d
docker-compose -f docker-compose.yml -f docker-compose.without-nginx.yml up -d
docker ps -a 
```

Ahora ya deberías ver tu sitio levantado en: mattermost.example.org
