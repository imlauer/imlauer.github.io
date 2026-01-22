---
title: "Subir archivo desde la terminal"
date: 2024-08-10T18:25:47-03:00
tags: ['hacking','upload','files']
---

```
wget --quiet -O- --post-file=append_input_to_file.c 'https://paste.c-net.org/'
curl --silent --data-binary @append_input.c https://paste.c-net.org
```

