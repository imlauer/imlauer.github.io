---
title: "Gitlab auto deployment"
date: 2024-09-24T00:01:02-03:00
tags: ['gitlab']
---

> Need CI/CD pipeline to deploy the code on merge request approval on target server. The Target sever is running Ubuntu. On every deployment the code need to be updated on the server , npm update , PM2 restart the node or start after purging the existing logs.

configure the GIT to send email on pipeline success.

NOTE: Git branch are specific to a server ( DEV or QA ) Etc.


---

```
stages:
  - deploy

deploy_to_production:
  stage: deploy
  script:
    - echo "Deploying to production server..."
    - cd /path/to/your/app
    - git pull origin master
    - npm install
    - npm update
    - pm2 restart your-app-name --update-env
    - pm2 flush
  environment:
    name: production
    url: http://your-production-url.com
  only:
    - master
  rules:
    - if: $CI_MERGE_REQUEST_APPROVED
```


PM2:
https://www.youtube.com/watch?v=ebdKIU6SDHI

Te permite mantener tu aplicación viva por más que ocurra un error.

```bash
npm install pm2@latest -g
pm2 start app.js
pm2 logs
pm2 stop app
pm2 start app.js "MY APP" --watch
pm2 logs
pm2 stop "MY APP"
pm2 stop "app"
pm2 delete all
pm2 start app.js "MY APP" --watch
pm2 ls
pm2 logs
```

https://pm2.keymetrics.io/docs/usage/quick-start/
