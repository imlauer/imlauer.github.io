---
title: "Eliminar el fondo de la cámara en OBS y como configurar push-to-talk."
date: 2024-09-20T17:09:37-03:00
tags: ['obs']
---
Instalá: https://github.com/locaal-ai/obs-backgroundremoval/releases/tag/1.1.13

En Linux: `sudo dpkg -i .deb`

Abrí el OBS agregá la cámara en sources (fuentes), botón derecho filters, botón derecho en effect filters y agregá background removal.

Y para agregarle otro fondo, en fuentes agregá una imágen cualquiera y con control seleccioná tu cámara y la imágen que agregaste botón derecho y "group items" (agrupar items).

Podés probar cambiando en opciones avanzadas el `segmentation model` y fijarte cual funciona mejor.
Podés ponerte borroso a vos mismo pero no el background (blur focus point)

#### Push to talk
https://www.youtube.com/watch?v=g2awrtf9zbs
