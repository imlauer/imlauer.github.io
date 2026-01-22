---
title: "Rebuild cmake"
date: 2025-02-07T16:18:55-03:00
tags: ['linux']
---
https://stackoverflow.com/questions/50102893/rebuild-configuration-file-when-there-are-no-cmake-changes

There are a few issues you need to overcome to have this work.

* When cmake is run any version information you extract from subversion is baked into the generated build files, and so becomes static.
* Cmake is only rerun if it detects the generated build files have become out of date (eg: if a CMakeLists.txt file is updated)
* You can create a custom_target which will be run every time you build (from the docs: "The target has no output file and is ALWAYS CONSIDERED OUT OF DATE") which generates the file, but that will force you to rebuild your generated version file every time.
