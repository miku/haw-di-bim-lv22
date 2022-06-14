# Data, Graphs and Query Languages

## Data Format

Most common structured data formats:

* JSON, [https://www.json.org/](https://www.json.org/)

> JSON (JavaScript Object Notation) is a lightweight data-interchange format. It
> is easy for humans to read and write. It is easy for machines to parse and
> generate. It is based on a subset of the JavaScript Programming Language
> Standard ECMA-262 3rd Edition - December 1999. JSON is a text format that is
> completely language independent but uses conventions that are familiar to
> programmers of the C-family of languages, including C, C++, C#, Java,
> JavaScript, Perl, Python, and many others. These properties make JSON an ideal
> data-interchange language.

* XML

XML was *hot* in the early 2000s but it has since then reached a [*plateau of productivity* ](https://www.google.com/search?q=plateau+of+productivity&tbm=isch)

## Graph

A graph is a set of nodes and edges.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/320px-6n-graf.svg.png)

It comes in many different flavors:

* directed
* undirected
* acyclic

One I use daily in various forms is a
[DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (e.g. in git,
citation graphs, job scheduling, ...).

Examples:

* cities and roads
* papers and citations
* people and their friends, social networks
* entities and their relations

## RDF

> RDF is a standard model for data interchange on the Web.

A primer on RDF: [https://www.w3.org/TR/2014/NOTE-rdf11-primer-20140624/](https://www.w3.org/TR/2014/NOTE-rdf11-primer-20140624/)

> The Resource Description Framework (RDF) is a framework for expressing
> information about resources. Resources can be anything, including documents,
> people, physical objects, and abstract concepts.

> RDF is intended for situations in which information on the Web needs to be
> processed by applications, rather than being only displayed to people. RDF
> provides a common framework for expressing this information so it can be
> exchanged between applications without loss of meaning.

```
<Bob> <is a> <person>.
<Bob> <is a friend of> <Alice>.
<Bob> <is born on> <the 4th of July 1990>.
<Bob> <is interested in> <the Mona Lisa>.
<the Mona Lisa> <was created by> <Leonardo da Vinci>.
<the video 'La Joconde à Washington'> <is about> <the Mona Lisa>
```

More information:

* [RDFa](https://rdfa.info/) - RDF in HTML, [tutorial](https://coffeecode.net/rdfa/codelab/)

## SPARQL

> SPARQL Protocol And RDF Query Language

* https://www.w3.org/2009/Talks/0615-qbe/

## Wikidata

* [https://www.wikidata.org](https://www.wikidata.org)

> Wikidata is a free and open knowledge base that can be read and edited by both humans and machines.

Wikidata acts as central storage for the structured data of its Wikimedia
sister projects including Wikipedia, Wikivoyage, Wiktionary, Wikisource, and
others.

* items
* properties, [list](https://www.wikidata.org/wiki/Wikidata:List_of_properties/all_in_one_table)

Try it out: [https://query.wikidata.org/](https://query.wikidata.org/)
