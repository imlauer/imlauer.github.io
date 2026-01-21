---
title: "ttyrec"
date: 2025-12-07T09:56:56-03:00
---
To **record ONLY the text that appears in the TTY** (not a video, not pixels — just the characters printed to the terminal), the correct tools are:

---

# ✅ **1. Best and simplest: `ttyrec`**

This records **everything printed to the TTY** (including control sequences, colors).

### Install:

```bash
sudo pacman -S ttyrec
```

### Record:

```bash
ttyrec mysession.tty
```

Do your work normally.

### Stop:

Press `Ctrl+D` or run:

```bash
exit
```

### Replay:

```bash
ttyplay mysession.tty
```

This is the closest thing to “OBS for pure text TTY”.

---

# ✅ **2. More modern + web-friendly: `asciinema`**

This records **your terminal session as text**, extremely efficient.

### Install:

```bash
sudo pacman -S asciinema
```

### Record:

```bash
asciinema rec session.cast
```

### Stop:

`Ctrl+D`

### Replay:

```bash
asciinema play session.cast
```

Pros:

* Can rewind, pause, speed up
* Perfect fidelity of text + colors
* Very small files (KB)
* Editable

---

# ✅ **3. Universal method: `script`**

Built into every Linux.

### Start recording:

```bash
script -t 2> timing.log text.log
```

Do your TTY work.

### Stop:

`Ctrl+D`

### Replay with timing:

```bash
scriptreplay timing.log text.log
```

---

# Which one should you use?

| Tool          | Records text? | Records timing? | Easy replay? | Output size |
| ------------- | ------------- | --------------- | ------------ | ----------- |
| **ttyrec**    | ✔             | ✔               | ✔            | small       |
| **asciinema** | ✔             | ✔               | ✔ (best)     | tiny        |
| **script**    | ✔             | ✔               | ✔            | small       |

---

# ⚠ Important:

These tools record only **what the shell prints**.

They **do NOT record screen redraws** from graphical TUI apps in raw framebuffer mode (like nvim in raw console) unless the app prints escape sequences.

But they DO correctly record:

* bash/zsh/fish output
* commands
* ncurses apps (htop, vim, etc.)
* colors
* cursor movement

Everything needed to replay the TTY experience.

---

# If you want, I can also show:

* how to convert a `ttyrec` to video using ffmpeg
* how to upload and embed terminal recordings
* how to capture TTY of another session (for demos)

Just tell me.

