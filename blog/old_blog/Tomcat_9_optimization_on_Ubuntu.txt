---
title: "Tomcat 9 Optimization on Ubuntu"
date: 2024-09-25T15:36:58-03:00
tags: ['tomcat']
---
> Tomcat es un servidor web o contenedor web donde los desarrolladores pueden implementar aplicaciones web Java. 

> Apache Tomcat es un contenedor de servlets que permite ejecutar aplicaciones web basadas en Java, facilitando la implementación y gestión de servicios web.

> Apache Tomcat es un contenedor de servlets de código abierto que se utiliza principalmente para compilar y ejecutar aplicaciones web basadas en Java, soportando tecnologías como JavaServer Pages (JSP), Java Servlet y WebSocket, lo que lo convierte en una opción popular para el desarrollo y despliegue de aplicaciones web dinámicas. Además, Tomcat puede funcionar de manera autónoma o en combinación con otros servidores web, como Apache HTTP, para mejorar su rendimiento y funcionalidad.

> Un servlet es un componente de software en Java que se ejecuta en un servidor web y gestiona solicitudes HTTP, permitiendo la creación de contenido web dinámico y la interacción con aplicaciones empresariales, actuando como intermediario entre el cliente y el servidor para procesar datos y generar respuestas adecuadas.



> Have an XWiki installation on Tomcat 9 and CPU Usage is through the roof and it is causing the web server to shut down and 504 people.  Looking for some expertise on solving the issue.  It is a virtual machine with 2 vCPUs and 8GB of RAM which is more than what should be needed.

> Tengo una instalación de XWiki en Tomcat 9 y el uso de la CPU está por las nubes y está provocando que el servidor web se apague y 504 personas. Buscando experiencia para resolver el problema. Es una máquina virtual con 2 vCPU y 8 GB de RAM, que es más de lo que debería necesitarse.


https://www.upwork.com/jobs/Tomcat-optimization-Ubuntu_~021839009814137104906/?referrer_url_path=find_work_home

#### Como instalar Tomcat
https://www.youtube.com/watch?v=TNZuqEglH9Y  
https://www.youtube.com/watch?v=7i0wj2QYo4M  
https://www.youtube.com/watch?v=lvl9MdkwiW4  
https://www.youtube.com/watch?v=GOFIEnT8E7E  
https://www.youtube.com/watch?v=rd6Owel1dIg  
https://www.youtube.com/watch?v=1bnla8eYcaI  
https://www.youtube.com/watch?v=Feui5F42bII  
https://www.youtube.com/watch?v=oma_zXH2a0s  
https://www.youtube.com/watch?v=Vvm7cY7P9JE  
https://www.youtube.com/watch?v=FZ7Mn2jUyDI  
https://www.youtube.com/watch?v=m_9QNRHnL0E  
https://www.youtube.com/watch?v=oZZYD50y2w8  
https://www.youtube.com/watch?v=aL8_tFNnQ_A  
https://www.youtube.com/watch?v=CptBO6wAiEQ  
https://www.youtube.com/watch?v=j-sNUzZLuUM  
https://www.youtube.com/watch?v=aL8_tFNnQ_A  
https://www.youtube.com/watch?v=oZZYD50y2w8  
https://www.youtube.com/watch?v=UTAMrGCZi2I  
  


### Instalación Instrucciones

https://www.youtube.com/watch?v=FZ7Mn2jUyDI  
```bash
sudo apt update
sudo apt-cache search tomcat
sudo apt install -y tomcat9 tomcat9-admin
ss -ltn
sudo systemctl enable tomcat9
sudo ufw allow from any to any port 8080 proto tcp
```

#### Instalación (el mejor)
https://tomcat.apache.org/download-10.cgi

https://www.youtube.com/watch?v=Vvm7cY7P9JE  

```bash
sudo apt update
### Instalamos openjdk 
sudo apt install -y default-jre
java --version
### Comando interesante: sudo update-java-alternatives -l
cd /usr/lib/jvm
ls -ltr
cd java-11-openjdk-amd64
cd
groupadd tomcat
useradd -g tomcat -d /opt/tomcat -s /bin/false false
id tomcat
sudo su - tomcat
mkdir -p /opt/tomcat
cd /opt
ls -ltr
chown -R tomcat:tomcat tomcat/
cd /opt
Ingresá a https://tomcat.apache.org/download-10.cgi copiá el link y descargá con wget Binary Distributions: Core: .tar.gz
wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.30/bin/apache-tomcat-10.1.30.tar.gz
tar xvf apache-tomcat-10.1.30.tar.gz -C /opt/tomcat --strip-components=1
cd tomcat
chown -R tomcat:tomcat *
./startup.sh
Ahora podés ingresar a localhost:8020
./shutdown.sh
```

### Creando un servicio en systemd
Creá un archivo llamado `tomcat.service`:

```bash
[Unit]
Description=Tomcat Webserver
After=network.target

[Service]
Type=forking

# Restart=always

Environment="JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" # Adaptalo al directorio que create anteriormente
Environment="CATALINA_HOME=/opt/tomcat"
Environment="CATALINA_BASE=/opt/tomcat"

ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh

User=tomcat
Group=tomcat

[Install]
WantedBy=multi-user.target
```

### Seguimos con la instalación:
```bash
cp tomcat.service /etc/systemd/system
systemd daemon-reload
systemctl start tomcat
### Ejecutá status para ver si hay algún error, en este caso saltó error de permisos en la carpeta logs
systemctl status tomcat
cd /opt/tomcat
chown -R tomcat:tomcat *
systemctl start tomcat
systemctl status tomcat
Ahora podés ingresar a: http://localhost:8020 y tu servidor estará funcionando
systemctl stop tomcat
systemctl status tomcat
systemctl enable tomcat
```

Ahora descargá una aplicación de ejemplo para probar:
En google buscá: `download sample war file for tomcat`

https://tomcat.apache.org/tomcat-7.0-doc/appdev/sample/

Descargá la aplicación con **wget** : https://tomcat.apache.org/tomcat-7.0-doc/appdev/sample/sample.war

```bash
cd /tmp
wget https://tomcat.apache.org/tomcat-7.0-doc/appdev/sample/sample.war
cp sample.war /opt/tomcat/webapps/
cd /opt/tomcat/webapps/
chown tomcat:tomcat sample.war
systemctl start tomcat
### Ahora se creará una carpeta llamada sample
Podés ingresar a localhost:8020/sample
```

Eso es todo.


# Otro método de instalación con AWS
https://www.coachdevops.com/2020/04/install-tomcat9-on-ubuntu-1804-setup.html

### Conectarse a una instancia y dale a SSH cliente.

https://www.youtube.com/watch?v=rd6Owel1dIg  

### Requisitos previos:

Primero cree una nueva instancia EC2 en AWS para configurar Tomcat.
Abra también el puerto 8080 en las reglas de firewall de seguridad para la instancia EC2 en AWS.

### Instalación de Tomcat
> Tomcat es un servidor web o contenedor web donde los desarrolladores pueden implementar aplicaciones web Java. Puede obtener más información haciendo clic en esta URL. Tomcat se puede instalar ejecutando los siguientes comandos:

Cambiar el nombre del host a Tomcat
```bash
sudo hostnamectl set-hostname Tomcat
```

### Actualizar a los paquetes más recientes
```bash
sudo apt update
```

#### Install Tomcat9
```bash
sudo apt install tomcat9 tomcat9-docs tomcat9-admin -y
```

#### Ejecutá el siguiente comando para configurar la aplicación tomcat admin app
```bash
sudo cp -r /usr/share/tomcat9-admin/* /var/lib/tomcat9/webapps/ -v
```

#### Configurá un usuario en tomcat
Abrí el archivo `tomcat-users.xml` ejecutando el siguiente comando:
```bash
sudo vi /var/lib/tomcat9/conf/tomcat-users.xml
```
Necesitamos agregar el usuario de Tomcat y asignarlo al rol de administrador de script.
Desplácese hacia abajo hasta el final del archivo,
Agregue las siguientes líneas en la penúltima línea arriba (arriba de </tomcat-users>)

Esto sale de cuando le das a Manage app y ponés una clave incorrecta, en el tomcat: localhost:8080

##### sustituí password por tu contraseña
```html
<role rolename="manager-script"/>
<user username="tomcat" password="password" roles="manager-script"/>
```

#### Ahora reinicie Tomcat para que los cambios surtan efecto.
```bash
sudo systemctl restart tomcat9
```

#### Verifique si Tomcat9 está funcionando bien
```bash
sudo systemctl status tomcat9
```
Ahora abra el navegador para acceder a Tomcat, ingrese

```bash
http://cambiar_a_Ec2_public_dns_name:8080
```
La ip está en el aws > ssh client 

### Debería salir este mensaje
![tomcat works](/tomcat.png)



### Otro método de instalación
https://www.youtube.com/watch?v=oma_zXH2a0s  

```bash
sudo apt update
sudo apt install -y openjdk-11-jdk
```
### Buscá tomcat 9 archive y bajate 9.0.65/bin/apache-tomcat.tar.gz
```bash
java --version
cd /opt
wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.8.65/bin/apache-tomcat.tar.gz
sudo tar xvf apache-tomcat.tar.gz
rm -rf apache-tomcat.tar.gz
cd /opt/apache-tomcat-9.8.65/conf
sudo vim tomcat-users.xml
Agregá lo mismo que expliqué arriba.
sudo vi /opt/apache-tomcat-9.8.65/webapps/manager/META-INF/content.xml
Comentá con `<!-- -->` la etiqueta  Valve  dejá Manager sin comentar 
sudo vi /opt/apache-tomcat-9.8.65/webapps/host-manager/META-INF/content.xml hacé lo mismo
sudo /opt/apache-tomcat-9.8.65/bin/startup.sh
sudo /opt/apache-tomcat-9.8.65/bin/shutdown.sh
```
### Cambiá el puerto
```bash
cd /opt/apache-tomcat-9.8.65/conf
vi server.xml y ahí buscá port y cambiá ese.

sudo /opt/apache-tomcat-9.8.65/bin/shutdown.sh
sudo /opt/apache-tomcat-9.8.65/bin/startup.sh
```

### Otra instalación
https://www.youtube.com/watch?v=lvl9MdkwiW4  
```bash
sudo apt update
sudo apt install -y openjdk-11-jdk
java --version
sudo apt install -y tomcat9 tomcat9-admin
ss -ltn
netstat -tulpn | grep 8080
sudo ufw allow from any to any port 8080 proto tcp
sudo vim /etc/tomcat9/tomcat-users.xml
Agregá lo que agregamos antes.

<role rolename="admin-gui"/>
<role rolename="manager-gui"/gt>
<user username="tomcat" password="solvetic" roles="admin-gui,manager-gui"/>

sudo systemctl restart tomcat9
ahora ingresá a localhost:8080/manager/html
```


### Another one
```bash
sudo apt update
sudo apt install -y default-jdk
chmod -R 777 /opt
mkdir /opt/tomcat
### Descargá el targz de core de binary packages googleando tomcat download con wget y como expliqué antes
sudo tar xvf apache-tomcat-10.0.2.tar.gz -C /opt/tomcat --strip-components=1
sudo /opt/tomcat/bin/startup.sh
Abrí el servidor: localhost:8080 y dale a examples

```

El video https://www.youtube.com/watch?v=7i0wj2QYo4M pone otra configuración en `tomcat-users.xml` agrega uno que es manager-gui y otro admin-gui creo.

Así:
```html
<role rolename="manager-gui"/>
<user username="manager" password="manager" roles="manager-gui"/>

<role rolename="admin-gui"/>
<user username="admin" password="admin" roles="manager-gui,admin-gui"/>
```


### Para probar
```bash
cd /opt/tomcat/bin/
./startup.sh
cd /opt/tomcat/webapps/
cd ROOT/
vim index.jsp
<%
  out.println("Your IP address is "+ request.getRemoteAddr());
%>
```
Y ahora accedé a `localhost:8080/test.jsp`


## Otro método
https://m.youtube.com/watch?v=j-sNUzZLuUM
```bash
$ javac

If it results in error, it means that there is no JDK installed. If JDK is not installed on your system then you can install it by using the following command in terminal:

$ sudo apt-get install openjdk-12-jdk

Make sure you watch complete video because command and data given won’t make sense without watching entire video.
All the commands and data used in the video is given below:

$ sudo groupadd tomcat
$ sudo useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat
$ sudo mkdir /opt/tomcat
$ wget https://www-us.apache....
$ sudo tar xzvf apache-tomcat-8*tar.gz -C /opt/tomcat --strip-components=1
$ cd /opt/tomcat
$ sudo chgrp -R tomcat /opt/tomcat
$ sudo chmod -R g+r conf
$ sudo chmod g+x conf
$ sudo chown -R tomcat logs
$ sudo update-java-alternatives -l
$ sudo nano /etc/systemd/system/tomcat.service
[Unit]
Description=Apache Tomcat Web Application Container
After=network.target

[Service]
Type=forking
Environment=JAVA_HOME=paste the copied path
Environment=CATALINA_PID=/opt/tomcat/temp/tomcat.pid
Environment=CATALINA_HOME=/opt/tomcat
Environment=CATALINA_BASE=/opt/tomcat
Environment='CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC'
Environment='JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom'
ExecStart=/opt/tomcat/bin/startup.sh
Exe

cStop=/opt/tomcat/bin/shutdown.sh
User=tomcat
Group=tomcat
UMask=0007
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target

$ sudo systemctl daemon-reload
$ sudo systemctl start tomcat
$ sudo systemctl status tomcat
$ sudo ufw allow 8080
$ sudo nano /opt/tomcat/conf/tomcat-users.xml

<user username="admin" password="password" roles="manager-gui,admin-gui"/>

$ sudo chown tomcat work
$ sudo systemctl restart tomcat
```
Ahora ingresá a localhost:8080/


### En otro video usan
```bash
sudo useradd -m -d /opt/tomcat -U -s /bin/false tomcat
sudo apt update
sudo apt install -y default-jdk
cd /tmp 
Descargá en quick navigation la versión más nueva.
wget apache-tomcat-10.1.13.tar.gz
sudo tar xvf apache-tomcat-10.1.13.tar.gz -C /opt/tomcat --strip-components=1
sudo chown -R tomcat:tomcat /opt/tomcat
sudo vi /opt/tomcat/conf/tomcat-users.xml
```

##### Agregá en ese archivo arriba de la etiqueta final 
```html
<role rolename="manager-gui"/>
<user username="manager" password="manager" roles="manager-gui"/>

<role rolename="admin-gui"/>
<user username="admin" password="admin" roles="manager-gui,admin-gui"/>
```

Ahora abrí
```bash
sudo su
vi /opt/tomcat/webapps/manager/META-INF/context.xml
y comentá como habíamos dicho antes 
sudo update-java-alternatives -l
```

### Another one
https://m.youtube.com/watch?v=aL8_tFNnQ_A

```bash
apt install default-jdk

mkdir /opt/tomcat

groupadd tomcat

useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat

wget http://apachemirror.wu...

tar xzvf apache-tomcat-*tar.gz -C /opt/tomcat

cd /opt/tomcat

chgrp -R tomcat /opt/tomcat

chmod -R g+r conf

chmod g+x conf

chown -R tomcat webapps/ work/ temp/ logs/

update-java-alternatives -l

nano /etc/systemd/system/tomcat.service

Unit
Description=Apache Tomcat Web Application Container
After=network.target

Service
Type=forking

Environment=JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64
Environment=CATALINA_PID=/opt/tomcat/temp/tomcat.pid
Environment=CATALINA_HOME=/opt/tomcat
Environment=CATALINA_BASE=/opt/tomcat
Environment='CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC'
Environment='JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom'

ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh

User=tomcat
Group=tomcat
UMask=0007
RestartSec=10
Restart=always

Install
WantedBy=multi-user.target

systemctl daemon-reload

systemctl start tomcat


nano /opt/tomcat/conf/tomcat-users.xml

tomcat-users . . .
    user username="admin" password="password" roles="manager-gui,admin-gui"/
/tomcat-users

nano /opt/tomcat/webapps/manager/META-INF/context.xml

nano /opt/tomcat/webapps/host-manager/META-INF/context.xml

systemctl restart tomcat
```

### AWS EC2
https://github.com/jaswanthnasa/Jaswanth-DevOps-Documentations/blob/master/tomcat.md

https://github.com/jaswanthnasa/Jaswanth-DevOps-Documentations/blob/master/jenkins.txt

https://www.youtube.com/watch?v=CptBO6wAiEQ  

