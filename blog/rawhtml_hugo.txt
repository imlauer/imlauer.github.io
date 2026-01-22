---
title: "Agregar Rawhtml en HUGO"
date: 2024-09-10T16:17:04-03:00
tags: ['hugo']
---
Para hacer esto previamente es recomendable tener clonado el repo del theme o forkeado y comitear los cambios.

Agregá en `/layouts/shortcodes/rawhtml.html`

```
<!-- raw html -->
{{.Inner}}
```

