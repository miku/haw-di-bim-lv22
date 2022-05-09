# Python Crash Course

> My younger son said "coding is basically just ifs and for loops."--
> [1466934223831506951](https://twitter.com/ID_AA_Carmack/status/1466934223831506951)

Essentials:

* [Library Carpentry Python Intro](https://librarycarpentry.org/lc-python-intro/)

## Exposure

Some concepts that may have been used in the past:

* XML validity check, e.g. via `xmlschema`
* exception handling
* importing libraries, via `import`
* reading xml with `pandas`
* data types: strings, lists, nodes
* writing to files
* working with XML and etree
* variables
* loops

## Why Python?

Have you tried any of these?

```python
>>> import antigravity
>>> import this
```

> The best part of programming is the triumph of seeing the machine do
> something useful. -- [Testimonial on Automate the Boring Stuff with
> Python](https://automatetheboringstuff.com/).

In 2022, we have a unprecedented amount of high quality code, open source code
available - and programming has become both writing code and understanding what
existing project may solve or help solve a problem.

There are:

* over 60K curated software packages in a current Ubuntu installation -- [docs](https://ubuntu.com/server/docs/package-management)
* as of 05/2022, the Python Package index has over [365000 packages](https://pypistats.org/) (with 2.5B+ interactions per month)

Some numbers for popular packages ([Open source now runs the world](https://www.wired.com/2016/08/open-source-won-now/)):

* also: [top stats](https://pypistats.org/top) -- the most downloaded package
  per month, with 288M downloads, translates to about over 110 installs per second

```
$ pypistats overall requests
| category        | percent |   downloads |
|:----------------|--------:|------------:|
| with_mirrors    | 100.00% | 912,864,628 |
| without_mirrors |  99.72% | 910,267,154 |
| Total           |         | 912,864,628 |

Date range: 2021-11-09 - 2022-05-08

tir@trieste:~/code/miku/rclone [git:ia-wt-1168+] $ pypistats overall numpy
| category        | percent |   downloads |
|:----------------|--------:|------------:|
| with_mirrors    | 100.00% | 583,886,833 |
| without_mirrors |  99.62% | 581,658,339 |
| Total           |         | 583,886,833 |

Date range: 2021-11-09 - 2022-05-08

$ pypistats overall pymarc
| category        | percent | downloads |
|:----------------|--------:|----------:|
| with_mirrors    | 100.00% |    56,688 |
| without_mirrors |  87.84% |    49,794 |
| Total           |         |    56,688 |

Date range: 2021-11-09 - 2022-05-08
```

* just curious: [https://pypistats.org/packages/marcx](https://pypistats.org/packages/marcx), [https://pypistats.org/packages/pymarc](https://pypistats.org/packages/pymarc), ...

Examples:

* generating HTML

> for writing HTML (or any textual document) we can write the raw document or
> we can use some template library

* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/templates/#synopsis) template example
* [Code/TemplateExample/](Code/TemplateExample)

## Examples

* [Code/HelloWorld/](Code/HelloWorld/)
* [Code/Variables/](Code/Variables/)
* [Code/Lists/](Code/Lists/)
* [Code/WordFrequencies/](Code/WordFrequencies/)

