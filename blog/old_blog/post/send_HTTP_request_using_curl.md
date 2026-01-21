---

title: "Enviar una simple consulta HTTP usando curl en C"
date: 2024-09-16T08:12:49-03:00
tags: ['c']
---
```c
// Compile: gcc curlcurl.c -o curlcurl -lcurl
#include <curl/curl.h>

CURL *curl = curl_easy_init();
curl_easy_setopt(curl, CURLOPT_URL, 
    "https://imlauera.github.io/index.xml");
curl_easy_perform(curl);
```

https://curl.se/libcurl/c/example.html    
https://curl.se/libcurl/c/simple.html
