---
title: "El nuevo Ares: qBittorrent y Jackett"
date: 2024-06-13T23:25:49-03:00
tags: ['ares','qbittorrent','jackett']
---
Instalá qBittorent: `sudo apt install -y qbittorrent`
Abrí qbittorrent, view -> search engine.
Ahora movete a la pestaña Search y abajo a la derecha dale a search plugins -> install a new one -> web link y pegá: [https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/jackett.py](https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/jackett.py)

Luego andá a `~/.local/share/qBittorrent/nova3/engines/` o seguí este tutorial: [https://github.com/qbittorrent/search-plugins/wiki/How-to-configure-Jackett-plugin](https://github.com/qbittorrent/search-plugins/wiki/How-to-configure-Jackett-plugin)

#### creá un archivo llamado jackett.json

```bash
{
    "api_key": "YOUR_API_KEY_HERE",
    "url": "http://127.0.0.1:9117",
    "tracker_first": false,
    "thread_count": 20
}
```
La API key lo copias de https://localhost:9117

Abrí Jackett y agregá todos los indexers publicos seleccionando uno por uno el checkbox de la izquierda.

Finalmente abrí qbittorrent andate a Search y buscá el torrent que quieras.


Podés descargarte qbittorrent-nox para y agregar `.config/qBittorrent/qBittorrent.conf` debajo de `[Preferences]`:
```bash
WebUI\Password_PBKDF2="@ByteArray(ARQ77eY1NUZaQsuDHbIMCA==:0WMRkYTUWVT9wVvdDtHAjU9b3b7uB8NR1Gur2hmQCvCDpm39Q+PsJRJPaCU51dEiz+dTzh8qbPsL8WkFljQYFQ==)"
```

Que establece la contraseña por defecto como adminadmin para no tener que estar copiando y pegando la contraseña temporal que te genera cada vez que abrís el programa.

###### Para instalar jackett en Arch usando el `AUR`:
```bash
yay -S jackett-bin
sudo systemctl start jackett
```
