---
title: "Makefile: Compilar todos los archivos de C de una."
date: 2025-02-27T00:46:28-03:00
tags: ['c']
---
```makefile
LIBS  = -lkernel32 -luser32 -lgdi32 -lopengl32
CFLAGS = -Wall 

# Should be equivalent to your list of C files, if you don't build selectively
SRC=$(wildcard *.c)

test: $(SRC)
    gcc -o $@ $^ $(CFLAGS) $(LIBS)
```
---
**Otra forma**:

```bash
SRCS=$(wildcard *.c)

OBJS=$(SRCS:.c=.o)

all: $(OBJS)
```

**Compilar main.c y ejecutarlo**:
```makefile
main: main.c
	gcc -Wall -Wextra -o main  main.c
	./main
```
