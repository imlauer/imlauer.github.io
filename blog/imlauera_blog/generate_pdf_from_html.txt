---
title: "Download entire site and generate a PDF from HTML"
date: 2025-11-02T11:22:05-03:00
tags: ['pdf']
---
Descargue todo un blog de Jekyll con el siguiente comando:

## **1️⃣ Mirror the site locally**
Use `wget` to download all pages, CSS, and images:

```bash
mkdir geohot

wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://geohot.github.io/blog/
```

* `--mirror` → download recursively
* `--convert-links` → make links local
* `--adjust-extension` → save files with proper extensions (`.html`)
* `--page-requisites` → include CSS, images, JS
* `--no-parent` → avoid downloading unrelated pages

The files will be saved under `geohot.github.io/blog/` in your current folder.

---

## **2️⃣ Combine all posts into a single HTML page**

If you want **one PDF**, it’s easiest to create a single `all.html` page that contains all posts:

```bash
# Create a blank HTML file
echo "<html><head><title>All Posts</title></head><body>" > all.html

# Append all HTML files downloaded by wget
find geohot.github.io/blog -name "*.html" | sort | while read f; do
    # Skip index.html if you want
    cat "$f" >> all.html
    echo "<hr>" >> all.html
done

# Close HTML tags
echo "</body></html>" >> all.html
```

> This will produce a giant HTML file containing all pages, separated by `<hr>`.

## Para arreglar ruta imágenes.

```bash
sed -i 's|\.\./\.\./\.\./\.\./\.\./assets/images/|geohot.github.io/blog/assets/images/|g' all.html
```

---

## **3️⃣ Convert HTML to PDF**

Now open the HTML file `all.html` with a browser run Control+P to print to PDF and save it as PDF.
