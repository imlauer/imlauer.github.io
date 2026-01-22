---
title: "CICDpipelines"
date: 2024-09-20T18:42:46-03:00
tags: ['CI','CD','pipelines']
draft: true
---
Es como hacer un `docker build . -t my-web-app -f docker/Dockerfile` pero hecho por gitlab automáticamente.

https://www.youtube.com/watch?v=qP8kir2GUgo

#### Pipeline scripts

#### Stages & jobs

#### Docker images

CI = Continuous Integration

Creá una cuenta en Gitlab. Creá un proyecto. Cloná el repositorio y creá una archivo llamado `.gitlab-ci.yml` 
```
create_file:
  image: alpine
  script: 
    - echo "Building ..."
    - mkdir build
    - touch build/somefile.txt

```

Cuando pusheas el archivo verás un ícono running job. Bajo de pipeline habrá un dialogo llamado `test` dentro `create_file`. A la derecha te dirá la duración y el runner que está ejecutando ese trabajo.


