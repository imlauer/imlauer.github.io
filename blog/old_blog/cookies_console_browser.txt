---
title: "Loading cookies from Falkon into a console web-browser or yt-dlp."
date: 2025-10-17T15:24:32-03:00
tags: ['console']
---

```bash
cp ~/.config/falkon/profiles/default/Cookies /tmp/falkon_cookies.sqlite
```

```bash
sqlite3 -separator $'\t' -noheader /tmp/falkon_cookies.sqlite "SELECT host_key,
 CASE WHEN host_key LIKE '.%' THEN 'TRUE' ELSE 'FALSE' END,
 path,
 CASE WHEN is_secure=1 THEN 'TRUE' ELSE 'FALSE' END,
 CAST((expires_utc/1000000.0 - 11644473600) AS INTEGER),
 name,
 value
FROM cookies;" > ~/cookies_netscape.txt
```

```bash
curl -v -L -b ~/cookies_netscape.txt -c ~/cookies_out.txt "https://inv.nadeko.net/" -o /tmp/forum.html && w3m /tmp/forum.html
curl -v -L -b ~/cookies_out.txt  "https://inv.nadeko.net/" -o /tmp/forum.html && w3m /tmp/forum.html

#### Ahora usamos las cookies para descargar videos o el instagram de una persona.

$ yt-dlp --cookies cookies_out.txt
$ gallery-dl --cookies ~/cookies_out.txt https://instagram.com/user

```

##### Para iniciarlo con startx (twm)


echo "exec twm" > .xinitrc


## w3m no usa un formato de netscape si queres cargar las cookies de Falkon a netscape: (lo que está abajo no me funcionó).

Perfecto — gracias por la aclaración. Te doy **una solución práctica (lista para ejecutar)** que hace esto:

1. localiza la base de datos de cookies de Falkon,
2. extrae las cookies de la tabla SQLite (formato Chromium/QtWebEngine),
3. las convierte al **formato tipo w3m** (una línea por cookie: URL <TAB> NAME <TAB> VALUE <TAB> EXPIRY <TAB> DOMAIN <TAB> PATH <TAB> HTTPONLY),
4. y te deja el fichero listo para copiar a `~/.w3m/cookie`.

También incluyo notas importantes (cookies cifradas, cerrar Falkon, cómo convertir la marca de tiempo).

---

# 1) Buscar el fichero de cookies de Falkon

En muchos navegadores basados en QtWebEngine/Chromium las cookies están en un fichero SQLite llamado `Cookies` o `cookies`. Busca así:

```bash
# busca en ~/.config y ~/.local por ficheros que se llamen "Cookies" o "cookies*"
find ~/.config ~/.local -type f \( -iname Cookies -o -iname 'cookies*' \) 2>/dev/null
```

Si aparece algo como `~/.config/falkon/Default/Cookies` o `~/.local/share/falkon/Network/Cookies` ese es el fichero que necesitamos.

> Consejo: **cierra Falkon** antes de trabajar con la base de datos (está bloqueada mientras el navegador corre).

---

# 2) Script Python que extrae y convierte a formato w3m

Crea un archivo `falkon_cookies_to_w3m.py` con este contenido (usa Python 3):

```python
#!/usr/bin/env python3
# falkon_cookies_to_w3m.py
#
# Extrae cookies desde una DB tipo Chromium (tabla `cookies`) y emite líneas:
# <url>\t<name>\t<value>\t<expiry_unix>\t<domain>\t<path>\t<httponly_flag>\n
#
# Uso:
#   python3 falkon_cookies_to_w3m.py /ruta/al/fichero/Cookies > cookies_w3m.txt

import sys, sqlite3, os, urllib.parse, datetime

if len(sys.argv) != 2:
    print("Uso: python3 falkon_cookies_to_w3m.py /ruta/al/fichero/Cookies", file=sys.stderr)
    sys.exit(2)

dbpath = sys.argv[1]
if not os.path.exists(dbpath):
    print("No existe:", dbpath, file=sys.stderr)
    sys.exit(3)

def webkit_to_unix(webkit_us):
    # Chrome/WebKit timestamps son microsegundos desde 1601-01-01
    try:
        us = int(webkit_us)
    except:
        return 0
    if us == 0:
        return 0
    return int(us/1_000_000 - 11644473600)

con = sqlite3.connect(dbpath)
con.text_factory = lambda b: b.decode(errors='ignore')
cur = con.cursor()

# Intenta columnas comunes en 'cookies' de Chromium: host_key, name, value, path, expires_utc, secure, httponly, encrypted_value
cols_try = ["host_key","name","value","path","expires_utc","secure","httponly","encrypted_value"]
# Query defensiva: selecciona sólo columnas que existan
cur.execute("PRAGMA table_info(cookies)")
tblinfo = [r[1] for r in cur.fetchall()]
present = [c for c in cols_try if c in tblinfo]

select_cols = ", ".join(present)
q = f"SELECT {select_cols} FROM cookies"
for row in cur.execute(q):
    # mapear por orden
    d = dict(zip(present, row))
    host = d.get("host_key","")
    name = d.get("name","")
    # si 'value' vacío, intentar 'encrypted_value' (no intentamos descifrar aquí)
    value = d.get("value") or d.get("encrypted_value") or ""
    path = d.get("path") or "/"
    expires = webkit_to_unix(d.get("expires_utc") or 0)
    secure = 1 if d.get("secure") else 0
    httponly = 1 if d.get("httponly") else 0

    # construir URL base (scheme asumido https si secure, sino http)
    scheme = "https" if secure else "http"
    # si host no empieza por dominio, limpiarlo
    host_clean = host.lstrip(".")
    url = f"{scheme}://{host_clean}{path}"
    # escape tabs/newlines en name/value
    safe_name = name.replace("\t","\\t").replace("\n","\\n")
    safe_value = value.replace("\t","\\t").replace("\n","\\n")

    print(f"{url}\t{safe_name}\t{safe_value}\t{expires}\t{host_clean}\t{path}\t{httponly}")

con.close()
```

Haz ejecutable y ejecútalo:

```bash
chmod +x falkon_cookies_to_w3m.py
./falkon_cookies_to_w3m.py /ruta/al/fichero/Cookies > cookies_w3m.txt
```

---

# 3) Resultado y prueba con w3m

El fichero `cookies_w3m.txt` tendrá líneas similares a tu ejemplo (pero con `path` y `httponly` al final). Para usarlo con w3m:

```bash
# copia al fichero que w3m usa (~/.w3m/cookie)
mkdir -p ~/.w3m
cp cookies_w3m.txt ~/.w3m/cookie
# prueba
w3m https://inv.nadeko.net
```

Si w3m usa exactamente la columna final como en tu ejemplo (`5 0`), y prefieres tener esos valores fijos, modifica el `print(...)` en el script para imprimir `\t5\t0` en lugar de `\t{path}\t{httponly}`.

---

# 4) Notas importantes / problemas comunes

* **No abrir la DB con el navegador en ejecución.** Copia el fichero `Cookies` antes de leerlo si no quieres cerrar Falkon:

  ```bash
  cp /ruta/al/Cookies /tmp/Cookies.copy
  ./falkon_cookies_to_w3m.py /tmp/Cookies.copy > cookies_w3m.txt
  ```

* **Valores en `encrypted_value`:** algunos navegadores (Chromium en Linux/Windows) guardan el valor cifrado en `encrypted_value` y la columna `value` puede estar vacía. El script copia `encrypted_value` si `value` está vacío — **pero no lo descifra**. Descifrarlo requiere acceder a la clave de cifrado del sistema (DPAPI / Keyring) y código adicional (platform-specific). Si ves valores binarios / no legibles, probablemente estén cifrados.

* **Conversión de fecha:** Chromium usa microsegundos desde `1601-01-01` (WebKit time). El script convierte `expires_utc` a UNIX epoch (segundos). Fuentes: explicación sobre `expires_utc` y conversión. ([Stack Overflow][1])

* **Formato exacto de w3m:** en tu ejemplo la última columna era `5 0`. Hay ligeras variantes entre versiones/compilaciones; por eso el script emite `path` y `httponly`. Si w3m en tu sistema **requiere** exactamente dos números al final (ej. `5 0`), dime y ajusto el `print()` para que produzca ese patrón fijo.

---

# 5) Si quieres, hago esto por vos ahora

Puedo:

* darte la versión del script que **forza** el formato exactamente igual a tu ejemplo (con `5 0`),
* o modificarlo para **intentar descifrar** `encrypted_value` si usás Linux (requiere `pycryptodomex` y leer la clave de GNOME/ KDE keyring — puedo darte pasos).

¿Cuál preferís? ¿Que genere las líneas con `5 0` fijas (para que coincida *exactamente* con tu ejemplo), o que use `path`+`httponly` como en el script?

[1]: https://stackoverflow.com/questions/43518199/cookies-expiration-time-format?utm_source=chatgpt.com "Cookies expiration time format - google chrome"

