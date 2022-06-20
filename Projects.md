# Projekte

Auswahl und Bearbeitung eines Projektes.

## P1: Datenanalyse

Analyse eines Datensatzes aus dem Bereich GLAM, z.B. eines der Datensätze von
Coding da Vinci [Coding da Vinci](https://codingdavinci.de/de/daten) -- es muß
hier **kein** Beitrag zu dem Wettbewerb eingereicht werden; es geht um einen
wichtigen ersten Schritt in der Arbeit mit Daten: *Verständnis*. Dazu müssen die
Daten geladen, bereinigt, aufbereitet und eventuell auch visualisiert werden.

Beispiele für Fragen an Daten:

* Welchen Typ haben bestimmte Werte? Das können Datentypen (aus der
  Programmierung) oder auch
  [Skalenniveaus](https://de.wikipedia.org/wiki/Skalenniveau)
* Woher stammen die Daten?
* Wie vollständig sind die Daten?
* Welchen Ausschnitt repräsentieren die Daten?
* Fehlstellen in den Daten?
* Fehlende Informationen, z.B. fehlende Einheiten?
* ...

Abgabeformat:

* der **Rohdatensatz** (eine oder mehrere Dateien, je nach Datensatz)
* ein **Jupyter-Notebooks** die anhand der Rohdaten bestimmte Fragen beantworten
* Kurzdokumentation (max. 3 Seiten) zur Bearbeitung: welche Probleme tauchten auf? Welche anderen Tools wurden verwendet (und warum)? ...

Manchmal ist es notwendig, bestimmte Daten zu Gruppieren (z.B. verschiedene
Schreibweise eines Names zu normalisieren). Dazu eigenen sich u.a. Tools wie
[OpenRefine](https://openrefine.org/) oder auch
[Pandas](https://pandas.pydata.org/) ([Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)).

Kenntnisse:

* Python
* Jupyter
* XML, JSON, CSV
* Pandas

Beispiele:

* [CSV HMT](https://github.com/miku/sundaypython/blob/master/notebooks/04%20Working%20with%20CSV.ipynb), Einschreibungen an der Hochschule für Musik und Theater Leipzig 1843-1893
* [CSV Muka-Statistik](https://github.com/miku/sundaypython/blob/master/notebooks/05%20Another%20CSV%20dataset.ipynb), *Muka-Statistik* über Anteil der sorbischen Minderheit (1884)
* [DWD Wetterdaten](...)
* [Datensatz: Automarkt](...)
* [OpenData Hamburg](...) - Statistisches Jahrbuch 2020, [https://suche.transparenz.hamburg.de/dataset/statistisches-jahrbuch-hamburg-berichtsjahr-2020](https://suche.transparenz.hamburg.de/dataset/statistisches-jahrbuch-hamburg-berichtsjahr-2020)

## P2: Text-Adventure

Aufgabe:

[Interactive Fiction](https://de.wikipedia.org/wiki/Interactive_Fiction) ist
ein Computer-Spiel-Genre, in der die Spielwelt in Textform vermittelt und
Spieler über ihre Aktionen die Handlung beeinflussen.

Ein Text-Adventure besteht aus einer Welt, durch die eine Figur navigieren
kann, Dinge sieht, Gegenstände findet, auf andere Figuren oder Rätsel trifft.

* [ ] Implementierung eines einfachen Text-Adventures mit Hilfe der
  Programmiersprache Python. Python ist sehr gut für die Arbeit mit Text
  geeignet.
* [ ] Modellierung der *Game-Mechanik*, Nutzer-Eingabe, Ausgabe, mögliche
  Aktionen.
* [ ] Das Spiel soll ohne Handbuch spielbar sein, also einfach sein und etwas
  Hilfe anbieten (z.B. beim Start).

Abgabeformat:

* eine **Programmdatei** `game.py`, die ausführbar ist (ggfs. weitere Dateien, die zum Spiel gehören)
    * Code sollte Dokumentation enthalten
* eine Kurzdokumentation der wichtigsten Entscheidungen hinsichtlich der
  Implementierung (max. 3 Seiten)

Kenntnisse:

* Python

Beispiele:

* [Projects/Adventure](https://github.com/miku/haw-di-bim-lv22/tree/main/Projects/Adventure)

## P3: Accessibility Report

Ziel: Existierende Seiten (aus dem GLAM Bereich) auf Accessibility und Nutzung
von modern Web-Technologien untersuchen. Erstellung eines Reports mit
IST-Zustand und Empfehlungen für SOLL-Zustand auf Basis modernen Web-Standards.

Hintergrund: Das moderne Web muss vielen Ansprüchen gerecht werden, unter
anderen sollen Seite zugänglich, navigierbar und performant sein. Dafür stehen
eine Vielzahl von Technologien und Standards zur Verfügung, die nicht immer
alle eingesetzt werden.

Aufgabe:

* [ ] Auswahl einer Webseite (Domain)
* [ ] Recherche zu Tools für die Messung von Accessibility und weiteren Metriken
* [ ] Zusammenstellung einer Liste von Bewertungskriterien (min. 8 Kriterien)
* [ ] Zusammenstellung von Alternativen und Verbesserungsvorschlägen, falls möglich
* [ ] Erstellung eines Berichtes mit allen relevanten Informationen

Mögliche Metriken:

* URL-Struktur
* Sind URL stabil? s.a. [Cool URIs don't change](https://www.w3.org/Provider/Style/URI)
* Welche Inhalte sind verlinkbar? In welcher Granularität? (als Beispiel können
  Sie an YouTube denken, wo z.B. Videos inklusive Start-Zeit, verlinkt werden
  können ([Beispiel](https://youtu.be/o8NPllzkFhE?t=12)))
* Werden [semantische Auszeichnungen](https://developer.mozilla.org/en-US/docs/Glossary/Semantics#semantic_elements) genutzt?
* Wie schnell lädt die Seite?
* Wie viele HTTP-Anfragen löst die Seite aus? (Sie können das z.B. über [Chrome devtools](https://developer.chrome.com/docs/devtools/) oder auch andere Tools sehen)
* Sind Bilder und andere Assets optimiert (in einem Web-Format, komprimiert, ...)?

Abgabeformat:

* Ausarbeitung (max. 5 Seiten) welche folgende Punkte enthält:
    * Welche Tools kamen zur Prüfung zu Einsatz? Begründung der Auswahl, ggfs. Vorteile/Nachteile
    * Wie schneidet die untersuchte Seite/Domain ab?
    * Welche Verbesserungsvorschläge kann man formulieren?
* Abgabe von erhobenen Daten, falls diese vorliegen

Kenntnisse:

* HTML
* Web standards: [https://www.w3.org/standards/](https://www.w3.org/standards/)

## P4: Webseite mit einem Static Site Generator erstellen

Static Site Generators bieten die Möglichkeit ein komplettes Web-Projekt in
kurzer Zeit zu realisieren.

Aufgabe:

* [ ] Wählen Sie ein Thema ihrer Wahl, welches Sie mittels eines Webprojektes
  veröffentlichen wollen (das kann aus dem bibliothekarischen Bereich sein,
  aber auch ein anderes)
* [ ] Nutzen sie [zola](https://www.getzola.org/) (oder ein andere [SSG
  tool](04-Static.md) zur Strukturierung Ihres Projektes
* [ ] Erstellen Sie einige Seiten für den Inhalt (z.B. einen Blog, eine
  Beschreibung ihres Themas, etc.) -- (hier können Sie auch über alternative
  Wege der Erstellung von Markdown-Dateien nachdenken, z.B. mit Hilfe von
  Scripten, die z.B. Daten in eine Tabellenform bringen, etc.)
* [ ] Passen Sie die Seite visuell an, nutzen Sie ein existierendes
  [Theme](https://www.getzola.org/themes/) oder passen Sie eigene Templates an

Kenntnisse:

* HTML
* CSS
* Command Line
* Markdown

Abgabeformat:

* eine zip-Datei, die alle Dateien und Verzeichnisse des Projektes enthält
* optional deployment auf bereitgestellten Server

----

Liste von Projektideen.


## Idee A: Erstellung eines Datensatzes

Ziel: Auswahl eines Themas und Erstellung eines Datensatzes aus verschiedenen
strukturierten, oder auch unstrukturierten und semi-strukturierten Daten.
Veröffentlichung dieser inklusive Dokumentation auf
[zenodo.org](https://zenodo.org/)

Hintergrund: Eine Vielzahl von Informationen liegen nur in halbstrukturierter
oder unstrukturierter Form vor; dennoch können diese Informationen interessant
oder notwendig sein (als Beispiel: während der COVID19 Pandemie haben einige
überregionale Zeitungen eigene Datenerhebungen begonnen).

Varianten:

* einmaliges Erstellen eines Datensatzes oder auch Möglichkeit für Updates

### Beispiele

* [Wikipedia Citations](https://github.com/Harshdeep1996/cite-classifications-wiki), "A comprehensive dataset of citations with identifiers extracted from English Wikipedia"
* Herunterladen von z.B. einer Menge von Tweets

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

Für dieses Projekt könnten auch Erweiterungen an existitierenden Tools in Betracht kommen:

* [pandoc](https://en.wikipedia.org/wiki/Pandoc) ist eine vielseitiges
  Transformationstool für Dokumente; mit Hilfe von Filtern kann die
Funktionalität erweitert werden: [Filters](https://pandoc.org/filters.html)
* [Hugo](https://gohugo.io/) ist ein static site generator

### Beispiele

* ...

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

### Beispiele

* ...

## Idee D: Interaktive Web Applikation

Ziel: Eine Web-Applikation, mit der Nutzer Inhalte teilen können oder auch
Tool-Website für internen Gebrauch.

Konkrete Ideen:

* eine Seite, wo man Dateien hochladen kann und eine Übersicht über die Inhalte
  der Datei bekommt (z.B. Hochladen einer Excel-Datei und Ausgabe von
ableitbaren Informationen, wie Anzahl der Datensätze, Encoding-Fehler, ...)
* eine Seite zum Kollaborativen Filtern von Inhalten (s.a. "reddit algorithmus")
* eine Seite zum Teilen von bestimmten Inhalten (z.B. Seite für das Teilen von Bildern zu technischen Themen)
* eine semi-statische Frage/Antwort Seite - Testaufgaben als Markup formuliert, als Web-Applikation implementiert

### Beispiele

...

## Idee E: Accessibility Report

Ziel: Existierende Seiten (aus dem GLAM Bereich) auf Accessibility und Nutzung
von modern Web-Technologien untersuchen. Erstellung eines Reports mit
IST-Zustand und Empfehlungen für SOLL-Zustand auf Basis modernen Web-Standards.

Hintergrund: Das moderne Web muss vielen Ansprüchen gerecht werden, unter
anderen sollen Seite zugänglich, navigierbar und performant sein. Dafür stehen
eine Vielzahl von Technologien und Standards zur Verfügung, die nicht immer
alle eingesetzt werden.

Mögliches Format:

* Auswahl einer Webseite (Domain)
* Recherche zu Tools für die Messung von Accessibility und weiteren Metriken
* Zusammenstellung einer Liste von Bewertungskriterien
* Zusammenstellung von Alternativen und Verbesserungsvorschlägen, falls möglich
* Erstellung eines Berichtes mit allen relevanten Informationen

Mögliche Metriken:

* URL-Struktur
* Sind URL stabil? s.a. [Cool URIs don't change](https://www.w3.org/Provider/Style/URI)
* Welche Inhalte sind verlinkbar? In welcher Granularität? (als Beispiel können Sie an YouTube denken, wo z.B. Videos inklusive Start-Zeit, verlinkt werden können ([Beispiel](https://youtu.be/o8NPllzkFhE?t=12)))
* Werden [semantische Auszeichnungen](https://developer.mozilla.org/en-US/docs/Glossary/Semantics#semantic_elements) genutzt?
* Wie schnell lädt die Seite?
* Wie viele Anfragen löst die Seite aus?
* Sind Bilder und andere Assets optimiert?

Abgabeformat:

* Ausarbeitung (max 8 Seiten) welche folgende Punkte enthält:
    * Welche Tools kamen zur Prüfung zu Einsatz? Begründung der Auswahl, ggfs. Vorteile/Nachteile
    * Wie schneidet die untersuchte Seite/Domain ab?
    * Welche Verbesserungsvorschläge kann man formulieren?
* Abgabe von erhobenen Daten, falls diese vorliegen

### Beispiele

...

## Idee F: Free Form Project

Ziel: Design und Implementierung einer Software-Applikation. Frei wählbares Thema.

### Beispiele

Siehe auch: [Projects](Projects)

#### Datenanalyse

Analyse eines Datensatzes aus dem Bereich GLAM, z.B. eines der Datensätze von
Coding da Vinci [Coding da Vinci](https://codingdavinci.de/de/daten) -- es muß
hier **kein** Beitrag zu dem Wettbewerb eingereicht werden; es geht um einen
wichtigen ersten Schritt in der Arbeit mit Daten: Verständnis. Dazu müssen die
Daten geladen, bereinigt, aufbereitet und eventuell auch visualisiert werden.

Abgabeformat:

* **Rohdatensatz**
* ein (oder mehrere) **Jupyter-Notebooks** die anhand der Rohdaten bestimmte Fragen beantworten

Beispiele für Fragen an Daten:

* Welchen Typ haben bestimmte Werte? Das können Datentypen (aus der Programmierung) oder auch [Skalenniveaus](https://de.wikipedia.org/wiki/Skalenniveau)
* Woher stammen die Daten?
* Wie vollständig sind die Daten?
* Welchen Ausschnitt repräsentieren die Daten?
* Fehlstellen in den Daten?
* Fehlende Informationen, z.B. fehlende Einheiten?
* ...

Manchmal ist es notwendig, bestimmte Daten zu Gruppieren (z.B. verschiedene
Schreibweise eines Names zu normalisieren). Dazu eigenen sich u.a. Tools wie [OpenRefine](https://openrefine.org/) oder auch [Pandas](https://pandas.pydata.org/).


#### Implementierung eines Text-Adventures

[Interactive Fiction](https://de.wikipedia.org/wiki/Interactive_Fiction) ist
ein Computer-Spiel-Genre, in der die Spielwelt in Textform vermittelt und
Spieler über ihre Aktionen die Handlung beeinflussen.

Ein Text-Adventure besteht aus einer Welt, durch die eine Figur navigieren
kann, Dinge sieht, Gegenstände findet, auf andere Figuren oder Rätsel trifft.

Aufgabe wäre die Implementierung eines einfachen Text-Adventures mit Hilfe der
Programmiersprache Python. Python ist sehr gut für die Arbeit mit Text geeignet.

Abgabeformat:

* eine **Programmdatei** `game.py`, die ausführbar ist
* eine Kurzdokumentation der wichtigsten Entscheidungen hinsichtlich der Implementierung (max 3 Seiten)

#### Design, Implementierung und Veröffentlichung einer Webseite mit einem SSG

Static Site Generators bieten die Möglichkeit ein komplettes Web-Projekt in kurzer Zeit zu realisieren.

Aufgabe:

* Wählen Sie ein Thema ihrer Wahl, welches Sie mittels eines Webprojektes veröffentlichen wollen
* Nutzen sie [zola](https://www.getzola.org/) (oder ein andere SSG tool) zur Strukturierung Ihres Projektes
* Erstellen Sie einige Seiten für den Inhalt (z.B. einen Blog, eine Beschreibung ihres Themas, etc.)
* Passen Sie die Seite visuell an, nutzen Sie ein existierendes [Theme](https://www.getzola.org/themes/) oder passen Sie eigene Templates an
* Veröffentlichen Sie die Seite (z.B. via exacloud)

Abgabeformat:

* eine zip-Datei, die alle Dateien und Verzeichnisse des Projektes enthält


## Idee G: Beitrag zu Coding da Vinci

> Seit 2014 vernetzt Coding da Vinci, der Kulturhackathon, Kultur- und
> Technikwelten miteinander und zeigt, welche überraschenden Möglichkeiten in
> offenen Kulturdaten stecken. In einer mehrwöchigen Sprintphase entwickeln
> Teams aus Hacker\*innen gemeinsam mit Kulturinstitutionen funktionierende
> Prototypen z.B. für Apps, Webseiten, Datenvisualisierungen, Spiele oder
> interaktive Installationen, die überraschende und inspirierende Wege zeigen,
> wie Sammlungsobjekte von Institutionen auf neue Weisen vermittelt und genutzt
> werden können.

### Beispiele

Siehe auch:
[https://codingdavinci.de/de/projekte](https://codingdavinci.de/de/projekte)
für über 150 bereits erstellte Projekte im Rahmen des Wettbewerbs (seit 2014)
