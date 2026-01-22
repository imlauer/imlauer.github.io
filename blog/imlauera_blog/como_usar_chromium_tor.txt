---
title: "Como usar chromium con tor"
date: 2024-10-14T04:02:40-03:00
tags: ['chrome','tor']
---
```bash
sudo apt install -y tor
tor
chromium --proxy-server="socks5://localhost:9050"
```
