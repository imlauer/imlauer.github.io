---
title: "Enviar simple GET request en C"
date: 2025-01-18T08:41:44-03:00
tags: ['programming']
---
```c
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[]){

	if (argc != 2){
		fprintf(stderr, "Usage: %s IP-Address\n", argv[0]);
		return EXIT_FAILURE;
	}

	struct sockaddr_in server_address;

	int s = socket(AF_INET, SOCK_STREAM, 0);
	if (s < 0){ 
		fprintf(stderr,"Error: socket.\n");
		return EXIT_FAILURE;
	}

	memset(&server_address, '0', sizeof(server_address));
	server_address.sin_family = AF_INET;
	server_address.sin_port = htons(80);
	if (inet_pton(AF_INET, argv[1], &server_address.sin_addr) <= 0){
		fprintf(stderr,"Error: inet_pton.\n");
		return EXIT_FAILURE;
	}

	if ( connect(s, (struct sockaddr *)&server_address, sizeof(server_address)) < 0 ){
		fprintf(stderr,"Error: Connect failed.\n");
		return EXIT_FAILURE;
	}

	char buffer[18] = "GET / HTTP/1.0\n\n";
	char recv[10000];

	send(s, buffer, sizeof(buffer),MSG_EOR);

	int n;
	while ( (n = read(s, recv, sizeof(recv)-1)) > 0)
	{
		recv[n] = 0;
		if (fputs(recv, stdout) == EOF){
			printf("\n Error: Fputs error\n");
		}
	}

	return 0;
}
```

Tremendo. `inet_pton` es una función que convierte direcciones IPv4 y IPv6 de texto a una forma binaria.
Lo más complicado fue saber que hay que castear server_address porque espera una estructura `sockaddr` no `sockaddr_in` sino no compila.

Lo programé leyendo las man pages (ubicaba el cursor sobre la función y apretaba Shfit+k en vim) fue difícil sin googlear y buscaba ejemplos en el código del `kernel de linux`.

Bastante complicado para ser sólo un GET.
