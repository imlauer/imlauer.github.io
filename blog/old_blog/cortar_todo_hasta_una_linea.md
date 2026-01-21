---
title: "Cortar todo hasta una línea"
date: 2025-02-18T16:47:46-03:00
tags: ['bash']
---
You can use GNU sed:

```bash
sed -i '5,$d' file.txt
```

That is, 5,$ means the range line 5 until the end, and d means to delete. Only the
first 4 lines will remain. The -i flag tells sed to edit the file in-place.

If you have only BSD sed, then the -i flag requires a backup file suffix:

```bash
sed -i.bak '5,$d' file.txt
```

As @ephemient pointed out, while this solution is simple, it's inefficient because
sed will still read the input until the end of the file, which is unnecessary.

As @agc pointed out, the inverse logic of my first proposal might be actually more
intuitive. That is, do not print by default (-n flag), and explicitly print range
1,4:

```bash
sed -ni.bak 1,4p file.txt
```

Another simple alternative, assuming that the first 4 lines are not excessively long
and so they easily fit in memory, and also assuming that the 4th line ends with a
newline character, you can read the first 4 lines into memory and then overwrite the
file:

```bash
lines=$(head -n 4 file.txt)
echo "$lines" > file.txt
```

---

Minor refinements on Janos' answer, ephemient's answer, and cdark's comment:

1. Simpler (and faster) sed code:

```bash
sed -i 4q file
```

2. When a filter util can't directly edit a file, there's sponge:

```bash
    head -4 file | sponge file
```
3. Most efficient for Linux might be truncate -- coreutils sibling util to fallocate, which offers the same minimal I/O of ephemient's more portable, (but more complex), dd-based answer:

```bash
truncate -s `head -4 file | wc -c` file
```

