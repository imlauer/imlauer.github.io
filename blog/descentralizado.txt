---
title: "Descentralizado: Redes P2P (Ares o eMule)"
date: 2025-10-13T02:31:00-03:00
---

Hoy en dia yo uso Jackett con qbittorrent, que tambien se puede utilizar con btstrm para ver y descargarlo al mismo tiempo (streamear).

### 🕹️ 1. Qué eran las redes P2P (como eMule o Ares)

Las **redes P2P (peer-to-peer)** permitían compartir archivos directamente entre usuarios sin depender de un servidor central.
Ejemplos clásicos:

* **eMule / eDonkey2000** → muy populares entre 2003 y 2010.
* **Ares** → más simple y masivo en América Latina.
* **BitTorrent** → más avanzado técnicamente, sigue vigente.

Funcionaban bien cuando:

* Mucha gente tenía archivos disponibles (“seeders”).
* Los ISP no bloqueaban el tráfico P2P.
* Las velocidades de subida eran suficientes.

---

### 📉 2. Por qué cayeron en desuso

**a) Aparición del streaming legal**
Plataformas como **YouTube, Netflix, Spotify, etc.** ofrecieron comodidad y velocidad.
Ya no hacía falta descargar ni esperar días.

**b) Menos comunidad y seeds**
Con el tiempo, los usuarios dejaron de compartir, por lo que los archivos eran más lentos o imposibles de conseguir.

**c) Bloqueos y persecución legal**
Las discográficas y estudios de cine presionaron a los ISP para **bloquear puertos P2P** o **rastrear IPs**.
Mucha gente tuvo miedo a sanciones.

**d) Riesgos de malware**
En Ares o eMule era común bajar un “.avi” o “.mp3” que en realidad era un virus o troyano.

---

### ⚙️ 3. Qué queda del P2P hoy

El **P2P no desapareció**, solo cambió de forma:

* **BitTorrent** sigue vivo (qBittorrent, Transmission, Deluge).

  * Redes privadas como **IPTorrents, RARBG (cerró), 1337x, The Pirate Bay**, etc.
  * Usado también de forma legítima (Linux, distribución de datos grandes).

* **WebTorrent / Torrent vía navegador**:
  Permite compartir sin cliente externo, desde la web.

* **IPFS (InterPlanetary File System)**:
  Un nuevo tipo de red descentralizada, sin servidores centrales, más moderna y distribuida.
  Usada para proyectos web descentralizados y archivos permanentes.

* **Blockchain y redes distribuidas**:
  Algunos proyectos tipo **Filecoin, Arweave, Sia** combinan P2P + blockchain para almacenamiento descentralizado.

---

### 💡 4. Alternativas actuales (legales y técnicas)

| Finalidad                                       | Alternativa moderna                                  |
| ----------------------------------------------- | ---------------------------------------------------- |
| Compartir archivos grandes sin servidor central | **Resilio Sync**, **Syncthing** (basados en P2P)     |
| Descargar contenido libre o legal               | **BitTorrent** (para Linux, videos educativos, etc.) |
| Streaming descentralizado                       | **WebTorrent**, **Peertube**                         |
| Almacenamiento distribuido                      | **IPFS**, **Filecoin**, **Arweave**                  |
| Comunicación P2P                                | **Tox**, **Briar**, **Retroshare**                   |

---

### 🧭 En resumen

* Las redes P2P clásicas no murieron, **evolucionaron hacia formas más eficientes y seguras**.
* Lo que cambió fue el **uso masivo para piratería**, desplazado por el **streaming centralizado**.
* Hoy el P2P sigue siendo muy usado “por debajo” de la superficie, en tecnología descentralizada moderna.


Hoy en día **sí existen redes P2P activas y modernas**, pero muchas ya **no se usan solo para piratería**, sino también para **compartir archivos, sincronizar datos o crear servicios descentralizados**.
Las agrupé por tipo y evolución:

---

## ⚡ 1. **BitTorrent y su ecosistema**

👉 Es la **única red P2P “clásica” que sigue muy viva**.

**Clientes populares (actuales):**

* **qBittorrent** 🟢 (el más usado hoy, libre y sin publicidad)
* **Transmission** 🟢 (ligero, multiplataforma)
* **Deluge** y **rTorrent** (más técnicos)
* **WebTorrent** 🌐 (funciona directo en el navegador)

**Usos actuales:**

* Distribución de **software libre** (ej: Ubuntu, Fedora, Debian).
* Compartir grandes archivos sin servidor.
* Aún existen comunidades privadas (IPTorrents, TorrentLeech, etc.).
* Algunas plataformas usan **streaming vía torrent** (ej: WebTorrent o Stremio en parte).

---

## 🌍 2. **IPFS (InterPlanetary File System)**

Una **red distribuida moderna**, sucesora conceptual del P2P clásico.

**Características:**

* Cada archivo tiene un “hash” único (como una huella digital).
* Los archivos se almacenan y replican en múltiples nodos.
* No depende de servidores: los datos viven “en la red”.

**Usos:**

* Sitios web descentralizados.
* Almacenamiento resistente a censura.
* NFTs, proyectos de blockchain, copias de seguridad permanentes.

**Ejemplos:**

* IPFS Desktop, Kubo (nodo oficial), Brave Browser lo soporta nativamente.

---

## 💾 3. **Filecoin, Arweave, Sia**

Son **redes P2P + blockchain** diseñadas para almacenamiento descentralizado.

| Red              | Característica principal                                         |
| ---------------- | ---------------------------------------------------------------- |
| **Filecoin**     | Usa el protocolo IPFS y paga a los nodos por almacenar datos.    |
| **Arweave**      | Guarda información “para siempre” (usa almacenamiento perpetuo). |
| **Sia / Skynet** | Enfocada en hosting descentralizado y aplicaciones distribuidas. |

Estas redes son la evolución del P2P hacia el **almacenamiento distribuido confiable**.

---

## 🔄 4. **Resilio Sync / Syncthing**

Redes P2P **privadas**, para sincronizar archivos entre tus propios dispositivos o grupos de confianza.

* **Resilio Sync** (antes *BitTorrent Sync*): usa el protocolo BitTorrent para sincronización privada.
* **Syncthing**: 100 % libre y cifrado extremo a extremo.

👉 Son alternativas P2P reales a Dropbox o Google Drive.

---

## 📺 5. **Plataformas descentralizadas de video y redes sociales**

* **PeerTube**: alternativa P2P y federada a YouTube (usa WebTorrent).
* **Odysee / LBRY**: combina P2P con blockchain.
* **Freenet / I2P / GNUnet**: redes P2P anónimas, resistentes a censura.

---

## 🗣️ 6. **Comunicación y mensajería P2P**

Algunos proyectos modernos usan P2P para chatear sin servidores:

* **Briar** (Android, funciona incluso sin Internet, por Bluetooth o Wi-Fi Direct).
* **Tox** (mensajería cifrada P2P de escritorio).
* **RetroShare** (red social y chat descentralizado).

---

## 🔚 En resumen

| Propósito           | Red / Proyecto actual                 | Tipo de evolución          |
| ------------------- | ------------------------------------- | -------------------------- |
| Descargas           | BitTorrent / qBittorrent / WebTorrent | Clásico → optimizado       |
| Web descentralizada | IPFS                                  | P2P moderno sin servidores |
| Almacenamiento      | Filecoin / Arweave / Sia              | P2P + blockchain           |
| Sincronización      | Syncthing / Resilio Sync              | P2P privado                |
| Video / streaming   | PeerTube / Odysee                     | P2P + federación           |
| Mensajería          | Tox / Briar                           | P2P puro                   |

