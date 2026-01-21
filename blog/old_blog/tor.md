---
title: "Tor: Failed to start Anonymizing overlay network for TCP."
date: 2025-03-17T10:11:31-03:00
tags: ['tor']
---
Nada que un 
```bash
sudo su
rm /etc/tor/torrc
pacman -Rns tor
pacman -S tor
```
No lo pueda solucionar.

### Privacy is not a crime: [Tor](https://www.torproject.org/download/), [I2P](https://geti2p.net/en/)([my I2P spanish tutorial](https://imlauera.github.io/i2p/)) and [Freenet](https://www.hyphanet.org/index.html), [ZeroNet](https://zeronet.io/), [Lokinet](https://imlauera.github.io/post/como-conectarse-lokinet-en-gnulinux/).

How do I use Tor:

```
sudo pacman --noconfirm -S tor torsocks w3m # (ArchLinux)
sudo systemctl start tor
torsocks curl https://ifconfig.me
mkdir onion && cd onion
# Save the index to your hard drive.
curl -L https://secretonions.neocities.org/index.html -o secret.html
curl -L https://davewebsite.neocities.org/index.html -o dave.html
torsocks w3m secret.html
sudo systemctl restart tor # To reroute Tor.
```

* [Tor: HiddenWiki](http://torwikijwqskahohtn35pyfde2uqmgrxgr2fru4mn4rer5muj445dxyd.onion/)
* [Tor: Daniel Tutoriales](http://danielas3rtn54uwmofdo3x2bsdifr47huasnmbgqzfrec5ubupvtpid.onion/tutorials/)
* [Tor: Email](http://j3bv7g27oramhbxxuv6gl3dcyfmf44qnvju3offdyrap7hurfprq74qd.onion/)
* [Tor: Email Sonar](http://sonarmsng5vzwqezlvtu2iiwwdn3dxkhotftikhowpfjuzg7p3ca5eid.onion/)
* [Tor: CIA](http://ciadotgov4sjwlzihbbgxnqg3xiyrg7so2r2o3lt5wz5ypk4sxyjstad.onion/)
* [Tor: Recommended F-DROID apps](http://jentyxddh2rf47gd3e43kuebyn2xsv6h72gzh46oe4rxyovvm7xe5ead.onion/fdroid.html)
* [Tor: WikiPage](http://uquroyobsaquslaunwkz6bmc3wutpzvwe7mv62xeq64645a57bugnsyd.onion/index.php)
* [Tor: Ahmia](http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion)
* [FreeNet: A la mierda copyright](http://127.0.0.1:8888/USK@NiPBeAA-PpA715zb8Jc~Q-ohFbKPt8Mo-YiH~w1D56A,--ZTBvgu7XMdX0QUJGBHp-Hogoh0AQK1p8WoY6IR80Q,AQACAAE/lawiki/5/)
