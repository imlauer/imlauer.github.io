---
title: "Aeneas"
date: 2025-12-24T00:29:37-03:00
draft: true
---



(aeneas) [esotericwarfare@arch nobloatnews.github.io]$ pip install aeneas
Collecting aeneas
  Using cached aeneas-1.7.3.0.tar.gz (5.5 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  error: subprocess-exited-with-error
  
  × Getting requirements to build wheel did not run successfully.
  │ exit code: 1
  ╰─> [3 lines of output]
      [ERRO] You must install numpy before installing aeneas
      [INFO] Try the following command:
      [INFO] $ sudo pip install numpy
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
ERROR: Failed to build 'aeneas' when getting requirements to build wheel
(aeneas) [esotericwarfare@arch nobloatnews.github.io]$ ls
aeneas           back_break_to_srt.sh  index.html   new.sh   posts    style.css  TODO
asfasdjfosi.txt  break_to_srt.sh       new_post.sh  new.txt  rss.xml  sub.py     youtube.fish
(aeneas) [esotericwarfare@arch nobloatnews.github.io]$ yay -Ss aeneas
(aeneas) [esotericwarfare@arch nobloatnews.github.io]$ pip install numpy
Requirement already satisfied: numpy in ./aeneas/lib/python3.13/site-packages (2.4.0)
(aeneas) [esotericwarfare@arch nobloatnews.github.io]$ sudo pip
sudo: pip: command not found
(aeneas) [esotericwarfare@arch nobloatnews.github.io]$ 


Ah, esto es un clásico problema en ArchLinux (y en general en entornos virtuales) al instalar `aeneas`. Vamos a analizarlo paso a paso:

---

### Lo que está pasando

1. `aeneas` requiere **`numpy`** instalado **antes** de compilar.
2. Tu entorno virtual ya tiene `numpy`:

   ```
   Requirement already satisfied: numpy in ./aeneas/lib/python3.13/site-packages (2.4.0)
   ```
3. Pero el instalador de `aeneas` no detecta `numpy` porque **intenta usar pip global (sudo pip)**, que no existe en tu sistema (`sudo: pip: command not found`).

> En ArchLinux, `pip` para sudo es `python-pip` o hay que usar `python -m pip`.

---

### Cómo solucionarlo

1. **Instala las dependencias del sistema**

   Arch requiere paquetes de compilación para `aeneas` (C++ y espeak):

   ```bash
   sudo pacman -S base-devel ffmpeg espeak python-pip
   ```

   * `base-devel` → herramientas de compilación (gcc, make, etc.)
   * `ffmpeg` → usado por `aeneas` para audio
   * `espeak` → motor de TTS requerido
   * `python-pip` → para poder usar `sudo python -m pip` si es necesario

2. **Usa el pip del virtualenv**
   No necesitas sudo si estás dentro del entorno virtual (`aeneas`). Haz:

   ```bash
   python -m pip install --upgrade pip setuptools wheel
   python -m pip install aeneas
   ```

   Esto fuerza a `aeneas` a usar tu `numpy` ya instalado en el virtualenv y evita el error de “sudo pip not found”.

3. **Si sigue fallando**, explícitamente instala `numpy` primero en el entorno virtual:

   ```bash
   python -m pip install numpy==1.26
   python -m pip install aeneas
   ```

   > Nota: Algunas versiones recientes de `numpy` pueden dar problemas; si `2.4.0` falla, baja a `1.26`.

---

💡 Tip extra: Nunca uses `sudo pip install` en ArchLinux a menos que sea necesario para el pip global; dentro de un virtualenv no es necesario.

---

Si querés, puedo pasarte **la línea exacta que debería funcionar desde tu entorno virtual de Arch** para instalar `aeneas` sin errores.

¿Querés que haga eso?

