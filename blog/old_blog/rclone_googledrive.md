---
title: "Rclone Google Drive"
date: 2025-05-29T20:24:15-03:00
tags: ['rclone']
---
Una forma mucho más fácil y rápida de acceder a tu Google Drive es usando `rclone`.

sudo pacman -S fuse3


https://www.youtube.com/embed/f8K-V3HHDA0

```bash
rclone config
n
gdrive
13 (google drive)
```
###### Ahora tenes que seguir esta guía para crear tu Google Drive ID para rclone:
https://rclone.org/drive/#making-your-own-client-id

1. Log into the Google API Console with your Google account. It doesn't matter what Google account you use. (It need not be the same account as the Google Drive you want to access)
2. Select a project or create a new project.
3. Under "ENABLE APIS AND SERVICES" search for "Drive", and enable the "Google Drive API".
4. Click "Credentials" in the left-side panel (not "Create credentials", which opens the wizard).
5. If you already configured an "Oauth Consent Screen", then skip to the next step; if not, click on "CONFIGURE CONSENT SCREEN" button (near the top right corner of the right panel), then select "External" and click on "CREATE"; on the next screen, enter an "Application name" ("rclone" is OK); enter "User Support Email" (your own email is OK); enter "Developer Contact Email" (your own email is OK); then click on "Save" (all other data is optional). You will also have to add some scopes, including

* https://www.googleapis.com/auth/docs
* https://www.googleapis.com/auth/drive in order to be able to edit, create and delete files with RClone.
* https://www.googleapis.com/auth/drive.metadata.readonly which you may also want to add.
* If you want to add all at once, comma separated it would be https://www.googleapis.com/auth/docs,https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/drive.metadata.readonly.

6. After adding scopes, click "Save and continue" to add test users. Be sure to add your own account to the test users. Once you've added yourself as a test user and saved the changes, click again on "Credentials" on the left panel to go back to the "Credentials" screen.

(PS: if you are a GSuite user, you could also select "Internal" instead of "External" above, but this will restrict API use to Google Workspace users in your organisation).

7. Click on the "+ CREATE CREDENTIALS" button at the top of the screen, then select "OAuth client ID".
8. Choose an application type of "Desktop app" and click "Create". (the default name is fine)
9. It will show you a client ID and client secret. Make a note of these.
(If you selected "External" at Step 5 continue to Step 10. If you chose "Internal" you don't need to publish and can skip straight to Step 11 but your destination drive must be part of the same Google Workspace.)
10. Go to "Oauth consent screen" and then click "PUBLISH APP" button and confirm. You will also want to add yourself as a test user.
11. Provide the noted client ID and client secret to rclone.

Luego de ingresar las credenciales:
```bash
1 (Full access all files) (drive)
root_folder_id> (vacío)
service_account_file> (vacío)
Edit advanced config?> n
use autoconfig?> y
```
Ahora ingresá desde el navegador
```bash
Configure this as a team drive? no
token = {....}
y) Yes this is OK
q
rclone ls gdrive:
mkdir gdrive
rclone mount --daemon gdrive: /home/esotericwarfare/gdrive/
```


###### Cifrar tus archivos de google drive:
https://www.youtube.com/embed/_YnHU0dJn1E
```bash
rclone config
n
crypted
Encrypt/Decrypt a remote "crypt" (10)
remote> gdrive:
filename_encryption> Enter
directory_name_encryption> Enter
Password or pass phrase for encryption.
y
Optional 2nd password 
y
y
q
mkdir crypted
rclone mount crypted: ~/crypted
rclone config file
```

Si creas archivos locales en esa carpeta los creas en Google Drive también, permite lectura y escritura.
