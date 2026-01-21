---
title: "Disk quota exceeded fix pip"
date: 2025-11-25T06:10:16-03:00
tags: ['pip']
---

#### Error

```bash
git clone https://github.com/rouralberto/zim-llm.git
./setup.sh

pip install -r requirements.txt

Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        99G   77G   17G  82% /
devtmpfs        1.9G     0  1.9G   0% /dev
tmpfs           1.9G     0  1.9G   0% /dev/shm
efivarfs         40K   30K  5.4K  85% /sys/firmware/efi/efivars
tmpfs           758M  1.2M  757M   1% /run
tmpfs           1.0M     0  1.0M   0% /run/credentials/systemd-journald.service
tmpfs           1.9G  1.3G  640M  67% /tmp
/dev/sda2      1017M  234M  784M  23% /boot

Downloading torch-2.9.1-cp313-cp313-manylinux_2_28_x86_64.whl (899.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━━━ 761.0/899.7 MB 11.7 MB/s eta 0:00:12ERROR: Could not install packages due to an OSError: [Errno 122] Disk quota exceeded

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━━━ 761.8/899.7 MB 11.7 MB/s eta 0:00:12
[I] (zim_rag_env) esotericwarfare@arch ~/zim-llm (master) [0|1]>
```

**How can I fix this?**

You're running out of space **on `/tmp` or your user quota**, not on the root filesystem as a whole.
The key clue is:

```bash
ERROR: [Errno 122] Disk quota exceeded
```

and your `/tmp` is **67% full (1.3G used)** and pip downloads large wheels **into /tmp by default**.

### ✔ Why the install is failing

PyTorch wheels are huge (~900 MB). Pip stores the temporary wheel during installation in:

```
/tmp/pip-*
```

Your temporary storage or user quota fills up before pip can finish writing the ~900 MB wheel + extracted files.

---

# ✅ Fix Options

## **Option 1 — Tell pip to use a different temp directory**

Choose a directory that has plenty of space, e.g. your home folder or `/var/tmp`.

```bash
mkdir -p ~/pip-tmp
TMPDIR=~/pip-tmp pip install -r requirements.txt
```

or

```bash
TMPDIR=/var/tmp pip install -r requirements.txt
```

---

## **Option 2 — Clean `/tmp`**

Check what’s using space:

```bash
du -sh /tmp/*
```

Then remove old temporary files:

```bash
sudo rm -rf /tmp/*
```

(Be careful: only do this if no applications depend on `/tmp`.)

---

## **Option 3 — Clear pip cache**

Pip cache can easily grow to several GB.

```bash
pip cache purge
```

---

## **Option 4 — Use a smaller PyTorch**

If you don’t need CUDA:

```bash
pip install torch==2.9.1+cpu --index-url https://download.pytorch.org/whl/cpu
```

This is **much smaller** (~150–200 MB instead of ~900 MB).

---

## **Option 5 — Increase storage**

If you’re on a VPS / container, you may need to expand:

* The filesystem space
* Your user quota

---

# 👉 Recommended quick fix:

Try this first:

```bash
mkdir ~/tmp
TMPDIR=~/tmp pip install -r requirements.txt
```

---

If you want, paste your `requirements.txt` and I can help you optimize or reduce the installed package sizes.

