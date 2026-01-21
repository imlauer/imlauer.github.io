---
title: "Pencil to pen"
date: 2025-08-26T15:18:59-03:00
---

Ninguno de estos métodos funciona, mejor pedilo a ChatGPT xD

Yes 👍 — you can definitely use **ImageMagick’s `convert` (or `magick` in newer versions)** to make pencil writing appear darker, bolder, and more like pen. What you’d usually do is increase contrast, darken grays toward black, and possibly threshold the image.

Here are some example commands you can try:

---

### 1. Increase contrast & make pencil strokes darker

```bash
magick input.jpg -level 20%,80% -contrast -contrast output.jpg
```

* `-level 20%,80%` remaps brightness so lighter grays become closer to white and darker grays closer to black.
* `-contrast` (repeat it 2–3 times if needed) boosts overall contrast.

---

### 2. Convert to pure black & white (pen-like effect)

```bash
magick input.jpg -threshold 60% output.jpg
```

* This removes gray tones entirely, leaving only black strokes and white background (like scanned ink).
* Adjust the value (`60%`, `70%`, etc.) until it looks right.

---

### 3. Sharpen and darken details

```bash
magick input.jpg -morphology Convolve DoG:0,0,1 -normalize -level 25%,75% output.jpg
```

* `-morphology Convolve DoG:0,0,1` enhances edges (like strokes).
* `-normalize` stretches brightness levels.
* This makes faint pencil lines look stronger.

---

### 4. Combine for a “pen ink” effect

```bash
magick input.jpg -colorspace Gray -level 30%,90% -contrast -sharpen 0x1 -threshold 65% output.jpg
```

This workflow:

1. Converts to grayscale
2. Darkens pencil
3. Boosts contrast
4. Sharpens edges
5. Thresholds into clean black strokes

---

👉 Do you want the result to stay a **bit natural (still grayscale, like a dark pencil)**, or go all the way to **pure black ink strokes (pen/scan effect)**?

