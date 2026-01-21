---
title: "AI en la terminal"
date: 2024-11-18T14:19:26-03:00
tags: ['cli']
---
[https://old.reddit.com/r/commandline/comments/1ba5k6h/claude_ai_in_terminal/?rdt=46031](https://old.reddit.com/r/commandline/comments/1ba5k6h/claude_ai_in_terminal/?rdt=46031)

https://git.blek.codes/blek/hey
```bash
yay -S hey-duck
```

[https://github.com/sigoden/aichat](https://github.com/sigoden/aichat) All in one CLI tool for 10+ AI platforms, including OpenAI (ChatGPT), Gemini, Claude, Mistral, LocalAI, Ollama, VertexAI, Ernie, Qianwen...

Actualmente estoy usando modelos gratuitos, no pago por ninguna API key de claude ai, ni chat gpt premium, estos son los modelos gratuitos que soporta:

```bash 
[I] esotericwarfare@arch ~> aichat --list-models
huggingface:NousResearch/Hermes-3-Llama-3.1-8B
huggingface:mistralai/Mistral-Small-Instruct-2409
huggingface:mistralai/Mistral-Nemo-Instruct-2407
[I] esotericwarfare@arch ~>
```

```bash

Options:
  -m, --model <MODEL>        Select a LLM model
      --prompt <PROMPT>      Use the system prompt
  -r, --role <ROLE>          Select a role
  -s, --session [<SESSION>]  Start or join a session
      --empty-session        Ensure the session is empty
      --save-session         Force the session to be saved
  -a, --agent <AGENT>        Start a agent
  -R, --rag <RAG>            Start a RAG
      --serve [<ADDRESS>]    Serve the LLM API and WebAPP
  -e, --execute              Execute commands in natural language
  -c, --code                 Output code only
  -f, --file <FILE>          Include files with the message
  -S, --no-stream            Turn off stream mode
      --dry-run              Display the message without sending it
      --info                 Display information
      --list-models          List all available chat models
      --list-roles           List all roles
      --list-sessions        List all sessions
      --list-agents          List all agents
      --list-rags            List all RAGs
  -h, --help                 Print help
  -V, --version              Print version
[I] esotericwarfare@arch ~>
```

Podemos usar el argumento `--code` y `-S` para que solo nos produzca código sin que escriba línea por línea sino que nos tire la salida de una.

Ejemplo de uso:
```bash
aichat -S --code "programá un juego multiple choice en C"
```

Y pueden usar también tgpt: `yay -S tgpt`

Ejemplos de uso: 

```bash
aichat
tgpt -m 
```

La AI es buena para construir aplicaciones en python.


Que te diviertas, hasta luego.
