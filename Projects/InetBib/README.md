# InetBib Analyse

* Mai 1994 an der Universitätsbibliothek Dortmund ins Leben gerufen
* Die Liste enthält über 9400 eingetragene E-Mailadressen (März 2019).

> Mittlerweile gehört das Internet zum Alltag, aber um
> Organisationsübergreifend effizient damit umgehen zu können braucht man eine
> Kommunikationsplattform. Diese Plattform stellt INETBIB für die Bibliotheken
> dar.

* [https://www.inetbib.de/was-ist-inetbib/](https://www.inetbib.de/was-ist-inetbib/)

Analyse von 70000 Nachrichten auf InetBib.

* Wie viele Nachrichten pro Jahr?
* Verteilung der Aktivität?
* Erwähnung von Institutionen?
* Frequenz von Begriffen


# Steps

## Data Acquisition

```
$ python generate_urls.py > urls.txt
$ wget -i urls.txt
```
