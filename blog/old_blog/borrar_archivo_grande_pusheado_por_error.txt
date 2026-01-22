---
title: "Borrar archivo grande pusheado por error"
date: 2024-11-15T10:20:34-03:00
tags: ['git']
---
```bash
git filter-branch --index-filter 'git rm -r --cached --ignore-unmatch <file/dir>' HEAD
```
