---
title: "Fix: Resources tocss"
date: 2024-12-17T21:29:23-03:00
tags: ['hugo']
---
```bash
Start building sites �
hugo v0.140.0+extended linux/amd64 BuildDate=unknown

ERROR deprecated: resources.ToCSS was deprecated in Hugo v0.128.0 and will be removed in Hugo 0.141.0. Use css.Sass instead.
```

Se arregla modificando en themes:
```html
{{ if $.Site.Params.postcss }}
{{ .Scratch.Set "sass" ($sass | resources.ToCSS $options | postCSS | resources.Minify) }}
{{ else }}
{{ .Scratch.Set "sass" ($sass | resources.ToCSS $options | resources.Minify) }}
{{ end }}
```
Por:

```html
{{ if $.Site.Params.postcss }}
{{ .Scratch.Set "sass" ($sass | css.Sass $options | postCSS | resources.Minify) }}
{{ else }}
{{ .Scratch.Set "sass" ($sass | css.Sass $options | resources.Minify) }}
{{ end }}
```
