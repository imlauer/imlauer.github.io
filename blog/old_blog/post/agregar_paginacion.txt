---
title: "Agregar paginación a un template en HUGO"
date: 2024-09-28T08:20:44-03:00
tags: ['hugo']
---

En `layouts/_default/list.html` de esto: 
```html
{{ partial "posts.html" .Pages }}
```

Lo **cambié** a esto:

```html
{{ partial "posts.html" . }}
```

En `layouts/index.html` de esto:
```html
{{ partial "posts.html" (where site.RegularPages "Type" "in" site.Params.mainSections) }}
```
Lo cambié a:
```html
{{ partial "posts.html" . }}
```

Y en `layouts/_default/posts.html` de esto:
```html
<div class="posts">
  {{ range . }}
  <div class="post">
    <div><a href="{{.Permalink }}" class="title is-size-5">{{ .Title }}</a></div>
    <div class="subtitle is-6">{{ .Date.Format "January 02, 2006" }}</div>
  </div>
  {{ end }}
</div>
```

lo cambié así

```html
<div class="posts">
{{ range .Paginator.Pages }}
  <div class="post">
    <div><a href="{{.Permalink }}" class="title is-size-5">{{ .Title }}</a></div>
    <div class="subtitle is-6">{{ .Date.Format "January 02, 2006" }}</div>
  </div>
{{ end }}
{{ template "_internal/pagination.html" . }}

</div>
```

---

Por último agregué `paginate = 200` en el `config.toml` y en `assets/css/site.sass` agrandé la letra de los links de paginación:

**CSS**
```css
.pagination
  font-size: 3rem!important
```
