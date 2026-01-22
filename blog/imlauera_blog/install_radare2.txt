---
title: "Instalación radare2"
date: 2024-11-07T03:46:26-03:00
tags: ['radare']
---
```bash
git clone https://github.com/radareorg/radare2
radare2/sys/install.sh
```

## Usage

These are the first steps to use r2, read the book or find tutorials for more details
```sh
$ r2 /bin/ls   # open file in read-only
> aaa          # analyse the program (r2 -A)
> afl          # list all functions (try aflt, aflm)
> px 32        # print 32 byte hexdump current block
> s sym.main   # seek to main (using flag name)
> f~foo        # filter flags matching 'foo' (internal |grep)
> iS;is        # list sections and symbols (rabin2 -Ss)
> pdf; agf     # disassembly and ascii-art function graph
> oo+;w hello  # reopen in read-write and write a string
> ?*~...       # interactive filter in all command help
> q            # quit
```

Many plugins are included in r2 by default. But you can extend its capabilities
by using the [r2pm](https://github.com/radareorg/radare2-pm) package manager.

```sh
r2pm -s <word>  # search packages matching a word
r2pm -Uci <pkg> # update database and clean install a package
r2pm -u <pkg>   # uninstall the given package
r2pm -l <pkg>   # list installed packages
```

Ejemplo: 
```bash
r2pm -Uci r2ghidra
r2pm -i r2ai
```

pdg (ghidra)
pdd (ai decompiler)
