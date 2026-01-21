---
title: "Gitlab send reports email"
date: 2024-09-23T20:38:26-03:00
tags: ['gitlab']
---
Mailgun = 10.000 correos gratuitos por mes sin tener que ingresar la tarjeta de crédito.

Create la cuenta en mailgun > settings > api key.

Copiá la private key apretá ojito y copiala y usala en gitlab.

En gitlab > settings > CI/CD > variables > expand 

El nombre lo podes definir como quieras en mi caso lo definí así

para la api_key el nombre de la variable será MAILGUN_API_KEY

La otra variable será: MAILGUN_DOMAIN, si no configuraste tu dominio de mailgun será random.

Andá a MAILGUN dashboard > abajo de todo verás tu dominio en sending domains (sandbox0.....mailgun.org) 

Copiá ese dominio y pegalo en la variable GITLAB.

Editá `.gitlab_ci.yml`:


Podes mirar el trabajo que envia el correo en gitlab.

Enviamos un correo con un archivo adjunto:

Si querés incluir multiples archivos repetí el mismo parámetro.
### Tenemos que asegurarnos que el trabajo de "send_email" es ejecutado incluso si la build job falla
Por defecto gitlab no publicará artifacts si el trabajo no fue exitoso. Para cambiar esto necesitamos decirle a cada trabajo cuando publicar el artifact y esto se hace agregando la condición llamada: `when`

Vamos a forzar un error y sólo mandaremos el reporte cuando el trabajo falle para eso agregamos `when: on_failure` poné `always` para mandar el correo siempre.

```bash
stages:
  - build
  - notify

build:
  stage: build
  script:
    - mkdir reports
    - touch reports/report.html
    - echo "<html><h1>Some report</h1></html>" > "reports/report.html"
    - exit 1
  artifacts:
    paths:
      - reports/
    when: always

send_mail:
  stage: notify
  when: on_failure
  script: curl -s --user "api:$MAILGUN_API_KEY"
    "https://api.mailgun.net/v3/$MAILGUN_DOMAIN/messages"
    -F from='Gitlab <gitlab@example.com>'
    -F to=$GITLAB_USER_EMAIL
    -F subject='Test results'
    -F text='Testing some Mailgun awesomeness!'
    -F attachment='@reports/report.html'
```

