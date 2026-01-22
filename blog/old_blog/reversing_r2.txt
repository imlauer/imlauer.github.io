---
title: "Reversing con radare"
date: 2024-11-11T14:40:37-03:00
tags: ['r2']
---
```bash
r2 /bin/ls
aaa # analiza el binario
afl # Lista las funciones
s main # selecciona una función
# decompila
pdf # asm
pdd # r2ai
pdg # ghidra
```

Ejemplo: 
```c
// gcc bucle.c -o bucle
#include <stdio.h>

int main(){
        for (int i = 0; i < 100; i++) printf("i: %d\n",i);
        return 0;
}
```

Analizamos el binario con radare:
```c
r2 bucle
aaa
afl 
s main
pdf
```
---
Este es el código ASM generado por radare:

```asm
            ; DATA XREF from entry0 @ 0x1058(r)
┌ 59: int main (int argc, char **argv, char **envp);
│ afv: vars(1:sp[0xc..0xc])
│           0x00001139      55             push rbp  ; Inicializa la pila
│           0x0000113a      4889e5         mov rbp, rsp ; Carga rsp a la base de la pila (rbp).
│           0x0000113d      4883ec10       sub rsp, 0x10 ; 0x10 = 16 en hexadecimal. Crea 16 bits de espacio para las variables.
│           0x00001141      c745fc0000..   mov dword [var_4h], 0 ; Mueve 0 a var_4h
│       ┌─< 0x00001148      eb1d           jmp 0x1167 ; Salta a la dirección 0x1167
│       │   ; CODE XREF from main @ 0x116b(x)
│      ┌──> 0x0000114a      8b45fc         mov eax, dword [var_4h] ; Mueve el contenido de var_4h a eax
│      ■│   0x0000114d      89c6           mov esi, eax ; Mueve el eax a esi
│      ■│   0x0000114f      488d05ae0e..   lea rax, str.i:__d_n        ; 0x2004 ; "i: %d\n" ; Mueve la string a rax
│      ■│   0x00001156      4889c7         mov rdi, rax                ; const char *format - carga el rax a rdi
│      ■│   0x00001159      b800000000     mov eax, 0 ; carga 0 al eax
│      ■│   0x0000115e      e8cdfeffff     call sym.imp.printf         ; int printf(const char *format) - llama a printf
│      ■│   0x00001163      8345fc01       add dword [var_4h], 1 ; suma 1 al contenido de var_4h
│      ■│   ; CODE XREF from main @ 0x1148(x)
│      ■└─> 0x00001167      837dfc63       cmp dword [var_4h], 0x63    ; 'c' - Compara contenido 0x63 = 99 en hexadecimal con el contenido de var_4h que es inicializado en 0.
│      └──< 0x0000116b      7edd           jle 0x114a ; Salta si el contenido de var_4h es menor a 99.
│           0x0000116d      b800000000     mov eax, 0 # Mueve el 0 al eax.
│           0x00001172      c9             leave
└           0x00001173      c3             ret
```
---
Otro código en C:

```c
#include <stdio.h>

int main(){
        int datos[5];
        int suma = 0;

        for (int contador = 0; contador < 5; contador++){
                printf("Ingrese el dato número: %d\n",contador+1);
                scanf("%d",&datos[contador]);
                suma += datos[contador];
        }

        printf("La suma es %d\n",suma);
        printf("Su media es %4.2f\n", (float)suma/5);

        return 0;
}
``` 

Esto es lo que nos decompila radare en asm:

```asm
            ; DATA XREF from entry0 @ 0x1078(r)                                                                                                           08:43:14 [18/37]┌ 240: int main (int argc, char **argv, char **envp);
│ afv: vars(4:sp[0x10..0x30])
│           0x00001159      55             push rbp
│           0x0000115a      4889e5         mov rbp, rsp
│           0x0000115d      4883ec30       sub rsp, 0x30
│           0x00001161      64488b0425..   mov rax, qword fs:[0x28]
│           0x0000116a      488945f8       mov qword [canary], rax
│           0x0000116e      31c0           xor eax, eax
│           0x00001170      c745d80000..   mov dword [var_28h], 0
│           0x00001177      c745dc0000..   mov dword [var_24h], 0
│       ┌─< 0x0000117e      eb54           jmp 0x11d4
│       │   ; CODE XREF from main @ 0x11d8(x)
│      ┌──> 0x00001180      8b45dc         mov eax, dword [var_24h]
│      ?│   0x00001183      83c001         add eax, 1
│      ?│   0x00001186      89c6           mov esi, eax
│      ?│   0x00001188      488d05750e..   lea rax, str.Ingrese_el_dato_nmero:__d_n ; 0x2004 ; "Ingrese el dato n\u00famero: %d\n"
│      ?│   0x0000118f      4889c7         mov rdi, rax                ; const char *format
│      ?│   0x00001192      b800000000     mov eax, 0
│      ?│   0x00001197      e8a4feffff     call sym.imp.printf         ; int printf(const char *format)
│      ?│   0x0000119c      488d45e0       lea rax, [var_20h]
│      ?│   0x000011a0      8b55dc         mov edx, dword [var_24h]
│      ?│   0x000011a3      4863d2         movsxd rdx, edx
│      ?│   0x000011a6      48c1e202       shl rdx, 2
│      ?│   0x000011aa      4801d0         add rax, rdx
│      ?│   0x000011ad      4889c6         mov rsi, rax
│      ?│   0x000011b0      488d056a0e..   lea rax, [0x00002021]       ; "%d"
│      ?│   0x000011b7      4889c7         mov rdi, rax                ; const char *format
│      ?│   0x000011ba      b800000000     mov eax, 0
│      ?│   0x000011bf      e88cfeffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│      ?│   0x000011c4      8b45dc         mov eax, dword [var_24h]
│      ?│   0x000011c7      4898           cdqe
│      ?│   0x000011c9      8b4485e0       mov eax, dword [rbp + rax*4 - 0x20]
│      ?│   0x000011cd      0145d8         add dword [var_28h], eax
│      ?│   0x000011d0      8345dc01       add dword [var_24h], 1
│      ?│   ; CODE XREF from main @ 0x117e(x)
│      ?└─> 0x000011d4      837ddc04       cmp dword [var_24h], 4
│      └──< 0x000011d8      7ea6           jle 0x1180
│           0x000011da      8b45d8         mov eax, dword [var_28h]
│           0x000011dd      89c6           mov esi, eax
│           0x000011df      488d053e0e..   lea rax, str.La_suma_es__d_n ; 0x2024 ; "La suma es %d\n"
│           0x000011e6      4889c7         mov rdi, rax                ; const char *format
│           0x000011e9      b800000000     mov eax, 0
│           0x000011ee      e84dfeffff     call sym.imp.printf         ; int printf(const char *format)
│           0x000011f3      660fefc0       pxor xmm0, xmm0
│           0x000011f7      f30f2a45d8     cvtsi2ss xmm0, dword [var_28h]
│           0x000011fc      f30f100d44..   movss xmm1, dword [0x00002048] ; [0x2048:4]=0x40a00000 Esto es un puntero a la dirección 0x2048 en donde está alojado el 5. Carga el 5 a xmm1
│           0x00001204      f30f5ec1       divss xmm0, xmm1 ; Acá divide la sumatoria que está en xmm0 con 5 que está alojado en xmm1. (sym.imp.printf(iVar1 / *0x2048, "Su media es %4.2f\n");)
│           0x00001208      660fefd2       pxor xmm2, xmm2
│           0x0000120c      f30f5ad0       cvtss2sd xmm2, xmm0
│           0x00001210      66480f7ed0     movq rax, xmm2
│           0x00001215      66480f6ec0     movq xmm0, rax
│           0x0000121a      488d05120e..   lea rax, str.Su_media_es__4.2f_n ; 0x2033 ; "Su media es %4.2f\n"
│           0x00001221      4889c7         mov rdi, rax                ; const char *format
│           0x00001224      b801000000     mov eax, 1
│           0x00001229      e812feffff     call sym.imp.printf         ; int printf(const char *format)
│           0x0000122e      b800000000     mov eax, 0
│           0x00001233      488b55f8       mov rdx, qword [canary]
│           0x00001237      64482b1425..   sub rdx, qword fs:[0x28]
│       ┌─< 0x00001240      7405           je 0x1247
│       │   0x00001242      e8e9fdffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
│       │   ; CODE XREF from main @ 0x1240(x)
│       └─> 0x00001247      c9             leave
└           0x00001248      c3             ret

```

Listar variables: `afv`.

```console
[0x00001159]> afv
var int64_t canary @ rbp-0x8
var int64_t var_20h @ rbp-0x20
var signed int64_t var_24h @ rbp-0x24
var int64_t var_28h @ rbp-0x28
[0x00001159]>
```

Renombrar variables:

```console
afvn contador var_20h
afvn sumatoria var_28h
```

### Como sé que en  `*0x2048` hay un 5?
