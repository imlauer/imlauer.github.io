---
title: "Buscá y streameá torrents desde la terminal usando Jackett y btstrm"
date: 2024-11-17T08:39:46-03:00
tags: ['torrents']
---

[https://old.reddit.com/r/animepiracy/comments/1bheyy7/btstrm_linux_cli_tool_for_torrent_searching](https://old.reddit.com/r/animepiracy/comments/1bheyy7/btstrm_linux_cli_tool_for_torrent_searching)

[https://pypi.org/project/btstrm/](https://pypi.org/project/btstrm/)

[https://github.com/Ajatt-Tools/btstrm](https://github.com/Ajatt-Tools/btstrm)

```bash
python -m venv btstrm
source btstrm/bin/activate # o source btstrm/bin/activate.fish depende de que shell uses
pip install btstrm
sudo pacman -S chafa fzf btfs # Si no encuentra con pacman probá con yay. 
```

### Prerequisites

Before using btstrm, ensure that you have the following dependencies installed:

* Python 3.x
* Player of your choice: mpv, vlc or omxplayer (for RPi)
* btfs (BitTorrent Filesystem)
* fzf (fuzzy finder)
* Jackett (optional, but highly recommended for torrent search integration)
* impd (optional, for language immersion enthusiasts)
* chafa (for displaying movie posters)
* osd (optional, for subtitle downloading)
* Required Python packages: requests, tqdm, colorama, beautifulsoup4, unidecode


Under the hood, btstrm uses some awesome tools:

* chafa for displaying movie posters
* fzf for selecting movies or torrents
* a handful of Python libraries


* Install btfs, fzf, and Jackett by following their respective installation instructions.
Vas a tener que instalar jackett y configurarlo desde la interfaz web, sólo la primera vez es necesario después nunca más.

* Configure Jackett and obtain the API key. 
El API key se encuentra a la esquina superior cuando ejecutás jackett y ingresás a https://127.0.0.1:9117

Si configuraste jackett con qBittorrent copia esos datos: acá está como configurar jackett con qbittorent: [el nuevo ares](https://imlauera.github.io/post/el_nuevo_ares/)

El archivo de configuración de jackett con qbittorent se encuentra en: `/.local/share/qBittorrent/nova3/engines/`

* Create a configuration file named btstrm.conf in the ~/.config directory with the following

La api key está en la página de Jackett (http://127.0.0.1:9117)

```bash
content:

[DEFAULT]
LANG = es-ES
JACKETT_API_KEY = your_jackett_api_key
JACKETT_URL = http://127.0.0.1:9117
TIMEOUT=30
REMOVE_PLAYED_FROM_LIST = True
```

Replace your_jackett_api_key with your actual Jackett API key and adjust the JACKETT_URL if necessary.

You can omit this step because btstrm creates configuration file automatically.


### Ejemplos de uso:
```bash
btstrm -p mpv -k magnet:?xt=urn:btih:example
btstrm -t "Movie Title"
btstrm "Big Buck Bunny"
```

Ahora ejecutá Jackett/jackett

