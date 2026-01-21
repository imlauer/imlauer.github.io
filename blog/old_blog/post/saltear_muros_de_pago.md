---
title: "Saltear muros de pago (Bypass paywalls)"
date: 2024-09-22T17:09:32-03:00
tags: ['bypass','paywall']
---

Lo borraron porque tienen miedo de que se haga tan famoso como los bloqueadores de publicidad:
https://github.com/bpc-clone/bpc_updates/releases/latest

backup firefox: https://archive.org/details/bypass-paywalls-firefox-clean-master3

backup chrome: https://archive.softwareheritage.org/browse/origin/directory/?origin_url=https://gitlab.com/magnolia1234/bypass-paywalls-chrome-clean.git

backup chrome mío: https://archive.org/details/bypass-paywalls-chrome-clean

Descargá el archivo de release y cargalo como extensión en chrome (habilitá developer mode)

https://old.reddit.com/r/Piracy/comments/180u498/how_to_bypass_any_paywall/?rdt=44346

Archive por si las dudas también lo borran: https://archive.is/RJhS9

Si instalás la extensión te aparecerá arriba de todo unos links en rojo así:
![bypass paywall](/img/bypass_paywalll.png)

Cualquiera de ellos funciona

#### Servicios con los que podés intentar 

https://12ft.io This is currently the most commonly used tool, with tens of millions of visitors per month. It claims that it only fetches without javascript (it uses a proxy so it fetches for you, the request isn't made from your browser), but I'm pretty sure it uses Googlebot, and maybe some other methods as well, although not directly stated. Got banned from its hosting provider recently, but is back up.  
https://removepaywall.com  This site does many things: it first tries to fetch from Wayback Machine (archive.org) and then with Google cache. Then it tries a direct fetch with Googlebot user agent. It claims it also tries archive.is, but redirects users to archive.is when it fails. In general, this might be the most robust solution I've seen.  
https://smry.ai Shameless self-plug (mods were made aware). Does everything removepaywall.com does, is completely open-source, and also generates free summaries of each article until I run out of money. Also, tells you where the content was fetched from and lets you try different options.  
1ft.io. This one is new and has blown up quickly because it is fast. From what I can guess, it just uses Googlebot. which is why it is so fast (fetching from Wayback Machine or Google cache would be slower). But it also fails a lot. Good quick solution to try before moving on to other more robust methods.  
https://darkread.com Read in dark mode. Nuff said.  
https://leiaisso.net Very popular in Brazil. Pretty buggy for me.  
