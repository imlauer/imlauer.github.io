---
title: "Conectarse a un servidor XMPP desde la consola"
date: 2025-11-02T11:28:48-03:00
tags: ['xmpp']
---

Usando profanity.

# 1️⃣ Install a CLI XMPP client

Popular CLI clients:

| Client        | Install on Arch            | Notes                                              |
| ------------- | -------------------------- | -------------------------------------------------- |
| **profanity** | `sudo pacman -S profanity` | Full-featured, supports OMEMO, commands are simple |
| **mcabber**   | `sudo pacman -S mcabber`   | Very minimal, uses `.mcabberrc` for config         |
| **finch**     | `sudo pacman -S finch`     | Console version of Pidgin, supports accounts       |

We’ll use **profanity** here — easiest for first-time setup.

---

# 2️⃣ Start profanity

```bash
profanity
```

You’ll enter the interactive CLI:

```text
profanity v0.xx
Type /help for commands
>
```

---

# 3️⃣ Create an account (in-band registration)

Inside profanity:

```text
/account add
```

It will prompt:

```
Username: yourusername
Domain: creep.im
Password: <choose a strong password>
Resource [optional]: CLI
```

* **Resource**: optional; identifies this session (like `CLI` or `laptop`).
* The client will attempt **in-band registration** on `creep.im`.
* If successful, your account is created instantly.

> ⚠️ If it fails, check that port `5222` is reachable (`nc -vz creep.im 5222`) and retry.

---

# 4️⃣ Select and enable your account

After creation:

```text
/account list
/account use yourusername@creep.im
```

Then connect:

```text
/connect
```

You should see:

```
Connecting to creep.im:5222...
Connected!
```

---

# 5️⃣ Sending a message

```text
/msg friend@creep.im Hello from CLI!
```

* Replace `friend@creep.im` with the recipient’s JID.
* You can also start a chat session:

```text
/chat friend@creep.im
```

Type messages normally; they are sent on Enter.

---

# 6️⃣ Receiving messages

* Incoming messages automatically appear in the terminal.
* To check online users:

```text
/roster
```

---

# 7️⃣ Disconnect

```text
/disconnect
/quit
```

---

# 8️⃣ Optional: Enable OMEMO encryption

```text
/omemo start
```

* Profanity supports OMEMO (end-to-end encryption) if both clients support it.
* You can verify device IDs and trust your contacts via `/omemo list`.

---

# 9️⃣ Debugging connection issues

From your shell:

```bash
# Check SRV records (XMPP standard)
dig +short _xmpp-client._tcp.creep.im SRV

# Test TCP port
nc -vz creep.im 5222

# Test TLS handshake
openssl s_client -connect creep.im:5222 -starttls xmpp
```

If these fail, the client won’t be able to connect.

---

✅ **Summary of basic workflow**

```text
profanity
/account add           # create account
/account use user@creep.im
/connect
/msg friend@creep.im Hello from CLI!
/disconnect
/quit
```


---

Perfect! We can set up **profanity fully from the command line** so you can register, connect, and even send a first message automatically. Here’s how to do it on **Arch Linux**.

---

## 1️⃣ Install profanity

```bash
sudo pacman -S profanity
```

---

## 2️⃣ Prepare a simple configuration file

Profanity can read commands from a file. Let’s create one:

```bash
nano ~/.profrc
```

Add:

```text
# Profanity auto config
account add yourusername@creep.im yourpassword CLI
account use yourusername@creep.im
connect
```

* Replace `yourusername` with your desired username.
* Replace `yourpassword` with a strong password.
* `CLI` is the resource name; can be anything (e.g., `laptop`, `phone`).

Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

---

## 3️⃣ Run profanity in **batch mode** to auto-connect

```bash
profanity -c ~/.profrc
```

* Profanity will:

  1. Add your account (in-band registration on `creep.im`)
  2. Use the account
  3. Connect to the server

---

## 4️⃣ Send a message automatically

You can add a message command to the config file:

```text
# ~/.profrc
account add yourusername@creep.im yourpassword CLI
account use yourusername@creep.im
connect
msg friend@creep.im Hello from CLI!
```

* Replace `friend@creep.im` with the recipient JID.
* When you run `profanity -c ~/.profrc`, it will connect **and send that message automatically**.

---

## 5️⃣ Optional: Run in non-interactive mode

If you want **fully automated scripts**, you can do:

```bash
echo "/account add user@creep.im password CLI
/account use user@creep.im
/connect
/msg friend@creep.im Hello from CLI!" > /tmp/profanity_commands.txt

profanity -c /tmp/profanity_commands.txt
```

---

## 6️⃣ Notes & tips

* **In-band registration** must be allowed on the server (creep.im supports it).
* If registration fails, check TCP port:

```bash
nc -vz creep.im 5222
```

* You can enable **OMEMO encryption** in CLI later:

```text
/omemo start
/omemo list
```
