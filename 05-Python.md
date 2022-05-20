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

## Example Reuse

* generating HTML

> for writing HTML (or any textual document) we can write the raw document or
> we can use some template library

* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/templates/#synopsis) template example
* [Code/TemplateExample/](Code/TemplateExample)

## Program Anatomy

* imports
* functions
* other modularization units, like classes
* comments

Python is a dynamically typed language. We have less to write but may not see,
what the type of a variable is (and what operations it supports).

Execution visualization:

* [https://pythontutor.com/](https://pythontutor.com/)

Python code runs:

* in a terminal (or a shell)
* in a python repl
* in a jupyter notebook
* in the browser (e.g. [pyscript](https://github.com/pyscript/pyscript))
* embedded in another application (e.g. [blender](https://docs.blender.org/api/current/info_overview.html#python-in-blender))

## More Examples

### Researching Code Solutions

* [Python Documentation](https://docs.python.org/3/library/index.html)
* [Questions Tagged Python](https://stackoverflow.com/questions/tagged/python)

Try things out in a REPL!

* [IPython](https://ipython.org/documentation.html)

### Review and Tasks

* [Code/HelloWorld/](Code/HelloWorld/)
* [Code/Variables/](Code/Variables/)
* [Code/Lists/](Code/Lists/)
* [Code/Dictionary/](Code/Dictionary/)
* [Code/MARC21/](Code/MARC21/)
* [Code/WordFrequencies/](Code/WordFrequencies/)

### Reading code

What are the following code snippets doing?

> [Code/Labs/](Code/Labs)

### Mob Programming

Let's try to code together.

#### Sequence 1

1. Create a variable that holds a string
2. Create a variable that holds an integer
3. Can we add them together?
4. How can we iterate over the characters in a string?
5. How can we uppercase every vowel?
6. How could we uppercase every second letter?

#### Sequence 2

1. Create a variable that holds a list of strings
2. Create a another variable that holds a list of string (with some overlap to 1.)
3. Write a function that takes two lists as arguments and returns a list of the common elements.
4. Is there a better way to do this?

#### Sequence 3

1. Create a dictionary with string keys and values, e.g. map countries to capitols, like "France" -> "Paris", "Germany" -> "Berlin", ...
2. Iterate over all keys and values and print out one country and capital per line, separated by a tab character.


#### Sequence 4

1. Create a variable that holds a list of strings
2. Iterate over the list and print out one string per line
3. Prefix each line with the current date, e.g. in "2022-05-17" format (make it so that each time the script is run, the current date is used)

#### Sequence 5

Fibonacci sequence.

The fibonacci sequence is a sequence of numbers ((https://oeis.org/A000045)[https://oeis.org/A000045]).

> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, ...

Write a function that given a number n, returns the nth number in the fibonacci sequence.

Example:

    >>> fibonacci(5)
    5
    >>> fibonacci(10)
    55

### Discussion

Problem: What was the average number of visitors per exhibition per German state in the year 2016?

> Discuss possible way to answer this question.
