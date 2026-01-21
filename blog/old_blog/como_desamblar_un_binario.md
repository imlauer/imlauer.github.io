---
title: "Reversing: Diferentes formas de desarmar un binario"
date: 2025-01-22T06:15:44-03:00
tags: ['reversing']
---
```bash
objdump -drwC -Mintel -d p
```

Podes fijar un alias en `.bashrc` o `.config/fish/config.fish`:   
```bash
disas='objdump -drwC -Mintel' (-w is no line-wrapping, -c is demangle, -r prints relocations in object files.)
```

Otras formas:
1. `llvm-objdump -drwC -Mintel`
2. `ndisasm`
3. 
```bash
gdb -q ./a.out

disassemble main
disassemble /m main
```

##### Agner Fog's disassembler: objconv

### Para generar archivo ASM usando sintaxis intel: `gcc p.c -c -S -masm=intel`

Otras alternativas: IDA, Ghidra, radare.


