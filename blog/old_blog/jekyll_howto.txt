---
title: "Jekyll: howto"
date: 2024-09-16T16:35:19-03:00
tags: ['jekyll']
---
Se pronuncia yakol. Sirve para generar páginas webs estáticas con capacidades de blog.

https://dontusesystemruby.com/#/     

https://stackoverflow.com/questions/75527034/struggling-with-bundle-install-could-not-delete-previous-installation-permi   
https://github.com/rbenv/rbenv#uninstalling-rbenv

### Rápida instalación
```bash
gem install jekyll bundler
jekyll new myblog
cd myblog
bundle exec jekyll serve
```

Instalará el `theme: minima` que te putea por algo del sass, tenés que agregar en `_config.yml`:
```bash
sass:
  quiet_deps: true
```

Para tener el comando `jekyll post` hay que instalar [jekyll-compose](https://github.com/jekyll/jekyll-compose).

```bash
gem 'jekyll-compose', group: [:jekyll_plugins]
bundle
```
Si te tira un `error installing` algo bigdecimal o hace esto:

Primero asegúrese de que el sitio de [Ruby Gems](https://rubygems.org/) esté activo y que su acceso a la red sea correcto.   
Borrá `Gemfile.lock`   
Luego ejecutá `gem update --system`   
Intentá cambiando la línea del source de `https` a `http`    

Comandos:   
```bash
draft      # Creates a new draft post with the given NAME
post       # Creates a new post with the given NAME
publish    # Moves a draft into the _posts directory and sets the date
unpublish  # Moves a post back into the _drafts directory
page       # Creates a new page with the given NAME
rename     # Moves a draft to a given NAME and sets the title
compose    # Creates a new file with the given NAME



$ bundle exec jekyll page "My New Page"
$ bundle exec jekyll post "My New Post"
# or specify a custom format for the date attribute in the yaml front matter
$ bundle exec jekyll post "My New Post" --timestamp-format "%Y-%m-%d %H:%M:%S %z"
# or by using the compose command
$ bundle exec jekyll compose "My New Post"
# or by using the compose command with post specified
$ bundle exec jekyll compose "My New Post" --post
# or by using the compose command with the posts collection specified
$ bundle exec jekyll compose "My New Post" --collection "posts"
$ bundle exec jekyll draft "My new draft"
# or by using the compose command with draft specified
$ bundle exec jekyll compose "My new draft" --draft
# or by using the compose command with the drafts collection specified
$ bundle exec jekyll compose "My new draft" --collection "drafts"
$ bundle exec jekyll rename _drafts/my-new-draft.md "My Renamed Draft"
# or rename it back
$ bundle exec jekyll rename _drafts/my-renamed-draft.md "My new draft"
$ bundle exec jekyll publish _drafts/my-new-draft.md
# or specify a specific date on which to publish it
$ bundle exec jekyll publish _drafts/my-new-draft.md --date 2014-01-24
# or specify a custom format for the date attribute in the yaml front matter
$ bundle exec jekyll publish _drafts/my-new-draft.md --timestamp-format "%Y-%m-%d %H:%M:%S %z"
$ bundle exec jekyll rename _posts/2014-01-24-my-new-draft.md "My New Post"
# or specify a specific date
$ bundle exec jekyll rename _posts/2014-01-24-my-new-post.md "My Old Post" --date "2012-03-04"
# or specify a specific date
$ bundle exec jekyll rename _posts/2014-01-24-my-new-post.md "My Old Post" --date "2012-03-04"
# or specify the current date
$ bundle exec jekyll rename _posts/2012-03-04-my-old-post.md "My New Post" --now
$ bundle exec jekyll compose "My New Thing" --collection "things"
```

https://jekyllrb.com/docs/


---

NO instales jekyll desde el repositorio con APT o pacman
```bash
(NO lo hagas) sudo apt install -y jekyll
```

Forkea un template por ejemplo: `SpencerPao/al-folio` luego de forkear el template andá a `settings-> cambiá el nombre del respositorio a tu nueva página: mipaginaweb.github.io` (mipaginaweb tiene que ser tu usuario de github sino no funcionará)

Cloná el repositorio que forkeaste.
```bash
cd mipaginaweb.github.io
git init
git remote add origin git@git...
git add . && git commit -m first && git push
git push --set-upstream origin master
```
Cambiá el `_config.yml`:

```bash
url: https://mipaginaweb.github.io
baseurl: /
imagemagick:
enabled: false
```

Si estás en windows tenés que agregarle `bash` en el `run:` de `deploy.yml`

En el gemfile hay que agregar 
`gem 'wdm', '>= 0.1.0'` debajo de `group :jekyll_plugins do` (sólo para windows)

Luego de editar todo ejecutá:

```bash
bundle install
bundle exec jekyll serve
```
en `deploy.yml` incluí
```bash
- name: fix permission
	run: |
		chmod a+x bin/*
		git commit -am "add execute permision to bin/deploy"
```

Ahora para deployarlo:
```bash
bin/deploy --user
```

Luego en `github actions` estará la acción ejecutandose.
