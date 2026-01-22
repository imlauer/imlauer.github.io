---
title: "Neomutt manual"
date: 2025-12-15T21:20:04-03:00
---
Perfect — **neomutt + Gmail (app password) on Arch** is a very solid setup. Below is a **clean, modern neomutt config** with Gmail-specific fixes.

---

## 1. Create a Gmail App Password (if not already done)

Google Account → **Security** → **2-Step Verification** → **App passwords**

* App: **Mail**
* Device: **Other**
* Copy the **16-character password**

---

## 2. Install neomutt on Arch

```bash
sudo pacman -S neomutt ca-certificates
```

(Optional but recommended later)

```bash
sudo pacman -S pass gnupg
```

---

## 3. Create config directory

```bash
mkdir -p ~/.config/neomutt
chmod 700 ~/.config/neomutt
```

---

## 4. Main config: `~/.config/neomutt/neomuttrc`

```muttrc
############
# Identity #
############
set from = "your@gmail.com"
set realname = "Your Name"

########
# IMAP #
########
set imap_user = "your@gmail.com"
set imap_pass = "APP_PASSWORD"
set folder = "imaps://imap.gmail.com:993"
set spoolfile = "+INBOX"

########
# SMTP #
########
set smtp_url = "smtp://your@gmail.com@smtp.gmail.com:587/"
set smtp_pass = "APP_PASSWORD"
set smtp_authenticators = "login"

################
# Gmail Folders #
################
set record = "+[Gmail]/Sent Mail"
set postponed = "+[Gmail]/Drafts"
set trash = "+[Gmail]/Trash"

#################
# Gmail behavior #
#################
set move = no                  # Gmail uses labels
set imap_keepalive = 300
set imap_pipeline_depth = 1
set sleep_time = 0

#######
# TLS #
#######
set ssl_force_tls = yes

###################
# Neomutt niceties #
###################
set sidebar_visible = yes
set sidebar_width = 30
set sidebar_short_path = yes

bind index,pager \CP sidebar-prev
bind index,pager \CN sidebar-next
bind index,pager \CO sidebar-open
bind index,pager \CC sidebar-close

############
# Defaults #
############
set editor = "nvim"
set pager_index_lines = 10
set sort = threads
set strict_threads = yes
```

🔐 **Protect credentials**

```bash
chmod 600 ~/.config/neomutt/neomuttrc
```

---

## 5. Start neomutt

```bash
neomutt
```

You should see your Gmail inbox and sidebar immediately.

---

## 6. (Recommended) Use `pass` instead of plain text passwords

### Store the app password

```bash
pass insert gmail/app
```

### Replace in `neomuttrc`

```muttrc
set imap_pass = "`pass gmail/app`"
set smtp_pass = "`pass gmail/app`"
```

Neomutt will execute `pass` and insert the password securely.

---

## 7. Gmail-specific notes

**Correct Gmail folder names**

```text
[Gmail]/Sent Mail
[Gmail]/Drafts
[Gmail]/Trash
```

**Archive (All Mail)**

```text
[Gmail]/All Mail
```

**Do not enable message moving**

```muttrc
set move = no
```

---

## 8. Debug if something fails

Start neomutt with debug:

```bash
neomutt -d 5
```

Common issues:

* ❌ Using your normal Gmail password instead of app password
* ❌ Wrong folder names
* ❌ File permissions too open

---

## 9. Optional next steps

I can help you add:

* 📬 **Multiple Gmail accounts**
* 🗄️ **Maildir + offline sync (isync/mbsync)**
* 🔐 **GPG signing/encryption**
* 🎨 **Themes & status line customization**

Just tell me what you want next.


Alright 😄 let’s build you a **proper power-user neomutt setup on Arch** with **everything**:

✔ multiple Gmail accounts
✔ offline Maildir sync (mbsync)
✔ GPG signing & encryption
✔ sidebar, theme, statusline
✔ clean file layout you won’t hate later

This is a **battle-tested setup**, not a blog-post toy.

---

# 0. What you’ll end up with (overview)

```
~/.config/neomutt/
├── neomuttrc
├── accounts/
│   ├── gmail-main.rc
│   └── gmail-work.rc
├── colors.rc
├── statusline.rc
├── gpg.rc
└── sidebar.rc

~/.mail/
├── gmail-main/
└── gmail-work/

~/.mbsyncrc
```

---

# 1. Install everything (Arch)

```bash
sudo pacman -S neomutt isync pass gnupg ca-certificates
```

Optional but nice:

```bash
sudo pacman -S lynx w3m urlscan
```

---

# 2. App passwords (per account)

For **each Gmail account**:

* Google Account → Security → 2-Step Verification → App Password
* Save them using `pass`:

```bash
pass insert gmail/main
pass insert gmail/work
```

---

# 3. Offline sync with mbsync (Maildir)

## `~/.mbsyncrc`

```ini
IMAPAccount gmail-main
Host imap.gmail.com
User your@gmail.com
PassCmd "pass gmail/main"
SSLType IMAPS

IMAPStore gmail-main-remote
Account gmail-main

MaildirStore gmail-main-local
Path ~/.mail/gmail-main/
Inbox ~/.mail/gmail-main/INBOX

Channel gmail-main
Master :gmail-main-remote:
Slave :gmail-main-local:
Patterns *
Create Slave
SyncState *
Remove None
Expunge None

############################

IMAPAccount gmail-work
Host imap.gmail.com
User work@gmail.com
PassCmd "pass gmail/work"
SSLType IMAPS

IMAPStore gmail-work-remote
Account gmail-work

MaildirStore gmail-work-local
Path ~/.mail/gmail-work/
Inbox ~/.mail/gmail-work/INBOX

Channel gmail-work
Master :gmail-work-remote:
Slave :gmail-work-local:
Patterns *
Create Slave
SyncState *
Remove None
Expunge None
```

### First sync

```bash
mbsync -a
```

(Optional cron/systemd later.)

---

# 4. neomutt main config

## `~/.config/neomutt/neomuttrc`

```muttrc
set mailcap_path = ~/.mailcap
set folder = ~/.mail
set header_cache = ~/.cache/neomutt
set message_cachedir = ~/.cache/neomutt

set editor = nvim
set charset = utf-8
set sort = threads
set strict_threads = yes

# Load components
source ~/.config/neomutt/sidebar.rc
source ~/.config/neomutt/colors.rc
source ~/.config/neomutt/statusline.rc
source ~/.config/neomutt/gpg.rc

# Default account
source ~/.config/neomutt/accounts/gmail-main.rc
```

---

# 5. Account configs (easy switching)

## `accounts/gmail-main.rc`

```muttrc
set realname = "Your Name"
set from = "your@gmail.com"

set spoolfile = "+gmail-main/INBOX"
set record = "+gmail-main/[Gmail]/Sent Mail"
set postponed = "+gmail-main/[Gmail]/Drafts"
set trash = "+gmail-main/[Gmail]/Trash"

set smtp_url = "smtp://your@gmail.com@smtp.gmail.com:587/"
set smtp_pass = "`pass gmail/main`"
set smtp_authenticators = "login"
```

## `accounts/gmail-work.rc`

```muttrc
set realname = "Your Name (Work)"
set from = "work@gmail.com"

set spoolfile = "+gmail-work/INBOX"
set record = "+gmail-work/[Gmail]/Sent Mail"
set postponed = "+gmail-work/[Gmail]/Drafts"
set trash = "+gmail-work/[Gmail]/Trash"

set smtp_url = "smtp://work@gmail.com@smtp.gmail.com:587/"
set smtp_pass = "`pass gmail/work`"
set smtp_authenticators = "login"
```

### Switch accounts inside neomutt

```muttrc
macro index,pager <F2> "<enter-command>source ~/.config/neomutt/accounts/gmail-main.rc<enter>"
macro index,pager <F3> "<enter-command>source ~/.config/neomutt/accounts/gmail-work.rc<enter>"
```

---

# 6. Sidebar

## `sidebar.rc`

```muttrc
set sidebar_visible = yes
set sidebar_width = 30
set sidebar_short_path = yes

bind index,pager \CP sidebar-prev
bind index,pager \CN sidebar-next
bind index,pager \CO sidebar-open
bind index,pager \CC sidebar-close
```

---

# 7. GPG signing & encryption

### Generate a key (if needed)

```bash
gpg --full-generate-key
```

### `gpg.rc`

```muttrc
set pgp_autosign = yes
set pgp_replyencrypt = yes
set pgp_timeout = 1800

set crypt_use_gpgme = yes
set crypt_autosign = yes
set crypt_replyencrypt = yes
```

Sign manually while composing:

```
p → s
```

Encrypt:

```
p → e
```

---

# 8. Theme & colors (clean, readable)

## `colors.rc`

```muttrc
color normal        white black
color status        black cyan
color indicator     black yellow
color sidebar_new   yellow black
color sidebar_highlight cyan black
color quoted        green black
color quoted1       cyan black
color quoted2       blue black
color error         red black
```

---

# 9. Status line (useful info)

## `statusline.rc`

```muttrc
set status_format = "[%a] %r | %f | %L msgs | %p%% | %y"
```

---

# 10. Daily workflow

Sync mail:

```bash
mbsync -a
```

Open mail:

```bash
neomutt
```

Switch accounts:

* **F2** → main
* **F3** → work

---

# 11. Optional next-level shit 🚀

If you want, next we can add:

* 🔁 systemd timer for auto-sync
* 🏷️ Gmail label macros
* 📎 attachment viewer config
* 🧠 notmuch integration (fast search)
* 🎨 true Nord / Gruvbox themes

Just tell me which rabbit hole you want first.
