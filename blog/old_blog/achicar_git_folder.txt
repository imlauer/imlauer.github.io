---
title: "Como reducir el tamaño de la carpeta .git"
date: 2024-12-29T08:12:00-03:00
tags: ['git']
---
https://stackoverflow.com/questions/5613345/how-to-shrink-the-git-folder

Linus Torvalds recomienda: `git repack -a -d -f --depth=250 --window=250`

Pero si pusheaste imágenes git repack no las borrará. Para borrar esa información tenés que reescribir todo tu historial. Un ejemplo común de esto es cuando accidentalmente pusheas tus contraseñas en git. Podés borrar los archivos pero luego tenés que reescrbiir tu historial desde que pusheaste la contraseña hasta ahora y luego el nuevo repositorio a al origen.

> Will this get rid of binary data that is orphaned in my repo? "git repack" will not git rid of images or binary data that you have checked into your repo and then deleted it. To delete those kind of data permanently from your repo you have to re-write your history. A common example of that is when you accidentally check in your passwords in git. You can go back and delete some files but then you have to re-write your history from then to now and then force push then new repo to your origin.


https://stackoverflow.com/questions/13716658/how-to-delete-all-commit-history-in-github

Deleting the .git folder may cause problems in your git repository. If you want to delete all your commit history but keep the code in its current state, it is very safe to do it as in the following:

Checkout/create orphan branch (this branch won't show in git branch command):

```bash
git checkout --orphan latest_branch
```
Add all the files to the newly created branch:

```bash
git add -A
```
Commit the changes:

```bash
git commit -am "commit message"
```
Delete `main` (default) branch (this step is permanent):

```bash
git branch -D main
```
Rename the current branch to main:

```bash
git branch -m main
```
Finally, all changes are completed on your local repository, and force update your remote repository:

```bash
git push -f origin main
```
PS: This will not keep your old commit history around. Now you should only see your new commit in the history of your git repository.

### Otra opción es borrar la carpeta `.git`

If you are sure you want to remove all commit history, simply delete the .git directory in your project root (note that it's hidden). Then initialize a new repository in the same folder and link it to the GitHub repository:

```bash
git init
git remote add origin git@github.com:user/repo
```
now commit your current version of code

```bash
git add *
git commit -am 'message'
```
and finally force the update to GitHub:

```bash
git push -f origin master
```
However, I suggest backing up the history (the .git folder in the repository) before taking these steps!
