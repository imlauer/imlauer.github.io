$'\r' : command not found 
Solución: bash -x scripts/f1.sh

You will need to use "percent encoding" in the URL to encode the special character.
https://www.w3schools.com/tags/ref_urlencode.ASP

For example, when testing an LDAP URL using curl, the below command will work in
previous versions of curl:

curl -v "ldap://[ip address]:389/OU=Active Service Accounts,OU=Service Accounts,OU=Co
However this will fail in the newer versions with the error "URL rejected: Malformed
input to a URL function". You will need to replace the space with "%20" like below:

curl -v ldap://[ip address]:389/OU=Active%20Service%20Accounts,OU=Service%20Accounts,
Feedback

