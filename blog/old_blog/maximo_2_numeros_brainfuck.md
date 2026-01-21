---
title: "Maximo entre 2 numeros en brainfuck"
date: 2025-11-04T06:44:20-03:00
tags: ['programming']
---
Cogida de cerebro.

Brainfuck es un lenguaje de programación esotérico que no contiene palabras, está muy cerca a ASM, más cerca que C.

#### Instalación

```bash
yay -S brainfuck
yay -Ql brainfuck
```

To find the maximum between two numbers in Brainfuck, you can use a simple comparison algorithm. Brainfuck is a minimalist language with only eight commands, so the code will be quite straightforward but might look unusual compared to more conventional programming languages.

Here's a basic approach to find the maximum of two numbers, let's say `a` and `b`, stored in the first two cells of the tape:

```brainfuck
,>,              # Read two numbers from input into the first two cells
[<-<->>]>        # If the first cell is not zero, proceed to compare
<[-<+>]<         # Move the value from the first cell to the third cell if it's not zero
>[>-<-]>         # Move the value from the second cell to the first cell if the first cell is zero
<.               # Output the value in the first cell, which should be the maximum
```

Explanation:
1. `,>,` reads two characters (numbers) from the input and stores them in the first two cells of the tape. Note that Brainfuck reads input as ASCII values, so the numbers should be input as their ASCII representations (e.g., '1' for the number 1).
2. `[<-<->>]>` checks if the first cell is not zero. If it's not zero, the program proceeds inside the loop.
3. `<[-<+>]<` moves the value from the first cell to the third cell if the first cell is not zero. This effectively prepares to compare or swap values based on their magnitudes.
4. `>[>-<-]>` moves the value from the second cell to the first cell if the first cell becomes zero (indicating the second cell holds a larger value or they are equal).
5. `<.` outputs the value in the first cell, which, after the comparison and potential swap, should be the maximum of the two input values.

However, this explanation simplifies the process. The actual implementation to correctly compare and output the maximum of two numbers in Brainfuck, considering its unique instruction set, involves a bit more complexity, especially when dealing with negative numbers or ensuring the comparison works as expected in all cases.

A more accurate and functional approach would involve a direct comparison and swap if necessary. Here's a corrected and simplified version of how you might approach finding the maximum, assuming you're working with non-negative integers and focusing on the basic concept:

```brainfuck
,>,            # Read two numbers
<[->>]<        # If first cell is less than second, swap
>[<-]>         # If first cell is greater or equal, do nothing (first cell already max)
<.             # Print the first cell, which should be the max
```

This version directly compares the two values and swaps them if the first is less than the second, ensuring the first cell always holds the maximum value after the comparison.

Keep in mind, Brainfuck programming can be very low-level and requires careful management of the tape and its values. This example assumes a basic understanding of Brainfuck's operation and is simplified for educational purposes.


**Introduction to Brainfuck**
==========================

Brainfuck is a minimalist programming language designed by Urban Müller in 1993. It is a Turing complete language, meaning it can simulate the behavior of any other Turing complete language. Brainfuck is known for its simplicity and obscurity, making it a challenging language to learn and use.

**Syntax and Commands**
----------------------

Brainfuck has a very simple syntax, consisting of only eight commands:

* `+` : Increment the current cell by 1
* `-` : Decrement the current cell by 1
* `>` : Move the pointer to the right by 1 cell
* `<` : Move the pointer to the left by 1 cell
* `.` : Output the value of the current cell as a character
* `,` : Input a character and store its ASCII value in the current cell
* `[` : If the current cell is 0, jump to the corresponding `]`
* `]` : If the current cell is not 0, jump back to the corresponding `[`


```bash
+-----------------------------------------------------------------------------+
| `+` : Incrementá la celda actual a 1.                                       |
| `-` : Decrementá la celda actual a 1.                                       |
| `>` : Mueve el puntero a la derecha 1 celda.                                |
| `<` : Mueve el puntero a la izquierda 1 celda.                              |
| `.` : Muestra el valor de la celda actual como carácter.                    |
| `,` : Ingresa un caracter y lo guarda como valor ASCII en la celda actual   |
| `[` : Si la celda actual es 0, salta a la correspondiente celda ']'         |
| `]` : Si la celda actual no es 0, salta atrás a la correspondiente celda '['|
+-----------------------------------------------------------------------------+
```









**Basic Example**
-----------------

Here is a simple "Hello World" program in Brainfuck:
```brainfuck
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.
```
This program uses a loop to increment the first cell to 8, then uses another loop to increment the next cells to the ASCII values of the characters in "Hello World". Finally, it outputs the characters using the `.` command.

**Step-by-Step Guide**
---------------------

To write a Brainfuck program, follow these steps:

1. **Initialize the tape**: Brainfuck uses an array of cells, each initialized to 0. You can think of the tape as a long row of boxes, where each box can hold a value between 0 and 255.
2. **Move the pointer**: Use the `>` and `<` commands to move the pointer to the desired cell.
3. **Increment or decrement**: Use the `+` and `-` commands to change the value of the current cell.
4. **Output or input**: Use the `.` and `,` commands to output or input characters.
5. **Loop**: Use the `[` and `]` commands to create loops that repeat until the current cell is 0.

**Tips and Tricks**
-------------------

* **Use a Brainfuck interpreter**: There are many online interpreters and compilers available that can help you run and debug your Brainfuck programs.
* **Use a text editor**: Write your Brainfuck programs in a text editor, and use a syntax highlighter to make the code more readable.
* **Start with simple programs**: Begin with simple programs that output a single character or perform basic arithmetic operations.
* **Use comments**: Although Brainfuck does not have a built-in commenting system, you can use comments in your code to explain what each section does.

**Example Use Cases**
--------------------

* **Printing a string**: Use a loop to output a string of characters.
* **Performing arithmetic**: Use the `+` and `-` commands to perform basic arithmetic operations.
* **Reading input**: Use the `,` command to read input from the user.

**Conclusion**
----------

Brainfuck is a challenging but rewarding language to learn. With practice and patience, you can master the basics of Brainfuck and create complex programs. Remember to use online resources and interpreters to help you learn and debug your code. Happy coding!

```
;  Ejercicio: Tomá un número, sumale 3 al número e imprimilo.
;  `+` : Incrementa la celda actual por 1.
;  `-` : Decrementa la celda actual por 1.
;  `>` : Mueve el puntero 1 celda a la derecha.
;  `<` : Mueve el puntero 1 celda a la izquierda.
;  `.` : Muestra la salida del valor de la celda actual como caracter.
;  `,` : Entrada de un caracter y guarda su valor como ASCII en la celda actual.
;  `[` : Si la celda actual es 0, salta a la celda correspondiente ']'
;  `]` : Si la celda actual no es 0, salta de regreso a la celda correspondiente '['

,>,+++.
```


#### Implementacion de un interpretador de BrainFuck en C:

```c 
#include <stdio.h>

const char program[] = ",[.-]"; // your program here

#define CELLS 30000
char tape[CELLS];

int main(void)
{
  unsigned int cell = 0;
  const char *i = program;
  int bDir, bCount;

  while (*i != 0)
  {
    switch (*i)
    {
      case '>': cell++; break;
      case '<': cell--; break;
      case '+': tape[cell]++; break;
      case '-': tape[cell]--; break;
      case '.': putchar(tape[cell]); fflush(stdout); break;
      case ',': scanf("%c",tape + cell); break;
      case '[':
      case ']':
        if ((tape[cell] == 0) == (*i == ']'))
          break;

        bDir = (*i == '[') ? 1 : -1;
        bCount = 0;

        while (1)
        {
          if (*i == '[')
            bCount += bDir;
          else if (*i == ']')
            bCount -= bDir;

          if (bCount == 0)
            break;

          i += bDir;
        }

        break;

      default: break;
    }

    i++;
  }

  return 0;
}

```
