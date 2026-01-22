---
title: "Creá test de preguntas con Hugo quiz"
date: 2024-10-20T11:45:15-03:00
tags: ['hugo','quiz']
---
[HUGO Quiz Master](/files/hugo-quiz-master.zip)

https://github.com/bonartm/hugo-quiz

#### Hugo-learn theme

1. Para instalar y configurar la biblioteca, copie el archivo `demo/layouts/partials/custom-header.html` en su carpeta local de `layouts/partials/`. Esto inserta el código javascript necesario dentro de la sección principal del sitio web de hugo.
2. Para instalar el código corto, copie el contenido de `demo/layouts/shortcodes/quizdown.html` en su carpeta local de `layouts/shortcodes/`.
3. En `vim _default/baseof.html` tenés que agregar arriba de footer.html:
```bash
  {{- partial "custom-header.html" . -}}

```
4. Actualmente, la marca `--minify` del comando hugo causa problemas con el código de rebajas de quizdown sin procesar. Elimine la bandera al crear su sitio web o utilice la siguiente opción en su `config.toml`:
```bash
[minify]
  disableHTML = true
```



# Hugo Quiz

{{< quizdown >}}

---
primary_color: orange
secondary_color: lightgray
text_color: black
shuffle_questions: false
---

## ASM 64 bits

---
shuffle_answers: false
---

Como se pasan los argumentos a las funciones en ASM de 64 bits?
![asdfs](https://w7.pngwing.com/pngs/572/973/png-transparent-red-triangle-right-triangle-red-triangle-angle-photography-triangle-thumbnail.png)

> Some hint

- [x] RCX, RDX, R8, R9
- [ ] Los argumentos se pasan por el stack.
- [ ] Los primeros 4 argumentos se pasan RCX, RDX, R8, R9 los demás por el stack.

## Poné los [días](https://en.wikipedia.org/wiki/Day) en órden!

> Lunes es el primer día de la semana.

1. Lunes
2. Martes
3. Miércoles
4. Viernes
5. Sábado  
{{< /quizdown >}}
