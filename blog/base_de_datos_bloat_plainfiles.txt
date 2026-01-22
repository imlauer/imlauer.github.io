---
title: "Las base de datos son bloat mejor usa un archivo de texto plano."
date: 2025-12-03T04:01:56-03:00
tags: ['db']
---

Las bases de datos son bloat, es mejor usar un archivo texto plano y usar las herramientas de Unix para buscar informacion dentro de ellos.

---

Aquí tenés una **guía práctica y realista** para usar **un archivo de texto plano como “base de datos”** para un colegio, usando solo **grep, awk, sed, sort, cut** y herramientas Unix.
La clave es **formato bien definido**, **un registro por línea** y **campos separados** de forma consistente.

---

# ✅ **1. Elegir un formato simple, estable y fácil de parsear**

El mejor formato para “base de datos en texto plano” usando Unix es:

### **Formato: TSV (tab-separated values, separado por TAB)**

Razones:

* No choca con comas dentro del texto.
* `awk -F '\t'` lo lee perfecto.
* `grep` funciona igual.
* Fácil de editar en Vim.

---

# ✅ **2. Estructura universal para cualquier tipo de registro**

Usá un **“schema” fijo**:

```
TYPE    ID      DATE        FIELD1      FIELD2     FIELD3     EXTRA
```

### Campos recomendados:

* `TYPE`: el tipo de dato → `DOCENTE`, `ALUMNO`, `ASISTENCIA`, `LICENCIA`, `AMON`, `TUTOR`, etc.
* `ID`: identificador único → DNI, legajo o código.
* `DATE`: formato estándar → `2025-03-04`
* `FIELD1..FIELDn`: depende del tipo.
* `EXTRA`: texto libre opcional.

---

# ✅ **3. Ejemplos reales**

### **Docentes**

```
DOCENTE  20300300    2025-03-01  ingreso     Juan Perez     Matemática
DOCENTE  20300300    2025-03-15  licencia    enfermedad     2-dias
```

### **Alumnos**

```
ALUMNO   55022110    2025-03-01  ingreso     Lopez Maria    2B
TUTOR    55022110    2025-03-01  tutor       Carlos Lopez   padre
```

### **Asistencias**

```
ASIST    55022110    2025-03-04  presente    2B
ASIST    55022110    2025-03-05  ausente     2B
```

### **Amonestaciones**

```
AMON     55022110    2025-03-05  leve        celular        profesorX
AMON     55022110    2025-03-10  grave       conducta       preceptorY
```

---

# ✅ **4. Cómo consultar rápido con Unix**

### ■ Todos los registros de un alumno:

```
grep -P "\t55022110\t" base2025.tsv
```

### ■ Solo asistencias:

```
grep "^ASIST" base2025.tsv
```

### ■ Asistencias de un alumno:

```
awk -F '\t' '$1=="ASIST" && $2=="55022110"' base2025.tsv
```

### ■ Cantidad de ausencias:

```
awk -F '\t' '$1=="ASIST" && $2=="55022110" && $4=="ausente" {c++} END {print c}' base2025.tsv
```

### ■ Sanciones de un curso:

```
awk -F '\t' '$1=="AMON" && $6=="2B"' base2025.tsv
```

---

# ✅ **5. Cómo agregar un registro desde Bash**

Hacete un script:

### `add.sh`

```bash
#!/bin/sh
echo -e "$@" >> base2025.tsv
```

Uso:

```bash
./add.sh "ASIST\t55022110\t2025-03-06\tpresente\t2B"
```

---

# ✅ **6. Cómo validar datos**

Podés agregar checks con awk:

```
awk -F '\t' 'NF < 4 { print "Registro inválido:", $0}' base2025.tsv
```

---

# ✅ **7. Organización por año**

Te recomiendo:

```
/datos-colegio/
    base2025.tsv
    base2026.tsv
    base2027.tsv
```

Un archivo grande por año es perfecto.

---

# ✅ **8. Opcional: separar por “tablas virtuales”**

Si querés dividir un poco:

```
docentes2025.tsv
alumnos2025.tsv
asistencias2025.tsv
amonestaciones2025.tsv
tutores2025.tsv
```

Pero tu idea de **un solo archivo** es totalmente válida — solo necesitás el campo `TYPE`.

---

# ⚡ ¿Querés que te genere un *schema* completo y lista de comandos útiles para cada tipo de dato?

Puedo armarte un “manual del sistema” con todo predefinido.






---

You can absolutely use a **plain text file as a database** in Unix. This is classic Unix philosophy: *“Text is the universal interface.”*
Below are **practical patterns** depending on how you want to store and query data — all without jq, without SQLite, without JSON — just text + grep/awk/sed.

---

# ✅ 1. Choose a Format (custom plain text)

The simplest and most robust **flat-file database** formats are:

### **A) KEY=VALUE (one record per line)**

```
id=1 name="John Doe" age=30
id=2 name="Alice" age=25
```

### **B) CSV (comma separated)**

```
1,John Doe,30
2,Alice,25
```

### **C) Pipe/Tab separated**

```
1|John Doe|30
2|Alice|25
```

### **D) One file per record (directory database)**

```
db/
  1.txt
  2.txt
```

Each file contains arbitrary text.

---

# ✅ 2. How to Query the “Database”

## 🔍 Search rows by field

### **KEY=VALUE format**

Find all entries where name contains "Alice":

```sh
grep 'name="Alice"' db.txt
```

Find id=2:

```sh
grep '^id=2 ' db.txt
```

### CSV example

Find records whose first column is "2":

```sh
awk -F, '$1 == 2' db.csv
```

---

# 🔄 3. Insert new record

Append:

```sh
echo 'id=3 name="Bob" age=50' >> db.txt
```

---

# ✏ 4. Update a record

Replace age for id=1:

```sh
sed -i 's/^id=1 .*/id=1 name="John Doe" age=31/' db.txt
```

---

# ❌ 5. Delete a record

Delete id=2:

```sh
sed -i '/^id=2 /d' db.txt
```

---

# 🔥 6. Example Flat-File Database Implementation

### **db.sh**

```sh
#!/bin/sh

DB="db.txt"

add() {
    echo "id=$1 name=\"$2\" age=$3" >> "$DB"
}

get() {
    grep "^id=$1 " "$DB"
}

delete() {
    sed -i "/^id=$1 /d" "$DB"
}

update_age() {
    sed -i "s/^id=$1 .*/id=$1 name=\"$2\" age=$3/" "$DB"
}
```

Usage:

```sh
./db.sh add 1 "John Doe" 30
./db.sh add 2 "Alice" 25
./db.sh get 2
./db.sh update_age 1 "John Doe" 31
./db.sh delete 2
```

---

# 📂 7. Alternative: directory per record

```
db/
  1
  2
```

Create:

```sh
echo "name=Alice" > db/2
echo "age=25" >> db/2
```

Search:

```sh
grep -R "Alice" db/
```

---

# ⭐ When is this useful?

✔ shell scripts
✔ embedded devices
✔ tiny systems
✔ config management
✔ low data volume (<50k records)
✔ no dependencies
✔ grep/awk/sed are extremely fast

---

# ⚠ When it falls apart

❌ hundreds of thousands of rows
❌ concurrent writes
❌ complex queries (joins, ordering, types)

---

# If you want, I can:

* design a full mini-database system in shell
* give you CRUD helpers
* make an “SQL-like” interface in bash
* design indexing for fast lookups (using grep caches)

Just tell me your ideal workflow.

---




Nice — you want a *practical*, file-based “database” using only Unix tools. Below is a focused, pragmatic guide + ready-to-run shell toolkit you can copy-paste and use. It covers data layout choices, common operations (CRUD + queries), performance & safety tips, and a simple script (`plaindb.sh`) that implements insert/find/update/delete on newline-delimited JSON (NDJSON) and on delimited CSV/TSV. I thought deeper about scale, concurrency, indexing, and schema evolution so you don't get burned later.

# Why plain files (quick pros/cons)

**Pros**

* Simple, transparent, easy to version with git.
* No DB server, low dependency surface.
* Fast for many read-heavy workloads using grep/rg/awk/jq.
  **Cons**
* No transactions unless you implement locking/atomic writes.
* Harder to scale and do complex joins/queries compared to a DB.
* Requires careful handling for concurrency, schema evolution, and backups.

# Recommended file formats

1. **NDJSON (newline-delimited JSON)** — each line is a JSON object. Best for structured records, works great with `jq`.

   * Example: `users.ndjson`
   * `{"id":1,"name":"A","email":"a@x.com"}`
2. **CSV/TSV** — great for tabular data and fast parsing with `awk`, `cut`.

   * Use `\t` (TSV) to avoid comma-escaping headaches.
3. **Flat key-value** — `key:value` per line for tiny lookup tables.
4. **Inverted index files** — precomputed index files to support fast full-text lookups.

# Tools to use (short)

* `grep` / `rg` (ripgrep) — text search
* `awk` — field processing, aggregations, joins-ish
* `sed` — in-place edits / transforms
* `jq` — JSON querying and mutation
* `cut`, `sort`, `uniq`, `join` — selection and joins on sorted files
* `flock` — file locking for safe concurrent writes
* `mv`/`cp` technique — atomic replace (`mv tmp file`)
* `gzip`/`xz` — compress cold data
* `git` — version your files for history & lightweight rollback
* `fzf` — interactive selection

---

# Patterns & examples

## 1) NDJSON: append, find, update, delete

File: `users.ndjson`

```json
{"id":1,"name":"Alice","email":"alice@example.com"}
{"id":2,"name":"Bob","email":"bob@example.com"}
```

### Insert (append safely)

```sh
# create a new record and append atomically
record='{"id":3,"name":"Carol","email":"carol@example.com"}'
printf '%s\n' "$record" >> users.ndjson
# better: use flock for multi-writer safety (see script below)
```

### Find records

* Full-text with grep:

```sh
grep -i 'alice' users.ndjson
```

* Field-level with jq:

```sh
jq -c 'select(.email=="alice@example.com")' users.ndjson
```

### Select columns (project)

```sh
jq -r '.id, .name' users.ndjson    # prints each field on a new line (not ideal)
jq -r '. | [.id, .name] | @tsv' users.ndjson  # id<TAB>name
```

### Update a record (idempotent pattern)

Can't modify in-place reliably — create a new file then move:

```sh
jq 'if .id==2 then .email="bob@new.com" else . end' users.ndjson > users.ndjson.tmp
mv users.ndjson.tmp users.ndjson
```

If multiple writers exist, use `flock` to protect the critical section (script later).

### Delete

```sh
jq 'select(.id != 2)' users.ndjson > users.ndjson.tmp && mv users.ndjson.tmp users.ndjson
```

## 2) CSV/TSV with awk

File: `products.tsv` (header: id<TAB>name<TAB>price)

```
id	name	price
1	Widget	12.50
2	Gizmo	9.99
```

### Find where price > 10

```sh
awk -F'\t' 'NR==1{print; next} $3+0 > 10' products.tsv
```

### Group by and count

Count products by name prefix:

```sh
awk -F'\t' 'NR>1 {prefix=substr($2,1,3); counts[prefix]++} END{for (k in counts) print k, counts[k]}' products.tsv | sort -k2 -n -r
```

### Join two files (both sorted by key)

`join` requires files sorted on join field:

```sh
# assume customers.tsv and orders.tsv keyed by customer_id in column1
join -t$'\t' -1 1 -2 1 <(sort -k1,1 customers.tsv) <(sort -k1,1 orders.tsv)
```

## 3) Indexing for speed (simple inverted index)

If you have lots of text and `grep` becomes slow / you need targeted search, create an index mapping token → list of record IDs.

Example pipeline to build a basic inverted index (tokenized lowercased words):

```sh
# input: docs.ndjson each line {"id":123, "text":"..."}
jq -r '. | [.id, .text] | @tsv' docs.ndjson \
  | tr '[:upper:]' '[:lower:]' \
  | awk -F'\t' '{id=$1; text=$2; gsub(/[^a-z0-9]+/," ",text); split(text, a, " "); for(i in a) if(length(a[i])>1) print a[i] "\t" id}' \
  | sort -k1,1 -u \
  | awk -F'\t' '{word=$1; id=$2; ids[word]=ids[word]?ids[word] "," id : id} END{for (w in ids) print w "\t" ids[w]}' \
  > index.tsv
```

Lookup:

```sh
grep -P '^keyword\t' index.tsv
# parse list of ids and then pull records from ndjson using jq or grep -Ff
```

## 4) Transactions & concurrency (flock + atomic move)

Example pattern for safe writes:

```sh
(
  flock -x 200 || exit 1
  # make changes in a tmp file
  jq '...update...' users.ndjson > users.ndjson.tmp
  mv users.ndjson.tmp users.ndjson
) 200>users.ndjson.lock
```

* `flock -x` grabs exclusive lock on file descriptor 200.
* Always write to a `.tmp` and `mv` to replace atomically.

## 5) Backups & snapshots

* Periodic snapshots: `cp users.ndjson users.$(date +%Y%m%d%H%M).ndjson`
* Lightweight: commit changes to git (`git add *.ndjson && git commit -m "snapshot"`).
* For big files, use incremental rsync to remote.

## 6) Validation & schema evolution

* Keep a small schema file `schema.json` that documents required fields and types.
* Validate new records with `jq` filter before appending:

```sh
jq -e '(.id|type=="number") and (.email|test("@"))' <<<"$candidate"
```

* For migration: write a one-shot `jq` or `awk` migration script that produces a new file, test it, then replace.

---

# Ready-to-use toolkit: `plaindb.sh`

Copy this script and put it in your `$PATH` (`chmod +x plaindb.sh`). It implements simple CRUD on an NDJSON file with locking.

```sh
#!/usr/bin/env bash
# plaindb.sh - minimal NDJSON "db" operations: insert, find, update, delete, list
# Usage: plaindb.sh <dbfile> <cmd> [args...]
# Requires: jq, flock, mktemp

DB="$1"; shift
CMD="$1"; shift

LOCK="${DB}.lock"

usage(){ cat <<EOF
Usage: $0 <dbfile> <cmd> [args...]
Commands:
  insert  <json>                 Append a JSON record (string)
  find    <jq-filter>            Print matching records (jq filter)
  list                           Print all records
  update  '<jq-update>'          Apply jq program to all records (e.g. 'if .id==2 then .name="X" else . end')
  delete  '<jq-condition>'       Delete records matching condition (jq select; e.g. '.id==2')
EOF
}

if [ -z "$DB" ] || [ -z "$CMD" ]; then usage; exit 1; fi
mkdir -p "$(dirname "$DB")" 2>/dev/null || true
: "${DB:=db.ndjson}"

with_lock() {
  # usage: with_lock <command...>
  exec 200>"$LOCK"
  flock -x 200
  "$@"
  flock -u 200
}

case "$CMD" in
  insert)
    json="$1"
    if ! echo "$json" | jq -e . >/dev/null 2>&1; then
      echo "invalid json" >&2; exit 2
    fi
    # append under lock
    with_lock bash -c "printf '%s\n' \"$json\" >> '$DB'"
    ;;
  find)
    filter="$1"
    if [ -z "$filter" ]; then filter='.'; fi
    # safe read, no write locking necessary
    jq -c "$filter" "$DB"
    ;;
  list)
    jq -c '.' "$DB"
    ;;
  update)
    prog="$1"
    tmp="$(mktemp "${DB}.tmp.XXXX")"
    with_lock bash -c "jq -c '$prog' '$DB' > '$tmp' && mv '$tmp' '$DB'"
    ;;
  delete)
    cond="$1"
    tmp="$(mktemp "${DB}.tmp.XXXX")"
    with_lock bash -c "jq -c \"select( ( $cond ) | not )\" '$DB' > '$tmp' && mv '$tmp' '$DB'"
    ;;
  *)
    usage; exit 1
esac
```

Examples:

```sh
# insert
./plaindb.sh users.ndjson insert '{"id":1,"name":"Alice"}'
# find by id
./plaindb.sh users.ndjson find 'select(.id==1)'
# update
./plaindb.sh users.ndjson update 'if .id==1 then .email="a@x.com" else . end'
# delete
./plaindb.sh users.ndjson delete '.id==1'
```

---

# Advanced tips (thinking deeper)

* **Search performance**: `rg` (ripgrep) is much faster than `grep`. For enormous files, split data by sharding keys (year, prefix), or maintain indexes.
* **Atomic counters**: maintain a small file `next_id` and `flock` it to safely increment IDs.
* **Multi-field joins**: sort files on join keys and use `join`. For complex joins, it's often simpler to load small sets into memory with `awk` associative arrays.
* **Partial reads**: store large blobs separately (e.g., `blobs/<id>.dat`) and keep metadata in the main NDJSON.
* **Full-text search**: if you need advanced text queries (stemming, ranking), either maintain an index or use `sqlite FTS` (that's a DB—but it's a single file).
* **Monitoring & metrics**: keep a `metrics.log` file with line-oriented events (timestamped) and roll it daily.
* **Immutable append-only log**: prefer append-only files and periodic compaction—this makes crash recovery trivial. Compaction script reads file, removes tombstones, writes compacted file, swaps atomically.
* **Encryption**: use `gpg --encrypt` for at-rest, `gpg --decrypt` when reading; or use `age`.
* **Testing & CI**: add schema tests that `jq`-validate every new commit to the repo.

---

# Quick cheatsheet

* `grep -i foo file` — fast text search
* `jq -c 'select(.field=="x")' file` — filter NDJSON
* `awk -F'\t' '$3>10' file.tsv` — numeric filter on column 3
* `sort -k1,1 file | join -t$'\t' -1 1 -2 1 file2` — join on column1
* `flock -x 200; mv tmp file;` — atomic replacement with lock
* `git add *.ndjson && git commit -m "snapshot"` — snapshot your DB state

---

If you want, I can:

* produce a slightly fancier CLI (with `getopts`, `--where`, `--select`) to make ad-hoc queries easier,
* show how to build a tiny inverted index for full-text search and a lookup tool that returns top-N results,
* or tailor the scripts for CSV/TSV only (no jq).

Which of those should I give you next?

---

If you want to use **jq** as your “database engine,” the **best possible format** is:

# ✅ NDJSON (Newline-Delimited JSON)

One JSON object **per line**:

`users.ndjson`:

```json
{"id":1, "name":"Alice", "email":"alice@example.com"}
{"id":2, "name":"Bob", "email":"bob@example.com"}
{"id":3, "name":"Carol", "email":"carol@example.com"}
```

No commas, no arrays, no brackets — **just one JSON per line**.
This is the format used by big data tools (Elasticsearch, Firehose, Hadoop, etc.).

---

# ✅ 1. FIND (query with jq)

List *all* records:

```sh
jq -c . users.ndjson
```

Find by name:

```sh
jq -c 'select(.name == "Alice")' users.ndjson
```

Case-insensitive:

```sh
jq -c 'select(.name | ascii_downcase == "alice")' users.ndjson
```

Find by ID:

```sh
jq -c 'select(.id == 2)' users.ndjson
```

Search email ending in `.com`:

```sh
jq -c 'select(.email | endswith(".com"))' users.ndjson
```

---

# ✅ 2. INSERT (append)

Append a new object:

```sh
echo '{"id":4, "name":"David", "email":"david@example.com"}' >> users.ndjson
```

---

# ✅ 3. DELETE a record

Delete ID=3:

```sh
jq -c 'select(.id != 3)' users.ndjson \
  > tmp && mv tmp users.ndjson
```

Delete every Bob:

```sh
jq -c 'select(.name != "Bob")' users.ndjson \
  > tmp && mv tmp users.ndjson
```

---

# ✅ 4. UPDATE a record

Example: change Bob’s email:

```sh
jq -c '
  if .id == 2
  then .email = "bob@newmail.com"
  else .
  end
' users.ndjson > tmp && mv tmp users.ndjson
```

Update multiple fields:

```sh
jq -c '
  if .id == 3
  then .name = "Carolina" | .email = "caro@example.com"
  else .
  end
' users.ndjson > tmp && mv tmp users.ndjson
```

---

# ✅ 5. SORT the "database"

Sort by ID:

```sh
jq -c . users.ndjson | sort -n -t: -k2
```

Better way (jq loads fully, sorts, outputs NDJSON):

```sh
jq -c -s 'sort_by(.id)[]' users.ndjson > tmp && mv tmp users.ndjson
```

(`-s` = "slurp" = load entire file)

Sort by name:

```sh
jq -c -s 'sort_by(.name)[]' users.ndjson > tmp && mv tmp users.ndjson
```

---

# ✅ 6. CREATE a reusable CLI tool

`jsondb.sh`:

```sh
#!/bin/sh
DB="$1"
CMD="$2"
shift 2

case "$CMD" in
  find)
    jq -c "select($1)" "$DB"
    ;;

  insert)
    echo "$1" >> "$DB"
    ;;

  delete)
    jq -c "select(($1) | not)" "$DB" > tmp && mv tmp "$DB"
    ;;

  update)
    filter="$1"   # e.g. '.id == 2'
    update="$2"   # e.g. '.email = "x@y.com"'
    jq -c "
      if ($filter) then $update else . end
    " "$DB" > tmp && mv tmp "$DB"
    ;;

  *)
    echo "Commands: find / insert / delete / update"
    ;;
esac
```

Example:

```sh
./jsondb.sh users.ndjson find '.id == 1'
./jsondb.sh users.ndjson insert '{"id":4,"name":"D","email":"d@mail"}'
./jsondb.sh users.ndjson delete '.id == 2'
./jsondb.sh users.ndjson update '.id == 3' '.name = "Carol X"'
```

---

# Want more?

I can generate:

* a full **query language** (where, select, limit, order by)
* automatic **primary key indexing**
* multi-table JSON structure
* a “transaction log” version
* CLI with subcommands and help text

Just tell me what you'd like to build next.

