# Intro

* B2: IT-Grundlagen und Coding, LV2.2: Werkstatt Coding/Webtechnologien

## Admin

* 3 online quizzes during the course
* 1 final project

Due dates:

* 2022-XX-XX

## About

### Protocols

> Web Protokolle und Standards, Anwendungs-Architekturen (z.B. Client-Server,
verteilte Systeme, dienstorientierte Architekturen, Web-Services) sowie
standardisierte Webtechnologien (HTML, CSS, JSON, RDF, Web APIs) und de-facto
Webframeworks unter Anleitung nutzen, die Anforderungen von Suchmaschinenopti-
mierung (Web Accessibility und Mehrsprachigkeit (Web I18N)) technisch erfassen
und berücksichtigen

Application programming interfaces (API) as a key technology for automation,
services, integration and cooperation. An API is a unit of Composability.

* Automation: allow to control abstract and physical processes through programs
* Services: provide services to humans and machines
* Integration: evolve existing technology landscapes
* Cooperation: define ways of data exchanges and services

One key approach for web services is to use standardized protocoals and data
formats, like HTTP and JSON. The human side: HTML, CSS. The machine side: JSON,
RDF, Web APIs.

Web services are typically not built from scratch, but leverage existing code in
form of [web frameworks](https://en.wikipedia.org/wiki/Web_framework). Most
mainstream programming languages have one or more web frameworks.

### Current Developments

> aktuelle Entwicklungen der Web- und Internettechnologie kennen und ihre
Relevanz einschätzen

The web evolves. There are a few directions:

* transport efficiency: while HTTP/1.1 (text protocol) continues to be
  supported, we have HTTP/2 (a binary protocol) and HTTP/3
  ([https://almanac.httparchive.org/en/2020/http](https://almanac.httparchive.org/en/2020/http))
* we saw increased centralization
  ([https://mnot.github.io/avoiding-internet-centralization/draft-nottingham-avoiding-internet-centralization.html](https://mnot.github.io/avoiding-internet-centralization/draft-nottingham-avoiding-internet-centralization.html))
* we see a drift towards more decentralized technologies (distribution
  technologies, like [ipfs](https://ipfs.io/),
  [web3](https://blog.cloudflare.com/what-is-web3/)); which in short is a
  strange world ([Blockchains Are a Bad Idea](https://www.youtube.com/watch?v=15RTC22Z2xI))
* from static pages to applications (e.g. [web assembly](https://developer.mozilla.org/en-US/docs/WebAssembly))
* immersive, creative applications; examples: [marzipano](https://www.marzipano.net/demos.html),

### Content

> die Entwicklung und ggf. cloud-basierte Bereitstellung von Webauftritten via
modularisierter Content Management Systeme an einem praktischen Beispiel
durchführen,

Modern CMS are typically large software projects. There is a spectrum of
functionality and hosting options.

* simple (single user, get bytes out) to enterprise (roles, workflows, media libraries, ...)
* self-hosted to managed

Most systems are modular. Plugins enhance functionality or appearance, via
application specific set of interfaces.

### Data Fusion

> Vorgehensweisen für die Anreicherung von Webinhalten mit
strukturierten, semantischen und graph-basierten, ggf. öffentlich verfügbaren
Daten kennen und anwenden lernen,

The data process is straight-forward (but *god is in the details*):

* data curation (finding, selecting data)
* data acquisition (API, scraping, manual labor, ...)
* data preparation (refinement, cleanup, ...)
* data fusion (combine data source, enhance existing applications)
* data products

There is a myriad of options to improve existing an existing document with
another data set. Examples:

* include microdata in a webpage; improve machine readability (e.g. catalog
  item, available for loan, structured metadata) -- this will happen mostly
server-side
* availability information for a catalog (separate metadata from live system status)
* recommendation systems (e.g. [litmaps](https://app.litmaps.co/?seedId=3174407535) for arxiv.org)

Other examples:

* fuse catalog data with citation data (offline or on-the-fly)
* fuse catalog data with authority data (GND)
* fuse ISIL data with map data

There are millions of datasets openly available on the web right now:

* [LOD cloud](https://lod-cloud.net/)
* [Dataset search](https://datasetsearch.research.google.com/)

See: [Datasets on the Internet](Datasets.md)


