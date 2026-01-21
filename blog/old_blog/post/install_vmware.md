---
title: "Install vmware"
date: 2024-09-29T13:20:26-03:00
tags: ['vmware']
---

So on Debian you need to install build-essentials and linux headers. 

```bash
chmod +x VMware-Workstation-Full-17.0.0-20800274.x86_64.bundle
sudo ./VMware-Workstation-Full-17.0.0-20800274.x86_64.bundle
sudo apt install -y build-essential linux-headers-$(uname -r)
vmware 
```

Works on Debian 6.1.0-25-amd64 

 
These are the steps on Ubuntu

```bash
chmod +x VMware-Workstation-Full-17.0.0-20800274.x86_64.bundle
sudo ./VMware-Workstation-Full-17.0.0-20800274.x86_64.bundle
wget https://github.com/mkubecek/vmware-host-modules/archive/workstation-17.5.0.tar.gz
tar -xzf workstation-17.5.0.tar.gz
cd vmware-host-modules-workstation-17.5.0/
tar -cf vmmon.tar vmmon-only/
tar -cf vmnet.tar vmnet-only/
sudo cp -v vmmon.tar vmnet.tar  /usr/lib/vmware/modules/source/
sudo vmware-modconfig --console --install-all
sudo /usr/lib/vmware/bin/vmware-vmx-debug --new-sn ZZ352-2UZDQ-48EUZ-9WW7Z-WCKYD 
vmware
```

## On kali
As you can see, VMware installations can vary significantly depending on the distribution you are using. I recently installed VMware on Kali Linux, which is a rolling release distribution, and had to manually modify the source code to build the vmware-host-modules.

Initially, I tried to install the Linux headers, but they were not available for my kernel version. So, I upgraded my system:

```bash
└─$ sudo apt update
└─$ sudo apt dist-upgrade -y
└─$ reboot
```

After the reboot I was able to install linux-headers with this command:
```bash
└─$ sudo apt install -y linux-headers-$(uname -r)
```

And then I did:
```bash
└─$ git clone https://github.com/mkubecek/vmware-host-modules
└─$ git checkout workstation-17.5.0
└─$ cd vmware-host-modules
└─$ cd vmnet-only
└─$ vim vmnetInt.h
```

I commented these lines:
```c
// #define dev_lock_list()    read_lock(&dev_base_lock)
// #define dev_unlock_list()  read_unlock(&dev_base_lock)
```

And I added these ones:
```c
#if LINUX_VERSION_CODE >= KERNEL_VERSION(6, 9, 0)
#   define dev_lock_list()    rcu_read_lock()
#   define dev_unlock_list()  rcu_read_unlock()
#else
#   define dev_lock_list()    read_lock(&dev_base_lock)
#   define dev_unlock_list()  read_unlock(&dev_base_lock)
#endif
```
 
After that

```bash
└─$ make
└─$ sudo make install
└─$ vmware
```

Ahora al iniciar vmware tenía problemas con vmmon así que cerré vmware y ejecuté:

```bash
└─# sudo modprobe -v vmmon
└─# sudo modprobe -v vmnet
└─$ vmware
```
Lo saqué de: https://stackoverflow.com/questions/49205162/install-vmware-could-not-open-dev-vmmon-no-such-file-or-directory-please-ma

And finally it works on KaliLinux 

```bash
└─$ uname -a
Linux mimachine 6.10.9-amd64 #1 SMP PREEMPT_DYNAMIC Kali 6.10.9-1kali1 (2024-09-09) x86_64 GNU/Linux
```


I am researching now about open-vm-tools
Thank you for your patience


### Reparar error de ethernet vmnet0 could not found

https://superuser.com/questions/662027/getting-a-vmnet0-error-in-vmware-workstation-after-updating-host-computer-from-w

Edité la configuración en menu > virtual network editor > introduje contraseña en consola > borré las entradas y agregué una Bridged 


### Acá explican lo de compilar vmmon y vmnet 

https://community.broadcom.com/vmware-cloud-foundation/question/vmware-workstation-pro-1752-on-ubuntu-2404-lts-compile-errors


#### Install vm-tools para compartir texto y archivos entre el host y la VM:

Dentro de la máquina virtual instalá 
```bash
sudo apt-get update
sudo apt-get install open-vm-tools-desktop
// sudo apt-get install open-vm-tools
sudo reboot
```

### Compartir carpetas (no hace falta agregar este servicio con el fstab es suficiente)
Para copiar una carpeta del guest al host, habilitá shared folder en edit virtual machine settings > options > shared folders.


Creá un archivo `/etc/systemd/system/mnt-hgfs.mount`
```bash
[Unit]
Description=VMware mount for hgfs
DefaultDependencies=no
Before=umount.target
ConditionVirtualization=vmware
After=sys-fs-fuse-connections.mount

[Mount]
What=vmhgfs-fuse
Where=/mnt/hgfs
Type=fuse
Options=default_permissions,allow_other

[Install]
WantedBy=multi-user.target
```

En el archivo `/etc/modules-load.d/open-vm-tools.conf` agregá o crealo si no existe:

```bash
fuse
```

Habilitá el servicio `mnt-hgfs.mount` con el siguiente comando:

```bash
sudo systemctl enable mnt-hgfs.mount # so that mount happens after reboot  
```

Si aún no lo ha hecho, en la pestaña VMware de su máquina > Configuración > Configuración > Opciones > Carpetas compartidas > (completa la información para la ruta y el nombre del host)


Iniciá el servicio:
```bash
sudo systemctl start mnt-hgfs.mount
```

https://superuser.com/questions/1731780/vmware-shared-folder-not-showing-on-ubuntu-guest

#### Como compartir carpetas entre el host y el guest.
If not already done, in VMware tab for your machine > Settings > Settings > Options > Shared Folders > (fill in information for Host Path and Name)

```console
Came across this solution on VMware website:

* Open a root shell in the VM
* Make sure the /mnt/hgfs directory exists. If not, create it.
* Add the following line to /etc/fstab: `vmhgfs-fuse /mnt/hgfs  fuse defaults,allow_other,_netdev   0   0`
* Then reboot your VM. The shared folders should now appear at the mount point /mnt/hgfs
```


El drag and drop no funciona, porque lee los archivos desde una dirección errónea, los copiia a `/tmp/VMwareDnD/folder_name/file.tar.gz` y cuando lo pegás lo quiere copiar desde `/folder_name/file.tar.gz`


### Pasa archivos a través de SSH
### Share files through ssh

Run these commands on guest and host machines:
```bash
hostname -I (get the IP address from the guest machine)
sudo apt install -y openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
sudo apt install -y rsync
```

##### How to run all rsync commands without password:
You will have to run these commands on the host and the guest machine:

```bash
### Generate ssh key
ssh-keygen -t ed25519 -C "your_email@gmail.com"
ssh-copy-id remote_username@remote_server_ip_address
rsync -v file.tar.gz GUEST_IP:/any/location
### If you wanna transfer entire folder you can use the r option: rsync -rv my_folder/ GUEST_IP:/any/location
You can run rsync with the u option. What the u option does is it says: "only re-upload those files that have changed since I last edited them"
```

I think **rsync** works on putty too.


#### Lo que luke smith usaba para actualizar su página
```bash
rsync -uvrP --delete-after ~/.local/src/newweb/ root@server_ip:/var/www/test
```
