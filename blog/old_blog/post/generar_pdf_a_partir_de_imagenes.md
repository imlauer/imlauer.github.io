---
title: "Generar pdf a partir de imagenes con LaTeX"
date: 2024-09-02T03:48:42-03:00
---
Generá un archivo llamado misimagenes.tex y guardá lo siguiente:
```latex
\documentclass{article}
\usepackage{graphicx}

\begin{document}

\title{Conversión de Imágenes a PDF}
\author{Tu Nombre}
\date{\today}
\maketitle

\section{Imágenes Incluidas}
Aquí hay una imagen incluida en el documento:

\includegraphics[width=\textwidth]{nombre_de_la_imagen.jpg}

\end{document}
```
En la línea de comandos ejecutá `ls -v *.jpg > mis_imagenes`
Copiá y pegá en tu LaTeX todas las imágenes ahora y en VIM seleccionando todas las líneas de los nombres de las imágenes y ejecutando `:norm I \includegraphics[width=\textwidth]{` y `:norm A}`

Luego `pdflatex misimagenes.tex`
