---
title: "Vim record"
date: 2024-12-02T20:39:16-03:00
tags: ['vim']
---

```bash
" Recording (BEST TIP of ALL)
qq  # record to q
your complex series of commands
q   # end recording
@q to execute
@@ to Repeat
5@@ to Repeat 5 times
qQ@qq                             : Make an existing recording q recursive *N*
" editing a register/recording
"qp                               :display contents of register q (normal mode)
<ctrl-R>q                         :display contents of register q (insert mode)
" you can now see recording contents, edit as required
"qdd                              :put changed contacts back into q
@q                                :execute recording/register q
```
