---
title: "Como Usar Chatgpt y DALL-E en la Terminal"
tags: ['chatgpt','consola','dall-e']
categories: ['linux']
date: 2023-03-23T00:09:11-03:00
---

### Instalación de chatGPT shelll client
Primero instalan esto:
<a href="https://github.com/0xacx/chatGPT-shell-cli">https://github.com/0xacx/chatGPT-shell-cli</a>
Con el siguiente comando:
```bash
curl -sS https://raw.githubusercontent.com/0xacx/chatGPT-shell-cli/main/install.sh | sudo -E bash
```

>Un script de shell simple y liviano para usar chatGPT y DALL-E de OpenAI desde la terminal sin instalar python o node.js. El script usa el modelo oficial de ChatGPT gpt-3.5-turbo con el punto de conexión /chat/completions de la API de OpenAI. También puede utilizar el nuevo modelo gpt-4, si tiene acceso.
>El script permite el uso de todos los demás modelos de OpenAI con el punto final de finalización y el punto final de imágenes/generaciones para generar imágenes.

Para poder usar esta aplicación necesitan una clave la generan aca:
<a href="https://platform.openai.com/account/api-keys">https://platform.openai.com/account/api-keys</a>

Luego agregan
```bash
export OPENAI_KEY=...sustituir_por_su_clave_generada...
```
En .zprofile o .zshrc o .profile o .bashrc en cualquiera de esos archivos funcionan


Y ya pueden disfrutar de chatgpt y dall-e en la terminal abriendo una consola y ejecutando chatgpt.
#### Ejemplos
Si pones image al principio usa DALL-E
```bash
image: un grupo de personas remando
image: una cocinando una pizza
```
o con chatgpt
```bash
Crea un ejemplo de carrusel de fondo dinámico usando bootstrap con javascript html
```
Aunque para estas cosas es mejor usar el plugin de chatgpt en neovim del que hable en la publicacion anterior.
