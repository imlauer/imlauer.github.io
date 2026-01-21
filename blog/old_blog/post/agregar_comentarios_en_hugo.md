---
title: "Agregar comentarios en HUGO"
date: 2024-09-22T20:31:07-03:00
tags: ['hugo']
---
Hugo viene con todo el código que necesitarías para incluir la carga de Disqus. Simplemente incluya la siguiente línea donde desea que aparezcan sus comentarios:

```bash
{{ template "_internal/disqus.html" . }}
```

### configurando disqus

Esa plantilla requiere que establezca un valor único en el archivo de configuración de su sitio, por ejemplo. config.yaml.

```bash
disqusShortname = "XYW"
```

Además, opcionalmente puede configurar lo siguiente en la portada de un contenido determinado:


* disqus_identifier
* disqus_title
* disqus_url

### Conditional Loading de comentarios de Disqus

Users have noticed that enabling Disqus comments when running the Hugo web server on localhost causes the creation of unwanted discussions on the associated Disqus account. In order to prevent this, a slightly tweaked partial template is required. So, rather than using the built-in `"_internal/disqus.html"` template referenced above, create a template in your `partials` folder that looks like this:

```bash
<div id="disqus_thread"></div>
<script type="text/javascript">

(function() {
    // Don't ever inject Disqus on localhost--it creates unwanted
    // discussions from 'localhost:1313' on your Disqus account...
    if (window.location.hostname == "localhost")
        return;

    var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
    var disqus_shortname = '{{ .Site.DisqusShortname }}';
    dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
<a href="http://disqus.com/" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>
```

Observe que hay una declaración if simple que detecta cuando está ejecutando en localhost y omite la inicialización de la inyección de comentarios de Disqus.

Ahora, haga referencia a la plantilla parcial de su plantilla de página:

```bash
{{ partial "disqus.html" . }}
```


### Alternativas
[Discourse](http://www.discourse.org/)
[IntenseDebate](http://intensedebate.com/)
[Livefyre](http://livefyre.com/)
[Muut](http://muut.com/)
[(Duoshuo, popular in China)](http://duoshuo.com/)
[isso (Self-hosted, Python)](http://posativ.org/isso/)
[Kaiju](https://github.com/spf13/kaiju)
