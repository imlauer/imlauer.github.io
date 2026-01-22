---
title: "Resolving blocked push"
date: 2025-11-03T07:46:47-03:00
tags: ['git']
---
https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-command-line#removing-a-secret-introduced-by-the-latest-commit-on-your-branch

Al final terminé haciendo un `cd public && rm -rf .git && git remote add origin github.com:imlauera/imlauera.github.io && git add . && git commit -m "chau historial" && git push --force` pero del repositorio público lol.
