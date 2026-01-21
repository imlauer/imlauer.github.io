---
title: "Compilar elinks con JavaScript e Instalar Links con soporte de FrameBuffer"
date: 2024-11-24T11:22:20-03:00
tags: ['elinks']
---
Si querés tener un mínimo soporte de javascript en un navegador de consola tenés que tener SpiderMonkey instalado y recompilarlo desde el source.

```bash
w3m http://elinks.or.cz/download/
tar xvf elinks-current-unstable.tar.gz
./configure | grep Spider
```

JavaScript is enabled by default if Spidermonkey is found, according to the config file in the
felinks git repo. Haven't tried it myself, though. More here: http://elinks.or.cz/documentation/manual.html#ecmascript


### Compilar links con fb support.

```bash
> Do I need Xorg to have graphics? I'm just using the tty

● No! For TTY/framebuffer, you don't need Xorg. Links2 can use the framebuffer directly. Let me build it with
  framebuffer support:

✓ Download links source
  $ cd /tmp && curl -O http://links.twibright.com/download/links-2.30.tar.gz
  ↪ 4 lines...

○ Extract and configure links with framebuffer and JS support
  # Fallo 
  $ cd /tmp && tar xzf links-2.30.tar.gz && cd links-2.30 && ./configure --enable-graphics --with-fb
  --enable-javascript 2>&1 | tail -30

  # Asi funciono (sin soporte javascript)

  $ cd /tmp/links-2.30 && make clean && ./configure --enable-graphics --with-fb 2>&1 | tail -20

  $ cd /tmp/links-2.30 && make -j$(nproc) && sudo make install
  $ /usr/local/bin/links -g -driver fb https://imlauer.github.io



```

#### Para usarlo con Tor

```bash
links -g -socks-proxy localhost:9050 https://check.torproject.org
```

