---
title: "Prevenir bufferoverflow scanf"
date: 2025-01-24T16:51:13-03:00
tags: ['hacking']
---

```c
while ( scanf("%20s", buf) == 1 ){
```

---

```c
int scanner(const char *data, char *buffer, size_t buflen)
{
    char format[32];
    if (buflen == 0)
        return 0;
    snprintf(format, sizeof(format), "%%%ds", (int)(buflen-1));
    return sscanf(data, format, buffer);
}
```

#### Desactivar la protección contra buffer overflow:
```bash
gcc letssee.c -o letssee -fno-stack-protector
```

#### Disable ASLR:

sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'

