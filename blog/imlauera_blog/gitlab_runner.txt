---
title: "Gitlab runner: CI/CDpipelines"
date: 2024-09-18T20:04:32-03:00
tags: ['CI','CD','pipelines']
---

Es como hacer un `docker build . -t my-web-app -f docker/Dockerfile` pero hecho por gitlab automáticamente.

https://www.youtube.com/watch?v=qP8kir2GUgo

#### Pipeline scripts

#### Stages & jobs

#### Docker images

CI = Continuous Integration

Creá una cuenta en Gitlab. Creá un proyecto. Cloná el repositorio y creá una archivo llamado `.gitlab-ci.yml` 

```bash
create_file:
  image: alpine
  script: 
    - echo "Building ..."
    - mkdir build
    - touch build/somefile.txt
```

Cuando pusheas el archivo verás un ícono running job. Bajo de pipeline habrá un dialogo llamado `test` dentro `create_file`. A la derecha te dirá la duración y el runner que está ejecutando ese trabajo.

En el menú izquierdo. `Build > pipelines ` encontrarás todos los trabajos ejecutados, **cada vez que hagas un commit aparecerá un nuevo trabajo**.

### ¿Pero donde está la carpeta build?

Test es un comando de linux.
Esto no funcionará:

```bash
create_file:
  image: alpine
  script: 
    - echo "Building ..."
    - mkdir build
    - touch build/somefile.txt
test_file:
  image: alpine
  script:
    - test -f build/somefile.txt
```
Esto nos dará un `ERROR: job failed: exit code 1` es decir no encontró el archivo.

### Hay que entender el órden de la ejecutación: se ejecutan en paralelo.
Por eso no funcionó, estás probando algo que no se creó.

Entonces tenemos que especificar `stages` para ordenar los trabajos.


```bash
stages:
  - build
  - test
create_file:
  image: alpine
  stage: build
  script: 
    - echo "Building ..."
    - mkdir build
    - touch build/somefile.txt
test_file:
  image: alpine
  stage: test
  script:
    - test -f build/somefile.txt
```

#### De todos modos esto también falló.
Cada vez que empezamos un trabajo, el runner empezará desde 0 usará una nueva imagen, si escribimos algún archivo esos archivos están perdidos, ese contenedor se destruye. **Para resolver esto se usa artifacts**.

Artifacts se usa para decirle a gitlab que creamos algo importante y necesitamos mantenerlo guardado.

```bash
stages:
  - build
  - test
create_file:
  image: alpine
  stage: build
  script: 
    - echo "Building ..."
    - mkdir build
    - touch build/somefile.txt
  artifacts:
    paths:
      - build/
test_file:
  image: alpine
  stage: test
  script:
    - test -f build/somefile.txt
```

**Y ahora finalmente el pipeline es exitoso.**
Si miramos dentro de `test_file` en una parte dice `downloading artifacts` el contenedor sigue siendo destruído pero los archivos se guardan en algún lugar y `uploading artifacts` a la derecha encontrarás `job artifacts` si le das browse encontrarás la carapeta llamada build y dentro estará el archivo: `somefile.txt`.

---

### Pasos para aplicarlo a un proyecto real
1. Buscá una imágen de docker que contenga el entorno runtime que necesites: por ejemplo si necesitás construir un proyecto que tenga PHP entonces necesitás una imagen docker que contenga PHP8.
2. Ejecutá todos los comandos para construir el proyecto: instalá todas las dependencias y compilarlo.

