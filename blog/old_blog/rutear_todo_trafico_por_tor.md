---
title: "Rutear todo tráfico por Tor"
date: 2024-11-23T23:01:12-03:00
tags: ['tor']
---
Lo mejor es usar Qubes OS.

Los dueños de las grandes redes sociales se hacen multimillonarios haciendo espionaje masivo estudiando como usas Instagram, TikTok, Facebook, Google, Spotify, Amazon, Mac, iOS, Android estudian que tipo de contenido mirás por qué apretaste esa publicidad por qué la cerraste, por qué bajaste dos centímetros para abajo y por qué apretaste la historia de tal persona. Estudian absolutamente todo para exprimirte al máximo por unos cuántos centavos más. Los procesadores Intel tienen una puerta trasera a partir del i3 hacia adelante. Spotify quiere que escuches la música online para hacer estadísticas y poner mejores publicidades y obtener mejores ganancias. Lo mejor es escuchar la música offline.

Google no te deja buscar a través de Tor, sí o sí quieren saber quién sos. Si no saben quién sos te tiran una captcha en donde te pide que seleccionenes las sendas peatonales, los semáforos, las escaleras y lo usan para entrenar a su robot que se maneja sólo: waymo.

Facebook, WhatsApp, Instagram son mucho peores.

### Posible solución: ejecutar el mínimo javascript y enrutar todo el tráfico por Tor.


```bash
You're probably interested in Whonix then - it's a virtual machine that creates a Tor-enabled
gateway that routes all traffic through it.

https://wiki.archlinux.org/title/Whonix - but you'll need to be running a separate Arch VM for
your TOR internet activities.

AFAIK, the underlying Host OS (Your existing Arch install) will be business as usual (not using
TOR)

Now - you can even go one step further and replace Arch with Qubes - a Linux distro for the
paranoid that can use Whonix - and also disposable VMs (Arch/Whonix/Debian/Fedora etc.) and are
spun up for various tasks and disposed of once done.

It's an interesting concept, but requires a fairly beefy PC/Laptop
```

```bash
You can try using this: https://github.com/ruped24/toriptables2. The Python script routes all
your traffic with iptables rules through Tor.

It's a potentially dangerous to route all traffic through Tor because some traffic can be
unencrypted and can be modified/read by the exit node.

```

