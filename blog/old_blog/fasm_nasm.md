---
title: "Fasm y nasm"
date: 2025-01-28T03:22:26-03:00
tags: ['asm']
---

Here is how registers look conceptually

  · rax is the 64-bit, “long" size register. It was added in 2003 during the
    transition to 64-bit processors.
  · eax is the 32-bit, “int" size register. It was added in 1985 during the
    transition to 32-bit processors with the 80386 CPU.
  · ax is the 16-bit, “short" size register. It was added in 1979 with the 8086 CPU,
    but is used in DOS or BIOS code to this day.
  · al and ah are the 8-bit, “char" size registers. al is the low 8 bits, ah is the
    high 8 bits. They're pretty similar to the old 8-bit registers of the 8008 back
    in 1972.

```console
| Name |                                             Notes                                              |   Type    | 64-bit long | 32-bit int |
|------|------------------------------------------------------------------------------------------------|-----------|-------------|------------|
| rax  | Value returned from functions in this register                                                 | scratch   | rax         | eax        |
| rcx  | Typical scratch register. Some instruction also use it as counter                              | scratch   | rcx         | ecx        |
| rdx  | Scratch regiser                                                                                | scratch   | rdx         | edx        |
| rbx  | Preserved register: don't use it without saving it                                             | preserved | rbx         | ebx        |
| rsp  | The stack register: Points to top of stack                                                     | preserved | rsp         | esp        |
| rbp  | Preserved register: Sometimes used to store the old value of the stack pointer, or the "base". | preserved | rbp         | ebp        |
| rsi  | Scratch regiser. Also used to pass argument #2 in 64-bit linux                                 | scratch   | rsi         | esi        |
| rdi  | Scratch regiser. Function argument #1 in 64-bit Linux                                          | scratch   | rdi         | edi        |
| r8   | Scratch register.  These were added in 64-bit mode, so they have numbers, not names.           | scratch   | r8          | r8d        |
| r9   | Scratch register.                                                                              | scratch   | r9          | r9d        |
| r10  | Scratch register.                                                                              | scratch   | r10         | r10d       |
| r11  | Scratch register.                                                                              | scratch   | r11         | r11d       |
| r12  | Preserved register.  You can use it, but you need to save and restore it.                      | preserved | r12         | r12d       |
| r13  | Preserved register.                                                                            | scratch   | r13         | r13d       |
| r14  | Preserved register.                                                                            | scratch   | r14         | r14d       |
| r15  | Preserved register.                                                                            | scratch   | r15         | r15d       |

```


#### Hello World - Linux 64 bits:

```asm
; fasm hello.asm
; file: hello.asm
; comment starts with semi-colon here
format ELF64 executable 3 ; defines that it will a ELF64 type executable

entry start               ; defines which address to look for when program starts

segment readable executable
start:
    mov rdi, 1 ; write(1, "Hola")
    mov rsi, msg ; rsi es el 2do argumento de write.
    mov rdx, 4 ; Longitud del mensaje
    mov rax, 1 ; stdout
    syscall               ; do syscall for code defined in rax here it is exit

    xor rdi, rdi ; Pongo en 0 rdi.
    mov rax, 60 ; exit
    syscall

segment readable writable
msg db 'Hola', 4, 0
```

##### Como usar system calls en C: 
https://jameshfisher.com/2018/02/19/how-to-syscall-in-c/

