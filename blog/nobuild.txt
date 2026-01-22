---
title: "C: Nobuild"
date: 2025-02-14T23:04:52-03:00
tags: ['c']
---
```c
#define NOBUILD_IMPLEMENTATION
#include "./nobuild.h"

#define CFLAGS "-Wall", "-Wextra", "-std=c11", "-pedantic", "-ggdb"

int main(int argc, char **argv)
{
    GO_REBUILD_URSELF(argc, argv);
    CMD("cc", CFLAGS, "-o", "minicel", "src/mainc.");

    if (argc > 1){
        if (strcmp(argv[1], "run") == 0){
            CMD("./minicel", "input.csv");
        } else if (strcmp(argv[1], "gdb") == 0){
            CMD("gdb", "./minicel");
        } else {
            PANIC("%s is unknown subcommand", argv[1]);
        }
    }
    return 0;
}
```

Es como usar C como shell script.
