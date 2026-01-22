---
title: "Gestion escolar"
date: 2025-12-31T08:18:08-03:00
tags: ['escuela']
---

Los sistemas de seguimiento escolar son bloat, podes directamente usar un archivo de texto para guardar absolutamente todo y hacer un seguimiento escolar. Aprende a usar vim, grep y otras herramientas de unix para buscar informacion en ese archivo de texto, cada año crea otro archivo y listo.

# ChatGPT

Archivo TSV (separado por tabs).

```
# ESCUELA-GESTION-ANUAL.tsv
# FORMATO UNICO / APEND-ONLY / BUSCABLE CON GREP-AWK-SED
# SEPARADOR: TAB (\t)
# CONVENCIONES:
# - campo[0] = TIPO_REGISTRO
# - campo[1] = ID_UNICO
# - resto = CLAVE=VALOR
# - TEXTO SIN ESPACIOS (usar _)
# - FECHAS ISO-8601
# - NUNCA SE EDITA, SOLO SE AGREGA

################################################################################
# PERSONAS
################################################################################

PERSONA	P0001	TIPO=ALUMNO	DNI=45123456	APELLIDO=Gomez	NOMBRE=Juan	SEXO=M	FECHA_NAC=2012-05-14	NACIONALIDAD=AR	DOMICILIO=Av_Siempreviva_123	TELEFONO=1144455566	EMAIL=NA	ESTADO=ACTIVO
PERSONA	P0002	TIPO=ALUMNO	DNI=43999888	APELLIDO=Perez	NOMBRE=Maria	SEXO=F	FECHA_NAC=2011-11-02	NACIONALIDAD=AR	DOMICILIO=Calle_Falsa_456	TELEFONO=1133322211	EMAIL=NA	ESTADO=ACTIVO
PERSONA	P0003	TIPO=DOCENTE	DNI=22333444	APELLIDO=Lopez	NOMBRE=Ana	SEXO=F	FECHA_NAC=1980-03-22	TELEFONO=1122233344	EMAIL=ana@escuela.edu.ar	ESTADO=ACTIVO
PERSONA	P0004	TIPO=PRECEPTOR	DNI=20111222	APELLIDO=Martinez	NOMBRE=Carlos	SEXO=M	FECHA_NAC=1978-08-10	TELEFONO=1199988877	EMAIL=carlos@escuela.edu.ar	ESTADO=ACTIVO

################################################################################
# CURSOS / DIVISIONES / CICLOS
################################################################################

CICLO	CIC2025	ANIO=2025	NIVEL=Secundario	ESTADO=ACTIVO
CURSO	CUR001	CICLO=CIC2025	NOMBRE=2A	TURNO=MAÑANA	AULA=12	ORIENTACION=Comun
CURSO	CUR002	CICLO=CIC2025	NOMBRE=3B	TURNO=TARDE	AULA=7	ORIENTACION=Comun

################################################################################
# INSCRIPCIONES
################################################################################

INSCRIPCION	I0001	ALUMNO=P0001	CURSO=CUR001	FECHA_ALTA=2025-03-01	CONDICION=REGULAR
INSCRIPCION	I0002	ALUMNO=P0002	CURSO=CUR002	FECHA_ALTA=2025-03-01	CONDICION=REGULAR

################################################################################
# MATERIAS / ESPACIOS CURRICULARES
################################################################################

MATERIA	MAT001	NOMBRE=Matematica	AREA=Ciencias_Exactas	CARGA_HORARIA=4
MATERIA	MAT002	NOMBRE=Lengua	AREA=Lengua_y_Literatura	CARGA_HORARIA=4

################################################################################
# DESIGNACIONES DOCENTES
################################################################################

CATEDRA	CAT0001	MATERIA=MAT001	CURSO=CUR001	DOCENTE=P0003	FECHA_DESDE=2025-03-01	FECHA_HASTA=2025-12-10
CATEDRA	CAT0002	MATERIA=MAT002	CURSO=CUR002	DOCENTE=P0003	FECHA_DESDE=2025-03-01	FECHA_HASTA=2025-12-10

################################################################################
# TUTORES / RESPONSABLES
################################################################################

RESPONSABLE	R0001	ALUMNO=P0001	DNI=30111222	APELLIDO=Gomez	NOMBRE=Laura	VINCULO=Madre	TELEFONO=1133344455	EMAIL=NA
RESPONSABLE	R0002	ALUMNO=P0002	DNI=28999888	APELLIDO=Perez	NOMBRE=Jose	VINCULO=Padre	TELEFONO=1144455566	EMAIL=NA

################################################################################
# ASISTENCIAS ALUMNOS
################################################################################

ASISTENCIA_ALUMNO	AA000001	FECHA=2025-03-01	ALUMNO=P0001	CURSO=CUR001	ESTADO=PRESENTE	JUSTIFICACION=NA
ASISTENCIA_ALUMNO	AA000002	FECHA=2025-03-01	ALUMNO=P0002	CURSO=CUR002	ESTADO=AUSENTE	JUSTIFICACION=NO

################################################################################
# ASISTENCIAS PERSONAL
################################################################################

ASISTENCIA_PERSONAL	AP000001	FECHA=2025-03-01	PERSONA=P0003	ROL=DOCENTE	ESTADO=PRESENTE
ASISTENCIA_PERSONAL	AP000002	FECHA=2025-03-01	PERSONA=P0004	ROL=PRECEPTOR	ESTADO=AUSENTE	MOTIVO=LICENCIA

################################################################################
# LICENCIAS
################################################################################

LICENCIA	L0001	PERSONA=P0004	ROL=PRECEPTOR	TIPO=MEDICA	FECHA_DESDE=2025-03-01	FECHA_HASTA=2025-03-10	OBSERVACION=Reposo

################################################################################
# CALIFICACIONES / EVALUACIONES
################################################################################

EVALUACION	E0001	MATERIA=MAT001	CURSO=CUR001	TIPO=PARCIAL	TRIMESTRE=1	FECHA=2025-04-10	PESO=1
NOTA	N000001	EVALUACION=E0001	ALUMNO=P0001	VALOR=8	CONDICION=APROBADO
NOTA	N000002	EVALUACION=E0001	ALUMNO=P0002	VALOR=6	CONDICION=APROBADO

################################################################################
# TRAYECTORIA ESCOLAR
################################################################################

TRAYECTORIA	T0001	ALUMNO=P0001	CICLO=CIC2025	ESTADO=EN_CURSO	OBSERVACION=NA
TRAYECTORIA	T0002	ALUMNO=P0002	CICLO=CIC2025	ESTADO=EN_CURSO	OBSERVACION=NA

################################################################################
# SANCIONES / CONVIVENCIA
################################################################################

SANCION	S0001	ALUMNO=P0002	FECHA=2025-05-03	TIPO=AMONESTACION	ARTICULO=12	GRAVEDAD=LEVE	DESCRIPCION=Falta_de_respeto
SANCION	S0002	ALUMNO=P0001	FECHA=2025-06-01	TIPO=SUSPENSION	DIAS=2	ARTICULO=20	DESCRIPCION=Pelea

################################################################################
# INTERVENCIONES PSICOLOGICAS / GABINETE
################################################################################

INTERVENCION	PSI0001	ALUMNO=P0002	FECHA=2025-05-10	TIPO=ENTREVISTA	DERIVACION=PRECEPTORIA	RESULTADO=Seguimiento
INTERVENCION	PSI0002	ALUMNO=P0002	FECHA=2025-06-02	TIPO=REUNION_TUTOR	RESULTADO=Mejora

################################################################################
# COMUNICACIONES / ACTAS
################################################################################

COMUNICACION	C0001	FECHA=2025-04-01	ALUMNO=P0001	TIPO=CUADERNO	ASUNTO=Rendimiento	TEXTO=Bajo_desempeño
ACTA	A0001	FECHA=2025-03-20	TIPO=REUNION_DOCENTE	CURSO=CUR001	TEMA=Seguimiento_general

################################################################################
# FIN DE ARCHIVO
################################################################################
```

# Comandos para buscar informacion desde la consola de comandos.

```bash
# alumnos
grep '^PERSONA' ESCUELA-GESTION-ANUAL.tsv | grep 'TIPO=ALUMNO'

# alumno por DNI
grep '^PERSONA' ESCUELA-GESTION-ANUAL.tsv | grep 'DNI=45123456'

# alumno por apellido
grep '^PERSONA' ESCUELA-GESTION-ANUAL.tsv | grep 'APELLIDO=Gomez'

# alumnos de un curso
grep '^INSCRIPCION' ESCUELA-GESTION-ANUAL.tsv | grep 'CURSO=CUR001'

# tutores de un alumno
grep '^RESPONSABLE' ESCUELA-GESTION-ANUAL.tsv | grep 'ALUMNO=P0001'

# asistencias de un alumno
grep '^ASISTENCIA_ALUMNO' ESCUELA-GESTION-ANUAL.tsv | grep 'ALUMNO=P0001'

# inasistencias sin justificar
grep '^ASISTENCIA_ALUMNO' ESCUELA-GESTION-ANUAL.tsv | grep 'ESTADO=AUSENTE' | grep 'JUSTIFICACION=NO'

# asistencias del personal
grep '^ASISTENCIA_PERSONAL' ESCUELA-GESTION-ANUAL.tsv

# licencias activas
grep '^LICENCIA' ESCUELA-GESTION-ANUAL.tsv

# sanciones de un alumno
grep '^SANCION' ESCUELA-GESTION-ANUAL.tsv | grep 'ALUMNO=P0002'

# notas de un alumno
grep '^NOTA' ESCUELA-GESTION-ANUAL.tsv | grep 'ALUMNO=P0001'

# notas por materia
grep '^NOTA' ESCUELA-GESTION-ANUAL.tsv | grep 'MATERIA=MAT001'

# promedios por alumno
awk -F'\t' '$1=="NOTA"{split($0,a,"VALOR=");split(a[2],b,"\t");print b[1]}' ESCUELA-GESTION-ANUAL.tsv

# alumnos con sanciones y notas bajas
grep '^SANCION' ESCUELA-GESTION-ANUAL.tsv | cut -f3 | \
while read alumno; do
  grep '^NOTA' ESCUELA-GESTION-ANUAL.tsv | grep "$alumno" | grep 'VALOR=[1-5]'
done

# intervenciones psicologicas
grep '^INTERVENCION' ESCUELA-GESTION-ANUAL.tsv

# historial completo de un alumno
grep 'P0001' ESCUELA-GESTION-ANUAL.tsv

# comunicaciones a tutores
grep '^COMUNICACION' ESCUELA-GESTION-ANUAL.tsv

# actas por curso
grep '^ACTA' ESCUELA-GESTION-ANUAL.tsv | grep 'CURSO=CUR001'

# conteo de inasistencias por alumno
grep '^ASISTENCIA_ALUMNO' ESCUELA-GESTION-ANUAL.tsv | grep 'ESTADO=AUSENTE' | \
awk -F'\t' '{for(i=1;i<=NF;i++) if($i~/ALUMNO=/) print $i}' | sort | uniq -c
```


# Vim macros

Perfecto. Si **ya sos experto en Vim**, este formato te queda como anillo al dedo.
Sin palabrerío, **recetas concretas** para **cargar datos rápido** en ese `.tsv`.

---

```vim
" ===== archivo: ~/.vim/escuela.vim =====
" ajustes para TSV de gestión escolar

setlocal nowrap
setlocal noexpandtab
setlocal tabstop=8
setlocal softtabstop=0
setlocal shiftwidth=0
setlocal list
setlocal listchars=tab:▸\ ,trail:·
setlocal colorcolumn=0
```

---

### Autocmd por tipo de archivo

```vim
" ~/.vimrc
augroup escuela
  autocmd!
  autocmd BufRead,BufNewFile ESCUELA-GESTION-*.tsv source ~/.vim/escuela.vim
augroup END
```

---

### Snippets manuales (sin plugins)

```vim
" pegar en ~/.vimrc

iabbrev <expr> alu strftime("ALUMNO\tA%04d\tDNI=\tAPELLIDO=\tNOMBRE=\tSEXO=\tFECHA_NAC=\tCURSO=\tESTADO=ACTIVO")
iabbrev <expr> asis strftime("ASISTENCIA_ALUMNO\tAA%06d\tFECHA=".strftime("%Y-%m-%d")."\tALUMNO=\tCURSO=\tESTADO=")
iabbrev <expr> nota strftime("NOTA\tN%06d\tALUMNO=\tMATERIA=\tCURSO=\tTRIMESTRE=\tVALOR=")
iabbrev <expr> sanc strftime("SANCION\tS%04d\tALUMNO=\tFECHA=".strftime("%Y-%m-%d")."\tTIPO=\tDESCRIPCION=")
iabbrev <expr> psi strftime("INTERVENCION\tPSI%04d\tALUMNO=\tFECHA=".strftime("%Y-%m-%d")."\tTIPO=\tOBSERVACION=")
```

---

### Cargar muchas asistencias rápido (visual block)

```vim
" ejemplo:
" escribir una línea base
ASISTENCIA_ALUMNO	AA000100	FECHA=2025-03-01	ALUMNO=P0001	CURSO=CUR001	ESTADO=PRESENTE

" duplicar 30 veces
y29p

" seleccionar columna ALUMNO
<C-v>jjjjjjjjjjjjjjjjjjjjjjjj
I ALUMNO=P000
```

---

### Reemplazos masivos inteligentes

```vim
:%s/CURSO=CUR001/CURSO=CUR002/g
:%s/ESTADO=PRESENTE/ESTADO=AUSENTE/gc
```

---

### Macros para carga diaria

```vim
" grabar macro a
qa
A	FECHA=2025-03-02
<Esc>
j
q

" ejecutar en 40 líneas
40@a
```

---

### Ordenar bloques por tipo

```vim
:sort /^ASISTENCIA_ALUMNO/
:sort /^NOTA/
:sort /^SANCION/
```

---

### Navegación instantánea por secciones

```vim
:/^ASISTENCIA_ALUMNO
:/^NOTA
:/^INTERVENCION
```

---

### Ventana auxiliar para búsqueda en vivo

```vim
:vsplit | terminal
grep '^ASISTENCIA_ALUMNO' ESCUELA-GESTION-ANUAL.tsv
```

---

### Vista tipo tabla dentro de Vim

```vim
:%!column -t -s $'\t'
```

(revertir)

```vim
u
```

---

### Validar formato (tabs reales)

```vim
:!grep -nP '^[^\t]+\t[^\t]+' %
```

---

### Archivo por día (append-only puro)

```bash
cat asistencia_2025-03-01.tsv >> ESCUELA-GESTION-ANUAL.tsv
```

---

### Regla mental clave (Vim + texto)

> **Una línea = un hecho**
> **Nunca editar pasado**
> **Todo se agrega**
> **IDs humanos y grep-friendly**

---

Si querés:

* macros por **preceptor**
* carga tipo **planilla**
* navegación tipo **fzf**
* generación automática de boletines desde el texto

decime y lo llevamos al extremo Unix 😈



# Claude AI

Perfecto, ya analicé el manual de Kimkelen. Ahora voy a diseñarte un formato de texto **completo y robusto** que capture TODO lo que necesitás para una gestión escolar argentina completa.

## Formato Propuesto: TSV con Convenciones Estrictas

### Estructura del archivo `escuela_2025.txt`

```text
################################################################################
# SISTEMA DE GESTIÓN ESCOLAR 2025
# Institución: [NOMBRE]
# Generado: 2025-03-01
# Formato: TSV (campos separados por TAB)
# Encoding: UTF-8
################################################################################

## META_CICLO_LECTIVO
# año_lectivo	fecha_inicio	fecha_fin	estado	cantidad_trimestres
2025	2025-03-01	2025-12-20	VIGENTE	3

## CARRERAS
# id_carrera	nombre	nombre_plan	años_duracion	nota_minima_aprobacion	max_previas	regimen
CAR001	Secundaria	Plan 2020 Secundaria	6	7	2	TRIMESTRAL
CAR002	Primaria	Plan 2018 Primaria	7	7	0	TRIMESTRAL

## ESPECIALIDADES
# id_especialidad	nombre	id_carrera
ESP001	Ciencias Naturales	CAR001
ESP002	Ciencias Sociales	CAR001
ESP003	Economía y Administración	CAR001

## ORIENTACIONES
# id_orientacion	nombre	id_especialidad
ORI001	Biología	ESP001
ORI002	Química	ESP001

## MATERIAS_CATALOGO
# id_materia	nombre	nombre_fantasia	es_optativa_madre	es_opcion_de
MAT001	Matemática	Mate	NO	-
MAT002	Lengua y Literatura	Lengua	NO	-
MAT003	Idioma Extranjero	Idioma	SI	-
MAT004	Inglés	Inglés	NO	MAT003
MAT005	Francés	Francés	NO	MAT003
MAT006	Educación Física	Ed.Fís	NO	-
MAT007	Biología	Bio	NO	-

## PLAN_ESTUDIOS
# id_carrera	año_carrera	id_materia	todas_correlativas_año_anterior	orientacion	orden_boletin	tipo_asistencia	max_faltas
CAR001	1	MAT001	SI	-	1	DIA	-
CAR001	1	MAT002	SI	-	2	DIA	-
CAR001	1	MAT003	SI	-	3	DIA	-
CAR001	1	MAT006	SI	-	10	MATERIA	25
CAR001	2	MAT001	SI	-	1	DIA	-
CAR001	2	MAT007	SI	ESP001	5	DIA	-

## PERIODOS
# año_lectivo	numero_periodo	nombre	fecha_inicio	fecha_fin	tipo
2025	1	Primer Trimestre	2025-03-01	2025-05-30	TRIMESTRAL
2025	2	Segundo Trimestre	2025-06-01	2025-09-15	TRIMESTRAL
2025	3	Tercer Trimestre	2025-09-16	2025-12-15	TRIMESTRAL

## TURNOS
# id_turno	nombre	horario_inicio	horario_fin
TUR001	Mañana	07:30	12:30
TUR002	Tarde	13:00	18:00
TUR003	Vespertino	18:00	22:00

## AULAS
# id_aula	nombre	capacidad	edificio	piso
AUL001	1A	35	Principal	1
AUL002	1B	35	Principal	1
AUL003	Lab_Informatica	30	Anexo	2
AUL004	Gimnasio	60	Deportes	PB

## OBRAS_SOCIALES
# id_obra_social	nombre	codigo
OS001	OSDE	310-1
OS002	Swiss Medical	310-2
OS003	IOMA	310-3
OS004	Sin obra social	-

## TIPOS_TUTOR
# id_tipo_tutor	nombre	prioridad
TIP001	Madre	1
TIP002	Padre	2
TIP003	Abuelo/a	3
TIP004	Tío/a	4
TIP005	Hermano/a mayor	5
TIP006	Tutor legal	6

## CATEGORIA_OCUPACIONAL
# id_categoria	nombre
CATOCU001	Profesional
CATOCU002	Empleado público
CATOCU003	Empleado privado
CATOCU004	Comerciante
CATOCU005	Desocupado
CATOCU006	Jubilado

## ESTUDIOS_CURSADOS
# id_estudio	nombre	nivel
EST001	Primario completo	PRIMARIO
EST002	Primario incompleto	PRIMARIO
EST003	Secundario completo	SECUNDARIO
EST004	Secundario incompleto	SECUNDARIO
EST005	Terciario completo	TERCIARIO
EST006	Terciario incompleto	TERCIARIO
EST007	Universitario completo	UNIVERSITARIO
EST008	Universitario incompleto	UNIVERSITARIO
EST009	Posgrado	POSGRADO

## TIPOS_JUSTIFICACION
# id_tipo_just	nombre	con_goce_sueldo
JUST001	Enfermedad	SI
JUST002	Duelo	SI
JUST003	Trámite personal	NO
JUST004	Capacitación	SI
JUST005	Maternidad	SI
JUST006	Paternidad	SI

## TIPOS_AUSENCIA
# id_tipo_ausencia	nombre	valor_numerico
TAUS001	Ausente	1.0
TAUS002	Media falta	0.5
TAUS003	Un cuarto	0.25
TAUS004	Tres cuartos	0.75
TAUS005	Presente	0.0
TAUS006	Tardanza	0.5

## MOTIVOS_SANCION
# id_motivo	nombre	gravedad
MSAN001	Falta de respeto a docente	GRAVE
MSAN002	Agresión física	MUY_GRAVE
MSAN003	Fuga del establecimiento	GRAVE
MSAN004	Daño a propiedad escolar	MODERADA
MSAN005	Uso de celular en clase	LEVE
MSAN006	No traer materiales	LEVE
MSAN007	Bullying	MUY_GRAVE

## TIPOS_SANCION
# id_tipo_sancion	nombre	amonestaciones
TSAN001	Llamado de atención	0
TSAN002	Apercibimiento	1
TSAN003	Amonestación	3
TSAN004	Suspensión 1 día	5
TSAN005	Suspensión 3 días	10
TSAN006	Último apercibimiento	15

## DIAS_FERIADOS
# fecha	nombre	tipo
2025-03-24	Día de la Memoria	NACIONAL
2025-04-02	Día del Veterano	NACIONAL
2025-04-18	Viernes Santo	RELIGIOSO
2025-05-01	Día del Trabajador	NACIONAL
2025-05-25	Revolución de Mayo	NACIONAL
2025-06-20	Día de la Bandera	NACIONAL
2025-07-09	Día de la Independencia	NACIONAL
2025-08-17	Paso a la Inmortalidad del Gral San Martín	NACIONAL
2025-10-12	Día del Respeto a la Diversidad Cultural	NACIONAL
2025-11-24	Día de la Soberanía Nacional	NACIONAL
2025-12-08	Inmaculada Concepción	RELIGIOSO
2025-12-25	Navidad	RELIGIOSO

## PERSONAL_DOCENTE
# dni	apellido	nombre	fecha_nacimiento	sexo	telefono	email	domicilio	ciudad	provincia	fecha_ingreso	legajo	obra_social	username	estado
20123456	Silva	Roberto	1978-05-15	M	3764-123456	rsilva@mail.com	San Martín 456	Posadas	Misiones	2010-03-01	DOC001	OS001	rsilva	ACTIVO
25234567	Gomez	Patricia	1982-11-20	F	3764-234567	pgomez@mail.com	Córdoba 789	Posadas	Misiones	2012-08-15	DOC002	OS002	pgomez	ACTIVO
18456789	Rodriguez	Carmen	1975-03-10	F	3764-345678	crodriguez@mail.com	Bolivar 321	Posadas	Misiones	2008-02-20	DOC003	OS001	crodriguez	ACTIVO

## PERSONAL_NO_DOCENTE
# dni	apellido	nombre	tipo_cargo	fecha_nacimiento	telefono	email	fecha_ingreso	legajo	username	estado
30567890	Fernandez	Luis	PRECEPTOR	1985-07-22	3764-456789	lfernandez@mail.com	2015-03-01	PREC001	lfernandez	ACTIVO
28678901	Martinez	Ana	PRECEPTOR	1983-09-14	3764-567890	amartinez@mail.com	2013-04-10	PREC002	amartinez	ACTIVO
22789012	Gonzalez	Pedro	JEFE_PRECEPTORES	1980-01-05	3764-678901	pgonzalez@mail.com	2010-03-01	JPREC001	pgonzalez	ACTIVO
32890123	Lopez	Maria	OFICINA_ALUMNOS	1988-12-18	3764-789012	mlopez@mail.com	2018-02-15	OFAL001	mlopez	ACTIVO

## TUTORES
# dni	apellido	nombre	fecha_nacimiento	sexo	telefono	email	domicilio	ciudad	categoria_ocupacional	ocupacion	estudios_cursados	obra_social
33123456	Perez	Juan	1980-04-12	M	3764-111222	jperez@mail.com	Mitre 123	Posadas	CATOCU003	Empleado comercio	EST003	OS003
34234567	Diaz	Laura	1982-08-25	F	3764-222333	ldiaz@mail.com	Mitre 123	Posadas	CATOCU002	Docente primaria	EST007	OS001
35345678	Ruiz	Carlos	1975-11-30	M	3764-333444	cruiz@mail.com	Sarmiento 456	Posadas	CATOCU001	Contador	EST007	OS002
36456789	Torres	Marta	1978-02-14	F	3764-444555	mtorres@mail.com	Sarmiento 456	Posadas	CATOCU003	Secretaria	EST003	OS001

## ALUMNOS
# dni	apellido	nombre	fecha_nacimiento	sexo	lugar_nacimiento	telefono	email	domicilio	ciudad	provincia	obra_social	grupo_sanguineo	alergias	medicacion_cronica	certificado_discapacidad	observaciones_salud	estado	numero_legajo
45123456	Gonzalez	María	2010-03-15	F	Posadas	3764-555666	-	Mitre 123	Posadas	Misiones	OS003	A+	Ninguna	-	NO	-	ACTIVO	0001
45234567	Perez	Juan	2010-07-22	M	Posadas	3764-666777	-	Mitre 123	Posadas	Misiones	OS001	O+	Polen	-	NO	-	ACTIVO	0002
45345678	Lopez	Ana	2009-11-08	F	Garupá	3764-777888	-	Sarmiento 456	Posadas	Misiones	OS002	B+	Penicilina	-	NO	-	ACTIVO	0003
45456789	Martinez	Pedro	2010-05-19	M	Posadas	3764-888999	-	Belgrano 789	Posadas	Misiones	OS004	AB+	Ninguna	Asma - Salbutamol	NO	Requiere inhalador en actividad física	ACTIVO	0004

## ALUMNOS_TUTORES
# dni_alumno	dni_tutor	tipo_relacion	es_responsable_principal	vive_con_alumno	observaciones
45123456	33123456	TIP002	SI	SI	-
45123456	34234567	TIP001	NO	SI	-
45234567	33123456	TIP002	SI	SI	-
45234567	34234567	TIP001	NO	SI	-
45345678	35345678	TIP002	SI	SI	-
45345678	36456789	TIP001	NO	SI	-
45456789	35345678	TIP002	NO	NO	Vive con la madre, padre separado
45456789	36456789	TIP001	SI	SI	-

## INSCRIPCION_CARRERAS
# dni_alumno	id_carrera	id_especialidad	id_orientacion	año_inicio	fecha_inscripcion	estado
45123456	CAR001	-	-	1	2024-12-10	REGULAR
45234567	CAR001	-	-	1	2024-12-10	REGULAR
45345678	CAR001	-	-	2	2023-12-08	REGULAR
45456789	CAR001	-	-	1	2024-12-10	REGULAR

## MATRICULACION
# dni_alumno	año_lectivo	id_turno	fecha_matriculacion	estado
45123456	2025	TUR001	2025-02-15	MATRICULADO
45234567	2025	TUR001	2025-02-15	MATRICULADO
45345678	2025	TUR001	2025-02-15	MATRICULADO
45456789	2025	TUR002	2025-02-15	MATRICULADO

## DIVISIONES
# id_division	nombre	id_carrera	año_carrera	año_lectivo	id_turno	fecha_creacion
DIV001	A	CAR001	1	2025	TUR001	2025-02-20
DIV002	B	CAR001	1	2025	TUR001	2025-02-20
DIV003	A	CAR001	2	2025	TUR001	2025-02-20

## DIVISIONES_ALUMNOS
# id_division	dni_alumno	fecha_asignacion	estado
DIV001	45123456	2025-02-25	ACTIVO
DIV001	45234567	2025-02-25	ACTIVO
DIV002	45456789	2025-02-25	ACTIVO
DIV003	45345678	2025-02-25	ACTIVO

## DIVISIONES_PRECEPTORES
# id_division	dni_preceptor	fecha_asignacion	es_titular
DIV001	30567890	2025-02-20	SI
DIV002	28678901	2025-02-20	SI
DIV003	30567890	2025-02-20	SI

## CURSOS
# id_curso	id_division	id_materia	año_lectivo	fecha_inicio	fecha_fin	id_aula	estado
CUR001	DIV001	MAT001	2025	2025-03-01	2025-12-15	AUL001	ABIERTO
CUR002	DIV001	MAT002	2025	2025-03-01	2025-12-15	AUL001	ABIERTO
CUR003	DIV001	MAT003	2025	2025-03-01	2025-12-15	AUL001	ABIERTO
CUR004	DIV002	MAT001	2025	2025-03-01	2025-12-15	AUL002	ABIERTO
CUR005	DIV003	MAT001	2025	2025-03-01	2025-12-15	AUL001	ABIERTO

## CURSOS_DOCENTES
# id_curso	dni_docente	fecha_asignacion	es_titular
CUR001	20123456	2025-02-25	SI
CUR002	25234567	2025-02-25	SI
CUR003	20123456	2025-02-25	SI
CUR004	20123456	2025-02-25	SI
CUR005	20123456	2025-02-25	SI

## HORARIOS_CURSOS
# id_curso	dia_semana	hora_inicio	hora_fin	observaciones
CUR001	Lunes	07:30	09:00	-
CUR001	Miércoles	07:30	09:00	-
CUR001	Viernes	07:30	09:00	-
CUR002	Lunes	09:15	10:45	-
CUR002	Jueves	09:15	10:45	-

## COMISIONES
# id_comision	nombre	id_materia	id_carrera	año_carrera	año_lectivo	fecha_inicio	capacidad_maxima	estado
COM001	Ed.Física Varones 1°	MAT006	CAR001	1	2025	2025-03-01	40	ABIERTA
COM002	Ed.Física Mujeres 1°	MAT006	CAR001	1	2025	2025-03-01	40	ABIERTA

## COMISIONES_ALUMNOS
# id_comision	dni_alumno	fecha_asignacion	estado
COM001	45234567	2025-03-01	ACTIVO
COM001	45456789	2025-03-01	ACTIVO
COM002	45123456	2025-03-01	ACTIVO

## COMISIONES_DOCENTES
# id_comision	dni_docente	fecha_asignacion	es_titular
COM001	18456789	2025-03-01	SI
COM002	18456789	2025-03-01	SI

## COMISIONES_PRECEPTORES
# id_comision	dni_preceptor	fecha_asignacion
COM001	30567890	2025-03-01
COM002	28678901	2025-03-01

## HORARIOS_COMISIONES
# id_comision	dia_semana	hora_inicio	hora_fin	id_aula
COM001	Martes	07:30	09:00	AUL004
COM001	Viernes	10:00	11:30	AUL004
COM002	Martes	09:15	10:45	AUL004
COM002	Viernes	11:45	13:15	AUL004

## ASISTENCIA_ALUMNOS_DIA
# fecha	dni_alumno	id_tipo_ausencia	justificada	observaciones
2025-03-15	45123456	TAUS005	-	-
2025-03-15	45234567	TAUS001	NO	-
2025-03-15	45345678	TAUS006	NO	Llegó 8:15
2025-03-15	45456789	TAUS005	-	-
2025-03-16	45234567	TAUS001	SI	Certificado médico presentado
2025-03-17	45345678	TAUS002	NO	Salió 10:00 por trámite familiar

## ASISTENCIA_ALUMNOS_MATERIA
# fecha	dni_alumno	id_curso	id_tipo_ausencia	justificada	observaciones
2025-03-15	45234567	COM001	TAUS001	NO	-
2025-03-16	45456789	COM001	TAUS002	NO	Lesión tobillo

## JUSTIFICACIONES_FALTAS_ALUMNOS
# id_justificacion	dni_alumno	fecha_desde	fecha_hasta	id_tipo_just	tipo_asistencia	observaciones	archivo_adjunto	fecha_presentacion
JUST_ALU001	45234567	2025-03-16	2025-03-17	JUST001	DIA	Gripe - Reposo 48hs	certificado_20250316_perez.pdf	2025-03-18

## CALIFICACIONES
# id_curso	dni_alumno	numero_periodo	nota	fecha_carga	observaciones	cerrado
CUR001	45123456	1	8	2025-05-29	-	SI
CUR001	45234567	1	6	2025-05-29	Muchas faltas	SI
CUR002	45123456	1	9	2025-05-29	Excelente	SI
CUR002	45234567	1	7	2025-05-29	-	SI
CUR001	45123456	2	7	2025-09-14	-	SI
CUR001	45234567	2	5	2025-09-14	Bajo rendimiento	SI

## CALIFICACIONES_COMISIONES
# id_comision	dni_alumno	numero_periodo	nota	fecha_carga	observaciones	cerrado
COM002	45123456	1	10	2025-05-29	Muy buena participación	SI
COM001	45234567	1	8	2025-05-29	-	SI

## EXENCIONES
# dni_alumno	id_curso	fecha_exencion	motivo	responsable	observaciones
45456789	CUR003	2025-03-10	Alumno federado	pgonzalez	Federado natación - Entrena con selección provincial

## ALUMNOS_LIBRES
# dni_alumno	id_curso	fecha	motivo	numero_periodo	estado
45234567	CUR001	2025-09-20	FALTAS_EXCEDIDAS	2	LIBRE

## REINCORPORACIONES
# dni_alumno	id_curso	fecha_libre	fecha_reincorporacion	numero_periodo	dias_gracia	observaciones	autorizado_por
45234567	CUR001	2025-09-20	2025-09-25	2	10	Problemas familiares - Tutoría compensatoria	pgonzalez

## SANCIONES
# id_sancion	dni_alumno	numero	fecha	id_motivo	id_tipo_sancion	amonestaciones	dni_solicitante	dni_responsable	observaciones	documento
SAN001	45234567	001	2025-04-10	MSAN005	TSAN002	1	20123456	30567890	Uso de celular en clase de matemática	-
SAN002	45234567	002	2025-05-15	MSAN001	TSAN003	3	25234567	30567890	Falta de respeto a profesora de lengua	acta_20250515.pdf
SAN003	45345678	001	2025-06-20	MSAN004	TSAN002	1	18456789	30567890	Rayó banco en aula	-

## CONDUCTA_ALUMNOS
# dni_alumno	id_division	numero_periodo	calificacion	observaciones
45123456	DIV001	1	MB	Excelente comportamiento
45234567	DIV001	1	R	Problemas de conducta recurrentes
45345678	DIV003	1	B	-
45456789	DIV002	1	MB	-

## MESAS_EXAMEN
# id_mesa	nombre	tipo	instancia	año_lectivo	fecha_desde	fecha_hasta	estado
MESA001	Diciembre 2025	SISTEMA	1	2025	2025-12-01	2025-12-15	ABIERTA
MESA002	Febrero 2026	SISTEMA	2	2025	2026-02-01	2026-02-15	CERRADA

## MESAS_EXAMEN_MATERIAS
# id_mesa	id_materia	id_carrera	año_carrera	id_aula	fecha_examen	hora_inicio
MESA001	MAT001	CAR001	1	AUL001	2025-12-05	08:00
MESA001	MAT002	CAR001	1	AUL002	2025-12-06	08:00

## MESAS_EXAMEN_DOCENTES
# id_mesa	id_materia	id_carrera	año_carrera	dni_docente	rol
MESA001	MAT001	CAR001	1	20123456	TITULAR
MESA001	MAT001	CAR001	1	25234567	VOCAL
MESA001	MAT002	CAR001	1	25234567	TITULAR

## MESAS_EXAMEN_ALUMNOS
# id_mesa	id_materia	id_carrera	año_carrera	dni_alumno	nota	ausente	fecha_carga	resultado
MESA001	MAT001	CAR001	1	45234567	8	NO	2025-12-05	APROBADO
MESA002	MAT001	CAR001	1	45234567	4	NO	2026-02-05	DESAPROBADO

## MESAS_PREVIAS
# id_mesa_previa	nombre	año_lectivo_vigente	fecha_desde	fecha_hasta	estado
PREV001	Previas Marzo 2026	2026	2026-03-01	2026-03-15	CERRADA
PREV002	Previas Julio 2026	2026	2026-07-01	2026-07-15	ABIERTA

## MESAS_PREVIAS_MATERIAS
# id_mesa_previa	id_materia	id_carrera	año_carrera	fecha_examen	id_aula	hora_inicio
PREV002	MAT001	CAR001	1	2026-07-08	AUL001	08:00

## MESAS_PREVIAS_ALUMNOS
# id_mesa_previa	id_materia	id_carrera	año_carrera	dni_alumno	nota	ausente	fecha_carga	resultado
PREV001	MAT001	CAR001	1	45234567	7	NO	2026-03-08	APROBADO

## MESAS_LIBRES
# id_mesa_libre	nombre	año_lectivo_vigente	fecha_desde	fecha_hasta	estado
LIB001	Libres Diciembre 2025	2025	2025-12-16	2025-12-20	CERRADA

## LICENCIAS_PERSONAL
# dni	tipo_personal	id_tipo_justificacion	fecha_desde	fecha_hasta	observaciones	documento
20123456	DOCENTE	JUST001	2025-03-10	2025-03-12	Gripe	certificado_silva.pdf
25234567	DOCENTE	JUST005	2025-04-01	2025-06-15	Maternidad	certificado_maternidad.pdf
30567890	NO_DOCENTE	JUST003	2025-05-20	2025-05-20	Trámite DNI	-

## ASISTENCIA_PERSONAL
# fecha	dni	tipo_personal	presente	id_tipo_ausencia	justificada	observaciones
2025-03-15	20123456	DOCENTE	SI	TAUS005	-	-
2025-03-15	25234567	DOCENTE	SI	TAUS005	-	-
2025-03-15	30567890	NO_DOCENTE	SI	TAUS005	-	-
2025-03-16	20123456	DOCENTE	NO	TAUS001	SI	En licencia por enfermedad
2025-05-20	30567890	NO_DOCENTE	NO	TAUS001	SI	Trámite autorizado

## EVENTOS_INSTITUCIONALES
# fecha	tipo	descripcion	responsable_dni	observaciones
2025-03-25	REUNION_PADRES	Reunión inicio ciclo lectivo 1° A y B	30567890	Asistencia obligatoria padres 1° año
2025-05-10	ACTO	Acto Día de la Revolución de Mayo	22789012	Acto 9:00hs en patio central
2025-06-15	JORNADA_CAPACITACION	Jornada ESI para docentes	22789012	Suspensión de clases - Capacitación obligatoria
2025-09-11	FERIA_CIENCIAS	Feria de Ciencias 2025	20123456	Participan todos los años

## OBSERVACIONES_PSICOPEDAGOGICAS
# id_observacion	dni_alumno	fecha	tipo	categoria	profesional_dni	observacion	seguimiento_requerido	privacidad
OBS001	45234567	2025-03-20	CONDUCTUAL	ATENCION	-	Se distrae fácilmente - Requiere seguimiento - Posible TDAH	SI	CONFIDENCIAL
OBS002	45123456	2025-04-10	ACADEMICA	RENDIMIENTO	-	Excelente desempeño - Propuesta para tutorías de apoyo a pares	NO	NORMAL
OBS003	45456789	2025-04-15	SALUD	CRONICA	-	Seguimiento asma - Coordinar con familia uso de inhalador en Ed.Física	SI	CONFIDENCIAL

## HISTORIAL_CAMBIOS_DIVISION
# dni_alumno	id_division_origen	id_division_destino	fecha_cambio	motivo	autorizado_por
45234567	DIV001	DIV002	2025-04-20	Problemas de integración grupal	pgonzalez

## MOVIMIENTOS_ALUMNOS
# dni_alumno	tipo_movimiento	fecha	id_carrera	año_carrera	estado_origen	estado_destino	observaciones
45345678	PASE_INTERNO	2024-12-10	CAR001	2	REGULAR	REGULAR	Pase de primaria a secundaria
45234567	CAMBIO_TURNO	2025-04-25	CAR001	1	MATRICULADO	MATRICULADO	Pase de turno tarde a mañana por disponibilidad familiar

## EQUIVALENCIAS
# dni_alumno	id_materia	año_lectivo_origen	institucion_origen	nota_original	fecha_reconocimiento	resolucion
45345678	MAT001	2024	Escuela N° 123 - CABA	9	2025-02-15	RES-2025-001

## NOTAS_FINALES_ANUALES
# dni_alumno	id_materia	año_lectivo	promedio_final	resultado	metodo_aprobacion	fecha_cierre
45123456	MAT001	2025	7.5	APROBADO	PROMOCION	2025-12-20
45234567	MAT001	2025	5.5	APROBADO	EXAMEN_FEBRERO	2026-02-05
45234567	MAT002	2025	6.8	APROBADO	EXAMEN_DICIEMBRE	2025-12-05

## HISTORIAL_ACADEMICO_COMPLETO
# dni_alumno	año_lectivo	id_carrera	año_carrera	promedio_general	materias_aprobadas	materias_previas	resultado_año	observaciones
45123456	2024	CAR002
45123456	2025	CAR001	1	8.1	6	0	EN_CURSO	-
45234567	2025	CAR001	1	6.3	4	1	EN_CURSO	Previa: Matemática

## ETIQUETAS
# id_etiqueta	nombre	tipo	descripcion
ETI001	Guitarra	INSTRUMENTO	Alumno estudia guitarra
ETI002	Piano	INSTRUMENTO	Alumno estudia piano
ETI003	Natacion_Federado	DEPORTE	Alumno federado natación
ETI004	Apoyo_Psicopedagogico	ACADEMICO	Requiere seguimiento psicopedagógico

## ALUMNOS_ETIQUETAS
# dni_alumno	id_etiqueta	fecha_asignacion	vigente
45123456	ETI001	2025-03-01	SI
45456789	ETI003	2025-03-01	SI
45234567	ETI004	2025-04-10	SI

## CORRELATIVIDADES_ESPECIFICAS
# id_materia	id_materia_correlativa	tipo	año_lectivo
MAT007	MAT001	REGULAR	2025
MAT007	MAT002	APROBADA	2025

## USUARIOS_SISTEMA
# username	tipo_usuario	dni	email	ultimo_acceso	estado	permisos
rsilva	DOCENTE	20123456	rsilva@mail.com	2025-03-15 14:30:00	ACTIVO	CALIFICAR,VER_CURSOS
pgonzalez	JEFE_PRECEPTORES	22789012	pgonzalez@mail.com	2025-03-15 16:45:00	ACTIVO	ADMIN_COMPLETO
lfernandez	PRECEPTOR	30567890	lfernandez@mail.com	2025-03-15 08:15:00	ACTIVO	ASISTENCIA,SANCIONES,VER_DIVISIONES
admin	ADMINISTRADOR	-	admin@escuela.edu.ar	2025-03-15 18:00:00	ACTIVO	TODOS
```

---

## Convenciones y Reglas:

### 1. **Formato General**
- Separador: **TAB** (`\t`)
- Codificación: **UTF-8**
- Primera línea de cada sección: nombres de campos (precedidos por `#`)
- Secciones separadas por línea en blanco
- Comentarios con `#` al inicio de línea

### 2. **IDs y Códigos**
- IDs alfanuméricos descriptivos (ej: `CAR001`, `DIV001`, `CUR001`)
- DNI sin puntos ni guiones (8 dígitos)
- Fechas: formato `YYYY-MM-DD`
- Horas: formato `HH:MM` (24hs)
- Timestamps: `YYYY-MM-DD HH:MM:SS`

### 3. **Valores especiales**
- Dato no aplicable: `-`
- Dato desconocido/vacío: campo vacío
- Booleanos: `SI`/`NO`
- Estados: MAYÚSCULAS con guiones bajos

### 4. **Claves foráneas**
- Siempre usar el ID/DNI exacto
- Mantener consistencia referencial

---

¿Querés que te muestre ahora **scripts de bash** para consultar y generar reportes desde este formato? Por ejemplo:
- Boletín de un alumno
- Listado de asistencias por división
- Reporte de sanciones
- Historial académico completo
- Estadísticas de aprobación
- etc.


---

# Grok

Aquí te dejo el contenido completo y bien formateado del archivo de texto que propuse como sistema de gestión escolar alternativo (basado en un solo archivo TSV plano, fácil de buscar con `grep`, `awk`, etc.). 

**Nombre sugerido para el archivo:** `gestion_escolar_2025.tsv`

Puedes copiar todo el texto de abajo (desde la primera línea hasta la última) y pegarlo en un editor de texto plano (como Notepad++, VS Code, Vim, etc.). Guárdalo con extensión `.tsv` o `.txt`. El separador es TAB (no comas ni espacios), por lo que al abrirlo en Excel o LibreOffice Calc se verá perfectamente en columnas.

```
################################################################################
# SISTEMA DE GESTIÓN ESCOLAR 2025
# Institución: [NOMBRE_DE_LA_INSTITUCION]
# Generado: 2025-12-31
# Formato: TSV (campos separados por TAB)
# Encoding: UTF-8
# Versión: 2.0 (Completa y optimizada para búsquedas con grep/awk)
# Notas: 
# - Campos obligatorios marcados con * en el header de comentarios.
# - Campos opcionales pueden estar vacíos (-) o en blanco.
# - IDs únicos con prefijo (ej: CAR para carreras).
# - Fechas: YYYY-MM-DD | Horas: HH:MM
# - Multi-valor: separador interno |
# - Búsquedas rápidas: grep '^## SECCION' archivo.tsv
################################################################################
## META_INSTITUCION
# nombre_institucion	direccion	ciudad	provincia	pais	codigo_postal	telefono	email	director_nombre	fecha_fundacion
Escuela Ejemplo	Calle Falsa 123	Posadas	Misiones	Argentina	3300	3764-000000	info@escuela.edu.ar	Director Ejemplo	1990-01-01

## META_CICLO_LECTIVO
# año_lectivo*	fecha_inicio*	fecha_fin*	estado*	cantidad_periodos*	regimen*
2025	2025-03-01	2025-12-20	VIGENTE	3	TRIMESTRAL

## CARRERAS
# id_carrera*	nombre*	nombre_plan*	años_duracion*	nota_minima_aprobacion*	max_previas*	regimen*	siguiente_num_alumno
CAR001	Secundaria	Plan 2020 Secundaria	6	7	2	TRIMESTRAL	1000
CAR002	Primaria	Plan 2018 Primaria	7	7	0	TRIMESTRAL	2000

## ESPECIALIDADES
# id_especialidad*	nombre*	id_carrera*
ESP001	Ciencias Naturales	CAR001
ESP002	Ciencias Sociales	CAR001
ESP003	Economía y Administración	CAR001

## ORIENTACIONES
# id_orientacion*	nombre*	id_especialidad*
ORI001	Biología	ESP001
ORI002	Química	ESP001

## MATERIAS_CATALOGO
# id_materia*	nombre*	nombre_fantasia*	es_optativa_madre*	es_opcion_de	carga_horaria_semanal
MAT001	Matemática	Mate	NO	-	4
MAT002	Lengua y Literatura	Lengua	NO	-	5
MAT003	Idioma Extranjero	Idioma	SI	-	3
MAT004	Inglés	Inglés	NO	MAT003	3
MAT005	Francés	Francés	NO	MAT003	3
MAT006	Educación Física	Ed.Fís	NO	-	2
MAT007	Biología	Bio	NO	-	3

## PLAN_ESTUDIOS
# id_carrera*	año_carrera*	id_materia*	todas_correlativas_año_anterior*	orientacion	orden_boletin	tipo_asistencia*	max_faltas
CAR001	1	MAT001	SI	-	1	DIA	-
CAR001	1	MAT002	SI	-	2	DIA	-
CAR001	1	MAT003	SI	-	3	DIA	-
CAR001	1	MAT006	SI	-	10	MATERIA	25
CAR001	2	MAT001	SI	-	1	DIA	-
CAR001	2	MAT007	SI	ORI001	5	DIA	-

## PERIODOS
# año_lectivo*	numero_periodo*	nombre*	fecha_inicio*	fecha_fin*	tipo*
2025	1	Primer Trimestre	2025-03-01	2025-05-30	TRIMESTRAL
2025	2	Segundo Trimestre	2025-06-01	2025-09-15	TRIMESTRAL
2025	3	Tercer Trimestre	2025-09-16	2025-12-15	TRIMESTRAL

## TURNOS
# id_turno*	nombre*	horario_inicio*	horario_fin*
TUR001	Mañana	07:30	12:30
TUR002	Tarde	13:00	18:00
TUR003	Vespertino	18:00	22:00

## AULAS
# id_aula*	nombre*	capacidad*	edificio	piso	equipamiento
AUL001	1A	35	Principal	1	Proyector|Pizarra
AUL002	1B	35	Principal	1	Pizarra
AUL003	Lab_Informatica	30	Anexo	2	Computadoras|Internet
AUL004	Gimnasio	60	Deportes	PB	Equipamiento deportivo

## OBRAS_SOCIALES
# id_obra_social*	nombre*	codigo
OS001	OSDE	310-1
OS002	Swiss Medical	310-2
OS003	IOMA	310-3
OS004	Sin obra social	-

## TIPOS_TUTOR
# id_tipo_tutor*	nombre*	prioridad*
TIP001	Madre	1
TIP002	Padre	2
TIP003	Abuelo/a	3
TIP004	Tío/a	4
TIP005	Hermano/a mayor	5
TIP006	Tutor legal	6

## CATEGORIAS_OCUPACIONALES
# id_categoria*	nombre*
CAT001	Profesional
CAT002	Empleado público
CAT003	Empleado privado
CAT004	Comerciante
CAT005	Desocupado
CAT006	Jubilado

## OCUPACIONES
# id_ocupacion*	nombre*	id_categoria*
OCU001	Docente	CAT001
OCU002	Contador	CAT001
OCU003	Secretaria	CAT003

## ESTUDIOS_CURSADOS
# id_estudio*	nombre*	nivel*
EST001	Primario completo	PRIMARIO
EST002	Primario incompleto	PRIMARIO
EST003	Secundario completo	SECUNDARIO
EST004	Secundario incompleto	SECUNDARIO
EST005	Terciario completo	TERCIARIO
EST006	Terciario incompleto	TERCIARIO
EST007	Universitario completo	UNIVERSITARIO
EST008	Universitario incompleto	UNIVERSITARIO
EST009	Posgrado	POSGRADO

## TIPOS_JUSTIFICACION
# id_tipo_just*	nombre*	con_goce_sueldo*	aplica_a
JUST001	Enfermedad	SI	TODOS
JUST002	Duelo	SI	TODOS
JUST003	Trámite personal	NO	PERSONAL
JUST004	Capacitación	SI	PERSONAL
JUST005	Maternidad	SI	PERSONAL
JUST006	Paternidad	SI	PERSONAL

## TIPOS_AUSENCIA
# id_tipo_ausencia*	nombre*	valor_numerico*	aplica_a
TAUS001	Ausente	1.0	TODOS
TAUS002	Media falta	0.5	ALUMNOS
TAUS003	Un cuarto	0.25	ALUMNOS
TAUS004	Tres cuartos	0.75	ALUMNOS
TAUS005	Presente	0.0	TODOS
TAUS006	Tardanza	0.5	ALUMNOS

## MOTIVOS_SANCION
# id_motivo*	nombre*	gravedad*
MSAN001	Falta de respeto a docente	GRAVE
MSAN002	Agresión física	MUY_GRAVE
MSAN003	Fuga del establecimiento	GRAVE
MSAN004	Daño a propiedad escolar	MODERADA
MSAN005	Uso de celular en clase	LEVE

## TIPOS_SANCION
# id_tipo_sancion*	nombre*	amonestaciones*
TSAN001	Llamado de atención	0
TSAN002	Apercibimiento	1
TSAN003	Amonestación	3
TSAN004	Suspensión 1 día	5
TSAN005	Suspensión 3 días	10

## DIAS_FERIADOS
# fecha*	nombre*	tipo*
2025-03-24	Día de la Memoria	NACIONAL
2025-04-02	Día del Veterano	NACIONAL
2025-04-18	Viernes Santo	RELIGIOSO
2025-05-01	Día del Trabajador	NACIONAL
2025-05-25	Revolución de Mayo	NACIONAL
2025-06-20	Día de la Bandera	NACIONAL
2025-07-09	Día de la Independencia	NACIONAL
2025-08-17	Paso a la Inmortalidad del Gral San Martín	NACIONAL
2025-10-12	Día del Respeto a la Diversidad Cultural	NACIONAL
2025-12-25	Navidad	RELIGIOSO

## PERSONAL_DOCENTE
# dni*	apellido*	nombre*	fecha_nacimiento	sexo	telefono	email	domicilio	ciudad	provincia	fecha_ingreso	legajo	obra_social	username	estado*
20123456	Silva	Roberto	1978-05-15	M	3764-123456	rsilva@mail.com	San Martín 456	Posadas	Misiones	2010-03-01	DOC001	OS001	rsilva	ACTIVO

## PERSONAL_NO_DOCENTE
# dni*	apellido*	nombre*	tipo_cargo*	fecha_nacimiento	telefono	email	fecha_ingreso	legajo	username	estado*
30567890	Fernandez	Luis	PRECEPTOR	1985-07-22	3764-456789	lfernandez@mail.com	2015-03-01	PREC001	lfernandez	ACTIVO

## TUTORES
# dni*	apellido*	nombre*	fecha_nacimiento	sexo	telefono	email	domicilio	ciudad	categoria_ocupacional	id_ocupacion	estudios_cursados	obra_social
33123456	Perez	Juan	1980-04-12	M	3764-111222	jperez@mail.com	Mitre 123	Posadas	CAT003	OCU003	EST003	OS003

## ALUMNOS
# dni*	apellido*	nombre*	fecha_nacimiento*	sexo*	lugar_nacimiento	telefono	email	domicilio	ciudad	provincia	obra_social	grupo_sanguineo	alergias	medicacion_cronica	certificado_discapacidad	observaciones_salud	estado*	numero_legajo
45123456	Gonzalez	María	2010-03-15	F	Posadas	3764-555666	-	Mitre 123	Posadas	Misiones	OS003	A+	Ninguna	-	NO	-	ACTIVO	0001

## ALUMNOS_TUTORES
# dni_alumno*	dni_tutor*	id_tipo_tutor*	es_responsable_principal*	vive_con_alumno*	observaciones
45123456	33123456	TIP002	SI	SI	-

## DIVISIONES
# id_division*	nombre*	id_carrera*	año_carrera*	año_lectivo*	id_turno*	fecha_creacion*
DIV001	1A	CAR001	1	2025	TUR001	2025-02-20

## DIVISIONES_ALUMNOS
# id_division*	dni_alumno*	fecha_asignacion*	estado*
DIV001	45123456	2025-02-25	ACTIVO

## ASISTENCIA_ALUMNOS_DIA
# fecha*	dni_alumno*	id_tipo_ausencia*	justificada*	observaciones	id_division
2025-03-15	45123456	TAUS005	-	-	DIV001

## CALIFICACIONES_CURSOS
# id_curso*	dni_alumno*	numero_periodo*	nota	fecha_carga	observaciones	cerrado*
CUR001	45123456	1	8	2025-05-29	-	SI

## SANCIONES
# id_sancion*	dni_alumno*	numero*	fecha*	id_motivo*	id_tipo_sancion*	amonestaciones	dni_solicitante	dni_responsable	observaciones
SAN001	45123456	001	2025-04-10	MSAN005	TSAN002	1	20123456	30567890	Uso de celular	-

## OBSERVACIONES_PSICOPEDAGOGICAS
# id_observacion*	dni_alumno*	fecha*	tipo*	categoria*	profesional_dni	observacion	seguimiento_requerido*	privacidad*
OBS001	45123456	2025-03-20	CONDUCTUAL	ATENCION	tu_dni	Ajuste de conducta leve	NO	NORMAL

## LOG_CAMBIOS
# fecha*	usuario*	accion*	seccion*	id_entidad	descripcion
2025-12-31	admin	CREAR	ALUMNOS	45123456	Nuevo alumno ingresado
```

(Este es un ejemplo completo pero con datos mínimos para que quepa aquí. Puedes ampliar cada sección con todos los registros reales de tu escuela siguiendo exactamente el mismo formato: una línea por registro, campos separados por TAB).

**Consejos para usarlo:**
- Para buscar un alumno: `grep 45123456 gestion_escolar_2025.tsv`
- Para ver todas las asistencias de marzo: `grep '^2025-03' gestion_escolar_2025.tsv | grep ASISTENCIA`
- Para extraer solo notas: `awk -F'\t' '/^## CALIFICACIONES_CURSOS/{p=1;next} p&&/^##/{p=0} p' gestion_escolar_2025.tsv`

Si necesitas que agregue más secciones o ejemplos reales con más datos, avisame. ¡Listo para descargar y usar!
