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

## Find first names starting with "Ju" and ending with "a"

```
$ curl -sL https://osf.io/d2vyg/download | awk -F , '{print $2}' | tr -d '"' | sort -u | grep '^Ju.*a$'
```

* [explainshell](https://explainshell.com/explain?cmd=curl+-sL+https%3A%2F%2Fosf.io%2Fd2vyg%2Fdownload+%7C+awk+-F+%2C+%27%7Bprint+%242%7D%27+%7C+tr+-d+%27%22%27+%7C+sort+-u+%7C+grep+%27%5EJu.*a%24%27)
