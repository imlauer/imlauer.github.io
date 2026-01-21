---
title: "Cómo usar errno en C"
date: 2025-02-06T23:48:17-03:00
tags: ['c']
---
```c
#include <errno.h>
#include <string.h>

/* ... */

if(read(fd, buf, 1)==-1) {
    printf("Oh dear, something went wrong with read()! %s\n", strerror(errno));
}

```
