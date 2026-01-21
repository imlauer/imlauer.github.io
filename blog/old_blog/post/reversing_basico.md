---
title: "Reversing keygen con CPUID"
date: 2024-09-20T23:56:53-03:00
tags: ['reversing']
---

#### Cómo genera el serial:
```c
_EAX = 0;
__asm { cpuid }
resul = _EDX + _EAX + 69;
_EAX = 1;
__asm { cpuid }

__itoa_s(_ECX ^ _EDX ^ resul, my_serial, 0x64u, 16);
```

The cpuid instruction tells you various things about the CPU depending on the content of the eax register. When eax contains zero, the registers ebx, edx, and ecx contain a string describing the processor's vendor. The code you have pulls the string from the registers and prints it out.

https://en.wikipedia.org/wiki/CPUID

```c
#include <stdio.h>
#include <string.h>
int main()
{
	char name[13];
	 __asm
	{
		XOR EAX,EAX
		CPUID
		MOV dword ptr [name], EBX
		MOV dword ptr [name+4], EDX
		MOV dword ptr [name+8], ECX
	}
	name[12]=0;
	printf("Procesor: %s\n", name);
	getchar();
	return 0;
}
```


En GCC:
```c
#include <cpuid.h>
#include <stdio.h>
#include <stdlib.h>
#include <err.h>
#include <string.h>

// https://en.wikipedia.org/wiki/CPUID
// https://github.com/gcc-mirror/gcc/blob/master/gcc/config/i386/cpuid.h

void print_as_ASCII(unsigned int value) {
    for (int i = 0; i < 4; i++) {
        char byte = (value >> (i * 8)) & 0xFF; // Extract byte
        printf("%c", byte); // Print as ASCII character
    }
}

void call_cpuid(unsigned int EAX_input, unsigned int *eax, unsigned int *ebx, unsigned int *ecx, unsigned int *edx) {
        unsigned int ret;

        ret = __get_cpuid(EAX_input, eax, ebx, ecx, edx);
        if (ret != 1) {
                errx(EXIT_FAILURE, "Failed to call CPUID with EAX=%d", EAX_input);
        }
}

int main() {
        unsigned int eax, ebx, ecx, edx;

        // EAX=0: Highest Function Parameter and Manufacturer ID
        call_cpuid(0, &eax, &ebx, &ecx, &edx);

        printf("CPU Manufacturer ID: ");
        print_as_ASCII(ebx);
        print_as_ASCII(edx);
        print_as_ASCII(ecx);
        printf("\n");

        return 0;
}
```
