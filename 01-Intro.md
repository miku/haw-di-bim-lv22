# Intro

![](https://i.imgur.com/78kHiAq.png)

See: [Introduction to computer data processing](https://archive.org/details/introductiontoco0000wuma_k0n6/page/n5/mode/2up) (1975)

> Today computers touch the lives of nearly everyone.

## Motivation

Programming is a generic technical skill, independent of any particular language or platform.

### Reasons to learn programming

* Programming helps you **understand computers**. The computer is only a tool. If
  you learn how to write simple programs, you will gain more knowledge about
  how a computer works.
* Writing a few simple programs increases your confidence level. Many people
  find great personal satisfaction in creating a set of instructions that **solve
  a problem**.
* Learning programming lets you find out quickly whether you like programming
  and whether you have the analytical turn of mind programmers need. Even if
  you decide that programming is not for you, understanding the process certainly
  will increase your appreciation of what programmers and computers can do.

Source: [https://homepage.cs.uri.edu/faculty/wolfe/book/Readings/Reading13.htm](https://homepage.cs.uri.edu/faculty/wolfe/book/Readings/Reading13.htm)

### Definitions

Mirriam-Webster defines programming:

> the planning, scheduling, or performing of a program

First known use 1896.

Other:

> Computer programming is the process of performing a particular computation
> (or more generally, accomplishing a specific computing result), usually by
> designing/building an executable computer program. Programming involves tasks
> such as analysis, generating algorithms, profiling algorithms' accuracy and
> resource consumption, and the implementation of algorithms (usually in a
> chosen programming language, commonly referred to as coding).

From:

* [https://web.archive.org/web/20200429195646/https://yearofcodes.tumblr.com/what-is-coding](https://web.archive.org/web/20200429195646/https://yearofcodes.tumblr.com/what-is-coding)
* [https://web.archive.org/web/20200429195958/https://yearofcodes.tumblr.com/what-is-programming](https://web.archive.org/web/20200429195958/https://yearofcodes.tumblr.com/what-is-programming)

Computers compute, but:

> Computers were invented to *compute*: to solve *complex mathema-
tical problems,* as the dictionary still defines that word. They still do
that, but that is not why we are living in an *Information Age.* That
reflects other things that computers do: **store and retrieve data**, **manage
networks of communications**, **process text**, **generate and manipulate
images and sounds**, **fly air and space craft**, and so on.


![](https://upload.wikimedia.org/wikipedia/commons/5/52/Monitor_Commodore_CBM_3016_with_BASIC_program-0309.jpg)


## Overview

### 10 Sessions

* [ ] L01 Intro
* [ ] L02 Collaboration with Git
* [ ] L03 Web Standards
* [ ] L04 Static site generators: a lean approach to content management
* [ ] L05 Python Programming
* [ ] L06 Microframework (HTML template; JSON HTTP APIs)
* [ ] L07 Data
* [ ] L08 Graphs
* [ ] L09 SPARQL
* [ ] L10 Project discussions

### LV2.2

From [LV2.2: Werkstatt Coding/Webtechnologien](https://www.haw-hamburg.de/fileadmin/DMI-I/PDF/BIM/Modulhandbuch_BIM_2021-02-24.pdf#page=7):

*  Web Protokolle und Standards, Anwendungs-Architekturen (z.B.  Client-Server,
   verteilte Systeme, dienstorientierte Architekturen, Web-Services) sowie
standardisierte Webtechnologien (HTML, CSS, JSON, RDF, Web APIs) und de-facto
Webframeworks unter Anleitung nutzen, die Anforderungen von Suchmaschinenopti-
mierung (Web Accessibility und Mehrsprachigkeit (Web I18N)) technisch erfassen
und berücksichtigen, (**L03**, **L05**, **L06**)
*  aktuelle Entwicklungen der Web- und Internettechnologie kennen und ihre
   Relevanz einschätzen, (**L02**, **L10**)
* die Entwicklung und ggf. cloud-basierte Bereitstellung von Webauftritten
  via modularisierter Content Management Systeme an einem praktischen Beispiel
durchführen, (**L04**)
* Vorgehensweisen für die Anreicherung von Webinhalten mit strukturierten,
  semantischen und graph-basierten, ggf. öffentlich verfügbaren Daten kennen
und anwenden lernen, (**L07**, **L08**, **L09**)
* auf diese Weise die Grundkenntnisse der Programmierung anhand eigener
  Projekte festigen und vertiefen, um die Anforderungen an die Bereitstellung
von semantisch angereicherten Informationen im Rahmen des Berufsfeldes
"Bibliothek/Information" für den praktischen Einsatz zu bewerten und
innovativ weiterzuentwickeln. (**Project**)

## Admin Things

* [ ] 2 small take-home exercises (2-3 weeks to complete; given out in L02 and L05)
* [ ] 1 expose (1/2 page) for final project (due L05)
* [ ] 1 final (programming) project ("Projektarbeit", various options); due end of semester

Project categories:

* 1. Create a novel dataset
* 2. Publication Pipeline
* 3. Combine and analyze multiple data sets
* 4. A small (web) application
* 5. Coding da Vinci Hackathon submission

## Workshop

![https://pixabay.com/photos/workshop-old-tools-factory-5517773/](workshop-g30288d7ce_1280.jpg)

In a programming workshop, we may deal with the following things.

* material: data
* tools: applications, command line tools, programming languages
* result: automation, scale, tools

Remember: In the best case, a workshop invites you to get acquainted with a few
tools and techniques. There is a preferred way of *using* some tools, but no
right or wrong in a strict sense. Please keep that in mind.

### Example Problems

A biased list of smaller workpieces.

> A gist snippet.

* Problem: I want to test an optimization algorithms.
* Approach: Use a non-convex function
* Solution: Rastrigin
* Snippet: [https://gist.github.com/miku/fca6afe05d65302f14c2b6f5242458d6](https://gist.github.com/miku/fca6afe05d65302f14c2b6f5242458d6)

> Coding da Vinci 2018, input session.

* Problem: I want to understand what this dataset it about
* Approach: Load the data and visualize it
* Solution: Jupyter Notebook
* Notebook: [CSV, HMT](https://github.com/miku/sundaypython/blob/master/notebooks/04%20Working%20with%20CSV.ipynb), [Muka-Statistik](https://github.com/miku/sundaypython/blob/master/notebooks/05%20Another%20CSV%20dataset.ipynb), ...

> A citation project.

* Problem: Not all catalog metadata contains explicit DOI values.
* Approach: Try to parse DOI values with regular expressions.
* Solution: Command line tool to find DOI in catalog data.
* Program: [doisniffer](https://github.com/slub/labe/tree/main/go/ckit#doisniffer)

> A list of all ISSN.

* Problem: I want to have a list of all ISSN.
* Approach: Find authorative data source
* Solution: Scrape data from issn.org sitemaps
* Program: [issnlister](https://github.com/miku/issnlister)

> Get all data out of a SOLR index.

* Problem: I want to have a file representation of a SOLR index for local processing.
* Approach: Export the data.
* Solution: Use the cursor mechanism of SOLR to get data our efficiently.
* Program: [solrdump](https://github.com/ubleipzig/solrdump)

> Publish a blog.

* Problem: I want to document activities of a user group.
* Approach: Use a blog.
* Solution: Use a static site generator, hugo.
* Site: [https://golangleipzig.space/](https://golangleipzig.space/)

Depending on the area of your work, your set of problems, approaches and tools will look different.

## Virtual Machine

Our first workbench, beside your own computer, will be a virtual machine.

* [ ] Install VirtualBox
* [ ] Download the VirtualBox image for LV2.2
* [ ] Start VirtualBox and boot image

This is an [Ubuntu 20.04.4 LTS](https://wiki.ubuntu.com/Releases) OS with a few
programs pre-installed.

## Linux

Ubuntu is a Linux distribution.

> Linux is a family of open-source Unix-like operating systems based on the
> Linux kernel, an operating system kernel first released on September 17,
> 1991, by Linus Torvalds. Linux is typically packaged in a Linux distribution.

From: [https://en.wikipedia.org/wiki/Linux](https://en.wikipedia.org/wiki/Linux)

## Terminal

![](https://user-images.githubusercontent.com/121322/32070715-163a1c94-ba42-11e7-80bb-41fbf10fc634.gif)

> A computer terminal is an electronic or electromechanical hardware device
> that can be used for entering data into, and transcribing data from, a
> computer or a computing system. The teletype was an example of an early day
> hardcopy terminal, and predated the use of a computer screen by decades.

![](https://upload.wikimedia.org/wikipedia/commons/5/50/Bundesarchiv_Bild_183-2008-0516-500%2C_Fernschreibmaschine_mit_Telefonanschluss.jpg)

## Command Line

* In the beginning ... (Essay, [Text](https://web.stanford.edu/class/cs81n/command.txt), [Wikipedia](https://en.wikipedia.org/wiki/In_the_Beginning..._Was_the_Command_Line))
* [Unix Cheat Sheet](http://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/unix_cheatsheet.html), [1 page](https://files.fosswire.com/2007/08/fwunixref.pdf)
* Interactive cheat sheet: [https://github.com/denisidoro/navi](https://github.com/denisidoro/navi)

More cheat sheets and references:

* Cheat Sheet:
  [https://www2.icp.uni-stuttgart.de/~icp/mediawiki/images/b/bd/Sim_Meth_I_T0_cheat_sheet_10_11.pdf](https://www2.icp.uni-stuttgart.de/~icp/mediawiki/images/b/bd/Sim_Meth_I_T0_cheat_sheet_10_11.pdf)
([archived](http://web.archive.org/web/20210416015839/https://www2.icp.uni-stuttgart.de/~icp/mediawiki/images/b/bd/Sim_Meth_I_T0_cheat_sheet_10_11.pdf))
* [Unix Command List](https://www.tjhsst.edu/~dhyatt/superap/unixcmd.html)
* [Die Top 50 universellen UNIX-Befehle](http://web.archive.org/web/20210613165139/https://www.computerweekly.com/de/ratgeber/Die-Top-50-universellen-UNIX-Befehle)
