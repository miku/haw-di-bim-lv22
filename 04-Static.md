# Static Site Generators

Static site generators (SSG) have become a popular choice to manage content.

It became popular because:

* more people learned a markup language beside HTML, like textile or markdown
* text is easier to version control
* easier deployment
* fewer resources to maintain
* better security

Many choices:

* [A List of Static Site Generators for Jamstack Sites](https://jamstack.org/generators/)

> JavaScript, APIs, and Markup (JAM) -- [https://jamstack.wtf/](https://jamstack.wtf/)

## Classic CMS

* more complex to setup
* higher maintenance costs
* larger attack surface

Many cases of classic CMS can be addressed by SSG.

## How an SSG works

* content
* templates
* tools that combine content and templates
* various add-ons, themes (depending on project)

Instead of using an application (like wordpress), we use mostly static files,
which can be versioned. The deployable site can be generated, typically with a
single command.

## Example: Zola

* [https://www.getzola.org/](https://www.getzola.org/)

### Installation

* [https://www.getzola.org/documentation/getting-started/installation/](https://www.getzola.org/documentation/getting-started/installation/)

### A First Site

* [https://www.getzola.org/documentation/getting-started/overview/#first-steps-with-zola](https://www.getzola.org/documentation/getting-started/overview/#first-steps-with-zola)

### Local Server

```
$ zola serve
```

----

## Zola: Steps

```
$ zola init zolademo
$ cd zolademo
$ zola serve
```

Going to [http://127.0.0.1:1111/](http://127.0.0.1:1111/) brings up an empty site.

![](static/zolaup.png)

Stop zola (or many other programs) with [CTRL-C](https://en.wikipedia.org/wiki/Control-C).

