---
title: "Buscar palabra en archivo comprimido"
date: 2025-02-05T19:44:23-03:00
tags: ['grep']
---
Since your files are actually tar.gz file you need to untar them as well. Tar is a archiving utility that packages multiple files together (in your case only one) and
was originally used to backup data to tape drives.

The tar utility did not originally compress content hence why it was usually streamed through gzip or other utilities for compression.. if you unzip a tar.gz you are
still left with the tar achieving layer which is why it is not working.

these days gun tar will tar and zip for you in one command using the "z" command.

so in order for you to do what you want I think you need to do use the tar extract "x" unzip "z" from a file target "f" and stream to stdout "O" then pipe to grep. It
should look something like this:

```bash
tar -xzf mycompressedlogfile.tar.gz -O | grep -l "pattern"
```

Since your tar version does not have -z then try piping the output of gzip through tar before your grep

```bash
 gzip -dc mycompressedlogfile.tar.gz | tar -xOf - | grep -l "pattern"
```

But I do not think Solaris 10 version of tar support the "O" option to stream the tar content to `stdout`. :( You are probably going to have to do the above (without the O so "`tar -xf -`") for each file from within a working directory, or some way to make sure you can account for the files that are created, search the content, and then
delete the file(s). Sorry unless you can install gnu-tar on the Solaris machine.

I guess from the answer selected you were able to search the tar stream for the pattern (since it is not compressed I guess that makes sense) and figure it out from
there.. :) good deal.

Glad you got your answer.

