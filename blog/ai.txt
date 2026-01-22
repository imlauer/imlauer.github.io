---
title: "AI ArchLinux"
date: 2025-09-06T04:47:42-03:00
tags: ['arch']
---

## 🐧 AI Control on Arch Linux

### 1. **AI in the Shell**

* **Shell-GPT (`sgpt`)** → An Arch package in the **AUR**:

  ```bash
  yay -S shell-gpt
  ```

  Lets you type things like:

  ```bash
  sgpt "find all .mp4 files larger than 1GB and delete them"
  ```

  → It will generate and (if you approve) run the correct Bash command.

* **Aider** ([GitHub](https://github.com/paul-gauthier/aider)) → AI pair-programmer that edits files directly in your repo. AUR package:

  ```bash
  yay -S aider
  ```

* **ChatGPT in the terminal** (several AUR packages):

  * `chatgpt-cli`
  * `gpt4all` (local model, no OpenAI key needed)

---

### 2. **Local AI Models (No Cloud Needed)**

Arch makes it easy to run **local LLMs** for full privacy + offline AI:

* **Ollama** ([ollama-bin in AUR](https://aur.archlinux.org/packages/ollama-bin)):

  ```bash
  yay -S ollama-bin
  ```

  Run models like LLaMA 3, Mistral, Gemma locally.
  Example:

  ```bash
  ollama run llama3 "Write a pacman command to update the system"
  ```

* **GPT4All** (`gpt4all` in AUR): desktop app for local models.

---

### 3. **Voice & Assistant AI**

* **Mycroft-core** (still in AUR):

  ```bash
  yay -S mycroft-core
  ```

  Gives you a voice assistant for Arch.

* **Jasper** (manual install via GitHub) → lightweight voice assistant using STT/TTS + AI models.

---

### 4. **AI Agent Control of Arch**

* **LangChain + Python** → You can make an “AI Arch controller” that runs commands safely.
* **AutoGPT / CrewAI** (install via pip) → autonomous AI agents that can manage tasks on Arch.
* Combine with **systemd services** so the agent is “always on,” managing tasks like updates, backups, or monitoring.

---

✅ **So yes:** you can turn Arch into an AI-controlled system today.
The fastest way is:

1. Install **Ollama** for local models.
2. Install **Shell-GPT** for AI command generation.
3. Add a voice layer like **Mycroft-core** if you want voice control.

---

👉 Do you want me to make you a **step-by-step Arch setup** (commands + config) for an “AI-controlled Arch Linux” using Ollama + Shell-GPT?

