---
title: "Insertar texto seleccionado a archivo vim"
date: 2025-02-16T17:06:43-03:00
tags: ['vim']
---

You can do it in three steps:

* type `Shift-vj...j` to select some lines
* type `:'<,'>w! >>file.bak` to save selected lines to file.bak(append)
* type gvd to delete original lines

You can write a user-defined command Sbak if you like:

com! -nargs=1 -range Sbak call MoveSelectedLinesToFile(<f-args>)
fun! MoveSelectedLinesToFile(filename)
    exec "'<,'>w! >>" . a:filename
    norm gvd
endfunc
