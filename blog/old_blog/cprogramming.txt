---
title: "C programming"
date: 2024-07-20T18:30:17-03:00
draft: true
---
#### definir booleano en C
agregá stdbool.h y podes usar la palabra clave bool o   
`typedef enum {false, true} bool;`  
o \_Bool es_soleado;  
o   
```c
#define false 0
#define true 0
typedef int bool; 
```

Cualquiera de las 3 funciona, \_Bool es la mas nueva forma de hacerlo desde C23.

#### abort()
```c
void cleanup(){
	printf("Doing cleanup!\n");
}
int main(void){
	atexit(cleanup);
	printf("Hello World!\n");
	abort();
	return 0;
}
```

#### valor absoluto
```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(void){
	int x = -5;
	int a = abs(x);
	double y = -2.5;
	double fabs_y = fabs(-2.5);
	printf("fabs(y): %f\n",fabs_y);
}
```


#### agrega numero de lineas a un archivo
Tenes que abrir dos archivos, tenes que definir el tamaño del archivo.
```c
#include <string.h>
#define FILENAME_SIZE 1024
#define MAX_LINE 2048
int main(int argc, char *argv[]){
	FILE *file, *temp;
	char *filename;

	char temp_filename[FILENAME_SIZE];
	char buffer[MAX_LINE];
	if (argc != 2){
		printf("Argument missing.\n");
		return 1;
	}
	else filename = argv[1];

	strcpy(temp_filename, "temp____");
	strcpy(temp_filename, filename);

	file = fopen(filename, "r");
	temp = fopen(temp_filename, "w");

	if(file == NULL || temp == NULL){
		printf("Error opening file.\n");
		return 1;
	}

	int current_line = 1;
	while(fgets(buffer, MAX_LINE, file) != NULL){
		fprintf(temp, "%d %s", current_line, buffer);
		current_line++;
	}
	fclose(temp);
	fclose(file);

	remove(filename);
	rename(temp_filename,filename);

	return 0;
}
```

#### Sumar dos enteros
```c
// Usa double no int
double number1, number2, sum;
scanf("%lf", &number1);
scanf("%lf", &number2);
sum = number1+number2;
printf("Sum: %f\n",sum);
```


#### Archivos
```c
#include <string.h>
#define MAX_LINE 1024

FILE *file;
file = fopen("file.txt", "a");
if (file == NULL)
{
printf("Error opening file.\n");
return 1;
}
while(1){
fgets(buffer, MAX_LINE, stdin);

// when the user enters quit, stop
if (strcmp(buffer, "quit\n") == 0)
break;
// write the buffer to the file
fputs(buffer, file);
}
fclose(file);
```

#### area de un circulo
```c
double radius = 0;
scanf("%lf", &radius);
double area = 3.141592 * radius * radius;
// Funcionamiento inesperado.
printf("%f + %f = %f", x,y,x/y);
```


#### Array average
```c
double arr4[] = {-50,50,-100,100,-2,2};

// call the average function to calculate the average, print the results
printf("arr1 avg: %.2lf\n", avg(arr1,5));

double avg(double array[], int length)
{
  // sum the array elements & divide the sum by the length (i.e. # of elements)
  double sum = 0;
  for (int i = 0; i < length; i++)
  {
    sum = sum + array[i];
  }
  return sum / length;
}
double es la máxima precisión
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```

#### 
```c
```


#### 
```c
```
