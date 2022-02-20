# [WIP] HAW HH, Werkstatt Coding/Webtechnologien

> LV2.2: Werkstatt *Coding/Webtechnologien*

Veranstaltung im Rahmen des Studiums [BA Bibliotheks- und
Informationsmanagement](https://www.haw-hamburg.de/fileadmin/DMI-I/PDF/BIM/Modulhandbuch_BIM_2021-02-24.pdf);
Modul B2: IT-Grundlagen und Coding

> My younger son said "coding is basically just ifs and for loops."--
> [1466934223831506951](https://twitter.com/ID_AA_Carmack/status/1466934223831506951)

Schwerpunkte:

* Webtechnologien  [W], Protokolle und Standards [S], Kollaboration [K], Arbeit mit Daten [D], Publikation [P]

Paralleler zu der Veranstaltung (SS2022) statt findende Wettbewerbe:

* [Coding da Vinci Ost3](https://codingdavinci.de/index.php/de/events/ost3-2022)

> Coding da Vinci, der Kultur-Hackathon, vernetzt die Kultur- und die
> Technikwelt miteinander. Im Frühjahr 2022 kommt Coding da Vinci nach Sachsen,
> Polen und in die Tschechische Republik und zeigt einmal mehr, welche
> überraschenden Möglichkeiten in offenen Kulturdaten stecken.

* [Coding da Vinci BW 2022](https://codingdavinci.de/de/events/baden-wuerttemberg-2022) Hackathon (07.05.2022 &mdash; 24.06.2022):

> Seit 2014 vernetzt Coding da Vinci, der Kulturhackathon, Kultur- und
> Technikwelten miteinander und zeigt, welche überraschenden Möglichkeiten in
> offenen Kulturdaten stecken. In einer mehrwöchigen Sprintphase entwickeln
> Teams aus Hacker\*innen gemeinsam mit Kulturinstitutionen funktionierende
> Prototypen z.B. für Apps, Webseiten, Datenvisualisierungen, Spiele oder
> interaktive Installationen, die überraschende und inspirierende Wege zeigen,
> wie Sammlungsobjekte von Institutionen auf neue Weisen vermittelt und genutzt
> werden können. -- [https://codingdavinci.de/de](https://codingdavinci.de/de)

# Material

* Skript (github); PDF export
* Cheat sheets

# Inhalt (wip)

* [1 Willkommen](#1-Willkommen)
* [2 Werkstatt-Umgebung](#2-werkstattumgebung), [Intro](Intro/README.md), [Datasets](Intro/Datasets.md), [Setup](Setup/README.md)
* [3 Projektverwaltung mit Git](#3-projektverwaltung-mit-git), [VersionControl](VersionControl/README.md)
* [4 Standards](#4-standards)
* [5 Publizieren im Web 1](#5-publizieren-im-web-1)
* [6 Publizieren im Web 2](#6-publizieren-im-web-2)
* [7 Dokumente Transformieren](#7-dokumente-transformieren)
* [8 Daten: Formate und Standards](#8-daten-formate-und-standards)
* [9 Daten: Finden](#9-daten-finden)
* [10 Daten: Speichern](#10-daten-speichern)
* [11 Daten: Verarbeiten](#11-daten-verarbeiten)
* [12 Web: Microframeworks](#12-web-microframeworks)
* [13 Web: Wir sind live!](#13-web-wir-sind-live)
* [14 Lab: Strings](#14-lab-strings)
* [15 Lab: Python](#15-lab-python)
* [16 Lab: Challenge](#16-lab-challenge)
* [17 Lab: Hacking](#17-lab-hacking)
* [Idee A: Erstellung eines Datensatzes](#idee-a-erstellung-eines-datensatzes)
* [Idee B: Publikationspipeline](#idee-b-publikationspipeline)
* [Idee C: Daten-Intensive Applikation](#idee-c-datenintensive-applikation)
* [Idee D: Interaktive Web Applikation](#idee-d-interaktive-web-applikation)
* [Idee E: Beitrag zu Coding da Vinci](#idee-e-beitrag-zu-coding-da-vinci)


## 1 Willkommen


## 2 Werkstatt-Umgebung

* Betriebssystem, Linux
* Command line
* Python
* Dateisystem

> virtualbox, vscode, ls, cd, mkdir, python, cat, less

Papers:

* [Programming as Theory Building](https://pages.cs.wisc.edu/~remzi/Naur.pdf)

> The present discussion is a contribution to the understanding of what
programming is. It suggests that programming properly should be regarded as an
activity by which the programmers form or achive a certain kind of insight, a
theory of the matters at hand. This suggestion is in contrast to what appears
to be a more common notion, that programming should be regarded as production
of a program and certain other texts

## 3 Projektverwaltung mit Git

* Versionskontrolle
* Projektverwaltung
* Kollaboration

> git, github, gitlab

Theory:

* [The First 30 Years of Cryptographic Hash Functions and the NIST SHA-3 Competition](https://www.esat.kuleuven.be/cosic/publications/article-1532.pdf)
* [A digital signature based on a conventional encryption function](http://people.eecs.berkeley.edu/~raluca/cs261-f15/readings/merkle.pdf)
* [Providing Authentication and Integrity in Outsourced Databases using Merkle Hash Tree’s](http://people.eecs.berkeley.edu/~raluca/cs261-f15/readings/merkleodb.pdf)

> Cryptographic hash functions map input strings of arbitrary (or very large)
length to short fixed length output strings. In their 1976 seminal paper on
public- key cryptography [31], Diffie and Hellman identified the need for a
one-way hash function as a building block of a digital signature scheme.

## 4 Standards

* URL/URI/URN, persistent identifiers
* HTTP, Hypertext; layer 7 protocol (OSI)
* HTML -> valid HTML, dev inspector -> change headline
* WARC; https://www.iso.org/standard/68004.html; ISO 28500:2017

> curl, wget, requests

Theory:

* Vannevar Bush; [http://web.mit.edu/STS.035/www/PDFs/think.pdf](http://web.mit.edu/STS.035/www/PDFs/think.pdf), [https://en.wikipedia.org/wiki/As_We_May_Think](https://en.wikipedia.org/wiki/As_We_May_Think)
* [https://twitter.com/mekarpeles/status/1468632186039513101](https://twitter.com/mekarpeles/status/1468632186039513101)

> Two centuries ago Leibnitz invented a calculating machine which embodied most
> of the essential features of recent keyboard devices, but it could not then
> come into use. The economics of the situation were against it: the labor
> involved in constructing it, before the days of mass production, exceeded the
> labor to be saved by its use, since all it could accomplish could be
> duplicated by sufficient use of pencil and paper.

## 5 Publizieren im Web 1

* FB / https://tilde.club / [https://heycloud.cc](https://heycloud.cc)
* Markdown
* Static Site Generators
* Git-Basierte Workflows
* Example SSG: Hugo

Papers:

* 2008, Hayes, Cloud Computing: [https://web.archive.org/web/20180713103129/http://www.cs.toronto.edu:80/~delara/courses/csc2228/papers/hayes.pdf](https://web.archive.org/web/20180713103129/http://www.cs.toronto.edu:80/~delara/courses/csc2228/papers/hayes.pdf)

> When  personal  computers  arrived in  the  1980s,  part  of  their  appeal
> was the  promise  of  “liberating” programs and  data  from  the  central
> computing center. (Ted Nelson, the prophet of hypertext,  published  a  book
> titled  Com- puter  Lib/Dream Machines  in 1974.)

* 1975; [http://worrydream.com/refs/Nelson-ComputerLibDreamMachines1975.pdf](http://worrydream.com/refs/Nelson-ComputerLibDreamMachines1975.pdf)

> Technology  fs  an  expression  of  man's  dreams. If man  did
not  Indulge  M s  fantasies, his  thoughts  alone  would  inhibit  the
development  of  technology  Itself. Ancient  visionaries  spoke  of distant
times  and  places, where  men  flew  around  and  about, and some  could  see
each  other  at  great  distance. The  technological realities  of  today  are
already  obsolete  and  the  future  of technology  is  bound  only  by  the
limits  of  our  dreams. Modern communications  media  and  in  particular
electronic  media  are outgrowths  and  extensions  of  those  senses  which
have  become dominant  1n our  social  development.

* [http://www.newmediareader.com/book_samples/nmr-21-nelson.pdf](http://www.newmediareader.com/book_samples/nmr-21-nelson.pdf)

## 6 Publizieren im Web 2

* Hosting-Optionen
* Lab: Deployment



## 7 Dokumente und Semantic Markup

* Pandoc
* Pandoc Filters
* e.g. md -> html [-> scp]
* Microformats
* RDFa

Papers:

* [Microformats: a Pragmatic Path to the Semantic Web](https://www.ramb.ethz.ch/CDstore/www2006/devel-www2006.ecs.soton.ac.uk/programme/files/pdf/p116.pdf)

Projects:

* [https://schema.org/](https://schema.org/)

## 8 Daten: Formate, Standards, APIs

* XML
* JSON
* Schema Languages
* Controlled Vocabularies
* Graphs
* RDF
* OWL

> xmllint, jq, xsltproc, rdflib

Papers:

* [XML spec 1998](http://www.renderx.com/~renderx/Demos/fo2html/xml.pdf), SGML

> As a document markup language, SGML was originally designed to enable the
> sharing of machine-readable large-project documents in government, law, and
> industry.

* [http://www.sgmlsource.com/history/roots.htm](http://www.sgmlsource.com/history/roots.htm)


## 9 Daten: Finden

* Web APIs
* datasets
* scraping
* OAI-PMH
* SPARQL

> google dataset search, pup, DDB API, fatcat API, ISSN API, crossref API, DOAJ API, metha

## 10 Daten: Speichern

* files
* sqlite3
* SQL
* triple und triple stores

> open, close, connect, iconv, file

## 11 Daten: Verarbeiten

* Automatisierung
* Transformation
* Qualität

> python, pandas, openrefine, cron

## 12 Web: Microframeworks

* Web Applicationss
* Micro-Framework

> python, flask, bottle

## 13 Web: Wir sind live!

* Deployment; heycloud

> scp, ssh, hosting, exposing local port (ngrok)

## 14 Lab: Strings

* Reguläre Ausdrücke

> re

## 15 Lab: Python

* Hilfreiche Bibliotheken

> dateparser, pandas, seaborn, jupyter

## 16 Lab: Challenge

* Typische Probleme im Umgang mit Daten
* Schnittstellen

> sort, uniq, comm

## 17 Lab: Hacking

* hacking, questions, ideas

----

# Themen: Projektarbeit

## Idee A: Erstellung eines Datensatzes

Ziel: Auswahl eines Themas und Erstellung eines Datensatzes aus
unstrukturierten oder semi-strukturierten Daten. Veröffentlichung dieser inklusive
Dokumentation auf [zenodo.org](https://zenodo.org/)

Hintergrund: Eine Vielzahl von Informationen liegen nur in halbstrukturierter
oder unstrukturierter Form vor; dennoch können diese Informationen interessant
oder notwendig sein (als Beispiel: während der COVID19 Pandemie haben einige
überregionale Zeitungen eigene Datenerhebungen begonnen).

## Idee B: Publikationspipeline

Ziel: ein Program, das aus einer Menge an Input-Dokumenten eine oder mehrere
HTML-Seiten erstellt. Minimalistisches Publikationstool - statische Seiten sind
einfacher zu deployen und zu pflegen.

* Daten können z.B. während der Prozessierung mit Daten aus externen Quellen
  angereichert werden
* Unterstützung von verschiedener Medientypen
* Mit entsprechenden Automatisierungsschnittstellen kann man auch in statische
  Seiten Dynamik einbauen, z.B. in dem man bestimmte Seiten mit aktuellen
Informationen stündlich oder täglich aktualisiert


## Idee C: Daten-Intensive Applikation

Ziel: Zwei oder mehr (größere) Datensätze verknüpfen und ggfs. analysieren,
Resultat als Report, Web Applikation oder Webseite publizieren.

* Daten Verknüpfen und anhand einer oder mehrerer Forschungsfragen mit Hilfe
  von eigenen Programmen Antworten finden
* Daten verschiedener OAI-Endpunkte verknüfen; z.B. für tägliche, wöchentliche
  Update-Listen
* Daten der Wikipedia analysieren; z.B. Anzahl der zitierten Publikationen
* Daten der Wikipedia analysieren; z.B. Anzahl der zitierten Publikationen und
  Empfehlungen für Literatur basierend auf Inhalt eines Artikels generieren

## Idee D: Interaktive Web Applikation

Ziel: Eine Web-Applikation, mit der Nutzer Inhalte teilen können.

Konkrete Ideen:

* eine Seite, wo man Dateien hochladen kann und eine Übersicht über die Inhalte
  der Datei bekommt (z.B. Hochladen einer Excel-Datei und Ausgabe von
ableitbaren Informationen, wie Anzahl der Datensätze, Encoding-Fehler, ...)
* eine Seite zum Kollaborativen Filtern von Inhalten (s.a. "reddit algorithmus")
* eine Seite zum Teilen von bestimmten Inhalten (z.B. Seite für das Teilen von Bildern zu technischen Themen)
* eine semi-statische Frage/Antwort Seite - Testaufgaben als Markup formuliert, als Web-Applikation implementiert

## Idee E: Beitrag zu Coding da Vinci

> Seit 2014 vernetzt Coding da Vinci, der Kulturhackathon, Kultur- und
> Technikwelten miteinander und zeigt, welche überraschenden Möglichkeiten in
> offenen Kulturdaten stecken. In einer mehrwöchigen Sprintphase entwickeln
> Teams aus Hacker\*innen gemeinsam mit Kulturinstitutionen funktionierende
> Prototypen z.B. für Apps, Webseiten, Datenvisualisierungen, Spiele oder
> interaktive Installationen, die überraschende und inspirierende Wege zeigen,
> wie Sammlungsobjekte von Institutionen auf neue Weisen vermittelt und genutzt
> werden können.
