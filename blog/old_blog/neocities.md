---
title: "Neocities: como buscar y pushear desde GitHub con GitHub Actions"
date: 2025-10-17T04:22:23-03:00
tags: ['tech']
---

Para buscar en Neocities (ya que Google censura y te muestra solo Reddit) podes usar estos 2 buscadores:
* [Wiby](http://wiby.me/)
* [Marginalia](https://marginalia-search.com/)

O directamente buscando por **tags**:

https://neocities.org/browse?tag=tor


#### Como deployar a Neocities desde GitHub yo tengo mi sitio alli tambien: https://imlauer.neocities.org

---

## ⚙️  **Automated deployment using GitHub Actions (recommended)**

Primero cree una carpeta llamada neocities porque no se permiten `.git` `.node_modules` e imagens creo y ahi puse el html con el siguiente script:
```bash
#!/usr/bin/bash

if [[ -z $1 ]]; then
echo "Falta commit";
exit;
fi

for html in *.html; do
        rm $html;
done
for markdown in *.md; do
        filename_only="${markdown%.*}"
        (
        echo '<!DOCTYPE html>'
        echo '<html lang="en">'
        echo '<head>'
        echo '  <meta charset="UTF-8">'
        echo "  <title>Imlauer | $filename_only </title>"
        echo '</head>'
        echo '<body>'
        cmark $markdown;
        echo '</body>'
        echo '</html>'
        ) | tee $filename_only.html &&
        cp $filename_only.html neocities/
done ;

git add . && git commit -m $1 && git push
```

You can make GitHub automatically push changes to Neocities when you push to `main`.

#### Step 1: Create an API key

1. Go to your [Neocities settings](https://neocities.org/settings).
2. Scroll to **API Key** → copy it.

#### Step 2: Add the key to your GitHub repo

1. On GitHub, open your repo → **Settings → Secrets → Actions**.
2. Add a new secret:

   * Name: `NEOCITIES_API_KEY`
   * Value: *(paste your key)*

#### Step 3: Add a workflow file

Create `.github/workflows/deploy.yml` in your repo:

```yaml
name: Deploy to neocities

# only run on changes to main. Use main or master depending on whatever your default branch is called.
on:
  push:
    branches:
      - main

concurrency: # prevent concurrent deploys doing strange things
  group: deploy-to-neocities
  cancel-in-progress: true

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    # The checkout step copies your repo into the action runner. Important!
    - uses: actions/checkout@v4
    # Set up any tools and build steps here
    # This example uses a Node.js toolchain to build a site
    # If you don't need Node.js to build your site, you can omit this.
    #- name: Use Node.js
    #  uses: actions/setup-node@v4
    #  with:
    #    node-version: lts/*
    ## If you have a different build process, replace this with your own build steps
    #- name: Install deps and build
    #  run: |
    #    npm i
    #    npm run build
    # When the dist_dir is ready, deploy it to neocities
    # Here we deploy the folder named `public`
    - name: Deploy to neocities
      uses: bcomnes/deploy-to-neocities@v3
      with:
        api_key: ${{ secrets.NEOCITIES_API_KEY }}
        cleanup: false
        neocities_supporter: false # set this to true if you have a supporter account and want to bypass unsuported files filter.
        preview_before_deploy: true # print a deployment plan prior to waiting for files to upload.
        dist_dir: neocities
```

This action will upload your repo’s files to Neocities automatically every time you push to `main`.

✅ **Reference:** [bcomnes/deploy-to-neocities](https://github.com/bcomnes/deploy-to-neocities)
