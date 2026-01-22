---
title: "Como usar VIM como editor hexadecimal"
date: 2024-08-14T00:20:03-03:00
tags: ['vim','editor','hexadecimal']
---
Para editar hexadecimal en vim renombrá el archivo a example.bin y agregá a tu `.vimrc` la siguiente configuración:


```
" vim -b : edit binary using xxd-format!
augroup Binary
  au!
  au BufReadPre  *.bin let &bin=1
  au BufReadPost *.bin if &bin | %!xxd
  au BufReadPost *.bin set ft=xxd | endif
  au BufWritePre *.bin if &bin | %!xxd -r
  au BufWritePre *.bin endif
  au BufWritePost *.bin if &bin | %!xxd
  au BufWritePost *.bin set nomod | endif
augroup END
```

Primero creá tu archivo `.txt` luego pasalo a `.bin` 

O podés usar ghex pero ahí no se puede insertar texto, sólo se puede modificar el texto que ya existe.
