---
title: "Capture Anarch game from TTY"
date: 2025-12-21T23:04:43-03:00
---
# Claude. 
Ah, **Anarch**! That's a great retro FPS. It's designed to be extremely portable and can run in various modes.

## **For Anarch specifically:**

Anarch supports multiple SDL backends. In TTY mode, it most likely uses **SDL framebuffer** or **SDL with fbcon/fbdev**.

### **Basic capture command:**

```bash
ffmpeg -f fbdev -framerate 30 -i /dev/fb0 \
       -vf "scale=1024:-2" \
       -c:v libx264 -preset ultrafast -crf 23 \
       output.mkv
```

### **With audio (Anarch has sound):**

```bash
ffmpeg -f alsa -i default \
       -f fbdev -framerate 30 -i /dev/fb0 \
       -vf "scale=1024:-2" \
       -c:v libx264 -preset ultrafast -crf 23 \
       -c:a aac -b:a 128k \
       output.mkv
```

---

## **Recommended workflow:**

1. **Start ffmpeg capture in one TTY** (e.g., TTY2):
   ```bash
   sudo ffmpeg -f fbdev -framerate 30 -i /dev/fb0 -c:v libx264 -preset ultrafast output.mkv
   ```

2. **Switch to another TTY** (Ctrl+Alt+F3) and **run Anarch**

3. **Play the game** - it's being captured!

4. **Stop recording**: Switch back to TTY2 (Ctrl+Alt+F2) and press `q` to stop ffmpeg

---

## **Performance tips for Anarch:**

Since Anarch is lightweight but you're capturing video:
- Use `-framerate 20` or `-framerate 15` if you get slowdown
- Use `-preset ultrafast` (already in command)
- Consider `-crf 28` for smaller files with acceptable quality

---

## **Troubleshooting:**

If the framebuffer capture shows a black screen, Anarch might be using a different rendering method. Try:

```bash
# Check what SDL backend Anarch is using
SDL_VIDEODRIVER=fbcon ./anarch
```

or force it to use framebuffer:

```bash
SDL_VIDEODRIVER=fbcon ./anarch &
ffmpeg -f fbdev -framerate 30 -i /dev/fb0 output.mkv
```

Let me know if you run into issues - Anarch is pretty straightforward but SDL backend detection can be tricky!
