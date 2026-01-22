---
title: "Debug crashing binary en Windows con WinDbg"
date: 2025-11-02T14:49:49-03:00
tags: ['exe']
---

##### Al final era el audio que no estaba conectado por eso el juego Richard Burns Rally crasheaba nada que ver todo lo demas.

##### Conectamos un auricular al puerto trasero de la PC y el juego funcionó y estaba mal la resolución tenías que configurar desde el 2do launcher que estaba en la carpeta.

Cuando iniciamos el juego se creo un archivo CRASHDUMP pero esto lo hizo despues que instalemos Windbg se creo un archivo parecido al que dice este video:

https://www.youtube.com/embed/wdHLuB4lkgg


### 1️⃣ Preparar el entorno

* **Modo de depuración:** Usa una cuenta con permisos de administrador si es posible.
* **Desactiva antivirus temporalmente** para descartar que esté bloqueando el juego.
* **Modo de compatibilidad:** A veces ejecutar en modo Windows 7/8 ayuda, pero para debug profundo no es crítico.

---

### 2️⃣ Usar un depurador en Windows

#### a) **WinDbg (de Microsoft)**

1. Instala **WinDbg** desde el [Windows SDK](https://learn.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk).
2. Abre WinDbg → `File → Open Executable`.
3. Selecciona el `.exe` del juego.
4. WinDbg lanzará el juego y podrás ver **excepciones**, **fallos de memoria**, o errores de librerías.
5. Usa `!analyze -v` después de un crash para obtener un stack trace detallado.

#### b) **Visual Studio**

Si tienes Visual Studio:

1. Abre **Visual Studio → File → Open → Project/Solution → select EXE**.
2. Ve a **Debug → Start Debugging (F5)**.
3. Cuando el juego falle, Visual Studio mostrará la línea exacta y call stack (si los símbolos están disponibles).

#### c) **Depuración ligera / logs**

* A veces los juegos generan **logs internos** en:

  * `C:\Users\<usuario>\AppData\Local\<Juego>\`
  * Carpeta del juego (`logs`, `crashdumps`)
* Activar **modo ventana** o agregar flags tipo `-debug` puede generar más información.

---

### 3️⃣ Usar herramientas externas

* **Process Monitor (ProcMon)**: rastrea acceso a archivos y registro, útil si el juego falla al cargar algo.
* **Dependency Walker**: identifica DLL faltantes que pueden provocar cierre inmediato.
* **Dr. Memory / AddressSanitizer**: detecta corrupciones de memoria, si el juego es compatible con depuración nativa.

---

### 4️⃣ Símbolos y stack traces

* Para ver **llamadas de función humanas**, necesitas símbolos (`.pdb`) del juego.
* Sin símbolos, aún puedes ver direcciones de memoria y DLLs implicadas.

---

### 5️⃣ Estrategia rápida de prueba

1. Ejecuta en CMD y observa errores impresos:

   ```cmd
   "C:\ruta\al\juego.exe"
   ```

   A veces sale un mensaje en consola antes de cerrar.
2. Habilita **crash dumps automáticos**:

   ```reg
   Windows Registry → HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting
   ```

   Así podrás abrir el dump con WinDbg.

---

💡 **Tip práctico:** Si quieres algo rápido sin WinDbg, puedes usar **x64dbg** (free, open source) para attach al juego, ejecutar y ver exactamente dónde falla.

---

Si quieres, puedo hacer una **guía concreta paso a paso con x64dbg** para abrir el binario del juego y capturar el crash, lista para principiantes en depuración de juegos en Windows.

¿Quieres que haga eso?


When a game closes by itself in **Windows 10** with no error message, you can debug it by checking logs, system resources, and drivers. Here's a step-by-step troubleshooting + debugging method:

---

## ✅ **1. Check Windows Event Viewer (Crash Logs)**

1. Press **Win + R**
2. Type: `eventvwr.msc`
3. Go to:

   ```
   Windows Logs → Application
   ```
4. Look for **Error** entries around the time of the crash (usually Application Error).

Common faulting modules:

| Module                   | Meaning                |
| ------------------------ | ---------------------- |
| `nvlddmkm.dll`           | NVIDIA driver crash    |
| `atidxx64.dll`           | AMD GPU driver crash   |
| `d3d11.dll` / `dxgi.dll` | DirectX crash          |
| `ucrtbase.dll`           | VC++ runtime crash     |
| `ntdll.dll`              | Windows internal error |

Tell me what you find there if you want help reading it.

---

## ✅ **2. Run the game with Debug Logging**

Some games support launch options like:

* `-log`
* `-debug`
* `-d3d11` / `-dx12`

You can also enable **Windows crash logs**:

1. Search *Windows Reliability Monitor*
2. See game crash history
3. Click **View Technical Details**

---

## ✅ **3. Update / Reinstall Graphics Drivers**

For NVIDIA:

```
Download from NVIDIA → Clean Install
(Optional) Use DDU in Safe Mode
```

For AMD:

```
Use AMD Cleanup Utility + latest driver
```

---

## ✅ **4. Check Missing Runtime Libraries**

Install/reinstall:

### Microsoft Visual C++ Redistributables

[https://aka.ms/vs/17/release/vc_redist.x64.exe](https://aka.ms/vs/17/release/vc_redist.x64.exe)
[https://aka.ms/vs/17/release/vc_redist.x86.exe](https://aka.ms/vs/17/release/vc_redist.x86.exe)

### DirectX Runtimes

[https://www.microsoft.com/en-us/download/details.aspx?id=8109](https://www.microsoft.com/en-us/download/details.aspx?id=8109)

### .NET Framework

Windows Update usually installs this.

---

## ✅ **5. Check GPU / CPU / RAM Health**

### **GPU / CPU Temps**

Use **MSI Afterburner** / **HWInfo**

* GPU should be < 85°C
* CPU < 90°C

### **RAM Test**

Run:

```
mdsched.exe
```

---

## ✅ **6. Disable Overlays & Background Apps**

Turn off:

* Discord overlay
* Steam overlay
* Xbox Game Bar
* MSI Afterburner OSD
* GeForce Experience overlay

---

## ✅ **7. Try Compatibility / Admin Mode**

Right-click game EXE → **Properties**:

* Run as administrator
* Disable fullscreen optimizations
* Compatibility mode Windows 7/8 (only sometimes helps)

---

## ✅ **8. Check Game Folder Integrity**

Steam:

```
Steam → Game → Properties → Verify Integrity of Files
```

Epic:

```
Library → three dots → Verify
```

---

## ✅ **9. Memory Leak / VRAM Debug**

Open **Task Manager → Performance Tab**

Watch:

* GPU memory usage
* CPU usage
* RAM usage

If a resource spikes then game dies → that's your culprit.

---

## ✅ If It Still Crashes — Advanced Debugging

### Windows Debugging Tools

Install:

```
Windows SDK → Debugging Tools for Windows
```

Run:

```
WinDbg (Preview)
```

Load crash dump from:

```
C:\Windows\Minidump
```

If you want, tell me the game's crash `.dmp` file results and I'll interpret them.

---

## ✅ Tell me what info you want to provide:

Reply with any of these:

### ⬜ Event Viewer error text

### ⬜ Reliability Monitor details

### ⬜ GPU / CPU temps

### ⬜ Game name & launcher (Steam/Epic/etc.)

### ⬜ Specs (CPU, GPU, RAM)

### ⬜ Crash dump file (I'll help read it)

---

If you want, I can give you:

* **WinDbg command guide**
* A **script to monitor real-time crash logs**
* **Anti-cheat crash troubleshooting** (Valorant, Apex, CS2, etc.)

---

Want to start with the **Event Viewer crash logs**? Paste them here 👇


---

Richard Burns Rally (RBR) is very old (2004) and often crashes on Windows 10 due to graphics + compatibility issues and modern mod loaders (RBRCIT / RBR Pro / RallySimFans).

Here’s a clean step-by-step way to **debug + fix** crashes.

---

## ✅ **1. Check if you're running modded or original**

Which one are you using?

| Version             | Notes                              |
| ------------------- | ---------------------------------- |
| Original CD/digital | Runs with fixes                    |
| RallySimFans Mod    | Very stable if installed correctly |
| RBRPro              | Can be unstable                    |
| RBRCIT + plugins    | Depends on DLL plugins             |

> Tell me which version you're using — fixes differ.

---

## ✅ **2. Enable Logs**

### 📂 RBR log location

Check for crash logs in:

```
Richard Burns Rally\RichardBurnsRally.ini
```

Enable logging by adding:

```
LOG = 1
```

Then check `RichardBurnsRally.log` after crash.

---

## ✅ **3. Check Event Viewer**

Find crashing module:

1. `Win + R` → `eventvwr.msc`
2. Windows Logs → **Application**
3. Look for “RichardBurnsRally_SSE.exe” error

Common fault modules:

| Faulting DLL                   | Meaning                             |
| ------------------------------ | ----------------------------------- |
| `d3d9.dll`                     | DX9 wrapper / graphics plugin crash |
| `dinput.dll`                   | Input plugin crash                  |
| `mss32.dll`                    | Audio engine crash                  |
| `nvd3dum.dll` / `atidxx64.dll` | GPU driver crash                    |

Paste the event error here and I’ll read it.

---

## ✅ **4. Install Required RBR Fixes**

### DirectX 9 Legacy

Install **DirectX June 2010** runtime:
[https://www.microsoft.com/en-us/download/details.aspx?id=8109](https://www.microsoft.com/en-us/download/details.aspx?id=8109)

### Microsoft Visual C++ Runtimes

Install:

* 2005 → 2022 x86 and x64

### Run as Administrator + Disable Fullscreen Optimizations

Right-click → Properties → Compatibility:

✔ Run as admin
✔ Disable fullscreen optimizations

(Optional) set to Windows XP SP3

---

## ✅ **5. GPU Compatibility**

### NVIDIA users

* Enable **NVIDIA Control Panel → Power Management = Prefer maximum performance**
* Disable **DSR**
* Do not force Antialiasing

### AMD users

* Disable Radeon Anti-Lag
* Disable Radeon Boost
* Disable Enhanced Sync

---

## ✅ **6. Common Fixes for Crashes**

### ✔ d3d9 wrapper (essential)

Download **dgVoodoo2** and place these in game folder:

```
d3d8.dll
d3d9.dll
D3DImm.dll
DDraw.dll
```

Configure:

* API = DirectX 11
* VRAM = 256MB–512MB

RBR is very picky; this fix alone stops 90% crashes.

---

### ✔ Audio Crash Fix

Copy `mss32.dll` from a known working RBR installation or reinstall sound drivers.

---

### ✔ Plugin / DLL problems

Trouble mods/plugins?
Rename plugin folder:

```
Richard Burns Rally\Plugins → Plugins.off
```

Test game — if works, a plugin is crashing it.

---

## ✅ **7. Modern Community Installer (best long-term)**

If you want the best stability:

| Installer            | Link                                                                           |
| -------------------- | ------------------------------------------------------------------------------ |
| **RallySimFans RBR** | [https://rallysimfans.hu/rbr/index.php](https://rallysimfans.hu/rbr/index.php) |

RSF RBR fixes almost all compatibility issues automatically.

---

## ✅ **8. Memory / Run Windowed to Debug**

Add to `RichardBurnsRally.ini`:

```
FULLSCREEN=0
```

Also cap framerate (60 or 90) — unlimited FPS crashes physics sometimes.

---

## ✅ Tell me what to send me to diagnose it

Reply with:

* Event Viewer crash info
* Whether you use mods (which?)
* GPU, CPU, RAM
* If you use Intel, AMD, or Nvidia graphics
* Your `RichardBurnsRally.log` if exists

You paste, I read it 👍

---

Want me to guide you through opening Event Viewer and reading the crash entry step-by-step?

