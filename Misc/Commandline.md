# Commandline

Examples of problems to solve with command line tools.

* Crawl web pages

## Crawl web pages

Crawl web pages and save them to a file.

```
$ wget -rkc --warc-file https://www.zeit.de/index
```

```
$ wget -rkc --warc-cdx --warc-file showcase https://showcase.design.haw-hamburg.de/
```

## On which weekday did the millenium start?

> Saturday

```
$ cal 1 2000
```

## Download a list of URLs given in a file

> Someone gives you a file with a list of URLs? How do you download all files?

```
$ wget -i urls.txt
```


