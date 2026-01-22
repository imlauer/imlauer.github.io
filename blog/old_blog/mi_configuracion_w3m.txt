---
title: "Mi configuración de w3m"
date: 2025-02-27T01:00:41-03:00
tags: ['w3m']
---
**External browser**:    

Chawan parecido a w3m es un navegador que soporta un poco de javascript.

`Escape+M` para iniciar el navegador externo o `Numero+Escape+M` 

```bash
Mailer                                     [/usr/bin/neomutt    ]
External browser                           [/usr/bin/mpv        ]
2nd external browser                       [elinks              ]
3rd external browser                       [vim                 ]
4th external browser                       [yt-dlp -f134+140 --c]
5th external browser                       [gallery-dl --cookies]
6th external browser                       [falkon              ]
7th external browser                       [cha                 ]
8th external browser                       [yt-dlp -f140 --cooki]
9th external browser                       [git clone           ]
```

Con `.config/fish/fish.conf`:

```bash
export XKB_DEFAULT_LAYOUT=es
export QT_QPA_PLATFORM=linuxfb:size=1000x1000
alias dgg 'w3m dgg.gg'
alias tdgg 'torsocks w3m dgg.gg'
alias telegram 'falkon web.telegram.org'
alias upwork 'falkon upwork.com'
alias whatsapp 'qutebrowser https://web.whatsapp.com'
alias yewtube 'w3m https://yewtu.be/feed/subscriptions'
alias invidious 'w3m https://inv.nadeko.net/feed/subscriptions'
```


Cargar imágenes en una nueva ventana del navegador así posteriormente abrirlos con mpv con (shift+M)

```bash
TITLE string
Load inline images automatically                        ( )YES  (*)NO
Maximum processes for parallel image loading            [4                   ]
Use external image viewer                               ( )YES  (*)NO
Scale of image (%)                                      [20                  ]
Inline image display method                             [external command   ]
External command to display image                       [w3mimgdisplay       ]
Use link list of image map                              (*)YES  ( )NO
Fold lines of plain text file                           ( )YES  (*)NO
Show line numbers                                       ( )YES  (*)NO
Show search string                                      (*)YES  ( )NO
Move cursor to top line when going to label             ( )YES  (*)NO
Move cursor to top line when moving to next page        ( )YES  (*)NO
```

Ahora tengo este comando para que lea las paginas.

```bash
links -dump -width 512 $1 | tr "\n\ r" " " | sed "s/^.*, consoomer version//g" | espeak -s 120 -p 30  &
```

Y tengo este comando para descargar páginas offline.

```bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://epet36misiones.edu.ar
```
