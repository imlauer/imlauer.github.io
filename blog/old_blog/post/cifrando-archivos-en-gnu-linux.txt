---
layout: post
title: Cifrando archivos en GNU/Linux
tags: ['cifrar','archivos']
categories: ['linux']
---

Para cifrar:
```bash
gpg -c archivo_privado
cat privado
```
Luego de cifrar borrá el archvio original

Para descifrar:
```
gpg archivo_privado.gpg
```
