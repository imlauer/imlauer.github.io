---
title: "Chromium headless w3m"
date: 2025-12-31T13:45:04-03:00
---

Intentamos renderizar upwork.com con headless chromium, a ver donde nos lleva
Como siempre Cloudflare arruinando Internet y bloqueando todo.


The issue you're facing is that Cloudflare is detecting your headless browser and blocking it. Here are several solutions:

## Quick Fixes

**1. Add user agent and disable headless detection:**
```bash
chromium --headless=new --user-data-dir=$HOME/.config/chromium-headless --disable-gpu --disable-blink-features=AutomationControlled --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" --dump-dom --virtual-time-budget=10000 "$1" | sed "s|<head>|<head><base href=$1>|g" | w3m -T text/html
```

Key changes:
- `--headless=new` - Uses newer headless mode that's harder to detect
- `--disable-blink-features=AutomationControlled` - Removes automation flags
- Custom user agent that looks like a real browser
- **Different user-data-dir** to avoid conflicts with your open Chromium

**2. Increase wait time for JavaScript execution:**
```bash
chromium --headless=new --user-data-dir=$HOME/.config/chromium-headless --disable-gpu --disable-blink-features=AutomationControlled --virtual-time-budget=30000 --dump-dom "$1" | sed "s|<head>|<head><base href=$1>|g" | w3m -T text/html
```

Increase `--virtual-time-budget` to 30000 (30 seconds) or more.

**3. Use a separate profile (fixes the conflict with open Chromium):**
```bash
chromium --headless=new --user-data-dir=/tmp/chromium-w3m --disable-gpu --disable-blink-features=AutomationControlled --dump-dom --virtual-time-budget=15000 "$1" | sed "s|<head>|<head><base href=$1>|g" | w3m -T text/html
```

## Alternative Approaches

**Use Playwright or Puppeteer with stealth plugins** (more reliable for Cloudflare):
```bash
# Install playwright
pip install playwright
playwright install chromium

# Simple script (save as fetch.py):
from playwright.sync_api import sync_playwright
import sys

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(sys.argv[1], wait_until='networkidle')
    print(page.content())
    browser.close()
```

Then use: `python fetch.py "$1" | w3m -T text/html`

**Use curl with JavaScript rendering services:**
Some sites offer APIs that render JavaScript, though this depends on your use case.

The main issue is Cloudflare's bot detection. The separate `--user-data-dir` should fix your "cannot use while chromium is open" problem, and the anti-detection flags should help with Cloudflare.


#### Para scrollear la pagina:

Para hacer scroll en la página antes de hacer el dump del DOM, necesitas usar un script. Aquí tienes varias opciones:

## Opción 1: Script simple de Node.js con Puppeteer

```bash
npm install puppeteer puppeteer-extra puppeteer-extra-plugin-stealth
```

Crea un archivo `scroll-fetch.js`:

```javascript
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  const page = await browser.newPage();
  await page.goto(process.argv[2], { waitUntil: 'networkidle2', timeout: 30000 });
  
  // Scroll gradualmente
  await page.evaluate(async () => {
    await new Promise((resolve) => {
      let totalHeight = 0;
      const distance = 100;
      const timer = setInterval(() => {
        const scrollHeight = document.body.scrollHeight;
        window.scrollBy(0, distance);
        totalHeight += distance;
        
        if(totalHeight >= scrollHeight){
          clearInterval(timer);
          resolve();
        }
      }, 100);
    });
  });
  
  // Esperar un poco más después del scroll
  await page.waitForTimeout(2000);
  
  const html = await page.content();
  console.log(html);
  
  await browser.close();
})();
```

Úsalo así:
```bash
node scroll-fetch.js "$1" | w3m -T text/html
```

## Opción 2: Script Python con Playwright

Crea `scroll-fetch.py`:

```python
from playwright.sync_api import sync_playwright
import sys
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(sys.argv[1], wait_until='networkidle', timeout=30000)
    
    # Scroll gradual
    page.evaluate("""
        () => {
            return new Promise((resolve) => {
                let totalHeight = 0;
                let distance = 100;
                let timer = setInterval(() => {
                    window.scrollBy(0, distance);
                    totalHeight += distance;
                    
                    if(totalHeight >= document.body.scrollHeight){
                        clearInterval(timer);
                        resolve();
                    }
                }, 100);
            });
        }
    """)
    
    time.sleep(2)
    print(page.content())
    browser.close()
```

Úsalo así:
```bash
python scroll-fetch.py "$1" | w3m -T text/html
```

## Opción 3: Con Chrome DevTools Protocol directamente

Si prefieres seguir usando chromium directamente, puedes crear un script que use CDP:

```bash
#!/bin/bash
# scroll-chrome.sh

URL="$1"
PORT=9222

# Inicia Chrome en modo headless con debugging
chromium --headless=new --remote-debugging-port=$PORT --user-data-dir=/tmp/chrome-scroll &
CHROME_PID=$!

sleep 2

# Usa curl para enviar comandos CDP
python3 << EOF
import json, requests, time

# Obtener la lista de targets
tabs = requests.get('http://localhost:$PORT/json').json()
ws_url = tabs[0]['webSocketDebuggerUrl']

# Aquí necesitarías websocket para comandos más complejos
# O usar una herramienta como chrome-remote-interface

EOF

kill $CHROME_PID
```

## Opción 4: Solución más simple con delay

Si solo necesitas que cargue más contenido lazy-load:

```bash
chromium --headless=new \
  --user-data-dir=/tmp/chromium-w3m \
  --disable-gpu \
  --disable-blink-features=AutomationControlled \
  --virtual-time-budget=30000 \
  --dump-dom \
  "$1" | sed "s|<head>|<head><base href=$1>|g" | w3m -T text/html
```

Aumenta `--virtual-time-budget` a 30000-60000 ms.

**Recomendación:** La opción con Puppeteer o Playwright (opciones 1 y 2) es la más confiable para Cloudflare y te da control total sobre el scroll. ¿Cuál prefieres probar?



```bash
#chromium --headless $1 --disable-gpu --run-all-compositor-stages-before-draw --dump-dom --virtual-time-budget=10000 | sed "s|<head>|<head><base href=$1>|g" | w3m -T text/html

#chromium --headless --user-data-dir=$HOME/.config/chromium --profile-directory=Default --disable-gpu --run-all-compositor-stages-before-draw --dump-dom --virtual-time-budget=10000 "$1" | sed "s|<head>|<head><base href=$1>|g" | w3m -T text/html

#chromium --headless=new --user-data-dir=$HOME/.config/chromium-headless --disable-gpu --disable-blink-features=AutomationControlled --virtual-time-budget=30000 --dump-dom "$1" | sed "s|<head>|<head><base href=$1>|g" | w3m -T text/html

#chromium --headless=new --user-data-dir=$HOME/.config/chromium-headless --disable-gpu --disable-blink-features=AutomationControlled --virtual-time-budget=30000 --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" --dump-dom --virtual-time-budget=10000 "$1" | sed "s|<head>|<head><base href=$1>|g" | w3m -T text/html

#chromium --headless $1 --run-all-compositor-stages-before-draw --dump-dom --virtual-time-budget=10000 | monolith - -I -b $1 | w3m -T text/html

source $HOME/playwright/bin/activate

python $HOME/playwright/fetch.py "$1" | w3m -T text/html
```



Perfecto. Aquí tienes la solución completa con Playwright para usar las cookies de tu Chromium:

## Opción 1: Usar tu perfil de Chromium directamente (Chromium cerrado)

```python
from playwright.sync_api import sync_playwright
import sys
import os

with sync_playwright() as p:
    # Usar tu perfil de Chromium
    browser = p.chromium.launch_persistent_context(
        user_data_dir=os.path.expanduser('~/.config/chromium'),
        headless=False,  # Debe ser False para usar perfil persistente
        channel='chromium',
        args=[
            '--profile-directory=Default',
            '--disable-blink-features=AutomationControlled'
        ]
    )
    
    page = browser.pages[0] if browser.pages else browser.new_page()
    page.goto(sys.argv[1], wait_until='networkidle', timeout=30000)
    
    # Scroll gradual
    page.evaluate("""
        () => {
            return new Promise((resolve) => {
                let totalHeight = 0;
                let distance = 100;
                let timer = setInterval(() => {
                    window.scrollBy(0, distance);
                    totalHeight += distance;
                    
                    if(totalHeight >= document.body.scrollHeight){
                        clearInterval(timer);
                        resolve();
                    }
                }, 100);
            });
        }
    """)
    
    page.wait_for_timeout(2000)
    print(page.content())
    browser.close()
```

**Nota:** Chromium debe estar cerrado para usar esto.

## Opción 2: Exportar e importar cookies automáticamente

```python
from playwright.sync_api import sync_playwright
import sys
import os
import sqlite3
import struct
from urllib.parse import urlparse

def get_chromium_cookies(url):
    """Extrae cookies de Chromium sin encriptación compleja"""
    domain = urlparse(url).netloc
    cookie_db = os.path.expanduser('~/.config/chromium/Default/Cookies')
    
    # Copiar la base de datos porque puede estar bloqueada
    import shutil
    temp_db = '/tmp/cookies_copy.db'
    shutil.copy2(cookie_db, temp_db)
    
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    
    # Buscar cookies del dominio
    cursor.execute("""
        SELECT host_key, name, encrypted_value, path, expires_utc, is_secure, is_httponly, samesite
        FROM cookies 
        WHERE host_key LIKE ?
    """, (f'%{domain}%',))
    
    cookies = []
    for row in cursor.fetchall():
        # encrypted_value puede estar en formato v10 o v11 (Chrome/Chromium en Linux)
        encrypted_value = row[2]
        
        # Intentar obtener el valor (puede estar sin encriptar en algunos casos)
        # Nota: En producción necesitarías libsecret para desencriptar
        try:
            # Si comienza con 'v10' o 'v11', está encriptado
            if encrypted_value[:3] in [b'v10', b'v11']:
                # Aquí necesitarías la clave de encriptación
                # Por simplicidad, saltamos cookies encriptadas
                continue
            else:
                value = encrypted_value.decode('utf-8', errors='ignore')
        except:
            continue
            
        cookies.append({
            'name': row[1],
            'value': value,
            'domain': row[0],
            'path': row[3],
            'expires': row[4] / 1000000 - 11644473600 if row[4] > 0 else -1,
            'httpOnly': bool(row[6]),
            'secure': bool(row[5]),
            'sameSite': ['None', 'Lax', 'Strict'][row[7]] if row[7] >= 0 else 'None'
        })
    
    conn.close()
    os.remove(temp_db)
    return cookies

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    
    # Intentar cargar cookies
    try:
        cookies = get_chromium_cookies(sys.argv[1])
        if cookies:
            context.add_cookies(cookies)
    except Exception as e:
        print(f"Warning: No se pudieron cargar cookies: {e}", file=sys.stderr)
    
    page = context.new_page()
    page.goto(sys.argv[1], wait_until='networkidle', timeout=30000)
    
    # Scroll
    page.evaluate("""
        () => {
            return new Promise((resolve) => {
                let totalHeight = 0;
                let distance = 100;
                let timer = setInterval(() => {
                    window.scrollBy(0, distance);
                    totalHeight += distance;
                    
                    if(totalHeight >= document.body.scrollHeight){
                        clearInterval(timer);
                        resolve();
                    }
                }, 100);
            });
        }
    """)
    
    page.wait_for_timeout(2000)
    print(page.content())
    browser.close()
```

## Opción 3: Método manual (más confiable)

**Paso 1:** Exportar cookies manualmente con una extensión de Chromium

**Paso 2:** Crear el script:

```python
from playwright.sync_api import sync_playwright
import sys
import json

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=['--disable-blink-features=AutomationControlled']
    )
    
    context = browser.new_context()
    
    # Cargar cookies desde archivo JSON
    try:
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)
            context.add_cookies(cookies)
    except FileNotFoundError:
        print("Warning: cookies.json not found", file=sys.stderr)
    
    page = context.new_page()
    page.goto(sys.argv[1], wait_until='networkidle', timeout=30000)
    
    # Scroll gradual
    page.evaluate("""
        () => {
            return new Promise((resolve) => {
                let totalHeight = 0;
                let distance = 100;
                let timer = setInterval(() => {
                    window.scrollBy(0, distance);
                    totalHeight += distance;
                    
                    if(totalHeight >= document.body.scrollHeight){
                        clearInterval(timer);
                        resolve();
                    }
                }, 100);
            });
        }
    """)
    
    page.wait_for_timeout(2000)
    print(page.content())
    browser.close()
```

## Opción 4: Con desencriptación de cookies (requiere pycryptodome)

```bash
pip install pycryptodome secretstorage
```

```python
from playwright.sync_api import sync_playwright
import sys
import os
import sqlite3
import secretstorage
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from urllib.parse import urlparse
import shutil

def get_encryption_key():
    """Obtiene la clave de encriptación de Chromium en Linux"""
    bus = secretstorage.dbus_init()
    collection = secretstorage.get_default_collection(bus)
    
    for item in collection.get_all_items():
        if item.get_label() == 'Chrome Safe Storage':
            return item.get_secret()
    
    # Fallback: password por defecto
    return b'peanuts'

def decrypt_cookie(encrypted_value, key):
    """Desencripta una cookie de Chromium"""
    if encrypted_value[:3] == b'v10':
        # Usar PBKDF2 para derivar la clave
        salt = b'saltysalt'
        iv = b' ' * 16
        length = 16
        
        derived_key = PBKDF2(key, salt, length, 1)
        cipher = AES.new(derived_key, AES.MODE_CBC, IV=iv)
        
        decrypted = cipher.decrypt(encrypted_value[3:])
        # Remover padding
        return decrypted[:-decrypted[-1]].decode('utf-8')
    
    return encrypted_value.decode('utf-8', errors='ignore')

def get_chromium_cookies_decrypted(url):
    """Extrae y desencripta cookies de Chromium"""
    domain = urlparse(url).netloc
    cookie_db = os.path.expanduser('~/.config/chromium/Default/Cookies')
    
    temp_db = '/tmp/cookies_copy.db'
    shutil.copy2(cookie_db, temp_db)
    
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT host_key, name, encrypted_value, path, expires_utc, is_secure, is_httponly, samesite
        FROM cookies 
        WHERE host_key LIKE ?
    """, (f'%{domain}%',))
    
    try:
        key = get_encryption_key()
    except:
        key = b'peanuts'
    
    cookies = []
    for row in cursor.fetchall():
        try:
            value = decrypt_cookie(row[2], key)
            
            cookies.append({
                'name': row[1],
                'value': value,
                'domain': row[0],
                'path': row[3],
                'expires': row[4] / 1000000 - 11644473600 if row[4] > 0 else -1,
                'httpOnly': bool(row[6]),
                'secure': bool(row[5]),
                'sameSite': ['None', 'Lax', 'Strict'][row[7]] if row[7] in [0,1,2] else 'None'
            })
        except Exception as e:
            continue
    
    conn.close()
    os.remove(temp_db)
    return cookies

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    
    try:
        cookies = get_chromium_cookies_decrypted(sys.argv[1])
        if cookies:
            context.add_cookies(cookies)
            print(f"Loaded {len(cookies)} cookies", file=sys.stderr)
    except Exception as e:
        print(f"Error loading cookies: {e}", file=sys.stderr)
    
    page = context.new_page()
    page.goto(sys.argv[1], wait_until='networkidle', timeout=30000)
    
    page.evaluate("""
        () => {
            return new Promise((resolve) => {
                let totalHeight = 0;
                let distance = 100;
                let timer = setInterval(() => {
                    window.scrollBy(0, distance);
                    totalHeight += distance;
                    
                    if(totalHeight >= document.body.scrollHeight){
                        clearInterval(timer);
                        resolve();
                    }
                }, 100);
            });
        }
    """)
    
    page.wait_for_timeout(2000)
    print(page.content())
    browser.close()
```

**Recomendación:** Empieza con la **Opción 1** (cierra Chromium temporalmente) o la **Opción 4** (desencriptación completa). ¿Cuál prefieres?



El error indica que el perfil de Chromium está siendo usado o hay un problema de permisos. Aquí está la solución:

## Opción 1: Usar un perfil temporal copiando las cookies

```python
from playwright.sync_api import sync_playwright
import sys
import os
import shutil

with sync_playwright() as p:
    # Crear directorio temporal para el perfil
    temp_profile = '/tmp/chromium-playwright'
    
    # Copiar solo las cookies del perfil original
    original_cookies = os.path.expanduser('~/.config/chromium/Default/Cookies')
    os.makedirs(f'{temp_profile}/Default', exist_ok=True)
    
    if os.path.exists(original_cookies):
        shutil.copy2(original_cookies, f'{temp_profile}/Default/Cookies')
    
    # Lanzar con el perfil temporal
    browser = p.chromium.launch_persistent_context(
        user_data_dir=temp_profile,
        headless=True,
        args=[
            '--disable-blink-features=AutomationControlled',
            '--profile-directory=Default'
        ]
    )
    
    page = browser.pages[0] if browser.pages else browser.new_page()
    page.goto(sys.argv[1], wait_until='networkidle', timeout=30000)
    
    # Scroll gradual
    page.evaluate("""
        () => {
            return new Promise((resolve) => {
                let totalHeight = 0;
                let distance = 100;
                let timer = setInterval(() => {
                    window.scrollBy(0, distance);
                    totalHeight += distance;
                    
                    if(totalHeight >= document.body.scrollHeight){
                        clearInterval(timer);
                        resolve();
                    }
                }, 100);
            });
        }
    """)
    
    page.wait_for_timeout(2000)
    print(page.content())
    browser.close()
```

## Opción 2: Usar la desencriptación de cookies (más limpio)

```python
from playwright.sync_api import sync_playwright
import sys
import os
import sqlite3
import shutil
from urllib.parse import urlparse

def get_chromium_cookies(url):
    """Extrae cookies de Chromium"""
    domain = urlparse(url).netloc
    cookie_db = os.path.expanduser('~/.config/chromium/Default/Cookies')
    
    if not os.path.exists(cookie_db):
        return []
    
    # Copiar la base de datos
    temp_db = '/tmp/cookies_copy.db'
    try:
        shutil.copy2(cookie_db, temp_db)
    except Exception as e:
        print(f"Error copiando cookies: {e}", file=sys.stderr)
        return []
    
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    
    # Obtener cookies del dominio
    cursor.execute("""
        SELECT host_key, name, value, path, expires_utc, is_secure, is_httponly, samesite
        FROM cookies 
        WHERE host_key LIKE ? OR host_key LIKE ?
    """, (f'%{domain}%', f'.{domain}'))
    
    cookies = []
    for row in cursor.fetchall():
        # Usar solo cookies no encriptadas (campo 'value')
        if row[2]:  # Si tiene valor en el campo 'value'
            cookies.append({
                'name': row[1],
                'value': row[2],
                'domain': row[0],
                'path': row[3],
                'expires': row[4] / 1000000 - 11644473600 if row[4] > 0 else -1,
                'httpOnly': bool(row[6]),
                'secure': bool(row[5]),
                'sameSite': ['None', 'Lax', 'Strict'][row[7]] if 0 <= row[7] <= 2 else 'Lax'
            })
    
    conn.close()
    try:
        os.remove(temp_db)
    except:
        pass
    
    return cookies

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=['--disable-blink-features=AutomationControlled']
    )
    
    context = browser.new_context(
        user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    )
    
    # Cargar cookies
    try:
        cookies = get_chromium_cookies(sys.argv[1])
        if cookies:
            context.add_cookies(cookies)
            print(f"Cargadas {len(cookies)} cookies", file=sys.stderr)
        else:
            print("No se encontraron cookies", file=sys.stderr)
    except Exception as e:
        print(f"Error cargando cookies: {e}", file=sys.stderr)
    
    page = context.new_page()
    page.goto(sys.argv[1], wait_until='networkidle', timeout=30000)
    
    # Scroll gradual
    page.evaluate("""
        () => {
            return new Promise((resolve) => {
                let totalHeight = 0;
                let distance = 100;
                let timer = setInterval(() => {
                    window.scrollBy(0, distance);
                    totalHeight += distance;
                    
                    if(totalHeight >= document.body.scrollHeight){
                        clearInterval(timer);
                        resolve();
                    }
                }, 100);
            });
        }
    """)
    
    page.wait_for_timeout(2000)
    print(page.content())
    browser.close()
```

## Opción 3: Si las cookies están encriptadas, usa esto

```bash
pip install pycryptodome
```

```python
from playwright.sync_api import sync_playwright
import sys
import os
import sqlite3
import shutil
from urllib.parse import urlparse
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

def get_encryption_key():
    """Obtiene la clave de encriptación"""
    try:
        import secretstorage
        bus = secretstorage.dbus_init()
        collection = secretstorage.get_default_collection(bus)
        for item in collection.get_all_items():
            if item.get_label() == 'Chrome Safe Storage':
                return item.get_secret()
    except:
        pass
    return b'peanuts'

def decrypt_value(encrypted_value, key):
    """Desencripta el valor de la cookie"""
    if encrypted_value[:3] == b'v10' or encrypted_value[:3] == b'v11':
        salt = b'saltysalt'
        iv = b' ' * 16
        derived_key = PBKDF2(key, salt, 16, 1)
        cipher = AES.new(derived_key, AES.MODE_CBC, IV=iv)
        decrypted = cipher.decrypt(encrypted_value[3:])
        return decrypted[:-decrypted[-1]].decode('utf-8')
    return encrypted_value.decode('utf-8', errors='ignore')

def get_chromium_cookies(url):
    domain = urlparse(url).netloc
    # Al final terminé usando el de falkon: .config/falkon/profiles/default/Cookies
    cookie_db = os.path.expanduser('~/.config/chromium/Default/Cookies')
    
    if not os.path.exists(cookie_db):
        return []
    
    temp_db = '/tmp/cookies_copy.db'
    shutil.copy2(cookie_db, temp_db)
    
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT host_key, name, value, encrypted_value, path, expires_utc, is_secure, is_httponly, samesite
        FROM cookies 
        WHERE host_key LIKE ? OR host_key LIKE ?
    """, (f'%{domain}%', f'.{domain}'))
    
    key = get_encryption_key()
    cookies = []
    
    for row in cursor.fetchall():
        try:
            # Intentar primero el campo 'value'
            if row[2]:
                value = row[2]
            # Si está vacío, desencriptar 'encrypted_value'
            elif row[3]:
                value = decrypt_value(row[3], key)
            else:
                continue
            
            cookies.append({
                'name': row[1],
                'value': value,
                'domain': row[0],
                'path': row[4],
                'expires': row[5] / 1000000 - 11644473600 if row[5] > 0 else -1,
                'httpOnly': bool(row[7]),
                'secure': bool(row[6]),
                'sameSite': ['None', 'Lax', 'Strict'][row[8]] if 0 <= row[8] <= 2 else 'Lax'
            })
        except Exception as e:
            continue
    
    conn.close()
    os.remove(temp_db)
    return cookies

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    
    try:
        cookies = get_chromium_cookies(sys.argv[1])
        if cookies:
            context.add_cookies(cookies)
            print(f"✓ {len(cookies)} cookies cargadas", file=sys.stderr)
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
    
    page = context.new_page()
    page.goto(sys.argv[1], wait_until='networkidle', timeout=30000)
    
    page.evaluate("""
        () => new Promise(resolve => {
            let total = 0;
            const int = setInterval(() => {
                window.scrollBy(0, 100);
                total += 100;
                if(total >= document.body.scrollHeight) {
                    clearInterval(int);
                    resolve();
                }
            }, 100);
        })
    """)
    
    page.wait_for_timeout(2000)
    print(page.content())
    browser.close()
```

**Prueba primero la Opción 2** (la más simple). Si las cookies no funcionan porque están encriptadas, usa la Opción 3.

Usa así:
```bash
python fetch.py "https://www.upwork.com/tu-url" | w3m -T text/html
```




