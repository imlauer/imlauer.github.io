---
title: "The account is locked due to 3 failed logins."
date: 2025-12-29T15:53:23-03:00
---
```bash
The account is locked due to 3 failed logins.
(9 minutes left to unlock)
Password:
```

how do I unlock it?

1. **Login as root**: If you have root access, you can login as root and use the `pam_tally2` or `faillock` command to reset the failed login counter. The exact command depends on the PAM configuration used on your system.
    * For `pam_tally2`, use: `pam_tally2 --user esotericwarfare --reset`
    * For `faillock`, use: `faillock --user esotericwarfare --reset`
2. **Reboot the system**: Rebooting the system will also reset the failed login counter. However, this might not be a feasible solution if you're on a production system or don't have physical access.

