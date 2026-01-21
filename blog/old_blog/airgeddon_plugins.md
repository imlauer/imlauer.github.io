---
title: "Agregando funcionalidades a Airgeddon: Airgeddon Plugins"
date: 2025-01-30T16:16:08-03:00
tags: ['airgeddon']
---
Para realizar el ataque de evil twin (gemelo malvado) se necesita una tarjeta de red que acepte dividirse en dos tarjetas lógicas: una para levantar el punto de acceso otra para hacer un ataque de denegación de servicio. En caso de no tenerla, tenemos que usar dos tarjetas de red e instalar el plugin `multint.sh`.

```bash
git clone https://github.com/xpz3/airgeddonplugins/
sudo cp multint.sh /usr/share/airgeddon/plugins
sudo cp mass_handshake_capture.sh /usr/share/airgeddon/plugins
sudo cp autoload_handshake.sh /usr/share/airgeddon/plugins
```

#### Descripción de cada plugin
**avoid_airmon.sh**: This plugin disables airmon-ng to be used to start and stop monitor mode on an interface. `iw` will be used instead.

**multint.sh**: This plugin enables Airgeddon to use more than one interface to be used with Captive Portal attack. By default, Airgeddon uses Virtual Interface method on supported chipsets to create  monitor mode and master mode required to run captive portal attack. For users who do not have a fully compatible chipset, they can use this plugin to use multiple cards that support monitor and master mode one per card to run captive portal attack.

**nogui.sh**: This plugin voids the requirement of xterm or tmux for evil twin attack. This plugin only works with Evil Twin attack with Captive Portal method (Option 9 in Evil Twin attacks menu)

**custom_essid.sh**: This plugin allows you to specify custom name for a target AP with hidden SSID, after discovering it with deauth attack.


**mass_handshake_capture.sh**: This plugin allows you to mass capture Handshake/PMKID from nearby WPA networks. After downloading the plugin to the airgeddon/plugins directory, run airgeddon, select interface and put the card into monitor mode and then goto `Handshake/PMKID/Decloaking tools menu` and choose Option `10. Mass Handshake/PMKID Capture` and then follow the instructions. There are some variables that can be set according to the needs. Open the plugin file and see the top section. The minimum required airgeddon version is now 11.40. __In the new update this plugin allows you to save the AP details(essid, bssid, channel, encryption and handshake/PMKID file location) whose handshake has been captured. You can use this file to automatically start Evil Twin captive portal attack using airgeddon_cli.sh plugin which takes the file as an argument and starts the evil twin attack.__

**airgeddon_cli.sh** This plugin enables command line interface for airgeddon evil twin with captive portal attack. It can work in two ways, one is to specify just the vif capable interface and a file containing essid, bssid, channel, encryption type and handshake/PMKID file location. The plugin will then start the evil twin attack using the provided values in the file. All other options will be set to default and can be edited from the plugin. The second method to use the plugin is to specify the bssid, essid, channel, encryption type, handshake/PMKID file path, vif capable interface and any other desired values as command line arguments. The detailed usage info can be found by downloading the plugin and then running `bash airgeddon.sh -u` If no command line arguments are passed, airgeddon will start normally.

**customportals.sh** This plugin makes it easy to create or edit custom portals to be used with airgeddon. I have included all portals from fluxion and fixed them to work properly. The plugin takes care of compatibility with airgeddon. If you just want to use these portals, then you dont have to do any changes. Just download the plugin file and also the customportals/ folder into airgeddon plugins directory. Then run airgeddon as normal and towards the end, it will ask whether you want to use custom portal or not. If you choose yes, then it will list all custom portals available in the `plugins/customportals/` directory. It will list all folders inside it. When you want to create a new portal, create or download the necessary files, put them in a folder and copy it to the `plugins/captiveportals/` folder along with the other portals. There are some things to note while developing a custom portal. Only use `.html` files and do not use any `.htm` files. It will not work. Your portal must have a `<form>` tag with a password field named `"password|password1|passphrase|key|key1|wpa|wpa_psw"` The `<form>` tag must have the action to post to `check.htm` with the password field and its value. If you want to use php for your custom portal you have to install php-cgi or apache or whatever you want and change the value of the variable in `customportals.sh` from `customportals_php_handle=1` to `customportals_php_handle=0` The value is set to "1" in the plugin file to handle the php files from the fluxion portals and make it compatible with airgeddon. If you have any questions, ask in airgeddon discord plugins channel rather than opening a bug report here.

**autoload_handshake.sh** This plugin automatically loads a previously captured handshake file for a selected target, if the user wishes to. You can change the default handshake location by editing the variable in the file.
