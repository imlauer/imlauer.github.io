---
title: "Instalando Mitmproxy certificado en firefox con docker"
date: 2024-09-20T10:58:37-03:00
tags: ['docker']
---


Dockerfile:
```bash
FROM apache/airflow:2.1.4

USER root
RUN apt-get update                             \
 && apt-get install -y --no-install-recommends \
    ca-certificates curl firefox-esr           \
 && rm -fr /var/lib/apt/lists/*                \
 && curl -L https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz | tar xz -C /usr/local/bin \
 && apt-get purge -y ca-certificates curl
USER airflow
```

#### Verificación
```bash
$ docker build -t abc:1 .
$ docker run --rm -it --entrypoint=which abc:1 firefox
/usr/bin/firefox
$ docker run --rm -it --entrypoint=which abc:1 geckodriver
/usr/local/bin/geckodriver
```


Dockerfile:
```bash
# firefox image, we're extending with mitmproxy
FROM jlesage/firefox

RUN apk add --no-cache \
        g++ \
        py-pip \
        libffi \
        libffi-dev \
        libjpeg-turbo \
        libjpeg-turbo-dev \
        libxml2 \
        libxml2-dev \
        libxslt \
        libxslt-dev \
        openssl \
        openssl-dev \
        python \
        python-dev \
        zlib \
        zlib-dev 

RUN LDFLAGS=-L/lib pip install mitmproxy==0.18.2 \
    && apk del --purge \
        g++ \
        py-pip \
        libffi-dev \
        libjpeg-turbo-dev \
        libxml2-dev \
        libxslt-dev \
        openssl-dev \
        python-dev \
        zlib-dev \
    && rm -rf ~/.cache/pip \
    && adduser -u 7799 -D mitmproxy

RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python \
    && easy_install pip \
    && pip install mitmproxy==0.18.2

COPY rootfs/ /
```
