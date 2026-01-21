---
title: "Crear ventana y pintarla en SDL2 en C"
date: 2025-02-20T19:56:57-03:00
tags: ['c']
---
Debés incluir `SDL2/SDL.h`.

```c
void scc(int code){
        if (code < 0){
            fprintf(stderr, "SDL ERROR: %s\n", SDL_GetError());
            exit(1);
        }
}
void *scp(void *ptr){
    if (ptr == NULL){
        fprintf(stderr, "SDL ERROR: %s\n", SDL_GetError());
        exit(1);
    }
}

SDL_Surface *surface_from_file(const char *file_path){
    int w, h, n;
    unsigned char *pixels = stbi_load(file_path, &w, &h, &n, STBI_rgb_alpha);
    if (pixels == NULL){
        fprintf(stderr, "ERROR: could not load file %s\n", file_path, stbi_failure_reason());
        exit(1);
    }
}

SDL_Window *window = SDL_CreateWindow
SDL_Renderer *renderer = SDL_CreateRenderer(window, -1 , SDL_RENDERER_ACCELERATED));

SDL_Surface *surface = scp(SDL_CreateRGBSurfaceWithFormat(flags, width, height, depth, format);
SDL_Surface *surface = scp(SDL_CreateRGBSurfaceFrom(FONT, FONT_WIDTH, FONT_HEIGHT, 32, FONT_WIDTH, 0xFF, 0xFF, 0xFF, 0xFF));
bool quit = false; 
while (!quit){
    SDL_Event event = {0};
    while (SDL_PollEvent(&event)) {
        switch(event.type){
            case SQL_QUIT: {
                quit = true;
            } break;
            }
        }
    }
}

SDL_SetRenderDrawColor(renderer, 0,0,0,0);
SDL_RendererClear(renderer);
SDL_RenderPresent(renderer);

```
