---
title: "Codeigniter"
date: 2024-09-19T09:12:55-03:00
tags: ['codeigniter']
---
```bash
sudo apt install -y composer

composer create-project codeigniter4/appstarter ci-news
CI_ENVIRONMENT = development
php spark serve
```

### Crear migraciones
```bash
php spark migrate:create blog
php spark migrate:refresh
php spark migrate:status
```
