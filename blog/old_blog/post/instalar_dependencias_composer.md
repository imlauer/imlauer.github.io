---
title: "Instalar dependencias de un proyecto con composer"
date: 2024-09-22T19:43:07-03:00
tags: ['composer']
---

https://stackoverflow.com/questions/20115757/how-to-install-dependencies-or-use-composer-at-all-in-windows

Ahora, cree el archivo `composer.json` en el mismo nivel donde tiene el directorio de `Vendor` (no dentro de `Vendor`).

Vaya al directorio donde tiene compositor.json con el símbolo del sistema y ejecute el siguiente comando:

```bash
composer install
```

Mostrará mensajes como "packages are downloading" y "autoload.php file created". (Compruebe su directorio /app/Vendor/)

Ahora inserte este código al comienzo de `/app/config/core.php`:

```bash
require_once nombredir(__DIR__) . '/Vendedor/autoload.php';
```

El código anterior cargará todas las clases automáticamente.
