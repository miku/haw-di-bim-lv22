# [WIP] HAW HH, Werkstatt Coding/Webtechnologien

> LV2.2: Werkstatt *Coding/Webtechnologien*

Veranstaltung im Rahmen des Studiums [BA Bibliotheks- und
Informationsmanagement](https://www.haw-hamburg.de/fileadmin/DMI-I/PDF/BIM/Modulhandbuch_BIM_2021-02-24.pdf);
Modul B2: IT-Grundlagen und Coding

> My younger son said "coding is basically just ifs and for loops."--
> [1466934223831506951](https://twitter.com/ID_AA_Carmack/status/1466934223831506951)

Schwerpunkte:

* Webtechnologien, Protokolle und Standards, Kollaboration, Arbeit mit Daten, Publikation

Paralleler zu der Veranstaltung (SS2022) statt findender Wettbewerb: [Coding da
Vinci BW 2022](https://codingdavinci.de/de/events/baden-wuerttemberg-2022)
Hackathon (07.05.2022 &mdash; 24.06.2022):

> Seit 2014 vernetzt Coding da Vinci, der Kulturhackathon, Kultur- und
> Technikwelten miteinander und zeigt, welche überraschenden Möglichkeiten in
> offenen Kulturdaten stecken. In einer mehrwöchigen Sprintphase entwickeln
> Teams aus Hacker\*innen gemeinsam mit Kulturinstitutionen funktionierende
> Prototypen z.B. für Apps, Webseiten, Datenvisualisierungen, Spiele oder
> interaktive Installationen, die überraschende und inspirierende Wege zeigen,
> wie Sammlungsobjekte von Institutionen auf neue Weisen vermittelt und genutzt
> werden können. -- [https://codingdavinci.de/de](https://codingdavinci.de/de)

# Material

* Lecture notes; md docs; pdf export
* Cheat sheets
* Credentials

# Inhalt

* [1 Werkstatt-Umgebung](#1-werkstattumgebung)
* [2 Projektverwaltung mit Git](#2-projektverwaltung-mit-git)
* [3 Standards](#3-standards)
* [4 Publizieren im Web 1](#4-publizieren-im-web-1)
* [5 Publizieren im Web 2](#5-publizieren-im-web-2)
* [6 Dokumente Transformieren](#6-dokumente-transformieren)
* [7 Daten: Formate und Standards](#7-daten-formate-und-standards)
* [8 Daten: Finden](#8-daten-finden)
* [9 Daten: Speichern](#9-daten-speichern)
* [10 Daten: Verarbeiten](#10-daten-verarbeiten)
* [11 Web: Microframeworks](#11-web-microframeworks)
* [12 Web: Wir sind live!](#12-web-wir-sind-live)
* [13 Lab: Strings](#13-lab-strings)
* [14 Lab: Python](#14-lab-python)
* [15 Lab: Challenge](#15-lab-challenge)
* [Idee A: Erstellung eines Datensatzes](#idee-a-erstellung-eines-datensatzes)
* [Idee B: Publikationspipeline](#idee-b-publikationspipeline)
* [Idee C: Daten-Intensive Applikation](#idee-c-datenintensive-applikation)
* [Idee D: Interaktive Web Applikation](#idee-d-interaktive-web-applikation)
* [Idee E: Beitrag zu Coding da Vinci](#idee-e-beitrag-zu-coding-da-vinci)



## 1 Werkstatt-Umgebung

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

## 2 Projektverwaltung mit Git

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

## 3 Standards

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

## 4 Publizieren im Web 1

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

## 5 Publizieren im Web 2

* Hosting-Optionen
* Lab: Deployment



## 6 Dokumente und Semantic Markup

* Pandoc
* Pandoc Filters
* e.g. md -> html [-> scp]
* Microformats
* RDFa

Papers:

* [Microformats: a Pragmatic Path to the Semantic Web](https://www.ramb.ethz.ch/CDstore/www2006/devel-www2006.ecs.soton.ac.uk/programme/files/pdf/p116.pdf)

Projects:

* [https://schema.org/](https://schema.org/)

## 7 Daten: Formate, Standards, APIs

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


## 8 Daten: Finden

* Web APIs
* datasets
* scraping
* OAI-PMH
* SPARQL

> google dataset search, pup, DDB API, fatcat API, ISSN API, crossref API, DOAJ API, metha

## 9 Daten: Speichern

* files
* sqlite3
* SQL
* triple und triple stores

> open, close, connect, iconv, file

## 10 Daten: Verarbeiten

* Automatisierung
* Transformation
* Qualität

> python, pandas, openrefine, cron

## 11 Web: Microframeworks

* Web Applicationss
* Micro-Framework

> python, flask, bottle

## 12 Web: Wir sind live!

* Deployment; heycloud

> scp, ssh, hosting, exposing local port (ngrok)

## 13 Lab: Strings

* Reguläre Ausdrücke

> re

## 14 Lab: Python

* Hilfreiche Bibliotheken

> dateparser, pandas, seaborn, jupyter

## 15 Lab: Challenge

* Typische Probleme im Umgang mit Daten
* Schnittstellen

> sort, uniq, comm

## 16 Lab: Hacking

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
