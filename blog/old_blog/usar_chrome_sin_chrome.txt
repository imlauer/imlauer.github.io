---
title: "Usar chrome sin chrome: Chrome headless con w3m"
date: 2025-03-08T08:02:01-03:00
tags: ['chrome']
---
```bash
chromium --headless https://youtube.com --run-all-compositor-stages-before-draw --screenshot --virtual-time-budget=10000
```

O también se puede usar el parámetro `--print-to-pdf=/tmp/tmp.pdf`

```bash
chromium --headless --dump-dom youtube.com
```

```bash
chromium --headless https://bilibili.com --run-all-compositor-stages-before-draw --dump-dom --virtual-time-budget=10000 | w3m -
```

Usarlo con w3m como navegador externo: Creá un archivo llamado `w3m_chromium.sh` con el siguiente contenido y agregalo como navegador externo en w3m.
```bash
chromium --headless $1 --run-all-compositor-stages-before-draw --dump-dom --virtual-time-budget=10000 | w3m -
```

```bash
chromium --headless $1 --run-all-compositor-stages-before-draw --dump-dom --virtual-time-budget=10000 | monolith - -I -b $1 | w3m -
```

### Sin monolith con sed es mas rápido

```bash
chromium --headless $1 --disable-gpu --run-all-compositor-stages-before-draw --dump-dom --virtual-time-budget=10000 | sed "s|<head>|<head><base href=$1>|g" | w3m -T text/html
```

# Este es el que estoy usando: con este te carga las cookies

```bash
chromium --headless --user-data-dir=$HOME/.config/chromium --profile-directory=Default --disable-gpu --run-all-compositor-stages-before-draw --dump-dom --virtual-time-budget=10000 "$1" | sed "s|<head>|<head><base href=$1>|g" | w3m -T text/html
```

#### o copiando

```bash
cp -r ~/.config/chromium ~/.config/chromium-headless

chromium --headless --user-data-dir=$HOME/.config/chromium-headless --profile-directory=Default --disable-gpu --run-all-compositor-stages-before-draw --dump-dom --virtual-time-budget=10000 "$1" | sed "s|<head>|<head><base href=$1>|g" | w3m -T text/html
```

##### Se pude usar puppeteer para scrollear y cargar todo el javascript.
Uso: `node chromium_headless.js URL numeroVecesScrolear`

Creá un archivo bash y lo llamás desde w3m.
```bash
node chromium_headless.js "$1" 20 | sed "s|<head>|<head><base href=$1>|g" | w3m -T text/html
```


```js

const puppeteer = require('puppeteer');

// Get arguments from the command line
const [,, url, numPagesToScrollStr] = process.argv;

// Convert numPagesToScroll from string to number
const numPagesToScroll = parseInt(numPagesToScrollStr, 10);

if (!url || isNaN(numPagesToScroll)) {
  console.log("Usage: node script.js <URL> <numPagesToScroll>");
  process.exit(1);
}

(async () => {
  // Launch a new instance of Chrome
  const browser = await puppeteer.launch({ headless: false, defaultViewport: null });
  const page = await browser.newPage();

  // Navigate to the desired webpage
  await page.goto(url, { waitUntil: 'networkidle2' });

  // Function to check if the page height has changed
  let lastHeight = await page.evaluate('document.body.scrollHeight');
  console.log('Initial page height: ', lastHeight);

  let retries = 5; // Retry up to 5 times in case no new content is loaded

  // Infinite scroll loop (with a limit of `numPagesToScroll` pages)
  let pagesScrolled = 0; // To keep track of the number of pages scrolled
  while (pagesScrolled < numPagesToScroll) {
    // Scroll down by the height of the viewport
    await page.evaluate(() => {
      window.scrollBy(0, window.innerHeight * 3); // Scroll by 3 viewport heights to ensure more content loads
    });

    // Wait for new content to load (increase the timeout)
    try {
      await page.waitForFunction(
        `document.body.scrollHeight > ${lastHeight}`,
        { timeout: 5000 } // Increase timeout to 5 seconds
      );
    } catch (error) {
      console.log("Timeout error: Content did not load in time.");
      retries -= 1;
      if (retries <= 0) {
        console.log("Maximum retries reached. Stopping scroll.");
        break;
      }
    }

    // Get the new scroll height
    const newHeight = await page.evaluate('document.body.scrollHeight');
    console.log('Current page height: ', newHeight);

    // If the height hasn't changed, stop scrolling (no more content)
    if (newHeight === lastHeight) {
      console.log('No more content to load.');
      break;
    }

    // Update the last height for the next iteration
    lastHeight = newHeight;
    pagesScrolled++; // Increment pages scrolled counter
  }

  // Fetch and print the HTML content of the page after scrolling
  const html = await page.content();
  console.log("HTML content after scrolling:\n", html);

  // Gracefully close the browser
  await browser.close();
})();
```

Con `alias dgg = "w3m dgg.gg"` mpv como navegador externo ya estás hecho para navegar casi toda la web.
