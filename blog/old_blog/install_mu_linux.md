---
title: "Jugar a MU Bless Online en ArchLinux"
date: 2025-05-17T10:56:37-03:00
tags: ['games']
---

Descargá el juego y create la cuenta acá: https://mu.bless.gs/es/index.php?page=files

Habilitá el repositorio `multilib` libs de ArchLinux e instalá `wine`:
```bash
sudo pacman -S wine mesa lib32-mesa
wine Bless Arkania Episode 5 (27.03.2025).exe
wine .wine/drive_c/Games/Launcher.exe
```

El `Launcher.exe` te putea diciendo que falló en actualizarse pero si ejecutás el juego desde:
```bash
cd .wine/drive_c/Games/Bless Arkania Episode 5
wine play.exe
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiruxcNTDcMFPopQHGirP1Zsxmo_akahlS0VBQBOnZ3n69FqY2nyjf80FXWcCZItYQwP0OoSH7QZqZJv6CiUZGqQISoTQiQPEvLRL0IRFx5mmw6ba4KZ8Y7Pj8mpx-y4SZH4ZE4_3I7KQ2aq7LiD71nnuuUF9m8kPTfTbQdBbIoOrkzr5LgT32nfpMKoyNY/s1366/20250517_20h25m56s_grim.png)
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRrrmHMU5rv28IVJaLiFeyQW-6nu0weuUN8SLcns3fwavtm1L3dz_b9oX0Qf0jba60pkx5FDTUK1eXeJA6-u7GPPpO2IJtNEi2TCeLyOJ_rCCQVBNQcyExYV60k-6oIuALN4SYYEKGXDqounzXecGMLblhEbw84xjODKWPjK3G3hzfpsyldcrZWjMaRuuJ/s1366/20250517_20h34m37s_grim.png)

Funciona bajo wayland/sway.
