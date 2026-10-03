#!/usr/bin/env bash
# Carga (o recarga) las cookies de X en accounts.db para twscrape.
#
# Uso:
#   1) Abrí x.com logueado con la cuenta, DevTools > Network > cualquier request a x.com
#      > copiá el header Cookie.
#   2) Pegalo en tinygrad-archive/cookies.txt (NO se commitea, ver .gitignore)
#      con formato: auth_token=...; ct0=...   (o uno por línea)
#   3) corré:  ./set_cookies.sh
#
# Para INVALIDAR una sesión filtrada: en x.com entrá con esa cuenta y usá
# Configuración -> Seguridad -> "Cerrar todas las otras sesiones" (o cambiá la
# contraseña). Eso mata el auth_token al instante.
set -euo pipefail

BASE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DB="$BASE/accounts.db"
COOKIES_FILE="$BASE/cookies.txt"
USER_ID="${X_ACCOUNT:-tinygrad_adhoc}"

if [ ! -s "$COOKIES_FILE" ]; then
  echo "error: falta $COOKIES_FILE (pegalo con el header Cookie de x.com)" >&2
  exit 1
fi

COOKIES="$(tr '\n' ';' < "$COOKIES_FILE" | sed 's/;;*/;/g; s/^; //; s/; $//')"

if ! printf '%s' "$COOKIES" | grep -q 'auth_token=' || ! printf '%s' "$COOKIES" | grep -q 'ct0='; then
  echo "error: cookies.txt necesita auth_token= y ct0=" >&2
  exit 1
fi

rm -f "$DB"
twscrape --db "$DB" add_cookie "$USER_ID" "$COOKIES"
twscrape --db "$DB" accounts

echo
echo "OK. Verificá que diga logged_in=1. Si dice 0, las cookies están malas o vencieron."
