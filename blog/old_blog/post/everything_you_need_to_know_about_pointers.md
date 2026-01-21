---
title: "Everything you need to know about pointers"
date: 2023-10-10T16:23:49-03:00
tags: ['punteros','C','programacion']
---
```c
#include <stdio.h>
#include <stdlib.h>


struct {
	int ancho;
	int alto;
} typedef Rectangulo;

struct queseyo{
	char nombre[256];
	char apellido[256];
	char fecha_nacimiento[256];
	int dni;
} ;

/*	Esto define una estructura Rectangulo
**	struct {
**		int ancho;
**		int alto;
**	} Rectangulo;
**
*/

int main(){
	struct queseyo agenda;
	Rectangulo abc;

	Rectangulo prueba1;
	prueba1.ancho = 10;
	prueba1.alto = 20;
	printf("ancho: %d, alto: %d\n",prueba1.ancho,prueba1.alto);

	char * pointer_to_readonly_memory_string = "asdf";
	//char pointer_to_memory_on_the_stack = malloc(sizeof(char)*5);
	char pointer_to_memory_on_the_stack[] = "asdf";

	// pointer_to_readonly_memory_string[0] = 'b'; // segmentation fault
	pointer_to_memory_on_the_stack[0] = 'b';

	printf(" pointer_to_readonly_memory_string: %s\n", pointer_to_readonly_memory_string);
	printf(" pointer_to_memory_on_the_stack: %s\n", pointer_to_memory_on_the_stack);

	// *pointer = *(pointer+0) = pointer[0]

	// Equivalentes
	int *pointer = malloc(sizeof(int)*4);
	// int *pointer1 = malloc(sizeof(*pointer1)*4);
	// int pointer2[4];

	*pointer = 1;
	*(pointer+1) = 2;
	pointer[2]=3;
	*(pointer+3) = 4;
	*(pointer+4) = 5;

	for (int i=0; i<4; i++){
		pointer[i]=i;
	}

	// malloc te crea en la memoria un espacio de 5 caracteres 
	//char *hola = malloc(sizeof(char)*5);
	char *hola = malloc(sizeof(*hola)*5);

	// Todas estas expresiones son equivalentes
	*hola = 'h';
	hola[0] = 'h';
	*(hola+0) = 'h';


	*(hola+1) = 'o';
	*(hola+2) = 'l';
	*(hola+3) = 'a';
	*(hola+4) = '\0';
	sprintf(hola,"%s","chau");
	
	for (int i=0; i<4; i++){
		printf("pointer: %d\n",pointer[i]);
	}
	printf("pointer: %s\n",hola);
	free(pointer);
	free(hola);

	return 0;

}
```


### Invertir una lista enlazada
### [https://www.geeksforgeeks.org/reverse-a-linked-list/](https://www.geeksforgeeks.org/reverse-a-linked-list/)
### Invertir un árbol binario
### [https://www.geeksforgeeks.org/flip-binary-tree/](https://www.geeksforgeeks.org/flip-binary-tree/)

```c
void reverse(struct node** head_ref) {
    struct node* prev  = NULL;
    struct node* current = *head_ref;
    struct node* next;
    while (current != NULL) {
        next  = current->next;  
        current->next = prev;   
        prev = current;
        current = next;
    }
    *head_ref = prev;
}
```


#### [Ejercicios resueltos sobre Estructura de Datos en C](/files/pointers/estrategias.7z)
#### [Más ejercicios resueltos](/files/pointers/PracticaresueltaEDyA.zip)
