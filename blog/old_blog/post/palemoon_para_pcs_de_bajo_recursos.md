---
title: "PaleMoon para PCs de bajo recursos"
date: 2023-07-10T10:17:19-03:00
tags: ['linux','palemoon']
---
Estuve probando este navegador en una Intel Celeron N2806 Dual Core @1.6GHz con 4GB de RAM con una grafica integrada Intel Atom Processor Z36xxx/Z37xxx. 
A comparacion de Firefox no levanta tanta temperatura y consume menos RAM. Lo use con una extension llamada Pentadactl en donde podes usar las keybindings de VIM, tuve que modificar el install.rdf para poder instalar la extension debido a que no me permitia la instalacion desde la pagina de Addons de PaleMoon por un supuesto problema de compatibilidad, en realidad solo tenes que clonar el repositorio de Pentadactl modificar el maxVersion a 32 o a la version de PaleMoon que sea que estes usando en el install.rdf, compilar la extension y abrirla en PaleMoon.
Tarda mas tiempo en renderizar las paginas pero en mi opinion vale la pena para no levantar tanta temperatura en PCs de bajos recursos.
