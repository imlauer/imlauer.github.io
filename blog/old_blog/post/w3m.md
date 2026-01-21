---
title: "El mejor navegador de consola con visor de imágenes"
date: 2024-08-05T05:36:57-03:00
tags: ['navegadores','w3m']
---
El mejor navegador de consola con soporte JavaScript hasta la fecha es **Carbonyl**, pero es demasiado pesado a comparación de w3m que todavía puede mostrar muchas páginas. Hubo un intento por implementar javascript en w3m pero se abandonó el proyecto (w3m-js).

Se navega usando flechas, tab, y las keybinding de vim.
Si querés buscar algo en la página se hace con `/` seguido de la palabra, n para la siguiente ocurrencia.   
Shift+t para abrir nueva pestaña.     
Shift+b para volver atrás.    
Shift+[ para moverse entre las pestañas.   
Shift+u para cambiar de url.  
Control+h para ver el historial.  
H mayúscula para ver el menú de ayuda.   

Tenés tabs, podés googlear imágenes.
```
sudo apt install -y w3m w3m-img
w3m https://imlauera.github.io
```

##### Como cambiar el tamaño de letra en xterm:
En .Xdefaults agregá:

```
xterm*faceName: Monospace
xterm*faceSize: 14
```

Ejecutá: `xrdb .Xdefaults`

### Redirecciones en w3m
```console
url m!^https?://([a-z]+\.)?x\.com/!
substitute_url "https://sotwe.com/"

url m!^https?://([a-z]+\.)?twitter\.com/!
substitute_url "https://sotwe.com/"

url m!^https?://([a-z]+\.)?reddit\.com/!
substitute_url "https://old.reddit.com/"

url "https://www.youtube.com/" exact
substitute_url "file:/cgi-bin/video.cgi?"
#substitute_url "https://yewtu.be/"

url m!^https?://([a-z]+\.)?wikipedia\.com/!
substitute_url "https://wl.vern.cc/"

url m!^https?://([a-z]+\.)?imgur\.com/!
substitute_url "https://rimgo.pussthecat.org/"

url "https://www.reuters.com/" exact
substitute_url "https://neuters.de/"

url "https://www.reuters.com/" exact
substitute_url "https://neuters.de/"

url "https://medium.com/" exact
substitute_url "https://scribe.rip/"

url "https://web.archive.org/" exact
substitute_url "https://wayback-classic.net/"
```

### Restaurar ventanas cerradas 
```bash
Inside ~/.w3m/keymap add:

keymap d COMMAND "EXTERN 'echo %s >> ~/.w3m/RestoreTab.txt' ; CLOSE_TAB"
keymap u COMMAND TAB_GOTO file:/cgi-bin/restore_tab.cgi

```
