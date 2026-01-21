---
title: "Reversing: Exámen 11 (Ricardo Narvaja)"
date: 2024-08-27T01:56:28-03:00
tags: ['reversing','cracking','ricardo','narvaja','examen','calculadora']
---
Los retos los hice usando vim con la siguiente configuracion:
```
" vim -b : edit binary using xxd-format!
augroup Binary
  au!
  au BufReadPre  *.bin let &bin=1
  au BufReadPost *.bin if &bin | %!xxd
  au BufReadPost *.bin set ft=xxd | endif
  au BufWritePre *.bin if &bin | %!xxd -r
  au BufWritePre *.bin endif
  au BufWritePost *.bin if &bin | %!xxd
  au BufWritePost *.bin set nomod | endif
augroup END

autocmd BufWritePost *.bin term ++close ++hidden cp % %:r.txt
```

### La segunda vez me generó un código muchísimo más entendible
Porque renombre el tipo de variable que tomaba check en vez de `int` lo puse como `char **` 
```c
int __cdecl check(int a1, char **a2)
{
  int i; // [esp+8h] [ebp-328h]
  char *v4[201]; // [esp+Ch] [ebp-324h] BYREF

  memset(v4, 0, 800u);
  for ( i = 0; i < a1; ++i )
  {
    v4[i] = malloc(228u);
    v4[i][54] = check;
    v4[i][55] = system;
    // strcpy copia hasta encontrar un caracter nulo (00 en hexa), acá no se produce overflow porque copias de un buffer de 200 a uno de 800
    strcpy(v4[i], a2[i]);
    // No queremos que pise el puntero a system con printf.
    v4[i][55] = printf;
    // Acá necesitamos copiar calc a v4[i]+200 (acá se produce el buffer overflow)
    strcpy(v4[i] + 200, a2[i]);
    // Acá necesitamos llamar a system(calc)
    v4[i][55](v4[i] + 200);
  }
  return printf("\nA repasarrrr ... \n");
}

int __cdecl main(int argc, const char **argv, const char **envp)
{
  FILE *v4; // [esp+4h] [ebp-3F8h]
  int v5; // [esp+8h] [ebp-3F4h]
  int i; // [esp+Ch] [ebp-3F0h]
  const char *v7[200]; // [esp+10h] [ebp-3ECh] BYREF
  char String[200]; // [esp+330h] [ebp-CCh] BYREF

  v4 = fopen("C:\\lista.txt", "rb");
  memset(String, 0, sizeof(String));
  if ( !v4 )
  {
    printf("No se puede leer la lista de alumnos bye bye \n");
    exit(1);
  }
  fread(String, 200u, 1u, v4);
  v7[0] = strtok(String, " ");
  if ( !v7[0] )
    exit(1);
  printf("nombre = %s\n", v7[0]);
  v5 = 1; for ( i = 1; i < 200; ++i )
  {
    // Esto sirve para pasar a la siguiente palabra separada por un espacio.
    v7[i] = strtok(0, " ");
    if ( !v7[i] )
      break;
    printf("nombre = %s\n", v7[i]);
    ++v5;
  }
  printf("cantidad de alumnos %d\n", v5);
  check(v5, v7);
  return 0;
}
```

Pero en la función check el decompilador no detectó el mensaje que decía "Aprobaste nivel 11", este mensaje si fue detectado por el decompilador de ghidra (aunque se puede ver en el gráfico del assembler en ida si accedés a la función check)

#### Este fue el código generado por ghidra
```c

void __cdecl check(int param_1,int param_2)

{
  char *pcVar1;
  int iVar2;
  int local_32c;
  char *local_328 [200];
  uint local_8;
  
  local_8 = DAT_10104004 ^ (uint)&stack0xfffffffc;
  iVar2 = 1;

  memset(local_328,0,800);
  for (local_32c = 0; local_32c < param_1; local_32c = local_32c + 1) {
    pcVar1 = (char *)operator_new(0xe4);
    local_328[local_32c] = pcVar1;
    *(code **)(local_328[local_32c] + 0xd8) = FUN_10101010;
    *(code **)(local_328[local_32c] + 0xdc) = system_exref;
    strcpy(local_328[local_32c],*(char **)(param_2 + local_32c * 4));
    *(code **)(local_328[local_32c] + 0xdc) = FUN_10101390;
    strcpy(local_328[local_32c] + 200,*(char **)(param_2 + local_32c * 4));
    (**(code **)(local_328[local_32c] + 0xdc))(local_328[local_32c] + 200);
  }
  if (iVar2 == 0) {
    printf("\nAprobaste Nivel 11\n",(char)iVar2);
  }
  else {
    printf("\nA repasarrrr ... \n",(char)iVar2);
  }
  @__security_check_cookie@4(local_8 ^ (uint)&stack0xfffffffc);
  return;
}


int main(void)

{
  FILE *_File;
  char *pcVar1;
  int iVar2;
  undefined in_stack_fffffc00;
  code *pcVar3;
  int local_3f8;
  int local_3f4;
  char *local_3f0 [200];
  char local_d0 [200];
  uint local_8;
  
  local_8 = DAT_10104004 ^ (uint)&stack0xfffffffc;
  _File = fopen("C:\\lista.txt","rb");
  memset(local_d0,0,200);
  if (_File == (FILE *)0x0) {
    printf("No se puede leer la lista de alumnos bye bye \n",in_stack_fffffc00);
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  fread(local_d0,200,1,_File);
  local_3f0[0] = strtok(local_d0," ");
  if (local_3f0[0] == (char *)0x0) {
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  printf("nombre = %s\n",(char)local_3f0[0]);
  local_3f8 = 1;
  for (local_3f4 = 1; local_3f4 < 200; local_3f4 = local_3f4 + 1) {
    pcVar1 = strtok((char *)0x0," ");
    local_3f0[local_3f4] = pcVar1;
    if (local_3f0[local_3f4] == (char *)0x0) break;
    printf("nombre = %s\n",(char)local_3f0[local_3f4]);
    local_3f8 = local_3f8 + 1;
  }
  pcVar3 = check;
  printf("cantidad de alumnos %d\n",(char)local_3f8);
  (*pcVar3)(local_3f8,local_3f0);
  iVar2 = @__security_check_cookie@4(local_8 ^ (uint)&stack0xfffffffc);
  return iVar2;
}

```

### Exploit (sin ejecutar la calculadora)
```
00000000: 6361 6c63 2063 616c 6320 4141 4141 4141  calc calc AAAAAA
00000010: 4141 4141 4141 4141 4141 4141 4141 5e11  AAAAAAAAAAAAAA^.
00000020: 1010 0000 0000 0000 0000 0000 0000 0000  ................
```

Saltamos a la dirección `1010115e` que es en donde está el mensaje "Aprobaste nivel 11"

Para ejecutar la calculadora tenés que usar un "gadget" y buscar un `call ecx` 
`Search > gadgets > search > control +f > call ecx` , hay un `call ecx` en `10102148`

El exploit de ricardo narvaja contiene `XXXXXXXX` al comienzo estos X's representan `POP EAX`

https://stackoverflow.com/questions/14349735/why-register-eax-esp-and-instructions-sub-push-and-pop-assemble-into-ascii-cha

O podés usar `rp++` o `ropper` en linux para buscar los gadgets.
