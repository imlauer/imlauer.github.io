---
title: "Ec2 aws cli"
date: 2024-09-24T22:59:39-03:00
tags: ['aws','ec2']
---
https://www.youtube.com/watch?v=crNyDkR3ulU

Hacer esto es inseguro:

```bash
aws configure
```

Andá a tu amazon y buscá IAM > instances > seleccioná tu país a la derecha.

Seleccioná la instancia y mirá la IP pública, hacele un ssh a esa IP.

```bash
ssh  -i EC2Tutorial.pem ec2-user@ippublica
```

Cuando ejecutes `aws s3 ls` configure te va a decir Unable to locale credentials. Tenés que ir en IAM y roles > create role > ec2 > s3 > next > name: myfirsts3role description: allows ec2 to make read-only calls to amazon s3. > next.
