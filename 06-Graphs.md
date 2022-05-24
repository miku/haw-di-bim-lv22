# Graphs and Query Languages

> SPARQL Protocol And RDF Query Language

## Graph

A graph is a set of nodes and edges.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/320px-6n-graf.svg.png)

Examples:

* cities and roads
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

