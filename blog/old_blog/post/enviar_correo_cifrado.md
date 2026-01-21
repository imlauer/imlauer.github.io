---
title: "Enviar archivo cifrado"
tags: ['gpg']
---
https://www.youtube.com/watch?v=DMGIlj7u7Eo

```bash
gpg --gen-key
gpg --armor --export imlauerandres@gmail.com > public_key.asc  
gpg --encrypt --recipient 'imlauerandres@gmail.com' --output confidential.txt.enc secret.txt 
gpg --decrypt --output secret.txt confidential.txt.enc
cat secret.txt

gpg --import publickey.gpg
gpg --import < publickey.gpg

openssl rand -out secret.key 32

openssl aes-256-cbc -in secretfile.txt -out secretfile.txt.enc -pass file:secret.key

```

https://medium.com/@michaelmeade3/using-gpg-71c6ae7c6199
https://archive.is/Zhz4T

https://superuser.com/questions/576506/how-to-use-ssh-rsa-public-key-to-encrypt-a-text

https://www.bjornjohansen.com/encrypt-file-using-ssh-key

https://superuser.com/questions/576506/how-to-use-ssh-rsa-public-key-to-encrypt-a-text


Note that this only works if the file is small enough. e.g. 200 bytes. 

```bash
ssh-keygen -f ~/.ssh/id_rsa.pub -e -m PKCS8 > id_rsa.pem.pub
openssl rsautl -encrypt -pubin -inkey id_rsa.pem.pub -ssl -in myMessage.txt -out myEncryptedMessage.txt
```


#### Usando ssh public key para cifrar un archivo

```bash
# Recently I had to send a password to someone over Skype. Since that's obviously not a good idea, I asked for 
# the person's public SSH RSA key, and used it to encrypt the password itself.


# Convert the public key into PEM format
ssh-keygen -f path/to/id_rsa.pub -e -m pem > ~/id_rsa.pub.pem

# Using the public pem file to encrypt a string
echo "sometext" | openssl rsautl -encrypt -pubin -inkey ~/id_rsa.pub.pem > ~/encrypted.txt

# Or a file
cat ~/some_file.txt | openssl rsautl -encrypt -pubin -inkey ~/id_rsa.pub.pem > ~/encrypted.txt

# To decrypt, you'll need the private key
cat ~/encrypted.txt | openssl rsautl -decrypt -inkey path/to/id_rsa > ~/decrypted.txt
```



```bash
ssh-keygen -f id_rsa.pub -e -m pem > ~/id_rsa.pub.pem
cat mensaje_secreto.txt | openssl rsautl -encrypt -pubin -inkey ~/id_rsa.pub.pem > ~/encrypted.txt

split -b 200 -d  secret.txt en_partes

for i in *en_partes*; do cat $i | openssl rsautl -encrypt -pubin -inkey ~/id_rsa.pub.pem > ~/mensajecifrado$i.txt ; done ```
