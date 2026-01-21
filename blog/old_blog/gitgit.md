---
title: "How to fix: Git mistake of pushing big file"
date: 2025-12-05T20:09:02-03:00
---
```bash
> how do I solve this? I push big file but I already deleted but I still get this error [main 7279758] certificaados
...  1 file changed, 0 insertions(+), 0 deletions(-)
...  create mode 100644 asfd
... Enumerating objects: 17, done.
... Counting objects: 100% (17/17), done.
... Delta compression using up to 2 threads
... Compressing objects: 100% (12/12), done.
... Writing objects: 100% (13/13), 95.26 MiB | 3.56 MiB/s, done.
... Total 13 (delta 7), reused 0 (delta 0), pack-reused 0 (from 0)
... remote: Resolving deltas: 100% (7/7), completed with 4 local objects.
... remote: error: Trace: f5b8d8909b994b8b492b5e9982e5b0cfa0566c55dcb5c0adb34db0ddd7cb87b1
... remote: error: See https://gh.io/lfs for more information.
... remote: error: File 00reflexiones/amen.wav is 137.08 MB; this exceeds GitHub's file size limit of 100.00 MB
... remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
... To github.com:analisismatematico2/analisismatematico2.github.io
...  ! [remote rejected] main -> main (pre-receive hook declined)
```

### Lo solucioné con esto.

```bash
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch 00reflexiones/amen.wav' --prune-empty --tag-name-filter cat -- --all
```
