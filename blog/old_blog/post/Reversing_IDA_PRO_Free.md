---
title: "Reversing: IDA Free"
date: 2024-06-27T21:22:58-03:00
tags: ['reversing','ida']
---

Lo más importante es entender C,ASM y el concepto básico de un buffer overflow.


Ayer estaba jugando un poco con IDA PRO aprendiendo un poco de ASM.
[https://hex-rays.com/ida-free/](https://hex-rays.com/ida-free/)

Analicemos el siguiente código
#### C:
```c
int main(){
	return -1;
}
```

Este es el código que nos genera el IDA:
#### ASM: 
```asm
; Attributes: bp-based frame

; int __cdecl main(int argc, const char **argv, const char **envp)
public main
main proc near
; __unwind {
push    rbp ; Almacenar el registro RBP en la pila
mov     rbp, rsp ; Asigna a RBP el valor del registro apuntador RSP
mov     eax, 0FFFFFFFFh ; Mueve el -1 (escrito hexadecimal) al registro acumulador (eax).
pop     rbp ; Restauramos el valor inicial de RBP.
retn
; } // starts at 1129
main endp
_text ends
```

##### Siguiente código:
#### C: 
```c
int main()
{
	int a = 0;
	a=a+1;
	return 0;
}

```


El IDA nos genera:
#### ASM: 
```asm
; Attributes: bp-based frame

; int __cdecl main(int argc, const char **argv, const char **envp)
public main
main proc near

var_4= dword ptr -4

; __unwind {
push    rbp ; Almacenar el registro RBP en la pila
mov     rbp, rsp ; Asigna a RBP el valor del registro apuntador RSP
mov     [rbp+var_4], 0 ; Almacena el valor 0 en la dirección de memoria correspondiente a la variable local var_4 dentro del marco de pila (stack frame) actual.
; `var_4` es una variable local que se encuentra a un desplazamiento de `-0x4` bytes desde rbp, ya que el stack crece hacia abajo en memoria.
; `[rbp+var_4]` es un modo de direccionamiento que calcula la dirección de memoria sumando el contenido de rbp (inicio del stack frame) y el desplazamiento `var_4 (-0x4 bytes)`.

add     [rbp+var_4], 1 ; Toma el valor almacenado en la dirección de memoria correspondiente a la variable local `var_4` dentro de ese marco de la pila actual y suma 1 a ese valor.
mov     eax, 0 ; eax es un registro que se utiliza para manipular datos
pop     rbp ; Restauramos el valor inicial de RBP.
retn
; } // starts at 1129
main endp

_text ends
```

#### Siguiente código:
#### C: 
```c
int main()
{
	char *variable1 = "Hola";
	return 0;
}
```

#### ASM: 
```asm
; Attributes: bp-based frame

; int __cdecl main(int argc, const char **argv, const char **envp)
public main
main proc near

var_8= qword ptr -8

; __unwind {
push    rbp ; Almacenar el registro RBP en la pila
mov     rbp, rsp ; Asigna a RBP el valor del registro apuntador RSP
lea     rax, aHola      ; "Hola" ; Carga Hola en el registro rax.
mov     [rbp+var_8], rax ; Carga el contenido del registro rax(Hola) al registro rbp+var_8.
mov     eax, 0 ; Carga 0 al registro eax para el return 0
pop     rbp ; Restauramos el valor inicial de RBP.
retn
; } // starts at 1129
main endp

_text ends
```

#### Siguiente código:
### C 
```c
int main(){
	int i;
	for (i = 0; i<100;i++);
}
```

Código ASM generado por IDA:
![IDA PRO FOR](/img/for.png)

En la imagen debajo de la cajita llamada loc\_113A: se puede ver que compara el registro [rbp+var\_4] con 63h que en hexadecimal representa 99, con la instruccion jle (jump if less or equal) si es menor o igual salta a loc\_1136 y suma 1 al registro en donde está la variable i y vuelve a ejecutar loc\_113A, si no es mayor entonces carga 0 al registro eax restaura el valor inicial de RBP y llama a return.

```c
struct point{ 
	int x;
	int y;
};

int main(){
	struct point p1;
	p1.x = 10;
	p1.y = 20;

	printf("p1: (%d,%d)\n", p1.x, p1.y);
	return 0;
}
```

Luego de asignar las variables como una estructura, llegué a obtener el siguiente código en el ida:

{{< rawhtml >}}
<video width="630" height="300" src="/img/cracking/ida_struct.mp4" controls></video>
{{< /rawhtml >}}

---

Un simple if:    
```c
int main(void){
	int a=10, b=20;
	if (a>b) a=20;
	return 0;
}
```
#### IDA:
![if asm](/img/cracking/if.png)
