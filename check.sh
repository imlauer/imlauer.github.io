#!/usr/bin/bash
# Verifica rapido que todos los mirrors responden.
# Tor: torsocks + w3m (curl 8.x se niega a resolver .onion por RFC 7686)
# I2P: proxy http de i2pd en 192.168.0.143:4444 (el primer request tarda, reintenta)
# Yggdrasil / local / IPFS: curl directo

ONION=rv7ffn5nnhmvi5ik4lrd6s6u4smolejq2mfgp2lnpsm3g54y3bxznwid.onion
I2P=sxyqnifh2zdzizjibys4q52tpr5qxpsthnwokzkrhi3si74nqqsq.b32.i2p
YGG="http://[201:1ce0:e526:93d7:ccb:2aac:17e7:c157]:8100"
CID=bafybeicjnhgtdudc34pin7gzrno2nt7jmxkpyhqbqrtyez6gs5kevgygjm
IPNS=k51qzi5uqu5dk2ezsd0tfqm7vnub5c0jdghrkygq1gel7cda8jnv0w9rtla2hk

ok()   { printf '\033[32m%-6s\033[0m %s\n' "$1" "$2"; }
bad()  { printf '\033[31m%-6s\033[0m %s\n' "$1" "$2"; }

check() { # check <cmd...>
	local out
	if out=$("$@" 2>&1); then ok "$out" "$label"; else bad "${out:-FAIL}" "$label"; fi
}

# clearnet
label="Clearnet principal"; check curl -s -o /dev/null -w '%{http_code}' --max-time 15 https://imlauer.github.io/
label="Clearnet foro (deberia ser 404, no existe en GH Pages)"; check curl -s -o /dev/null -w '%{http_code}' --max-time 15 https://imlauer.github.io/forum/

# Tor (w3m porque curl bloquea .onion)
for p in "" "forum/"; do
	label="Tor /$p"
	if timeout 30 torsocks w3m -dump "http://$ONION/$p" >/dev/null 2>&1; then
		ok "OK" "$label"
	else
		bad "FAIL" "$label"
	fi
done

# I2P (reintentos: i2pd tarda en montar el tunnel)
for p in "" "forum/"; do
	label="I2P /$p"; code=000
	for i in 1 2 3; do
		code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 40 -x http://192.168.0.143:4444 "http://$I2P/$p")
		[ "$code" = 200 ] && break
		sleep 2
	done
	if [ "$code" = 200 ]; then ok "$code" "$label"; else bad "$code" "$label"; fi
done

# Yggdrasil (local 8100 y la direccion ygg)
for p in "" "forum/"; do
	label="Yggdrasil /$p"; check curl -s -o /dev/null -w '%{http_code}' --max-time 15 "$YGG/$p"
	label="Local    /$p"; check curl -s -o /dev/null -w '%{http_code}' --max-time 10 "http://127.0.0.1:8100/$p"
done

# IPFS
label="IPFS CID";    check curl -s -o /dev/null -w '%{http_code}' --max-time 30 "http://127.0.0.1:8090/ipfs/$CID/"
label="IPFS IPNS";   check curl -s -o /dev/null -w '%{http_code}' --max-time 30 "http://127.0.0.1:8090/ipns/$IPNS/"
label="IPFS pin";    check env IPFS_PATH=/mnt/linux2/ipfs ipfs pin ls "/ipfs/$CID"

# servicios systemd
echo
systemctl is-active tor i2pd yggdrasil ipfs sitio | paste -d' ' <(printf 'tor\ni2pd\nyggdrasil\nipfs\nsitio\n') -
