---
title: "Arduboy"
tags: ['games']
---

Estaria bueno crear un negocio como Duolingo en donde supuestamente aprendes idiomas pero en realidad es solo una empresa de publicidad, un idioma no se aprende asi.

https://markus.hofer.rocks/diy-arduboy


![](https://www.notion.so/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F474223a1-be8f-4bfa-8faf-9a5c71758855%2F467e1ae2-e970-46a9-8f7b-e53a1cbff202%2FScreenshot_2024-02-27_at_5.03.42_PM.png)

https://blackish.at/files/ArduboySketch.fzz


Perfecto — te preparo una guía práctica, paso a paso, para convertir el DIY Arduboy (o un dispositivo inspirado en él) en un **producto final vendible**. La guía cubre desde la investigación y el diseño hasta la fabricación, certificaciones, costes aproximados y lanzamiento. Voy directo a la acción y te doy plantillas y números reales para que los uses ya.

# 1) Nota legal y ética (imprescindible)

* **No copies marcas registradas ni uses el nombre “Arduboy” en tu producto si no tienes permiso.** Puedes inspirarte, reutilizar ideas y hardware abierto, pero crea una **marca propia** y comprueba las licencias de cualquier firmware/hardware que uses.
* Revisa licencias: si usas código/hardware open-source, respeta la licencia (p. ej. MIT, GPL — cada una tiene obligaciones distintas).
* Evita infracción: modifica el diseño estético y el nombre; documenta las fuentes open-source que uses.

# 2) Visión de producto — decide lo mínimo imprescindible (MVP)

Define el producto mínimo vendible:

* Pantalla 128×64 (OLED o LCD) con SPI
* Microcontrolador con USB HID (para cargar juegos y actuar como control)
* Batería LiPo recargable + circuito de carga (micro USB / USB-C)
* 5 botones frontales + pad direccional o D-pad
* Altavoz piezo o pequeño buzzer
* Carcasa portátil estilo tarjeta (diseño atractivo y ergonómico)
* Firmware que ejecute juegos (compatibilidad con bibliotecas Arduino o motor propio)

# 3) Investigación de mercado rápida (hazlo ya)

* Busca competidores: quién vende dispositivos retro portátiles, precios, canales (Etsy, Kickstarter, Amazon).
* Público objetivo: nostálgicos, makers, estudiantes, coleccionistas.
* Canales de venta ideales: Kickstarter para validación + tienda web propia + tiendas de electrónica/retrogaming.

# 4) Diseño y prototipado (acciones concretas)

A. **Especificaciones técnicas**

* MCU: ATmega32U4 o ARM Cortex M0 con USB (elige según costo y ecosistema de desarrollo).
* Pantalla: OLED 128×64 (SSD1306 o compatible) — SPI.
* Batería: LiPo 3.7 V 300–500 mAh.
* Carga: circuito TP4056 (si usas microUSB) o controlador USB-C con protección si optas USB-C.
* Botones: micro switches SMD o tact switches.
* Conector/USB: micro USB o USB-C.
* PCB: 2 capas inicialmente.

B. **Prototipo rápido**

1. Haz un prototipo en placa de pruebas / perfboard con los módulos (OLED, MCU devboard, LiPo).
2. Sube firmware de ejemplo (ej. ejemplo “hello world” para pantalla + lectura botones).
3. Valida ergonomía con carcasa impresa en 3D.

C. **PCB y diseño industrial**

* Diseña PCB en KiCad / Eagle.
* Crea varios prototipos de carcasa en 3D (Fusion/FreeCAD + impresión 3D).
* Itera: usa pruebas reales para ajustar botones y posición de pantalla.

# 5) Firmware y ecosistema

* Base: usa Arduino/PlatformIO para acelerar desarrollo.
* Usa bibliotecas existentes para pantalla (SSD1306), entrada y audio.
* Diseña un cargador/instalador de juegos fácil (USB drag-and-drop o cargador por app).
* Documenta API para desarrolladores (si quieres comunidad).

# 6) Producción — aprovisionamiento y opciones

* **Pequeña tirada**: pide PCBs y ensamblaje manual o con THT+SMD small-batch en un taller local.
* **Mediano/grande**: fabrica PCBs con ensamblado (SMT) y con moldes para inyección de plástico (carcasas).
* Cotiza: PCBs (2 capas), ensamblaje P&P, inyección de moldes (costo alto inicial; amortizable a volumen).

# 7) Control de calidad y pruebas

* Pruebas funcionales: encendido, carga batería, conectividad USB, lectura botones, audio, estabilidad juegos.
* Pruebas físicas: durabilidad, botones, montaje.
* Programa de pruebas en línea de producción: 100% unit test de arranque + muestreo para EMC.

# 8) Regulaciones y certificaciones importantes

* **RoHS** (si vendes en EU): restringe sustancias.
* **CE (EMC + Directiva de baja tensión)** para Europa.
* **FCC (EMI)** para EE. UU. (si tiene radio o altas emisiones).
* **UN38.3**: para transporte de baterías LiPo (envío internacional).
* Considera ensayos de seguridad y EMC — cuestan dinero (varios miles USD según laboratorio).

# 9) Costes aproximados (BOM y ejemplo de margen)

Abajo tienes un **BOM orientativo** y el cálculo por unidad y para una tirada de 500 unidades. Son **ejemplos conservadores** para que tengas números con los que trabajar.

**Lista de componentes (coste unitario estimado)**

* MCU: $3.00
* Pantalla OLED: $6.00
* PCB (fabricación): $2.00
* Batería LiPo: $2.50
* Conector USB: $0.20
* Botones (5): $1.50   (5 × $0.30)
* Altavoz/piezo: $0.50
* Pasivos y pequeños componentes: $0.50
* Carcasa (inyección amortizada / 3D batch): $2.00
* Ensamblaje (P&P + mano de obra): $2.50
* Test y carga firmware: $0.50
* Packaging: $0.75
* Envío (por unidad en lote): $0.80

**Cálculo (suma por unidad):**
3.00 + 6.00 + 2.00 + 2.50 + 0.20 + 1.50 + 0.50 + 0.50 + 2.00 + 2.50 + 0.50 + 0.75 + 0.80 = **$22.75 por unidad**

(he sumado componente a componente para evitar errores aritméticos — total: **$22.75**)

**Costo total para 500 unidades:**
$22.75 × 500 = **$11,375.00**

**Precio de venta sugerido (MSRP) y márgenes**

* Precio sugerido 1: $59 → margen bruto = (59 − 22.75) / 59 = **61.44%**
* Precio sugerido 2: $79 → margen bruto = (79 − 22.75) / 79 = **71.20%**

Estos márgenes permiten cubrir marketing, soporte, devoluciones, impuestos y beneficios.

# 10) Producción y logística — pasos concretos

1. **Prototipado y validación** (prototipo funcional, 3 o 4 iteraciones).
2. **Preproducción (run piloto)**: 30–100 unidades para test de mercado y QA.
3. **Fabricación a escala**: decide entre fabricante local o China/Taiwán (costes y tiempos).
4. **Envío y almacenamiento**: almacén local o fulfillment (ej. ShipBob, fulfillment propio).
5. **Soporte post-venta**: guía de usuario, firmware OTA o modo fácil de actualización, políticas de RMA.

# 11) Marketing y lanzamiento

* Historia del producto: enfócate en nostalgia + DIY + retro games.
* Lanzamiento recomendado: **Kickstarter** o campaña previa (pre-orders) para financiar la primera tirada y validar demanda.
* Contenido: videos cortos demostrativos, demos jugables, comparativas con competidores.
* Comunidades: foros retro, Reddit r/retrogaming, subreddits maker, Discord.

# 12) Atención al detalle técnico que suele fallar

* Protecciones para la batería (circuito de protección y protección contra sobrecarga).
* Administración de energía: optimiza consumo (sleep modes) para buena autonomía.
* Diseño de antena/emisión si incluirás radio (evitar problemas EMC).
* Documentación de firmware y control de versiones.

# 13) Plantilla rápida para la primera página del pitch / Kickstarter

Título: [Nombre de tu marca] — mini consola retro, open-source, portátil
Elevator: Pequeña, recargable y programable: la consola que cabe en tu bolsillo para jugar o programar tus propios juegos.
Incluye: 128×64 OLED, batería recargable, entrada USB para cargar y subir juegos, SDK fácil para crear juegos.

# 14) Checklist resumido (lista de control mínima)

* [ ] Marca registrada y nombre propio (no “Arduboy”)
* [ ] Validar licencias del software que vayas a usar
* [ ] Prototipo funcional con todos los componentes
* [ ] PCB revisada y revisiones DFM (design for manufacturing)
* [ ] Moldes / carcasas y prueba de ergonomía
* [ ] Cotizaciones para 100 / 500 / 2000 unidades
* [ ] Pruebas eléctricas y funcionales automatizadas
* [ ] Plan de certificaciones (CE/FCC/UN38.3/ROHS)
* [ ] Estrategia de ventas y atención al cliente

# 15) Siguientes pasos prácticos que puedes empezar hoy (elige cualquiera y te lo desarrollo)

* A) Te preparo un **BOM detallado en formato CSV** con enlaces de componentes y alternativas.
* B) Te diseño un **roadmap** (hit list de tareas) para lanzar un prototipo funcional (qué hacer paso a paso).
* C) Te escribo un **guion de vídeo demo** + texto para una campaña de Kickstarter.
* D) Te doy **plantilla de firmware** (esqueleto Arduino/PlatformIO) para pantalla + botones + USB.

Dime cuál de estas opciones (A–D) quieres que haga ahora y lo preparo ya (entregaré el contenido completo en este mismo mensaje). Si quieres otra cosa práctica, hazlo saber y la hago de inmediato.

