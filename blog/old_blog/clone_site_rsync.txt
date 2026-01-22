---
title: "Clone a folder of a rsync server"
---
**As simple as**:

```bash
rsync -avcr --delete rsync://rsync_server.com:1111/folder .
```
---

**Cronjob**:

```bash
@daily rsync -avcr --delete rsync://rsync_server.com:1111/folder /home/esotericwarfare/offline_site
```
