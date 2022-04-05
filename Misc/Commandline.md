# Commandline

Examples of problems to solve with command line tools.


* Convert a PNG image to a JPG
* Find files
* Concatenate two PDF files
* Crawl web pages
* Download a list of URLs given in a file
* On which weekday did the millenium start?
* Find first names starting with "Ju" and ending with "a"
* Random selection of ten names containing the letter "y"

## Convert a PNG image to a JPG

```
$ convert sample.png sample.jpg
```

## Find files

* Create a file containing all path to files ending with ".txt" in the current
  directories (and all its subdirectories)

```
$ find . -name "*.txt"
```

## Concatenate two PDF files

```
$ pdfjam -o combined.pdf Misc/Files/go-study.pdf Misc/Files/p6-zobel.pdf
```

## Find abstract for the article with DOI 10.1145/357980.358021

```
$ curl -s https://api.crossref.org/works/10.1145/357980.358021 | jq -rc .message.abstract | fold -s
```

## Find author and title for a DOI and format as TSV

```
$ curl -s https://api.crossref.org/works/10.1145/357980.358021 | jq -rc '.message | [.title[], .author[0].given + " " + .author[0].family] | @tsv'
```

## Download a youtube video

```
$ youtube-dl https://www.youtube.com/watch?v=RU0wScIj36o
```

## Pretty print an XML document

```
$ curl -s https://www.fzt.haw-hamburg.de/pers/Scholz/Repository1.xml | xmllint --format -
```

## Crawl web pages

Crawl web pages and save them to a file.

```
$ wget -rkc --warc-file https://www.zeit.de/index
```

Other example (2GB+):

```
$ wget -rkc --warc-cdx --warc-file showcase https://showcase.design.haw-hamburg.de/
```

## Download a list of URLs given in a file

> Someone gives you a file with a list of URLs? How do you download all files?

```
$ wget -i urls.txt
```

## On which weekday did the millenium start?

> Saturday

```
$ cal 1 2000
```

## Find first names starting with "Ju" and ending with "a"

```
$ curl -sL https://osf.io/d2vyg/download | awk -F , '{print $2}' | tr -d '"' | sort -u | grep '^Ju.*a$'
```

* [explainshell](https://explainshell.com/explain?cmd=curl+-sL+https%3A%2F%2Fosf.io%2Fd2vyg%2Fdownload+%7C+awk+-F+%2C+%27%7Bprint+%242%7D%27+%7C+tr+-d+%27%22%27+%7C+sort+-u+%7C+grep+%27%5EJu.*a%24%27)

## Random selection of ten names containing the letter "y"

```
$ curl -sL https://osf.io/d2vyg/download | awk -F , '$2 ~ /.*y.*/ {print $2}' | tr -d '"' | sort -u | shuf -n 10
```

