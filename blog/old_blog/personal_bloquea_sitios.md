---
title: "Personal Telecom bloquea sitios: ThePirateBay y Example.com"
tags: ['blocked']
---
Bloquean https://thepiratebay.org y https://example.com cambien las DNS y se darán cuenta que funcionan esos sitios.

Lo hace a través de la DNS. La solución es cambiarla.

En el caso de Linux:

https://superuser.com/questions/442096/change-default-dns-server-in-arch-linux
https://bbs.archlinux.org/viewtopic.php?id=225794


En el caso de Windows lo tendrán que buscar ustedes.

Ante cualquier duda pueden acceder a través de Tor.

sudo vim /etc/resolv.conf:
```bash
nameserver 1.1.1.1
```

```
Re: NetworkManager keeps rewriting my /etc/recolv.conf

I guess you have to add rc-manager=unmanaged.

/etc/NetworkManager/NetworkManager.conf

[main]
dns=none
rc-manager=unmanaged
```

La última alternativa: Para hacer al archivo inmodificable:
```bash
sudo chattr +i /etc/resolv.conf
```

---

```bash
yay -S fatrace
sudo fatrace | grep /etc/resolv\.conf
```
