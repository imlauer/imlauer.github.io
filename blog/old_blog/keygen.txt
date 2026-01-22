---
title: "Keygen si puedes"
date: 2024-09-09T06:41:05-03:00
tags: ['reversing','ida']
---

El keygen se encuentra en: https://drive.google.com/file/d/1QRIk3zBGGXH54nSZorX3jnuNmURCHw6K/view?pli=1

El código que me generó el ida es:
```c

#include <windows.h>
#include <defs.h>

#include <stdarg.h>


//-------------------------------------------------------------------------
// Function declarations

void __fastcall _mingw_invalidParameterHandler(const wchar_t *expression, const wchar_t *function, const wchar_t *file, unsigned int line, uintptr_t pReserved);
int __cdecl pre_c_init();
void __cdecl pre_cpp_init();
// int __cdecl _tmainCRTStartup();
// int __cdecl WinMainCRTStartup();
int __cdecl mainCRTStartup();
char *__fastcall generaLetras(int a1, char *a2);
__int64 __fastcall generaNumero(char *a1); // idb
int __fastcall generaSerial(char *a1, char *a2);
int __fastcall checkSerial(char *a1, char *a2);
INT_PTR __fastcall DialogProc(HWND a1, int a2, unsigned __int16 a3);
int __stdcall WinMain(HINSTANCE hInst, HINSTANCE hPreInst, LPSTR lpszCmdLine, int nCmdShow);
void *__fastcall decode_pointer(void *codedptr);
void *__fastcall encode_pointer(void *ptr);
int __cdecl setargv();
void __fastcall _mingw_raise_matherr(int typ, const char *name, double a3, double a1, double rslt);
void __fastcall _mingw_setusermatherr(int (*f)(_exception *));
int __fastcall matherr(_exception *pexcept);
void _report_error(const char *msg, ...);
void __fastcall _write_memory_part_0(void *addr, const void *src, size_t len);
void __cdecl pei386_runtime_relocator();
int __fastcall _mingw_SEH_error_handler(_EXCEPTION_RECORD *ExceptionRecord, void *EstablisherFrame, _CONTEXT *ContextRecord, void *DispatcherContext);
int __cdecl _mingw_init_ehandler();
int __fastcall gnu_exception_handler(EXCEPTION_POINTERS *exception_data);
void __cdecl fpreset();
void __cdecl _do_global_dtors();
void __cdecl _do_global_ctors();
void __cdecl _main();
void __cdecl _security_init_cookie();
void __fastcall _report_gsfailure(ULONG_PTR StackCookie);
BOOL __fastcall _dyn_tls_dtor(HANDLE hDllHandle, DWORD dwReason, LPVOID lpreserved);
BOOL __fastcall _dyn_tls_init(HANDLE hDllHandle, DWORD dwReason, LPVOID lpreserved);
int __fastcall _tlregdtor(_PVFV func);
_onexit_t __fastcall mingw_onexit(_onexit_t func);
int __fastcall atexit(_PVFV func);
int __cdecl my_lconv_init();
WINBOOL __fastcall ValidateImageBase_part_0(PBYTE pImageBase);
WINBOOL __fastcall ValidateImageBase(PBYTE pImageBase);
PIMAGE_SECTION_HEADER __fastcall FindPESection(PBYTE pImageBase, DWORD_PTR rva);
PIMAGE_SECTION_HEADER __fastcall FindPESectionByName(const char *pName);
PIMAGE_SECTION_HEADER __fastcall _mingw_GetSectionForAddress(LPVOID p);
int __cdecl _mingw_GetSectionCount();
PIMAGE_SECTION_HEADER __fastcall FindPESectionExec(size_t eNo);
PBYTE __cdecl GetPEImageBase();
WINBOOL __fastcall IsNonwritableInCurrentImage(PBYTE pTarget);
const char *__fastcall _mingw_enum_import_library_names(int i);
void __cdecl _mingwthr_run_key_dtors_part_0();
int __fastcall __w64_mingwthr_add_key_dtor(DWORD key, void (*dtor)(void *));
int __fastcall __w64_mingwthr_remove_key_dtor(DWORD key);
WINBOOL __fastcall _mingw_TLScallback(HANDLE hDllHandle, DWORD reason, LPVOID reserved);
// void __cdecl _set_app_type(_crt_app_type Type);
// __int64 __fastcall _getmainargs(_QWORD, _QWORD, _QWORD, _QWORD, _QWORD); weak
void (*__cdecl get_invalid_parameter_handler())(const wchar_t *, const wchar_t *, const wchar_t *, unsigned int, uintptr_t);
void (*__fastcall set_invalid_parameter_handler(void (*new_handler)(const wchar_t *, const wchar_t *, const wchar_t *, unsigned int, uintptr_t)))(const wchar_t *, const wchar_t *, const wchar_t *, unsigned int, uintptr_t);
// void *__cdecl malloc(size_t Size);
// size_t __cdecl strlen(const char *Str);
// void *__cdecl memcpy(void *, const void *Src, size_t Size);
// void __cdecl cexit();
// __int64 __fastcall amsg_exit(_QWORD); weak
// void __cdecl initterm(_PVFV *First, _PVFV *Last);
// void __cdecl __noreturn exit(int Code);
// int printf(const char *const Format, ...);
// int sprintf(char *const Buffer, const char *const Format, ...);
// void __cdecl _setusermatherr(_UserMathErrorFunctionPointer UserMathErrorFunction);
// FILE *__cdecl _iob_func();
// int fprintf(FILE *const Stream, const char *const Format, ...);
// size_t __cdecl fwrite(const void *Buffer, size_t ElementSize, size_t ElementCount, FILE *Stream);
// int __cdecl vfprintf(FILE *const Stream, const char *const Format, va_list ArgList);
// void __cdecl __noreturn abort();
// _crt_signal_t __cdecl signal(int Signal, _crt_signal_t Function);
// __int64 __fastcall lock(_QWORD); weak
// __int64 __fastcall _dllonexit(_QWORD, _QWORD, _QWORD); weak
// __int64 __fastcall unlock(_QWORD); weak
// int __cdecl strncmp(const char *Str1, const char *Str2, size_t MaxCount);
// void *__cdecl calloc(size_t Count, size_t Size);
// void __cdecl free(void *Block);
// int __fastcall main(int flags, char **cmdline, char **inst); idb
// __int64 __fastcall _IAT_start__(_QWORD, _QWORD, _QWORD); weak
// __int64 __lconv_init(void); weak

//-------------------------------------------------------------------------
// Data declarations

func_ptr *p_73208 = (func_ptr *)0x403338LL; // idb
UINT_PTR _security_cookie = 47936899621426uLL; // idb
UINT_PTR _security_cookie_complement = 18446696136809930189uLL; // idb
char aSfmsilqzdxajhn[53] = "sfMSiLQzdXajhnZKrPyAoHbTDNREWtuVOcGIxkYemgBClvwFUpqJ"; // weak
const EXCEPTION_POINTERS GS_ExceptionPointers = { &GS_ExceptionRecord, &GS_ContextRecord }; // idb
int *refptr__CRT_MT = &CRT_MT; // weak
int *refptr__MINGW_INSTALL_DEBUG_MATHERR = &MINGW_INSTALL_DEBUG_MATHERR; // weak
__int64 (*refptr___CTOR_LIST__)[2] = &__CTOR_LIST__; // weak
_UNKNOWN *refptr___RUNTIME_PSEUDO_RELOC_LIST_END__ = &_RUNTIME_PSEUDO_RELOC_LIST_END___0; // weak
_UNKNOWN *refptr___RUNTIME_PSEUDO_RELOC_LIST__ = &_RUNTIME_PSEUDO_RELOC_LIST_END___0; // weak
const PBYTE refptr___image_base__ = (const PBYTE)0x400000LL; // idb
_UNKNOWN *refptr___imp__fmode = &_fmode; // weak
_UNKNOWN *refptr___imp__onexit = &_onexit; // weak
__int64 *refptr___onexitbegin = &_onexitbegin; // weak
__int64 *refptr___onexitend = &_onexitend; // weak
int *refptr__dowildcard = &dowildcard; // weak
int *refptr__fmode = &fmode; // weak
int *refptr__newmode = &newmode; // weak
int *refptr_mingw_app_type = &mingw_app_type; // weak
int *refptr_mingw_initcharmax = &mingw_initcharmax; // weak
int *refptr_mingw_initltsdrot_force = &mingw_initltsdrot_force; // weak
int *refptr_mingw_initltsdyn_force = &mingw_initltsdyn_force; // weak
int *refptr_mingw_initltssuo_force = &mingw_initltssuo_force; // weak
_startupinfo _bss_start__; // idb
int managedapp; // idb
int argret; // idb
char **envp; // idb
char **argv; // idb
int argc; // idb
fUserMathErr stUserMathErr; // idb
int was_init_73980; // idb
int maxSections; // idb
sSecInfo *the_secs; // idb
int was_here_73812; // idb
UNWIND_INFO emu_xdata[32]; // idb
RUNTIME_FUNCTION emu_pdata[32]; // idb
int initialized; // idb
CONTEXT GS_ContextRecord; // idb
EXCEPTION_RECORD GS_ExceptionRecord; // idb
volatile __mingwthr_key_t *key_dtor_list; // idb
volatile int _mingwthr_cs_init; // idb
CRITICAL_SECTION _mingwthr_cs; // idb
void (*handler)(const wchar_t *, const wchar_t *, const wchar_t *, unsigned int, uintptr_t); // idb
_PVFV *_onexitbegin; // idb
_PVFV *_onexitend; // idb
// extern void (__stdcall *EnterCriticalSection)(LPCRITICAL_SECTION lpCriticalSection);
// extern HANDLE (__stdcall *GetCurrentProcess)();
// extern DWORD (__stdcall *GetCurrentProcessId)();
// extern DWORD (__stdcall *GetCurrentThreadId)();
// extern DWORD (__stdcall *GetLastError)();
// extern void (__stdcall *GetSystemTimeAsFileTime)(LPFILETIME lpSystemTimeAsFileTime);
// extern DWORD (__stdcall *GetTickCount)();
// extern void (__stdcall *InitializeCriticalSection)(LPCRITICAL_SECTION lpCriticalSection);
// extern void (__stdcall *LeaveCriticalSection)(LPCRITICAL_SECTION lpCriticalSection);
// extern BOOL (__stdcall *QueryPerformanceCounter)(LARGE_INTEGER *lpPerformanceCount);
// extern BOOLEAN (__cdecl *RtlAddFunctionTable)(PRUNTIME_FUNCTION FunctionTable, ULONG EntryCount, ULONG64 BaseAddress);
// extern void (__stdcall *RtlCaptureContext)(PCONTEXT ContextRecord);
// extern PRUNTIME_FUNCTION (__stdcall *RtlLookupFunctionEntry)(ULONG64 ControlPc, PULONG64 ImageBase, PUNWIND_HISTORY_TABLE HistoryTable);
// extern PEXCEPTION_ROUTINE (__stdcall *RtlVirtualUnwind)(ULONG HandlerType, ULONG64 ImageBase, ULONG64 ControlPc, PRUNTIME_FUNCTION FunctionEntry, PCONTEXT ContextRecord, PVOID *HandlerData, PULONG64 EstablisherFrame, PKNONVOLATILE_CONTEXT_POINTERS ContextPointers);
// extern LPTOP_LEVEL_EXCEPTION_FILTER (__stdcall *SetUnhandledExceptionFilter)(LPTOP_LEVEL_EXCEPTION_FILTER lpTopLevelExceptionFilter);
// extern BOOL (__stdcall *TerminateProcess)(HANDLE hProcess, UINT uExitCode);
// extern LPVOID (__stdcall *TlsGetValue)(DWORD dwTlsIndex);
// extern LONG (__stdcall *UnhandledExceptionFilter)(struct _EXCEPTION_POINTERS *ExceptionInfo);
// extern BOOL (__stdcall *VirtualProtect)(LPVOID lpAddress, SIZE_T dwSize, DWORD flNewProtect, PDWORD lpflOldProtect);
// extern SIZE_T (__stdcall *VirtualQuery)(LPCVOID lpAddress, PMEMORY_BASIC_INFORMATION lpBuffer, SIZE_T dwLength);
// extern HWND (__stdcall *CreateDialogParamA)(HINSTANCE hInstance, LPCSTR lpTemplateName, HWND hWndParent, DLGPROC lpDialogFunc, LPARAM dwInitParam);
// extern LRESULT (__stdcall *DispatchMessageA)(const MSG *lpMsg);
// extern BOOL (__stdcall *EndDialog)(HWND hDlg, INT_PTR nResult);
// extern UINT (__stdcall *GetDlgItemTextA)(HWND hDlg, int nIDDlgItem, LPSTR lpString, int cchMax);
// extern BOOL (__stdcall *GetMessageA)(LPMSG lpMsg, HWND hWnd, UINT wMsgFilterMin, UINT wMsgFilterMax);
// extern BOOL (__stdcall *IsDialogMessageA)(HWND hDlg, LPMSG lpMsg);
// extern HMENU (__stdcall *LoadMenuA)(HINSTANCE hInstance, LPCSTR lpMenuName);
// extern int (__stdcall *MessageBoxA)(HWND hWnd, LPCSTR lpText, LPCSTR lpCaption, UINT uType);
// extern BOOL (__stdcall *SetMenu)(HWND hWnd, HMENU hMenu);
// extern BOOL (__stdcall *ShowWindow)(HWND hWnd, int nCmdShow);
// extern BOOL (__stdcall *TranslateMessage)(const MSG *lpMsg);


//----- (0000000000401010) ----------------------------------------------------
int __cdecl pre_c_init()
{
  _BOOL8 v0; // rdx
  void *v1; // rax
  BYTE *v3; // rax
  __int16 v4; // cx

  LODWORD(v0) = 0;
  *refptr_mingw_initltsdrot_force = 1;
  *refptr_mingw_initltsdyn_force = 1;
  *refptr_mingw_initltssuo_force = 1;
  *refptr_mingw_initcharmax = 1;
  if ( *refptr___image_base__ == 23117 )
  {
    v3 = &refptr___image_base__[*(refptr___image_base__ + 15)];
    if ( *v3 == 17744 )
    {
      v4 = *(v3 + 12);
      if ( v4 == 267 )
      {
        if ( *(v3 + 29) > 0xEu )
          v0 = *(v3 + 58) != 0;
      }
      else if ( v4 == 523 && *(v3 + 33) > 0xEu )
      {
        v0 = *(v3 + 62) != 0;
      }
    }
  }
  managedapp = v0;
  if ( *refptr_mingw_app_type )
    _set_app_type(_crt_gui_app);
  else
    _set_app_type(_crt_console_app);
  v1 = encode_pointer(0xFFFFFFFFFFFFFFFFLL);
  *refptr___onexitend = v1;
  *refptr___onexitbegin = v1;
  **refptr___imp__fmode = *refptr__fmode;
  setargv();
  if ( *refptr__MINGW_INSTALL_DEBUG_MATHERR == 1 )
    _mingw_setusermatherr(matherr);
  return 0;
}
// 405370: using guessed type int *refptr__MINGW_INSTALL_DEBUG_MATHERR;
// 4053F0: using guessed type _UNKNOWN *refptr___imp__fmode;
// 405470: using guessed type __int64 *refptr___onexitbegin;
// 405480: using guessed type __int64 *refptr___onexitend;
// 4054E0: using guessed type int *refptr__fmode;
// 405520: using guessed type int *refptr_mingw_app_type;
// 405530: using guessed type int *refptr_mingw_initcharmax;
// 405540: using guessed type int *refptr_mingw_initltsdrot_force;
// 405550: using guessed type int *refptr_mingw_initltsdyn_force;
// 405560: using guessed type int *refptr_mingw_initltssuo_force;

//----- (0000000000401160) ----------------------------------------------------
void __cdecl pre_cpp_init()
{
  _bss_start__.newmode = *refptr__newmode;
  argret = _getmainargs(&argc, &argv, &envp, *refptr__dowildcard, &_bss_start__);
}
// 4030D0: using guessed type __int64 __fastcall _getmainargs(_QWORD, _QWORD, _QWORD, _QWORD, _QWORD);
// 4054D0: using guessed type int *refptr__dowildcard;
// 405510: using guessed type int *refptr__newmode;

//----- (0000000000401500) ----------------------------------------------------
int __cdecl mainCRTStartup()
{
  *refptr_mingw_app_type = 0;
  _security_init_cookie();
  return _tmainCRTStartup();
}
// 405520: using guessed type int *refptr_mingw_app_type;

//----- (0000000000401530) ----------------------------------------------------
char *__fastcall generaLetras(int a1, char *a2)
{
  size_t v2; // rax
  char *result; // rax
  int v4; // [rsp+28h] [rbp-58h]
  int v5; // [rsp+2Ch] [rbp-54h]
  int v6; // [rsp+30h] [rbp-50h]
  int v7; // [rsp+34h] [rbp-4Ch]

  v7 = (a1 + 15) % strlen("sfMSiLQzdXajhnZKrPyAoHbTDNREWtuVOcGIxkYemgBClvwFUpqJ");
  v6 = (a1 + 22) % strlen("sfMSiLQzdXajhnZKrPyAoHbTDNREWtuVOcGIxkYemgBClvwFUpqJ");
  v5 = (a1 + 32) % strlen("sfMSiLQzdXajhnZKrPyAoHbTDNREWtuVOcGIxkYemgBClvwFUpqJ");
  v4 = (a1 + 17) % strlen("sfMSiLQzdXajhnZKrPyAoHbTDNREWtuVOcGIxkYemgBClvwFUpqJ");
  v2 = strlen("sfMSiLQzdXajhnZKrPyAoHbTDNREWtuVOcGIxkYemgBClvwFUpqJ");
  *a2 = aSfmsilqzdxajhn[v7];
  a2[1] = aSfmsilqzdxajhn[v6];
  a2[2] = aSfmsilqzdxajhn[v5];
  a2[3] = aSfmsilqzdxajhn[v4];
  a2[4] = aSfmsilqzdxajhn[((a1 + 4) % v2)];
  result = a2 + 5;
  a2[5] = 0;
  return result;
}

//----- (00000000004016AD) ----------------------------------------------------
__int64 __fastcall generaNumero(char *a1)
{
  int i; // [rsp+28h] [rbp-58h]
  int v3; // [rsp+2Ch] [rbp-54h]

  v3 = 0;
  for ( i = 0; i < strlen(a1); ++i )
    v3 += a1[i];
  printf("Numero: %d", v3 + 6572);
  return (v3 + 6572);
}

//----- (0000000000401746) ----------------------------------------------------
int __fastcall generaSerial(char *a1, char *a2)
{
  char v3[16]; // [rsp+40h] [rbp-50h] BYREF
  char v4[16]; // [rsp+50h] [rbp-40h] BYREF
  char v5[16]; // [rsp+60h] [rbp-30h] BYREF
  char v6[16]; // [rsp+70h] [rbp-20h] BYREF
  char v7[12]; // [rsp+80h] [rbp-10h] BYREF
  int v8; // [rsp+8Ch] [rbp-4h]

  v8 = generaNumero(a1);
  generaLetras(v8, v7);
  v8 = generaNumero(v7);
  generaLetras(v8, v6);
  v8 = generaNumero(v6);
  generaLetras(v8, v5);
  v8 = generaNumero(v5);
  generaLetras(v8, v4);
  v8 = generaNumero(v4);
  generaLetras(v8, v3);
  return sprintf(a2, "%s-%s-%s-%s-%s", v7, v6, v5, v4, v3);
}

//----- (000000000040182D) ----------------------------------------------------
int __fastcall checkSerial(char *a1, char *a2)
{
  size_t v2; // rbx
  size_t v3; // rax
  int i; // [rsp+28h] [rbp-58h]
  char v6; // [rsp+2Fh] [rbp-51h]

  v6 = 1;
  v2 = strlen(a1);
  if ( v2 == strlen(a2) )
  {
    for ( i = 0; ; ++i )
    {
      v3 = strlen(a2);
      if ( i >= v3 )
        break;
      if ( a1[i] != a2[i] )
      {
        LODWORD(v3) = MessageBoxA(0LL, "Nope sigue intentando", "Nop", 0x30u);
        v6 = 0;
        break;
      }
    }
    if ( v6 )
      LODWORD(v3) = MessageBoxA(0LL, "Genial lo lograste", "Felicitaciones", 0);
  }
  else
  {
    MessageBoxA(0LL, "Nope sigue intentando", "Nop", 0x30u);
    LODWORD(v3) = 0;
  }
  return v3;
}

//----- (000000000040192F) ----------------------------------------------------
INT_PTR __fastcall DialogProc(HWND a1, int a2, unsigned __int16 a3)
{
  char v4[32]; // [rsp+20h] [rbp-60h] BYREF
  CHAR v5[32]; // [rsp+40h] [rbp-40h] BYREF
  CHAR String[28]; // [rsp+60h] [rbp-20h] BYREF
  UINT DlgItemTextA; // [rsp+7Ch] [rbp-4h]

  DlgItemTextA = 0;
  switch ( a2 )
  {
    case 272:
      return 1LL;
    case 273:
      if ( a3 == 40000 )
      {
        DlgItemTextA = GetDlgItemTextA(a1, 40002, String, 20);
        if ( DlgItemTextA )
        {
          DlgItemTextA = GetDlgItemTextA(a1, 40003, v5, 30);
          if ( DlgItemTextA )
          {
            generaSerial(String, v4);
            checkSerial(v5, v4);
            return 1LL;
          }
          MessageBoxA(a1, "Nope sigue intentando", "Nop", 0x30u);
        }
        else
        {
          MessageBoxA(a1, "Nope sigue intentando", "Nop", 0x30u);
        }
      }
      else if ( a3 == 40006 )
      {
        MessageBoxA(a1, "keygeneame si puedes\n\nEl objetivo es crear el keygen sin parchear nada", "About", 0x40u);
        return 1LL;
      }
      return 1LL;
    case 16:
      EndDialog(a1, 0LL);
      return 1LL;
    default:
      return 0LL;
  }
}

//----- (0000000000401AA6) ----------------------------------------------------
int __stdcall WinMain(HINSTANCE hInst, HINSTANCE hPreInst, LPSTR lpszCmdLine, int nCmdShow)
{
  tagMSG Msg; // [rsp+30h] [rbp-40h] BYREF
  HMENU hMenu; // [rsp+60h] [rbp-10h]
  HWND hWnd; // [rsp+68h] [rbp-8h]

  hWnd = CreateDialogParamA(hInst, 102, 0LL, DialogProc, 0LL);
  hMenu = LoadMenuA(hInst, 0x69);
  SetMenu(hWnd, hMenu);
  ShowWindow(hWnd, 10);
  while ( GetMessageA(&Msg, 0LL, 0, 0) > 0 )
  {
    if ( !IsDialogMessageA(hWnd, &Msg) )
    {
      TranslateMessage(&Msg);
      DispatchMessageA(&Msg);
    }
  }
  return 0;
}

//----- (0000000000401BA0) ----------------------------------------------------
void *__fastcall decode_pointer(void *codedptr)
{
  return codedptr;
}

//----- (0000000000401BB0) ----------------------------------------------------
void *__fastcall encode_pointer(void *ptr)
{
  return ptr;
}

//----- (0000000000401BC0) ----------------------------------------------------
int __cdecl setargv()
{
  return 0;
}

//----- (0000000000401BD0) ----------------------------------------------------
void __fastcall _mingw_raise_matherr(int typ, const char *name, double a3, double a1, double rslt)
{
  _exception ex; // [rsp+20h] [rbp-38h] BYREF

  if ( stUserMathErr )
  {
    ex.type = typ;
    ex.name = name;
    ex.arg1 = a3;
    ex.arg2 = a1;
    ex.retval = rslt;
    stUserMathErr(&ex);
  }
}

//----- (0000000000401C20) ----------------------------------------------------
void __fastcall _mingw_setusermatherr(int (*f)(_exception *))
{
  stUserMathErr = f;
  _setusermatherr(f);
}

//----- (0000000000401C30) ----------------------------------------------------
int __fastcall matherr(_exception *pexcept)
{
  const char *v1; // rbx
  double retval; // xmm8_8
  const char *name; // rsi
  double arg2; // xmm7_8
  double arg1; // xmm6_8
  FILE *v6; // rax

  switch ( pexcept->type )
  {
    case 1:
      v1 = "Argument domain error (DOMAIN)";
      break;
    case 2:
      v1 = "Argument singularity (SIGN)";
      break;
    case 3:
      v1 = "Overflow range error (OVERFLOW)";
      break;
    case 4:
      v1 = "The result is too small to be represented (UNDERFLOW)";
      break;
    case 5:
      v1 = "Total loss of significance (TLOSS)";
      break;
    case 6:
      v1 = "Partial loss of significance (PLOSS)";
      break;
    default:
      v1 = "Unknown error";
      break;
  }
  retval = pexcept->retval;
  name = pexcept->name;
  arg2 = pexcept->arg2;
  arg1 = pexcept->arg1;
  v6 = _iob_func();
  fprintf(v6 + 2, "_matherr(): %s in %s(%g, %g)  (retval=%g)\n", v1, name, arg1, arg2, retval);
  return 0;
}

//----- (0000000000401D30) ----------------------------------------------------
void __noreturn _report_error(const char *msg, ...)
{
  FILE *v2; // rax
  FILE *v3; // rax
  va_list va; // [rsp+58h] [rbp+10h] BYREF

  va_start(va, msg);
  v2 = _iob_func();
  fwrite("Mingw-w64 runtime failure:\n", 1uLL, 0x1BuLL, v2 + 2);
  v3 = _iob_func();
  vfprintf(v3 + 2, msg, va);
  abort();
}

//----- (0000000000401DA0) ----------------------------------------------------
void __fastcall _write_memory_part_0(void *addr, const void *src, size_t len)
{
  __int64 v3; // rbp
  int v7; // r9d
  PBYTE *p_sec_start; // rax
  PIMAGE_SECTION_HEADER SectionForAddress; // rax
  PIMAGE_SECTION_HEADER v10; // r12
  __int64 v11; // rbp
  sSecInfo *v12; // r13
  DWORD LastError; // eax
  struct _MEMORY_BASIC_INFORMATION Buffer; // [rsp+20h] [rbp-68h] BYREF

  v3 = maxSections;
  if ( maxSections <= 0 )
  {
    v3 = 0LL;
LABEL_6:
    SectionForAddress = _mingw_GetSectionForAddress(addr);
    v10 = SectionForAddress;
    if ( !SectionForAddress )
      _report_error("Address %p has no image-section", addr);
    v11 = v3;
    v12 = &the_secs[v11];
    v12->hash = SectionForAddress;
    v12->old_protect = 0;
    v12->sec_start = &GetPEImageBase()[SectionForAddress->VirtualAddress];
    if ( !VirtualQuery(the_secs[v11].sec_start, &Buffer, 0x30uLL) )
      _report_error(
        "  VirtualQuery failed for %d bytes at address %p",
        v10->Misc.PhysicalAddress,
        the_secs[v11].sec_start);
    if ( ((Buffer.Protect - 4) & 0xFFFFFFFB) != 0
      && ((Buffer.Protect - 64) & 0xFFFFFFBF) != 0
      && !VirtualProtect(Buffer.BaseAddress, Buffer.RegionSize, 0x40u, &the_secs[v11].old_protect) )
    {
      LastError = GetLastError();
      _report_error("  VirtualProtect failed with code 0x%x", LastError);
    }
    ++maxSections;
  }
  else
  {
    v7 = 0;
    p_sec_start = &the_secs->sec_start;
    while ( addr < *p_sec_start || addr >= &(*p_sec_start)[*(p_sec_start[1] + 2)] )
    {
      ++v7;
      p_sec_start += 3;
      if ( v7 == maxSections )
        goto LABEL_6;
    }
  }
  memcpy(addr, src, len);
}

//----- (0000000000401F10) ----------------------------------------------------
void __cdecl pei386_runtime_relocator()
{
  unsigned __int64 v0; // rax
  void *v1; // rsp
  _DWORD *v2; // rbx
  void *v3; // rsp
  int v4; // edx
  unsigned int *v5; // rbx
  unsigned int v6; // edx
  BYTE *v7; // rax
  BYTE *v8; // rcx
  __int64 v9; // r8
  __int64 v10; // rbx
  int i; // esi
  __int64 v12; // rcx
  int v13; // eax
  BYTE *v14; // rcx
  unsigned __int64 v15; // rdx
  unsigned __int64 v16; // rdx
  unsigned __int64 v17; // rdx
  char v18; // [rsp+20h] [rbp-40h] BYREF
  DWORD flOldProtect; // [rsp+2Ch] [rbp-34h] BYREF
  struct _MEMORY_BASIC_INFORMATION src; // [rsp+30h] [rbp-30h] BYREF

  if ( was_init_73980 )
    return;
  was_init_73980 = 1;
  v0 = (24LL * _mingw_GetSectionCount() + 30) & 0xFFFFFFFFFFFFFFF0uLL;
  v1 = alloca(v0);
  v2 = refptr___RUNTIME_PSEUDO_RELOC_LIST__;
  v3 = alloca(v0);
  maxSections = 0;
  the_secs = &v18;
  if ( refptr___RUNTIME_PSEUDO_RELOC_LIST_END__ - refptr___RUNTIME_PSEUDO_RELOC_LIST__ <= 7 )
    return;
  if ( refptr___RUNTIME_PSEUDO_RELOC_LIST_END__ - refptr___RUNTIME_PSEUDO_RELOC_LIST__ > 11 )
  {
    if ( *refptr___RUNTIME_PSEUDO_RELOC_LIST__ || *(refptr___RUNTIME_PSEUDO_RELOC_LIST__ + 1) )
      goto LABEL_25;
    if ( *(refptr___RUNTIME_PSEUDO_RELOC_LIST__ + 2) )
      goto LABEL_11;
    v2 = (refptr___RUNTIME_PSEUDO_RELOC_LIST__ + 12);
  }
  if ( *v2 || v2[1] )
  {
LABEL_25:
    if ( v2 >= refptr___RUNTIME_PSEUDO_RELOC_LIST_END__ )
      return;
    do
    {
      v12 = v2[1];
      v13 = *v2;
      v2 += 2;
      v14 = &refptr___image_base__[v12];
      LODWORD(src.BaseAddress) = *v14 + v13;
      _write_memory_part_0(v14, &src, 4uLL);
    }
    while ( v2 < refptr___RUNTIME_PSEUDO_RELOC_LIST_END__ );
    goto LABEL_19;
  }
LABEL_11:
  v4 = v2[2];
  if ( v4 != 1 )
    _report_error("  Unknown pseudo relocation protocol version %d.\n", v4);
  v5 = v2 + 3;
  if ( v5 < refptr___RUNTIME_PSEUDO_RELOC_LIST_END__ )
  {
    do
    {
      v6 = *(v5 + 8);
      v7 = &refptr___image_base__[*v5];
      v8 = &refptr___image_base__[v5[1]];
      v9 = *v7;
      if ( v6 == 16 )
      {
        v16 = *v8;
        if ( (v16 & 0x8000u) != 0LL )
          v16 = *v8 | 0xFFFFFFFFFFFF0000uLL;
        src.BaseAddress = (v9 + v16 - v7);
        _write_memory_part_0(v8, &src, 2uLL);
      }
      else if ( v6 <= 0x10 )
      {
        if ( v6 != 8 )
        {
LABEL_35:
          src.BaseAddress = 0LL;
          _report_error("  Unknown pseudo relocation bit size %d.\n", v6);
        }
        v15 = *v8;
        if ( (v15 & 0x80u) != 0LL )
          v15 = *v8 | 0xFFFFFFFFFFFFFF00uLL;
        src.BaseAddress = (v9 + v15 - v7);
        _write_memory_part_0(v8, &src, 1uLL);
      }
      else if ( v6 == 32 )
      {
        v17 = *v8;
        if ( (v17 & 0x80000000) != 0LL )
          v17 = *v8 | 0xFFFFFFFF00000000uLL;
        src.BaseAddress = (v9 + v17 - v7);
        _write_memory_part_0(v8, &src, 4uLL);
      }
      else
      {
        if ( v6 != 64 )
          goto LABEL_35;
        src.BaseAddress = (*v8 + v9 - v7);
        _write_memory_part_0(v8, &src, 8uLL);
      }
      v5 += 3;
    }
    while ( v5 < refptr___RUNTIME_PSEUDO_RELOC_LIST_END__ );
LABEL_19:
    v10 = 0LL;
    for ( i = 0; i < maxSections; ++v10 )
    {
      if ( the_secs[v10].old_protect )
      {
        if ( !VirtualQuery(the_secs[v10].sec_start, &src, 0x30uLL) )
          _report_error(
            "  VirtualQuery failed for %d bytes at address %p",
            the_secs[v10].hash->Misc.PhysicalAddress,
            the_secs[v10].sec_start);
        VirtualProtect(src.BaseAddress, src.RegionSize, the_secs[v10].old_protect, &flOldProtect);
      }
      ++i;
    }
  }
}
// 405390: using guessed type _UNKNOWN *refptr___RUNTIME_PSEUDO_RELOC_LIST_END__;
// 4053A0: using guessed type _UNKNOWN *refptr___RUNTIME_PSEUDO_RELOC_LIST__;

//----- (0000000000402210) ----------------------------------------------------
int __fastcall _mingw_SEH_error_handler(
        _EXCEPTION_RECORD *ExceptionRecord,
        void *EstablisherFrame,
        _CONTEXT *ContextRecord,
        void *DispatcherContext)
{
  DWORD ExceptionCode; // eax
  _crt_signal_t v5; // rax
  int result; // eax
  _crt_signal_t v7; // rdx
  _crt_signal_t v8; // rax

  ExceptionCode = ExceptionRecord->ExceptionCode;
  if ( ExceptionRecord->ExceptionCode > 0xC0000091 )
  {
    if ( ExceptionCode == -1073741676 )
    {
      v7 = signal(8, 0LL);
      if ( v7 == 1 )
      {
        signal(8, 1);
        return 0;
      }
      goto LABEL_16;
    }
    if ( ExceptionCode > 0xC0000094 )
    {
      if ( ExceptionCode == -1073741675 )
        return 0;
      if ( ExceptionCode != -1073741674 )
        return 1;
      goto LABEL_20;
    }
    if ( ExceptionCode == -1073741678 )
      return 0;
    if ( ExceptionCode != -1073741677 )
      return 1;
  }
  else if ( ExceptionCode < 0xC000008D )
  {
    if ( ExceptionCode == -1073741816 )
      return 0;
    if ( ExceptionCode <= 0xC0000008 )
    {
      if ( ExceptionCode != -2147483646 )
      {
        if ( ExceptionCode == -1073741819 )
        {
          v5 = signal(11, 0LL);
          if ( v5 == 1 )
          {
            signal(11, 1);
            return 0;
          }
          if ( v5 )
          {
            (v5)(11LL);
            return 0;
          }
          return 4;
        }
        return 1;
      }
      return 0;
    }
    if ( ExceptionCode != -1073741795 )
      return ExceptionCode != -1073741684;
LABEL_20:
    v8 = signal(4, 0LL);
    if ( v8 == 1 )
    {
      signal(4, 1);
      return 0;
    }
    if ( v8 )
    {
      (v8)(4LL);
      return 0;
    }
    return 4;
  }
  v7 = signal(8, 0LL);
  if ( v7 == 1 )
  {
    signal(8, 1);
    fpreset();
    return 0;
  }
LABEL_16:
  result = 1;
  if ( v7 )
  {
    (v7)(8LL);
    return 0;
  }
  return result;
}

//----- (00000000004023C0) ----------------------------------------------------
int __cdecl _mingw_init_ehandler()
{
  PBYTE PEImageBase; // rbp
  int result; // eax
  RUNTIME_FUNCTION *v2; // rbx
  size_t v3; // rsi
  UNWIND_INFO *v4; // rdi
  DWORD VirtualAddress; // edx
  DWORD v6; // edx
  DWORD v7; // eax
  PIMAGE_SECTION_HEADER PESectionExec; // rax
  ULONG v9; // edx

  PEImageBase = GetPEImageBase();
  result = was_here_73812;
  if ( !was_here_73812 && PEImageBase )
  {
    was_here_73812 = 1;
    if ( !FindPESectionByName(".pdata") )
    {
      v2 = emu_pdata;
      v3 = 0LL;
      memset(emu_pdata, 0, sizeof(emu_pdata));
      memset(emu_xdata, 0, sizeof(emu_xdata));
      v4 = emu_xdata;
      while ( 1 )
      {
        PESectionExec = FindPESectionExec(v3);
        if ( !PESectionExec )
          break;
        v4->VersionAndFlags = 9;
        v4->AddressOfExceptionHandler = _mingw_SEH_error_handler - PEImageBase;
        ++v3;
        VirtualAddress = PESectionExec->VirtualAddress;
        ++v2;
        v2[-1].BeginAddress = VirtualAddress;
        v6 = PESectionExec->Misc.PhysicalAddress + VirtualAddress;
        v7 = v4++ - PEImageBase;
        v2[-1].UnwindData = v7;
        v2[-1].EndAddress = v6;
        if ( v3 == 32 )
        {
          v9 = 32;
          goto LABEL_11;
        }
      }
      if ( !v3 )
        return 1;
      v9 = v3;
LABEL_11:
      RtlAddFunctionTable(emu_pdata, v9, PEImageBase);
    }
    return 1;
  }
  return result;
}

//----- (0000000000402670) ----------------------------------------------------
void __cdecl fpreset()
{
  __asm { fninit }
}

//----- (0000000000402680) ----------------------------------------------------
void __cdecl _do_global_dtors()
{
  void (*i)(void); // rax

  for ( i = *p_73208; i; ++p_73208 )
  {
    i();
    i = p_73208[1];
  }
}

//----- (00000000004026C0) ----------------------------------------------------
void __cdecl _do_global_ctors()
{
  int i; // ebx

  i = (*refptr___CTOR_LIST__)[0];
  if ( i == -1 )
  {
    for ( i = 0; (*refptr___CTOR_LIST__)[i + 1]; ++i )
      ;
  }
  for ( ; i; --i )
    ((*refptr___CTOR_LIST__)[i])();
  atexit(_do_global_dtors);
}
// 405380: using guessed type __int64 (*refptr___CTOR_LIST__)[2];

//----- (0000000000402720) ----------------------------------------------------
void __cdecl _main()
{
  if ( !initialized )
  {
    initialized = 1;
    _do_global_ctors();
  }
}

//----- (0000000000402740) ----------------------------------------------------
void __cdecl _security_init_cookie()
{
  FT v0; // r12
  __int64 CurrentProcessId; // rbp
  DWORD CurrentThreadId; // edi
  DWORD TickCount; // esi
  LONGLONG v4; // rsi
  UINT_PTR v5; // rax
  FT systime; // [rsp+20h] [rbp-48h] BYREF
  LARGE_INTEGER perfctr; // [rsp+30h] [rbp-38h] BYREF

  systime.ft_scalar = 0LL;
  if ( _security_cookie == 0x2B992DDFA232LL )
  {
    GetSystemTimeAsFileTime(&systime);
    v0.ft_scalar = systime.ft_scalar;
    CurrentProcessId = GetCurrentProcessId();
    CurrentThreadId = GetCurrentThreadId();
    TickCount = GetTickCount();
    QueryPerformanceCounter(&perfctr);
    v4 = (TickCount ^ CurrentThreadId ^ perfctr.QuadPart ^ v0.ft_scalar ^ CurrentProcessId) & 0xFFFFFFFFFFFFLL;
    if ( v4 == 0x2B992DDFA232LL )
    {
      v5 = 0xFFFFD466D2205DCCuLL;
      v4 = 0x2B992DDFA233LL;
    }
    else
    {
      v5 = ~v4;
    }
    _security_cookie = v4;
    _security_cookie_complement = v5;
  }
  else
  {
    _security_cookie_complement = ~_security_cookie;
  }
}

//----- (0000000000402820) ----------------------------------------------------
void __fastcall __noreturn _report_gsfailure(ULONG_PTR StackCookie)
{
  ULONG64 Rip; // rbx
  _RUNTIME_FUNCTION *v3; // r9
  HANDLE CurrentProcess; // rax
  ULONG64 imgBase; // [rsp+48h] [rbp-28h] BYREF
  ULONG64 establisherFrame; // [rsp+50h] [rbp-20h] BYREF
  PVOID hndData; // [rsp+58h] [rbp-18h] BYREF
  UINT_PTR cookie[2]; // [rsp+60h] [rbp-10h]
  char vars8; // [rsp+78h] [rbp+8h] BYREF
  DWORD64 retaddr; // [rsp+88h] [rbp+18h]

  RtlCaptureContext(&GS_ContextRecord);
  Rip = GS_ContextRecord.Rip;
  v3 = RtlLookupFunctionEntry(GS_ContextRecord.Rip, &imgBase, 0LL);
  if ( v3 )
  {
    RtlVirtualUnwind(0, imgBase, Rip, v3, &GS_ContextRecord, &hndData, &establisherFrame, 0LL);
  }
  else
  {
    GS_ContextRecord.Rip = retaddr;
    GS_ContextRecord.Rsp = &vars8;
  }
  GS_ContextRecord.Rcx = StackCookie;
  GS_ExceptionRecord.ExceptionCode = -1073740791;
  GS_ExceptionRecord.ExceptionFlags = 1;
  GS_ExceptionRecord.ExceptionAddress = GS_ContextRecord.Rip;
  cookie[1] = _security_cookie_complement;
  SetUnhandledExceptionFilter(0LL);
  UnhandledExceptionFilter(&GS_ExceptionPointers);
  CurrentProcess = GetCurrentProcess();
  TerminateProcess(CurrentProcess, 0xC0000409);
  abort();
}

//----- (0000000000402920) ----------------------------------------------------
BOOL __fastcall _dyn_tls_dtor(HANDLE hDllHandle, DWORD dwReason, LPVOID lpreserved)
{
  if ( dwReason && dwReason != 3 )
    return 1;
  _mingw_TLScallback(hDllHandle, dwReason, lpreserved);
  return 1;
}

//----- (0000000000402950) ----------------------------------------------------
BOOL __fastcall _dyn_tls_init(HANDLE hDllHandle, DWORD dwReason, LPVOID lpreserved)
{
  if ( *refptr__CRT_MT != 2 )
    *refptr__CRT_MT = 2;
  if ( dwReason == 1 )
    _mingw_TLScallback(hDllHandle, 1u, lpreserved);
  return 1;
}
// 405360: using guessed type int *refptr__CRT_MT;

//----- (00000000004029C0) ----------------------------------------------------
int __fastcall _tlregdtor(_PVFV func)
{
  return 0;
}

//----- (00000000004029D0) ----------------------------------------------------
_onexit_t __fastcall mingw_onexit(_onexit_t func)
{
  int (*v2)(void); // rbx
  _PVFV *onexitbegin; // [rsp+20h] [rbp-18h] BYREF
  _PVFV *onexitend; // [rsp+28h] [rbp-10h] BYREF

  onexitbegin = decode_pointer(_onexitbegin);
  if ( onexitbegin == -1LL )
    return (*refptr___imp__onexit)(func);
  lock(8LL);
  onexitbegin = decode_pointer(_onexitbegin);
  onexitend = decode_pointer(_onexitend);
  v2 = _dllonexit(func, &onexitbegin, &onexitend);
  _onexitbegin = encode_pointer(onexitbegin);
  _onexitend = encode_pointer(onexitend);
  unlock(8LL);
  return v2;
}
// 403180: using guessed type __int64 __fastcall lock(_QWORD);
// 403188: using guessed type __int64 __fastcall _dllonexit(_QWORD, _QWORD, _QWORD);
// 403190: using guessed type __int64 __fastcall unlock(_QWORD);
// 405400: using guessed type _UNKNOWN *refptr___imp__onexit;

//----- (0000000000402A80) ----------------------------------------------------
int __fastcall atexit(_PVFV func)
{
  return -(mingw_onexit(func) == 0LL);
}

//----- (0000000000402AA0) ----------------------------------------------------
int __cdecl my_lconv_init()
{
  return __lconv_init();
}
// 409350: using guessed type __int64 __lconv_init(void);

//----- (0000000000402AB0) ----------------------------------------------------
WINBOOL __fastcall ValidateImageBase_part_0(PBYTE pImageBase)
{
  BYTE *v1; // rcx
  WINBOOL result; // eax

  v1 = &pImageBase[*(pImageBase + 15)];
  result = 0;
  if ( *v1 == 17744 )
    return *(v1 + 12) == 523;
  return result;
}

//----- (0000000000402AD0) ----------------------------------------------------
WINBOOL __fastcall ValidateImageBase(PBYTE pImageBase)
{
  if ( *pImageBase == 23117 )
    return ValidateImageBase_part_0(pImageBase);
  else
    return 0;
}

//----- (0000000000402AF0) ----------------------------------------------------
PIMAGE_SECTION_HEADER __fastcall FindPESection(PBYTE pImageBase, DWORD_PTR rva)
{
  BYTE *v2; // rcx
  PIMAGE_SECTION_HEADER result; // rax
  int v4; // ecx
  _IMAGE_SECTION_HEADER *v5; // r9

  v2 = &pImageBase[*(pImageBase + 15)];
  result = &v2[*(v2 + 10) + 24];
  v4 = *(v2 + 3);
  if ( !v4 )
    return 0LL;
  v5 = &result[(v4 - 1) + 1];
  while ( result->VirtualAddress > rva || rva >= result->Misc.PhysicalAddress + result->VirtualAddress )
  {
    if ( ++result == v5 )
      return 0LL;
  }
  return result;
}

//----- (0000000000402B40) ----------------------------------------------------
PIMAGE_SECTION_HEADER __fastcall FindPESectionByName(const char *pName)
{
  BYTE *v3; // rdx
  _IMAGE_SECTION_HEADER *v4; // rbx
  int v5; // edx
  __int64 v6; // rdi

  if ( strlen(pName) > 8 )
    return 0LL;
  if ( *refptr___image_base__ != 23117 )
    return 0LL;
  if ( !ValidateImageBase_part_0(refptr___image_base__) )
    return 0LL;
  v3 = &refptr___image_base__[*(refptr___image_base__ + 15)];
  v4 = &v3[*(v3 + 10) + 24];
  v5 = *(v3 + 3);
  if ( !v5 )
    return 0LL;
  v6 = &v4[(v5 - 1) + 1];
  while ( strncmp(v4, pName, 8uLL) )
  {
    if ( ++v4 == v6 )
      return 0LL;
  }
  return v4;
}

//----- (0000000000402BE0) ----------------------------------------------------
PIMAGE_SECTION_HEADER __fastcall _mingw_GetSectionForAddress(LPVOID p)
{
  if ( *refptr___image_base__ == 23117 && ValidateImageBase_part_0(refptr___image_base__) )
    return FindPESection(refptr___image_base__, p - refptr___image_base__);
  else
    return 0LL;
}

//----- (0000000000402C30) ----------------------------------------------------
int __cdecl _mingw_GetSectionCount()
{
  int result; // eax

  result = 0;
  if ( *refptr___image_base__ == 23117 )
  {
    result = ValidateImageBase_part_0(refptr___image_base__);
    if ( result )
      return *&refptr___image_base__[*(refptr___image_base__ + 15) + 6];
  }
  return result;
}

//----- (0000000000402C70) ----------------------------------------------------
PIMAGE_SECTION_HEADER __fastcall FindPESectionExec(size_t eNo)
{
  BYTE *v3; // rsi
  __int64 v4; // rdx
  __int64 v5; // rax

  if ( *refptr___image_base__ != 23117 )
    return 0LL;
  if ( !ValidateImageBase_part_0(refptr___image_base__) )
    return 0LL;
  v3 = &refptr___image_base__[*(refptr___image_base__ + 15)];
  v4 = &v3[*(v3 + 10) + 24];
  if ( !*(v3 + 3) )
    return 0LL;
  v5 = v4 + 40LL * (*(v3 + 3) - 1) + 40;
  while ( (*(v4 + 39) & 0x20) == 0 )
  {
LABEL_9:
    v4 += 40LL;
    if ( v4 == v5 )
      return 0LL;
  }
  if ( eNo )
  {
    --eNo;
    goto LABEL_9;
  }
  return v4;
}

//----- (0000000000402D00) ----------------------------------------------------
PBYTE __cdecl GetPEImageBase()
{
  BYTE *v0; // rbx

  v0 = 0LL;
  if ( *refptr___image_base__ != 23117 )
    return 0LL;
  if ( ValidateImageBase_part_0(refptr___image_base__) )
    return refptr___image_base__;
  return v0;
}

//----- (0000000000402D40) ----------------------------------------------------
WINBOOL __fastcall IsNonwritableInCurrentImage(PBYTE pTarget)
{
  WINBOOL result; // eax
  PIMAGE_SECTION_HEADER PESection; // rax

  result = 0;
  if ( *refptr___image_base__ == 23117 )
  {
    result = ValidateImageBase_part_0(refptr___image_base__);
    if ( result )
    {
      PESection = FindPESection(refptr___image_base__, pTarget - refptr___image_base__);
      return PESection && (PESection->Characteristics & 0x80000000) == 0;
    }
  }
  return result;
}

//----- (0000000000402DA0) ----------------------------------------------------
const char *__fastcall _mingw_enum_import_library_names(int i)
{
  unsigned int v3; // edx
  __int64 v4; // rbx
  BYTE *v5; // rdx

  if ( *refptr___image_base__ != 23117 )
    return 0LL;
  if ( !ValidateImageBase_part_0(refptr___image_base__) )
    return 0LL;
  v3 = *&refptr___image_base__[*(refptr___image_base__ + 15) + 144];
  if ( !v3 )
    return 0LL;
  v4 = v3;
  if ( !FindPESection(refptr___image_base__, v3) )
    return 0LL;
  v5 = &refptr___image_base__[v4];
  if ( !&refptr___image_base__[v4] )
    return 0LL;
  while ( *(v5 + 1) || *(v5 + 3) )
  {
    if ( i <= 0 )
      return &refptr___image_base__[*(v5 + 3)];
    --i;
    v5 += 20;
  }
  return 0LL;
}

//----- (0000000000402E50) ----------------------------------------------------
void __cdecl _mingwthr_run_key_dtors_part_0()
{
  volatile __mingwthr_key_t *i; // rbx
  LPVOID Value; // rsi

  EnterCriticalSection(&_mingwthr_cs);
  for ( i = key_dtor_list; i; i = i->next )
  {
    Value = TlsGetValue(i->key);
    if ( !GetLastError() && Value )
      i->dtor(Value);
  }
  LeaveCriticalSection(&_mingwthr_cs);
}

//----- (0000000000402EC0) ----------------------------------------------------
int __fastcall __w64_mingwthr_add_key_dtor(DWORD key, void (*dtor)(void *))
{
  int result; // eax
  volatile __mingwthr_key_t *v5; // rax
  volatile __mingwthr_key_t *v6; // rbx
  volatile __mingwthr_key_t *v7; // rax

  result = _mingwthr_cs_init;
  if ( _mingwthr_cs_init )
  {
    v5 = calloc(1uLL, 0x18uLL);
    v6 = v5;
    if ( v5 )
    {
      v5->key = key;
      v5->dtor = dtor;
      EnterCriticalSection(&_mingwthr_cs);
      v7 = key_dtor_list;
      key_dtor_list = v6;
      v6->next = v7;
      LeaveCriticalSection(&_mingwthr_cs);
      return 0;
    }
    else
    {
      return -1;
    }
  }
  return result;
}

//----- (0000000000402F40) ----------------------------------------------------
int __fastcall __w64_mingwthr_remove_key_dtor(DWORD key)
{
  volatile __mingwthr_key_t *v3; // rdx
  volatile __mingwthr_key_t *next; // rax
  volatile __mingwthr_key_t *v5; // rcx

  if ( !_mingwthr_cs_init )
    return 0;
  EnterCriticalSection(&_mingwthr_cs);
  v3 = key_dtor_list;
  if ( key_dtor_list )
  {
    if ( key_dtor_list->key == key )
    {
      v5 = key_dtor_list;
      key_dtor_list = key_dtor_list->next;
LABEL_12:
      free(v5);
      LeaveCriticalSection(&_mingwthr_cs);
      return 0;
    }
    while ( 1 )
    {
      next = v3->next;
      if ( !next )
        break;
      if ( next->key == key )
      {
        v5 = v3->next;
        v3->next = next->next;
        goto LABEL_12;
      }
      v3 = v3->next;
    }
  }
  LeaveCriticalSection(&_mingwthr_cs);
  return 0;
}

//----- (0000000000402FE0) ----------------------------------------------------
// local variable allocation has failed, the output may be wrong!
WINBOOL __fastcall _mingw_TLScallback(HANDLE hDllHandle, DWORD reason, LPVOID reserved)
{
  WINBOOL result; // eax

  if ( reason == 1 )
  {
    if ( !_mingwthr_cs_init )
      InitializeCriticalSection(&_mingwthr_cs);
    result = 1;
    _mingwthr_cs_init = 1;
  }
  else
  {
    if ( reason )
    {
      if ( reason == 3 )
      {
        if ( _mingwthr_cs_init )
          _mingwthr_run_key_dtors_part_0();
      }
    }
    else
    {
      if ( _mingwthr_cs_init )
        _mingwthr_run_key_dtors_part_0();
      if ( _mingwthr_cs_init == 1 )
      {
        _mingwthr_cs_init = 0;
        _IAT_start__(&_mingwthr_cs, *&reason, reserved);
      }
    }
    return 1;
  }
  return result;
}
// 402FE0: variables would overlap: edx.4 and rdx.8
// 409268: using guessed type __int64 __fastcall _IAT_start__(_QWORD, _QWORD, _QWORD);

//----- (00000000004030E0) ----------------------------------------------------
void (*__cdecl get_invalid_parameter_handler())(const wchar_t *, const wchar_t *, const wchar_t *, unsigned int, uintptr_t)
{
  return handler;
}

//----- (00000000004030F0) ----------------------------------------------------
void (*__fastcall set_invalid_parameter_handler(
        void (*new_handler)(const wchar_t *, const wchar_t *, const wchar_t *, unsigned int, uintptr_t)))(const wchar_t *, const wchar_t *, const wchar_t *, unsigned int, uintptr_t)
{
  return _InterlockedExchange64(&handler, new_handler);
}

// nfuncs=114 queued=48 decompiled=48 lumina nreq=0 worse=0 better=0
// ALL OK, 48 function(s) have been successfully decompiled
```

Exploit:
```c
#include <stdio.h>
#include <string.h>

char aSfmsilqzdxajhn[53] = "sfMSiLQzdXajhnZKrPyAoHbTDNREWtuVOcGIxkYemgBClvwFUpqJ"; // weak


int generaNumero(char *a1)
{
  int i; // [rsp+28h] [rbp-58h]
  int v3; // [rsp+2Ch] [rbp-54h]

  v3 = 0;
  for ( i = 0; i < strlen(a1); ++i )
    v3 += a1[i];
  printf("Numero: %d", v3 + 6572);
  return (v3 + 6572);
}

char *generaLetras(int a1, char *a2)
{
  size_t v2; // rax
  char *result; // rax
  int v4; // [rsp+28h] [rbp-58h]
  int v5; // [rsp+2Ch] [rbp-54h]
  int v6; // [rsp+30h] [rbp-50h]
  int v7; // [rsp+34h] [rbp-4Ch]

  v7 = (a1 + 15) % strlen("sfMSiLQzdXajhnZKrPyAoHbTDNREWtuVOcGIxkYemgBClvwFUpqJ");
  v6 = (a1 + 22) % strlen("sfMSiLQzdXajhnZKrPyAoHbTDNREWtuVOcGIxkYemgBClvwFUpqJ");
  v5 = (a1 + 32) % strlen("sfMSiLQzdXajhnZKrPyAoHbTDNREWtuVOcGIxkYemgBClvwFUpqJ");
  v4 = (a1 + 17) % strlen("sfMSiLQzdXajhnZKrPyAoHbTDNREWtuVOcGIxkYemgBClvwFUpqJ");
  v2 = strlen("sfMSiLQzdXajhnZKrPyAoHbTDNREWtuVOcGIxkYemgBClvwFUpqJ");
  *a2 = aSfmsilqzdxajhn[v7];
  a2[1] = aSfmsilqzdxajhn[v6];
  a2[2] = aSfmsilqzdxajhn[v5];
  a2[3] = aSfmsilqzdxajhn[v4];
  a2[4] = aSfmsilqzdxajhn[((a1 + 4) % v2)];
  result = a2 + 5;
  a2[5] = 0;
  return result;
}

int generaSerial(char *a1, char *a2)
{
  char v3[16]; // [rsp+40h] [rbp-50h] BYREF
  char v4[16]; // [rsp+50h] [rbp-40h] BYREF
  char v5[16]; // [rsp+60h] [rbp-30h] BYREF
  char v6[16]; // [rsp+70h] [rbp-20h] BYREF
  char v7[12]; // [rsp+80h] [rbp-10h] BYREF
  int v8; // [rsp+8Ch] [rbp-4h]

  v8 = generaNumero(a1);
  generaLetras(v8, v7);
  v8 = generaNumero(v7);
  generaLetras(v8, v6);
  v8 = generaNumero(v6);
  generaLetras(v8, v5);
  v8 = generaNumero(v5);
  generaLetras(v8, v4);
  v8 = generaNumero(v4);
  generaLetras(v8, v3);
  printf("\nEl serial es: %s-%s-%s-%s-%s\n", v7, v6, v5, v4, v3);
  return sprintf(a2, "%s-%s-%s-%s-%s", v7, v6, v5, v4, v3);
}

int main(){
  char *a1 = "A";
  char serial[32]; 
  printf("El nombre es: %s\n",a1);
  generaSerial(a1,serial);
}
```

![keygen](/img/keygen_si_puedes.png)

