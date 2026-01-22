---
title: "Access Point Wifi ArchLinux"
date: 2026-01-04T15:44:59-03:00
---
Use esto para saltear una proteccion de celular HUAWEI FIG-LX3. Configure un access point me conecte desde el celular y cuando le di Next corte el access point y me dejo pasar el filtro 


Usa la aplicacion create_ap del AUR o hacelo manualmente asi:

`create_ap` es mucho más simple de usar. Te automatiza todo el proceso.

## Instalación

```bash
yay -S create_ap
# o
paru -S create_ap
```

También necesitas las dependencias:
```bash
sudo pacman -S hostapd dnsmasq
```

## Uso básico

**Compartir WiFi a través de WiFi:**
```bash
sudo create_ap wlan0 wlan0 NombreDeRed Contraseña
```

**Compartir conexión Ethernet a través de WiFi:**
```bash
sudo create_ap wlan0 eth0 NombreDeRed Contraseña
```

El formato general es:
```bash
sudo create_ap <interfaz-wifi> <interfaz-internet> <SSID> <contraseña>
```

## Ejemplos prácticos

**Con configuración básica:**
```bash
sudo create_ap wlan0 eth0 MiHotspot mipassword123
```

**Sin contraseña (red abierta):**
```bash
sudo create_ap wlan0 eth0 MiHotspot
```

**Elegir canal específico:**
```bash
sudo create_ap -c 6 wlan0 eth0 MiHotspot mipassword123
```

**Ver interfaces disponibles:**
```bash
ip link show
# o
iw dev
```

## Hacer que inicie automáticamente

Crea un servicio systemd (`/etc/systemd/system/create_ap.service`):

```ini
[Unit]
Description=Create AP Service
After=network.target

[Service]
ExecStart=/usr/bin/create_ap wlan0 eth0 NombreDeRed Contraseña

[Install]
WantedBy=multi-user.target
```

Luego:
```bash
sudo systemctl enable create_ap
sudo systemctl start create_ap
```

## Detener el AP

Simplemente presiona `Ctrl+C` o si está corriendo como servicio:
```bash
sudo systemctl stop create_ap
```























To set up your Arch Linux PC as a WiFi access point to share your internet connection, you'll need to use a tool like `hostapd` for the AP and configure network forwarding. Here's how:

## Prerequisites

Your WiFi card needs to support AP mode. Check with:
```bash
iw list | grep -A 10 "Supported interface modes"
```

Look for "AP" in the output.

## Installation

```bash
sudo pacman -S hostapd dnsmasq
```

## Configuration

**1. Create hostapd config** (`/etc/hostapd/hostapd.conf`):

```
interface=wlan0
driver=nl80211
ssid=YourAPName
hw_mode=g
channel=6
wmm_enabled=1
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=YourPassword
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
```

**2. Configure dnsmasq** (`/etc/dnsmasq.conf`):

```
interface=wlan0
dhcp-range=192.168.50.2,192.168.50.20,255.255.255.0,24h
```

**3. Set up IP forwarding and NAT:**

```bash
# Assign static IP to wlan0
sudo ip addr add 192.168.50.1/24 dev wlan0

# Enable IP forwarding
sudo sysctl net.ipv4.ip_forward=1

# Set up NAT (replace eth0 with your internet interface)
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
```

**4. Start services:**

```bash
sudo systemctl start hostapd
sudo systemctl start dnsmasq
```

## Make it permanent

To make IP forwarding persistent, add to `/etc/sysctl.d/30-ipforward.conf`:
```
net.ipv4.ip_forward=1
```

For iptables rules, save them:
```bash
sudo iptables-save > /etc/iptables/iptables.rules
sudo systemctl enable iptables
```

Enable services on boot:
```bash
sudo systemctl enable hostapd dnsmasq
```

Alternatively, consider using `create_ap` (available in AUR) which automates much of this setup.


El problema es que tu adaptador WiFi Realtek tiene limitaciones. Hay dos errores:

1. **No puede transmitir en el canal 1** - tu adaptador/región tiene restricciones
2. **Es un driver Realtek** - conocidos por tener problemas con AP mode

## Soluciones a probar:

**1. Usa un canal permitido (prueba canales más altos):**

```bash
sudo create_ap -c 6 wlp1s0 enp2s0 NombreDeRed jajajajajaja
```

O prueba con canal 11:
```bash
sudo create_ap -c 11 wlp1s0 enp2s0 NombreDeRed jajajajajaja
```

**2. Especifica la banda de frecuencia:**

```bash
sudo create_ap --freq-band 2.4 -c 6 wlp1s0 enp2s0 NombreDeRed jajajajajaja
```

**3. Ve qué canales soporta tu adaptador:**

```bash
iw list | grep -A 20 "Frequencies"
```

Busca los canales que **no** tengan marcas como "disabled", "no IR", o "radar detection". Usa uno de esos canales.

**4. Verifica el código de país (puede limitar canales):**

```bash
iw reg get
```

Si es necesario, configúralo:
```bash
sudo iw reg set AR  # para Argentina
```

**5. Si nada funciona, considera linux-wifi-hotspot:**

```bash
yay -S linux-wifi-hotspot
```

Es una interfaz gráfica que a veces maneja mejor los drivers Realtek problemáticos.

Prueba primero con diferentes canales (6 u 11) y muéstrame qué dice. ¿Qué te devuelve `iw list | grep -A 20 "Frequencies"`?

Veo que los canales están disponibles pero hay un problema de permisos regulatorios. El adaptador reporta que soporta los canales, pero no puede transmitir en ellos.

## Solución: Configura el código de país correctamente

```bash
# Ver configuración actual
iw reg get

# Configurar para Argentina
sudo iw reg set AR
```

Luego intenta de nuevo:
```bash
sudo create_ap -c 6 wlp1s0 enp2s0 NombreDeRed jajajajajaja
```

## Si eso no funciona, hazlo permanente:

Edita `/etc/conf.d/wireless-regdom` y descomenta la línea de Argentina:
```bash
sudo nano /etc/conf.d/wireless-regdom
```

Busca y descomenta:
```
WIRELESS_REGDOM="AR"
```

Luego reinicia o recarga:
```bash
sudo systemctl restart systemd-modules-load
```

## Alternativa: Prueba con linux-wifi-hotspot

Si el problema persiste (los drivers Realtek son problemáticos), usa esta herramienta gráfica:

```bash
yay -S linux-wifi-hotspot
sudo wihotspot
```

Es más amigable y a veces maneja mejor estos drivers caprichosos.

## Otra opción: Verifica el módulo del kernel

```bash
lsmod | grep rtl
```

Algunos drivers Realtek necesitan parámetros especiales. ¿Qué modelo de adaptador WiFi tienes?

```bash
lspci | grep -i network
# o
lsusb | grep -i wireless
```

Prueba primero con `iw reg set AR` y dime si funciona.



```bash
sudo pacman -S linux-headers
```


Ah, perfecto. Instala los headers:

```bash
# Presiona Y para instalar
```

Luego **reinicia** tu PC para cargar el kernel correcto:

```bash
sudo reboot
```

Después del reinicio, verifica que todo coincida:

```bash
uname -r
ls /lib/modules/
```

Deberías ver `6.18.3.arch1-1` en ambos.

Luego intenta de nuevo:

```bash
sudo create_ap -c 6 wlp1s0 enp2s0 NombreDeRed jajajajajaja
```

Los módulos de iptables deberían cargarse automáticamente ahora. Si no, cárgalos manualmente:

```bash
sudo modprobe iptable_nat
sudo modprobe iptable_filter
```

El problema era simplemente que tenías un kernel desactualizado corriendo pero los módulos nuevos instalados. Después del reinicio debería funcionar. ¡Avísame cómo te va!



---

Lo que te está pasando es el **bloqueo FRP** (Factory Reset Protection) de Google, una función de seguridad que se activa después de un reseteo de fábrica si el teléfono tenía una cuenta Google asociada. Como te lo regalaron y no eres el propietario original, no tienes las credenciales, y el teléfono queda bloqueado.

### Opción recomendada y legal
Lo ideal es **contactar a la persona que te lo regaló** y pedirle que ingrese su cuenta Google en la pantalla de verificación (o que te dé las credenciales para que lo hagas tú). Una vez dentro, puede eliminar la cuenta desde Ajustes > Cuentas > Google > Quitar cuenta, y luego hacer otro reseteo si es necesario. Esto es la forma más segura y no viola ninguna norma.

### ¿Se puede bypass (omitir) el FRP?
Sí, existen métodos para omitir el FRP, y **es legal hacerlo en un teléfono de segunda mano que te regalaron legítimamente** (ya que eres el dueño actual), siempre y cuando no sea robado. Sin embargo:

- En teléfonos Huawei **antiguos** (con Android 5, 6 o EMUI vieja, antes de 2019-2020), a veces funcionan trucos sin PC, como:
  - Usar la llamada de emergencia y marcar códigos como *#*#1357946#*#* para acceder a ajustes y crear un PIN nuevo.
  - Activar TalkBack (accesibilidad) para abrir el navegador y descargar APKs de bypass (como FRP Bypass o QuickShortcutMaker).
  
  Pero en 2025-2026, **muchos de estos trucos gratuitos ya no funcionan** porque Google y Huawei han parcheado las vulnerabilidades, especialmente en versiones más nuevas de Android/EMUI.

- La forma más confiable hoy en día es usar una **herramienta pagada con PC** (Windows o Mac), como:
  - Tenorshare 4uKey for Android
  - iMobie DroidKit
  - Wondershare Dr.Fone
  - UltFone o similares
  
  Estas herramientas conectan el teléfono por USB, detectan el modelo y eliminan el FRP en minutos. Cuestan alrededor de 30-50 USD (licencia temporal), pero tienen alta tasa de éxito en Huawei antiguos y nuevos.

### Advertencias importantes
- Evita descargar APKs dudosos o herramientas gratuitas de sitios desconocidos: pueden contener virus o malware.
- Si el teléfono es muy antiguo y ninguno de los trucos manuales funciona, considera llevarlo a un servicio técnico de confianza (no oficial Huawei, ya que ellos suelen pedir prueba de compra).
- No hay una forma "mágica" de borrarlo por completo sin pasar el FRP, porque esa es precisamente la función de seguridad.

Si me das el **modelo exacto del Huawei** (por ejemplo, P10, Y6, Mate 20, etc.) y la versión de Android/EMUI que tenía antes del reseteo, puedo buscar si hay un método específico que aún funcione en 2026. ¡Suerte!
