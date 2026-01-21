---
title: "BAUL de CRACKING: WINNER.zip"
date: 2024-09-09T17:37:00-03:00
---
BAUL: https://drive.google.com/file/d/1QRIk3zBGGXH54nSZorX3jnuNmURCHw6K/view?pli=1

Para iniciar el programa tenés que darle un número negativo como entrada. 

IDA
```c

#include <windows.h>
#include <defs.h>

#include <stdarg.h>


//-------------------------------------------------------------------------
// Function declarations

int sub_401020(FILE *Stream, wchar_t *Format, ...);
int vfwprintf(wchar_t *Format, ...);
int printf(char *Format, ...);
int scanf(char *Format, ...);
DWORD __stdcall StartAddress(FILE *const lpThreadParameter, const wchar_t *const Format, va_list ArgList);
int __cdecl main(int argc, const char **argv, const char **envp);
int __cdecl vfwprintf(FILE *const Stream, const wchar_t *const Format, va_list ArgList);
int sub_40142F();
int sub_401437();
int __cdecl UserMathErrorFunction();
int sub_4019E2();
void sub_4019EC();
char sub_4019F8();
// int __scrt_initialize_default_local_stdio_options(void); weak
BOOL sub_401A3C();
void *sub_401A48();
void *sub_401A4E();
LPTOP_LEVEL_EXCEPTION_FILTER sub_401BB6();
// LONG __stdcall __scrt_unhandled_exception_filter(struct _EXCEPTION_POINTERS *ExceptionInfo); idb
void sub_401C18();
void sub_401C20();
void __cdecl sub_401C4C(); // idb
// int __cdecl set_new_mode(int NewMode);

//-------------------------------------------------------------------------
// Data declarations

// extern BOOL (__stdcall *TlsSetValue)(DWORD dwTlsIndex, LPVOID lpTlsValue);
// extern DWORD (__stdcall *WaitForSingleObject)(HANDLE hHandle, DWORD dwMilliseconds);
// extern DWORD (__stdcall *GetCurrentThreadId)();
// extern void (__stdcall *Sleep)(DWORD dwMilliseconds);
// extern DWORD (__stdcall *GetLastError)();
// extern DWORD (__stdcall *TlsAlloc)();
// extern HANDLE (__stdcall *CreateThread)(LPSECURITY_ATTRIBUTES lpThreadAttributes, SIZE_T dwStackSize, LPTHREAD_START_ROUTINE lpStartAddress, LPVOID lpParameter, DWORD dwCreationFlags, LPDWORD lpThreadId);
// extern HLOCAL (__stdcall *LocalFree)(HLOCAL hMem);
// extern void (__stdcall __noreturn *ExitProcess)(UINT uExitCode);
// extern LPVOID (__stdcall *TlsGetValue)(DWORD dwTlsIndex);
// extern BOOL (__stdcall *TlsFree)(DWORD dwTlsIndex);
// extern void (__stdcall *InitializeSListHead)(PSLIST_HEADER ListHead);
// extern LPTOP_LEVEL_EXCEPTION_FILTER (__stdcall *SetUnhandledExceptionFilter)(LPTOP_LEVEL_EXCEPTION_FILTER lpTopLevelExceptionFilter);
// extern void (__cdecl __noreturn *exit)(int Code);
// extern FILE *(__cdecl *_acrt_iob_func)(unsigned int Ix);
int dword_40500C = 1; // weak
union _SLIST_HEADER ListHead; // idb
int dword_405360; // weak
DWORD dwTlsIndex; // idb
int dword_405374; // weak
LPVOID lpTlsValue; // idb
int dword_40537C; // weak
int ingresado_numero; // weak
_UNKNOWN unk_405384; // weak
_UNKNOWN unk_405398; // weak
_UNKNOWN unk_40539C; // weak


//----- (00401000) --------------------------------------------------------
void *sub_401000()
{
  return &unk_405390;
}

//----- (00401010) --------------------------------------------------------
void *sub_401010()
{
  return &unk_405388;
}

//----- (00401020) --------------------------------------------------------
int sub_401020(FILE *Stream, wchar_t *Format, ...)
{
  unsigned __int64 *v2; // eax
  va_list va; // [esp+10h] [ebp+10h] BYREF

  va_start(va, Format);
  v2 = sub_401000();
  return _stdio_common_vfwprintf_s(*v2, Stream, Format, 0, va);
}

//----- (00401050) --------------------------------------------------------
int sub_401050(wchar_t *Format, ...)
{
  unsigned __int64 *v1; // eax
  FILE *v3; // [esp-10h] [ebp-14h]
  va_list va; // [esp+10h] [ebp+Ch] BYREF

  va_start(va, Format);
  v3 = _acrt_iob_func(1u);
  v1 = sub_401000();
  return _stdio_common_vfwprintf(*v1, v3, Format, 0, va);
}
// 401000: using guessed type int sub_401000(void);

//----- (00401080) --------------------------------------------------------
int printf(char *Format, ...)
{
  unsigned __int64 *v1; // eax
  FILE *v3; // [esp-10h] [ebp-14h]
  va_list va; // [esp+10h] [ebp+Ch] BYREF

  va_start(va, Format);
  v3 = _acrt_iob_func(1u);
  v1 = sub_401000();
  return _stdio_common_vfprintf(*v1, v3, Format, 0, va);
}

//----- (004010B0) --------------------------------------------------------
int scanf(char *Format, ...)
{
  _DWORD *v1; // eax
  unsigned __int64 v3; // [esp-18h] [ebp-1Ch]
  FILE *v4; // [esp-10h] [ebp-14h]
  va_list va; // [esp+10h] [ebp+Ch] BYREF

  va_start(va, Format);
  v4 = _acrt_iob_func(0);
  v1 = sub_401010();
  HIDWORD(v3) = v1[1];
  LODWORD(v3) = *v1 | 1;
  return _stdio_common_vfscanf(v3, v4, Format, 0, va);
}

//----- (004010F0) --------------------------------------------------------
DWORD __stdcall StartAddress(FILE *const lpThreadParameter, const wchar_t *const Format, va_list ArgList)
{
  DWORD CurrentThreadId; // eax
  LPVOID v4; // eax
  void *Value; // eax
  DWORD v6; // eax
  void *v7; // eax
  void *v9; // [esp-4h] [ebp-4h]

  lpTlsValue = &dword_405374;

  dword_405374 = ingresado_numero ^ (dword_405374 + 5);

  dword_40537C = &unk_405384;
  CurrentThreadId = GetCurrentThreadId();
  vfwprintf(L"Creation: Current thread Id is % d : Its data pointer, lpvData = % lx\n", CurrentThreadId, &dword_405374);
  if ( !TlsSetValue(dwTlsIndex, lpTlsValue) )
    vfwprintf(lpThreadParameter, Format, ArgList);
  v4 = dword_40537C;
  if ( dword_405374 > 48 )
    v4 = lpTlsValue;
  dword_40537C = v4;
  Value = TlsGetValue(dwTlsIndex);
  lpTlsValue = Value;
  if ( !Value )
  {
    if ( GetLastError() )
      vfwprintf(lpThreadParameter, Format, ArgList);
    Value = lpTlsValue;
  }
  v9 = Value;
  v6 = GetCurrentThreadId();
  vfwprintf(L"common: Current thread Id is % d : Its data pointer, lpvData = % lx\n", v6, v9);
  Sleep(0x1388u);
  v7 = TlsGetValue(dwTlsIndex);
  lpTlsValue = v7;
  if ( v7 )
    LocalFree(v7);
  else
    vfwprintf(L"lpvData already freed!\n");
  return 0;
}
// 405374: using guessed type int dword_405374;
// 40537C: using guessed type int dword_40537C;
// 405380: using guessed type int ingresado_numero;

//----- (004011F0) --------------------------------------------------------
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int i; // esi
  HANDLE v4; // eax
  int j; // esi
  DWORD v6; // eax
  wchar_t *v7; // ecx
  FILE *v9; // [esp-8h] [ebp-4Ch]
  const wchar_t *v10; // [esp-4h] [ebp-48h]
  HANDLE hHandle[15]; // [esp+0h] [ebp-44h]
  DWORD ThreadId; // [esp+3Ch] [ebp-8h] BYREF

  printf("ENTER A NUMBER \n");
  scanf("%d", &ingresado_numero);
  dword_405374 += ingresado_numero;
  printf("ENTER ANOTHER NUMBER \n");
  scanf("%d", &ingresado_numero);
  if ( ingresado_numero < 5 )
    exit(1);
  dwTlsIndex = TlsAlloc();
  if ( dwTlsIndex == -1 )
    vfwprintf(hHandle[0], hHandle[1], hHandle[2]);
  vfwprintf(L"TlsAlloc() is OK!\n");
  for ( i = 0; i < 15; ++i )
  {
    v4 = CreateThread(0, 0, StartAddress, 0, 0, &ThreadId);
    hHandle[i] = v4;
    if ( !v4 )
      vfwprintf(v9, v10, hHandle[0]);
    vfwprintf(L"CreateThread() # % u is OK.Thread ID is % u\n", i, ThreadId);
  }
  for ( j = 0; j < 15; ++j )
  {
    v6 = WaitForSingleObject(hHandle[j], 0xFFFFFFFF);
    vfwprintf(L"The WaitForSingleObject() return value is 0X % .8x\n", v6);
  }
  if ( TlsFree(dwTlsIndex) )
    vfwprintf(L"The TLS index, dwTlsIndex was released!\n");
  v7 = L"\nTotal genious!\n";
  if ( dword_405374 != *dword_40537C + 67 )
    v7 = L"\nNopo :-( \n";
  vfwprintf(v7);
  return 0;
}
// 401336: variable 'v9' is possibly undefined
// 401336: variable 'v10' is possibly undefined
// 403494: using guessed type wchar_t aTotalGenious[17];
// 405374: using guessed type int dword_405374;
// 40537C: using guessed type int dword_40537C;
// 405380: using guessed type int ingresado_numero;

//----- (00401350) --------------------------------------------------------
int __cdecl __noreturn vfwprintf(FILE *const Stream, const wchar_t *const Format, va_list ArgList)
{
  int v3; // ecx
  FILE *v4; // eax
  int v5; // [esp-4h] [ebp-4h]

  v5 = v3;
  v4 = _acrt_iob_func(2u);
  sub_401020(v4, L" % s\n", v5);
  ExitProcess(0);
}
// 401350: variable 'v3' is possibly undefined

//----- (0040142F) --------------------------------------------------------
int sub_40142F()
{
  __scrt_initialize_default_local_stdio_options();
  return 0;
}
// 401A1F: using guessed type int __scrt_initialize_default_local_stdio_options(void);

//----- (00401437) --------------------------------------------------------
int sub_401437()
{
  int v0; // eax

  sub_401BB6();
  v0 = UserMathErrorFunction();
  return set_new_mode(v0);
}

//----- (004019DF) --------------------------------------------------------
int __cdecl UserMathErrorFunction()
{
  return 0;
}

//----- (004019E2) --------------------------------------------------------
int sub_4019E2()
{
  return 1;
}

//----- (004019EC) --------------------------------------------------------
void sub_4019EC()
{
  InitializeSListHead(&ListHead);
}

//----- (004019F8) --------------------------------------------------------
char sub_4019F8()
{
  return 1;
}

//----- (00401A3C) --------------------------------------------------------
BOOL sub_401A3C()
{
  return dword_40500C == 0;
}
// 40500C: using guessed type int dword_40500C;

//----- (00401A48) --------------------------------------------------------
void *sub_401A48()
{
  return &unk_40539C;
}

//----- (00401A4E) --------------------------------------------------------
void *sub_401A4E()
{
  return &unk_405398;
}

//----- (00401BB6) --------------------------------------------------------
LPTOP_LEVEL_EXCEPTION_FILTER sub_401BB6()
{
  return SetUnhandledExceptionFilter(__scrt_unhandled_exception_filter);
}

//----- (00401C18) --------------------------------------------------------
void sub_401C18()
{
  dword_405360 = 0;
}
// 405360: using guessed type int dword_405360;

//----- (00401C20) --------------------------------------------------------
void sub_401C20()
{
  ;
}
// 401C20: could not find valid save-restore pair for edi

//----- (00401C4C) --------------------------------------------------------
void __cdecl sub_401C4C()
{
  ;
}
// 401C4C: could not find valid save-restore pair for edi

// nfuncs=81 queued=22 decompiled=22 lumina nreq=0 worse=0 better=0
// ALL OK, 22 function(s) have been successfully decompiled
```

## Ghidra

hay un if que ida no me muestra.
`if (0xe < iVar6) {`


```c
void FUN_004011f0(void)

{
  code *pcVar1;
  HANDLE pvVar2;
  DWORD DVar3;
  BOOL BVar4;
  wchar_t *pwVar5;
  int iVar6;
  undefined1 unaff_DI;
  undefined uVar7;
  undefined in_stack_ffffffb8;
  DWORD local_c;
  uint local_8;
  
  local_8 = DAT_00405004 ^ (uint)&stack0xfffffffc;
  printf("ENTER A NUMBER \n",in_stack_ffffffb8);
  uVar7 = 0xe4;
  scanf("%d",(int *)&numero_ingresado);
  DAT_00405374 = DAT_00405374 + numero_ingresado;
  printf("ENTER ANOTHER NUMBER \n",uVar7);
  scanf("%d",(int *)&numero_ingresado);
  if (numero_ingresado < 5) {
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  DAT_00405370 = TlsAlloc();
  if (DAT_00405370 != 0xffffffff) {
    printf(L"TlsAlloc() is OK!\n",unaff_DI);
    iVar6 = 0;
    while( true ) {
      pvVar2 = CreateThread((LPSECURITY_ATTRIBUTES)0x0,0,(LPTHREAD_START_ROUTINE)&LAB_004010f0, (LPVOID)0x0,0,&local_c);

      *(HANDLE *)(&stack0xffffffb8 + iVar6 * 4) = pvVar2;
      if (pvVar2 == (HANDLE)0x0) break;
      printf(L"CreateThread() # % u is OK.Thread ID is % u\n",(char)iVar6);
      iVar6 = iVar6 + 1;
      if (0xe < iVar6) {
        iVar6 = 0;
        do {
          DVar3 = WaitForSingleObject(*(HANDLE *)(&stack0xffffffb8 + iVar6 * 4),0xffffffff);
          printf(L"The WaitForSingleObject() return value is 0X % .8x\n",(char)DVar3);
          iVar6 = iVar6 + 1;
        } while (iVar6 < 0xf);
        BVar4 = TlsFree(DAT_00405370);
        if (BVar4 != 0) {
          printf(L"The TLS index, dwTlsIndex was released!\n",in_stack_ffffffb8);
        }
        pwVar5 = L"\nTotal genious!\n";
        if (DAT_00405374 != *DAT_0040537c + 0x43) {
          pwVar5 = L"\nNopo :-( \n";
        }
        printf(pwVar5,in_stack_ffffffb8);
        @__security_check_cookie@4(local_8 ^ (uint)&stack0xfffffffc);
        return;
      }
    }
    FUN_00401350(L"CreateThread() error\n");
  }
  FUN_00401350(L"TlsAlloc() failed");
  pcVar1 = (code *)swi(3);
  (*pcVar1)();
  return;
}

```
