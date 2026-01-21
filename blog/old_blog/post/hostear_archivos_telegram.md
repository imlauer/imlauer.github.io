---
title: "Hostear archivos telegram"
date: 2024-09-25T19:57:24-03:00
tags: ['telegram']
---
#### Configurar hosteo de archivos en Telegram
* Para hacerlo deben crear un canal de telegram
* Crear un bot https://core.telegram.org/bots
* Añadir el bot al canal
* Conseguir la id del canal https://stackoverflow.com/questions/33858927/how-to-obtain-the-chat-id-of-a-private-telegram-channel
* Una vez hecho esto deben editar el archivo de configuracion

Una vez hecho esto deben editar el archivo de configuracion `/appsettings.development.json`
En usar telegram ponen true, en BotId y ChatId ponen el token del bot y la id del canal.
