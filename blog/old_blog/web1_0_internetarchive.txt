---
title: "Build Web1.0 y como subir imagenes a archive.org desde la consola."
date: 2025-10-23T22:36:10-03:00
---
La web moderna esta llena de publicidad y manipulacion, volvamos a la web1.0, si quieren ver como era antes usen [Wiby.me](https://wiby.me)

Subo las imágenes a Archive.org o a Blogger.com si lo haces desde Archive.org se puede usar el comando `source internetarchive/bin/activate.fish  && ia upload tag_name *` y luego `ia metadata tag_name`

## 🧱 1. Folder structure

Create a folder like this:

```
my-site/
├── index.html
├── about.html
├── posts/
│   ├── 2025-01-hello.html
│   └── 2025-02-another.html
├── style.css
└── rss.xml
```

You can host this folder on:

* **Neocities**, **GitHub Pages**, or **any static web host**.

---

## 🧾 2. The HTML (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>My Old Web 1.0 Site</title>
  <link rel="stylesheet" href="style.css">
  <link rel="alternate" type="application/rss+xml" href="rss.xml" title="RSS Feed">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <header>
    <h1>My Old Web 1.0 Site</h1>
    <nav>
      <a href="index.html">Home</a> |
      <a href="about.html">About</a> |
      <a href="rss.xml">RSS</a>
    </nav>
  </header>

  <main>
    <h2>Recent posts</h2>
    <ul>
      <li><a href="posts/2025-02-another.html">Another Post</a> – Feb 2025</li>
      <li><a href="posts/2025-01-hello.html">Hello World</a> – Jan 2025</li>
    </ul>
  </main>

  <footer>
    <p>© 2025 Me — handcrafted HTML like it’s 1999</p>
  </footer>
</body>
</html>
```

---

## 🎨 3. The CSS (style.css)

Minimal, readable and light on the eyes.

```css
body {
  font-family: "Verdana", sans-serif;
  max-width: 700px;
  margin: auto;
  background: #fefefe;
  color: #222;
  line-height: 1.5;
  padding: 1em;
}

header, footer {
  text-align: center;
  margin-bottom: 2em;
}

nav a {
  text-decoration: none;
  color: blue;
}

a:hover {
  text-decoration: underline;
}
```

---

## 📝 4. A simple post (posts/2025-01-hello.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Hello World</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header><a href="../index.html">← Home</a></header>
  <article>
    <h1>Hello World</h1>
    <time datetime="2025-01-01">Jan 1, 2025</time>
    <p>This is my first post on my old-school HTML website!</p>
  </article>
</body>
</html>
```

---

## 📰 5. RSS feed (rss.xml)

This is what lets readers (and other sites) subscribe to updates.
You can update it manually each time you add a new post.

En la fecha `Tue, 18 Feb 2025 00:00:00 +0000` el +0000 es el UTC, tenes que reemplazarlo por tu horario en mi caso es `-0300` que es el de Argentina.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>My Old Web 1.0 Site</title>
  <link>https://example.com/</link>
  <description>Handcrafted HTML and thoughts.</description>
  <language>en-us</language>

  <item>
    <title>Another Post</title>
    <link>https://example.com/posts/2025-02-another.html</link>
    <pubDate>Tue, 18 Feb 2025 00:00:00 +0000</pubDate>
    <description>My second post — no JavaScript, just vibes.</description>
  </item>

  <item>
    <title>Hello World</title>
    <link>https://example.com/posts/2025-01-hello.html</link>
    <pubDate>Wed, 1 Jan 2025 00:00:00 +0000</pubDate>
    <description>My first post on my old-school site.</description>
  </item>

</channel>
</rss>
```

👉 To validate it, use [validator.w3.org/feed/](https://validator.w3.org/feed/).

---

## 🌐 6. Hosting

* [**Neocities.org**](https://neocities.org) — simplest for static sites.
* [**GitHub Pages**](https://pages.github.com) — free hosting tied to GitHub repos.
* [**Any VPS or web server**] — just drop your folder in `/var/www/html`.

---

## 🧩 7. Optional retro touches

* Add a **guestbook** (via [HTMLCommentBox.com](https://www.htmlcommentbox.com/) or a CGI script if you want authenticity).
* Include a **“Webring”** or “Links” section.
* Add a **GIF banner** like:

  ```html
  <img src="https://web.archive.org/web/20091027094317im_/http://geocities.com/athens/academy/8259/under_construction.gif" alt="Under Construction">
  ```
* Use **inline hit counters**, ASCII art, or `<marquee>` (for full nostalgia).

---

## 🧭 8. Workflow

Each time you add a post:

1. Copy `posts/2025-01-hello.html` → new file.
2. Add a `<li>` in `index.html` linking to it.
3. Add a new `<item>` in `rss.xml`.
4. Upload your files. Done.

### Otro ejemplo miren mi repositorio de `github.com/imlauer/imlauer.github.io` el index.html o `nobloatnews`.

Pueden copiar todo.

Se ve bien con lynx, links, elinks, chawan, w3m, netsurf.


