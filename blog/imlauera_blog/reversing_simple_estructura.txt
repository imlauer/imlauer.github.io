---
title: "Reversing: simple estructura en C"
date: 2025-01-04T19:18:02-03:00
tags: ['estructura']
---
```c
#include <stdio.h>

struct persona {
        char nombre[20];
        int edad;
        char telefono[60];
};

int main(void){
        struct persona persona1;
        printf("Tamaño de la estructura: %d\n",sizeof(persona1));
        // Esto no se puede hacer.
        printf("Ingrese su nombre: ");
        scanf("%s",persona1.nombre);
        printf("Ingrese su edad: ");
        scanf("%d",&persona1.edad);
        printf("Ingrese su telefono: ");
        scanf("%s",persona1.telefono);

        printf("Nombre: %s, Edad: %d, Teléfono: %s\n", persona1.nombre, persona1.edad, persona1.telefono);
        return 0;
}
```

--- 
#### Codigo generado por radare (r2 executable).

```asm
│           0x00001159      55             push rbp
│           0x0000115a      4889e5         mov rbp, rsp
│           0x0000115d      4883ec60       sub rsp, 0x60
│           0x00001161      64488b0425..   mov rax, qword fs:[0x28]
│           0x0000116a      488945f8       mov qword [canary], rax
│           0x0000116e      31c0           xor eax, eax
│           0x00001170      be54000000     mov esi, 0x54               ; 'T'
│           0x00001175      488d058c0e..   lea rax, str.Tamao_de_la_estructura:__d_n ; 0x2008 ; "Tama\u00f1o de la estructura: %d\n"
│           0x0000117c      4889c7         mov rdi, rax                ; const char *format
│           0x0000117f      b800000000     mov eax, 0
│           0x00001184      e8b7feffff     call sym.imp.printf         ; int printf(const char *format)
│           0x00001189      488d05960e..   lea rax, str.Ingrese_su_nombre: ; 0x2026 ; "Ingrese su nombre: "
│           0x00001190      4889c7         mov rdi, rax                ; const char *format
│           0x00001193      b800000000     mov eax, 0
│           0x00001198      e8a3feffff     call sym.imp.printf         ; int printf(const char *format)
│           0x0000119d      488d45a0       lea rax, [var_60h]
│           0x000011a1      4889c6         mov rsi, rax
│           0x000011a4      488d058f0e..   lea rax, [0x0000203a]       ; "%s"
│           0x000011ab      4889c7         mov rdi, rax                ; const char *format
│           0x000011ae      b800000000     mov eax, 0
│           0x000011b3      e898feffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│           0x000011b8      488d057e0e..   lea rax, str.Ingrese_su_edad: ; 0x203d ; "Ingrese su edad: "
│           0x000011bf      4889c7         mov rdi, rax                ; const char *format
│           0x000011c2      b800000000     mov eax, 0
│           0x000011c7      e874feffff     call sym.imp.printf         ; int printf(const char *format)
│           0x000011cc      488d45a0       lea rax, [var_60h]
│           0x000011d0      4883c014       add rax, 0x14
│           0x000011d4      4889c6         mov rsi, rax
│           0x000011d7      488d05710e..   lea rax, [0x0000204f]       ; "%d"
│           0x000011de      4889c7         mov rdi, rax                ; const char *format
│           0x000011e1      b800000000     mov eax, 0
│           0x000011e6      e865feffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│           0x000011eb      488d05600e..   lea rax, str.Ingrese_su_telefono: ; 0x2052 ; "Ingrese su telefono: "
│           0x000011f2      4889c7         mov rdi, rax                ; const char *format
│           0x000011f5      b800000000     mov eax, 0
│           0x000011fa      e841feffff     call sym.imp.printf         ; int printf(const char *format)
│           0x000011ff      488d45a0       lea rax, [var_60h]
│           0x00001203      4883c018       add rax, 0x18               ; "`\x10"
│           0x00001207      4889c6         mov rsi, rax
│           0x0000120a      488d05290e..   lea rax, [0x0000203a]       ; "%s"
│           0x00001211      4889c7         mov rdi, rax                ; const char *format
│           0x00001214      b800000000     mov eax, 0
│           0x00001219      e832feffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│           0x0000121e      8b55b4         mov edx, dword [var_4ch]
│           0x00001221      488d45a0       lea rax, [var_60h]
│           0x00001225      488d4818       lea rcx, [rax + 0x18]
│           0x00001229      488d45a0       lea rax, [var_60h]
│           0x0000122d      4889c6         mov rsi, rax
│           0x00001230      488d05310e..   lea rax, str.Nombre:__s__Edad:__d__Telfono:__s_n ; 0x2068 ; "Nombre: %s, Edad: %d, Tel\u00e9fono: %s\n"
│           0x00001237      4889c7         mov rdi, rax                ; const char *format
│           0x0000123a      b800000000     mov eax, 0
│           0x0000123f      e8fcfdffff     call sym.imp.printf         ; int printf(const char *format)
│           0x00001244      b800000000     mov eax, 0
│           0x00001249      488b55f8       mov rdx, qword [canary]
│           0x0000124d      64482b1425..   sub rdx, qword fs:[0x28]
│       ┌─< 0x00001256      7405           je 0x125d
│       │   0x00001258      e8d3fdffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
│       │   ; CODE XREF from sub.main_1159 @ 0x1256(x)
│       └─> 0x0000125d      c9             leave
└           0x0000125e      c3             ret

```



#### Explicación



Todos los registros que empiezan con r toman los primeros 64 bits, los que empiezan con e los primeros 32 bits, y si no tienen ninguno hacen referencia a los primeros 16 bits. Ejemplo: `rax(64 bits), eax(32 bits), AX(16 bits)`.

En este caso:

RDI: Es el primer argumento de una llamada a la función.   
RSI: Es el segundo argumento de una llamada a la función.   
RCX: Es el tercero argumento de una llamada a la función.   
RDX: Es el cuarto argumento de una llamada a la función.   

Luego tenemos r8 que es el 3er argumento y r9 que es el 4to argumento en muchos casos.


Por ejemplo acá tenemos un caso en donde no es así: en este caso rcx es el 1er argumento, ... y r9 es el 4to.
```asm
┌ 116: sub.fcn.1400012d0_1400012d0 (int64_t arg1, int64_t arg2, int64_t arg3, int64_t arg4);
│ `- args(rcx, rdx, r8, r9) vars(7:sp[0x8..0x50])
│           0x1400012d0      48894c2408     mov qword [var_8h], rcx    ; arg1
│           0x1400012d5      4889542410     mov qword [var_10h], rdx   ; arg2
│           0x1400012da      4c89442418     mov qword [var_18h], r8    ; arg3
│           0x1400012df      4c894c2420     mov qword [var_20h], r9    ; arg4
```

Es decir: printf("Nombre: %s, Edad: %d, Teléfono: %s\n", persona1.nombre, persona1.edad, persona1.telefono);

##### Sería:

RDI = "Nombre: %s, Edad: %d, Teléfono: %s\n"
RSI = persona1.nombre
RCX = persona1.edad
RDX = persona1.telefono

#### Pero acá como es una estructura usa la dirección de memoria del primer elemento y le suma un offset para llegar al segundo. Es decir por ejemplo para llegar al elemento edad, le suma 20 bytes al primer elemento (nombre).

Los demás argumentos se pasan por el stack a la pila.

Estas dos líneas están presentes en todos los programas, push "empuja" a la pila la dirección de la base de la pila. 

`mov` siempre copia del 2do argumento al 1ero.

```asm
push rbp
mov rbp, rsp
```

```asm
sub rsp, 0x60
```

Resta al puntero de la pila (stack pointer) 0x60 que son 96 bytes (la estructura tiene 20 bytes de nombre + 4 bytes de int + 60 bytes de teléfono = 84 bytes). **Es como que le pide espacio para las variables.**

```asm
mov rax, qword fs:[0x28]
mov qword [canary], rax
```

Esto es equivalente a:

```asm
mov qword [canary], qword fs:[0x28]
```

Pero en ASM siempre un argumento debe ser un registro no podés tener 2 variables.


`mov rax, qword fs:[0x28]` 

- `mov`: This is the instruction to move data.
- `rax`: This is the destination register, a 64-bit general-purpose register in the x86-64 architecture.
- `qword`: This indicates that the operation is dealing with a 64-bit (8-byte) value.- `fs:[0x28]`: This indicates that we are accessing memory at an offset of `0x28` from the base address stored in the `fs` segment register.

### Context:
In the x86-64 architecture, segment registers like `fs` (and `gs`) are typically used for special purposes. The `fs` register often points to a specific segment of memory, and in many modern operating systems, it is used to access thread-local storage (TLS) or other system-specific data.

In the case of `fs:[0x28]`, it's commonly used in the Windows kernel (or similar systems) to refer to a specific location in the thread information block (TIB). On Windows, for example, `fs:[0x28]` often holds the address of the thread's environment block (TEB).


```asm
xor eax, eax
```

```asm
mov esi, 0x54 
```
ESI es el 2do argumento pero los primeros 32 bits. En este caso carga 0x54 que son 84 bytes (el tamaño de la estructura).

lea rax, str.Tamao_de_la_estructura:__d_n ; 0x2008 ; "Tama\u00f1o de la estructura: %d\n"

`lea` es como el `mov`. Carga en el `rax` que es un registro acumulador la cadena: "Tamaño de la estructura: %d\n"


Luego del rax lo mueve al rdi: `mov rdi, rax` como dije anteriormente hace esto porque no se puede trabajar con 2 variables, siempre hay que un registro en cada mov.

rdi es el primer argumento del printf luego carga 0 al eax y llama al printf: 
```asm
mov eax, 0
call sym.imp.printf
```

Desde el siguiente código podemos asumir que `var_60h` es el puntero (es un puntero cuando tiene los corchetes `[var_60h]`) a la variable **nombre**. Lo carga al RSI es decir al segundo argumento de la función `scanf` y en el primer argumento carga: `"%s"`. Es deicr: `scanf("%s", &var_60h);`

```asm
│           0x0000119d      488d45a0       lea rax, [var_60h]
│           0x000011a1      4889c6         mov rsi, rax
│           0x000011a4      488d058f0e..   lea rax, [0x0000203a]       ; "%s"
│           0x000011ab      4889c7         mov rdi, rax                ; const char *format
│           0x000011ae      b800000000     mov eax, 0
│           0x000011b3      e898feffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
```

---

Acá hace algo similar: carga la dirección de memoria del comienzo de la cadena de caracteres al rax, y luego lo carga al rdi (el 1er argumento de la función) y llama a printf con ese argumento:

```asm
│           0x000011b8      488d057e0e..   lea rax, str.Ingrese_su_edad: ; 0x203d ; "Ingrese su edad: "
│           0x000011bf      4889c7         mov rdi, rax                ; const char *format
│           0x000011c2      b800000000     mov eax, 0
│           0x000011c7      e874feffff     call sym.imp.printf         ; int printf(const char *format)

```

scanf: Aca vemos algo importante, le suma 0x14 (20 bytes) al puntero al primer byte de nombre para llegar a edad que es el 2do elemento de la estructura: `add rax, 0x14`, y lo carga al rsi (2do argumento de la función). Luego carga "%d" que está ubicado en la dirección de memoria `0x0000204f` al rax, carga 0 al eax y llama a scanf.

```asm
│           0x000011cc      488d45a0       lea rax, [var_60h]
│           0x000011d0      4883c014       add rax, 0x14
│           0x000011d4      4889c6         mov rsi, rax
│           0x000011d7      488d05710e..   lea rax, [0x0000204f]       ; "%d"
│           0x000011de      4889c7         mov rdi, rax                ; const char *format
│           0x000011e1      b800000000     mov eax, 0
│           0x000011e6      e865feffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)

```

---

```asm
│           0x0000121e      8b55b4         mov edx, dword [var_4ch]
│           0x00001221      488d45a0       lea rax, [var_60h]
│           0x00001225      488d4818       lea rcx, [rax + 0x18]
│           0x00001229      488d45a0       lea rax, [var_60h]
│           0x0000122d      4889c6         mov rsi, rax
│           0x00001230      488d05310e..   lea rax, str.Nombre:__s__Edad:__d__Telfono:__s_n ; 0x2068 ; "Nombre: %s, Edad: %d, Tel\u00e9fono: %s\n"
│           0x00001237      4889c7         mov rdi, rax                ; const char *format
│           0x0000123a      b800000000     mov eax, 0
│           0x0000123f      e8fcfdffff     call sym.imp.printf         ; int printf(const char *format)
│           0x00001244      b800000000     mov eax, 0
```

Bool - 1 bit    
Byte - 1 Byte    
Word - 2 Byte - 16 bits    
Dword - 2 Word - 4 Bytes - 32 bits    

`var_4ch = telefono`, lo carga al edx que es el 4 argumento.

`var_60h = nombre persona (primer elemento de la estructura y es el 2do argumento porque lo carga al rsi)`

`rax + 0x18 = edad (2do elemento de la estructura y es el 3er argumento porque lo carga al rcx)` 

`str.Nombre:__s__Edad:__d__Telfono:__s_n ; 0x2068 ; "Nombre: %s, Edad: %d, Tel\u00e9fono: %s\n"` es el 1er argumento de la función `printf` porque lo carga al `rdi`.

---

Finalmente:

```asm
│           0x00001244      b800000000     mov eax, 0
│           0x00001249      488b55f8       mov rdx, qword [canary]
│           0x0000124d      64482b1425..   sub rdx, qword fs:[0x28]
│       ┌─< 0x00001256      7405           je 0x125d
│       │   0x00001258      e8d3fdffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
│       │   ; CODE XREF from sub.main_1159 @ 0x1256(x)
│       └─> 0x0000125d      c9             leave
└           0x0000125e      c3             ret
```
