---
title: "Module Not Found Error No module named 'rembg'"
date: 2024-10-18T16:50:21-03:00
tags: ['rembg']
---
Como arreglé este problema:

```bash
ModuleNotFoundError: No module named 'rembg'
```

---

```bash
rm .local/bin/rembg
pip uninstall rembg
python -m venv rembg
source rembg/bin/activate
pip install asyncer gradio aiohttp watchdog filetype click
rembg i image.jpg asdf.png
```

