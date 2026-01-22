---
title: "Yt Dlp audio"
date: 2025-10-01T09:32:35-03:00
tags: ['tools']
---

Para descargar cualquier audio de cualquier video de YouTube: `yt-dlp -f bestaudio`

### ✅ Correct syntax for fallbacks

```bash
yt-dlp -f "233/140/251" URL
```

* `233/140/251` means:

  > Try format **233**, if not available then **140**, if not then **251**.

---

### 🔀 Difference between separators

* `/` → fallback (first available one is used).
* `+` → combine (e.g., video+audio).
* `,` → download multiple formats at once.

---

### Example

If you want **Opus (251)** but fallback to **M4A (140)**:

```bash
yt-dlp -f "251/140" URL
```

If you want **video 137** with **audio 251** but fallback to **140** if 251 isn’t available:

```bash
yt-dlp -f "137+251/140" URL
```

---

⚡ Pro tip: If you just want the **best available audio** without worrying about IDs:

```bash
yt-dlp -f "bestaudio" URL
```

---

Do you want me to show you how to **prefer Opus > M4A > MP3 automatically** so you don’t have to type IDs every time?




