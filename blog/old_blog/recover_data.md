---
title: "Como recuperar particion: Formatee una partición de ext4 como swap por accidente."
date: 2025-04-18T09:24:49-03:00
tags: ['data','recovery']
---
Formatee una partición de ext4 como swap accidentalmente. Que capo.

ChatGPT me dió respuestas boludas durante 1 hora estuve boludiando con eso. El 1er resultado de Google me dió la respuesta.

```bash
sudo blkid /dev/sda5

/dev/sda5: UUID="ddebee74-bcb2-45ce-86e5-0d79bb0bf80f" TYPE="swap" PARTUUID="093b9d2d-69d3-4eed-beeb-f6276b63faae"
```

https://old.reddit.com/r/linuxquestions/comments/k9m61h/accidentally_ran_mkswap_on_ext4_partition/


```bash
sudo dumpe2fs -h -o superblock=8193 /dev/sde2
```

If 8193 doesn't work, try 32768. (There's a bit of complicated logic to determine where alternate superblocks might live. Hopefully one of these two will work on your filesystem.)

```bash
sudo e2fsck -b 8193 /dev/sde2
```
