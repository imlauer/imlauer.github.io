---
title: "Agregando LaTeX a HUGO"
date: 2024-08-14T09:44:43-03:00
tags: ['latex','hugo']
---
Podés tener $$\LaTeX$$ en tu blog con HUGO simplemente agregando el siguiente scripts al template de la página: `layouts/partials/footer.html`

https://www.mathjax.org/#gettingstarted

```js
{{ $script := .Site.Data.webpack_assets.app }}
{{ with $script.js }}
     <script src="{{ relURL (printf "%s%s" "dist/" .) }}"></script>
{{ end }}

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [["$$","$$"],["\\(","\\)"]]} })
</script>
```

#### Prueba LaTeX
$$ e^{i\pi}+1= 0 $$

\begin{aligned}
KL(\hat{y} || y) &= \sum_{c=1}^{M}\hat{y}_c \log{\frac{\hat{y}_c}{y_c}} \\
JS(\hat{y} || y) &= \frac{1}{2}(KL(y||\frac{y+\hat{y}}{2}) + KL(\hat{y}||\frac{y+\hat{y}}{2}))
\end{aligned}

Para insertar \\(\LaTeX\\) tenés que usar lo que dice luego de inlineMath:

```js
$$ $$ 
\\( \\)
```


#### Esto es todo.
