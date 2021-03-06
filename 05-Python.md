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

## Python Types

* a variable is declared and assigned a value
* a variable defines the set of possible values (like numbers, strings, a list of numbers, a mapping from strings to numbers, an object representing tabular data, ...)
* each variable has a type - use `type(v)` to check what the type of each variable is

There are a few elementary types: numbers, strings, truth values.

### Numbers

Python has integers and floats and complex numbers

* integers are whole numbers (arbitrary large)
* floats are decimal numbers (double precision, [issues](https://docs.python.org/3/tutorial/floatingpoint.html))

### Strings

* a string is a sequence of characters
* a character is typically a letter, a digit, a punctuation mark, a space, ...
* today, we can express most symbols as a string
* emojis are strings, too ????

### Truth values

* True and False are a distinct type: `bool`
* named after George Boole, author of "The Laws of Thought" (1854)

### None Type

* `None` is a special value that represents the absence of a value
* there is only one value of type `None`

### Compound types

Compound type are typically a collection of other types.

In Python we have

* lists
* tuples
* dictionaries
* sets

> Q: Intuitively, what are the differences between these types? What kind of
> operations could be supported by these types?

### Lists

Lists are a sequence of elements.

* [list](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Tuples

Tuples are like lists but immutable.

* [tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)


### Dictionaries

Dictionaries implement a key-value mapping.

* [dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

### Sets

Sets implements an unordered collection of unique elements.

* [sets](https://docs.python.org/3/tutorial/datastructures.html#sets)

### Custom types

In python, you can define your own types.

For example, you want to model a Course, which has a name, a number of credits:

```python
class Module:
    def __init__(self, name, credits, courses):
        self.name = name
        self.credits = credits
        self.course = courses

class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
```

## Python builtin functions

* builtin function quiz: [builtin functions](https://docs.python.org/3/library/functions.html)

> given the name, what do you expect the function to do?


## Control Structures

* "ifs and for loops"

### Conditions / Jumps

```python
if condition:
    # do something
else:
    # do something else
```

* many things can be used in "condition", but finally we are working with a
  boolean type (the condition is either true of false)

### Loops / Repetition

```python
for element in sequence:
    # do something
```

If we need an iteration index, we can use `enumerate`:

```python
for index, element in enumerate(sequence):
    # do something
```

Sometime, we want to range over integers:

```python
for i in range(10):
    # do something
```

* range is a builtin function to generate a sequence of integers

## Functions

Functions are a way to group code together.

```python
def sum_of_first_n_integers(n):
    """ Returns the sum of the first n integers (a bit verbosely). """
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

s = sum_of_first_n_integers(10)
print(s)
```

* you *define* a function
* you can *call* a function
* [builtin functions](https://docs.python.org/3/library/functions.html) are just functions

> Builtin function quiz: Just reading the name, what do you expect the function to do?

* you can give it a *name* and *parameters*
* there are *positional* and *keyword* parameters
* function can return a value (or they return `None`)

```python
def underline(s, char="."):
    return s + "\n" + char * len(s)


print(underline("Hello World"))
```

## Object Orientation

> Everything in Python is an object.

If we see an "object" in python, we often see a method called on it.

```python
s = "hello world"
print(s.upper())
```

* here "upper" is called a "method of string" - in essence it is a function
  that is called on an object
* the method can return something or manipulate the object

Example: when we call `append` on a list, we are adding a value, but we are not returning anything.

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

#### Sequence 6

Reading JSON data with Python. JSON is a very common, flexible data format. Its
use cases are similar to that of XML. JSON documents maps naturally to Python
data structures.

1. Download example file (best outside of Python, e.g. with curl or wget)
2. Import "json" module 
3. Open file, e.g. with the `with` statement
4. Parse data into a Python data structure

The data contains information about incoming and outgoing media of a library.
There are elements in the data named `incoming` and `outgoing` in the data.

5. Count how many incoming and outgoing are contained in the file.


#### Sequence 7

Word frequency allows us to gather a bit of insight into a text in a statistical
manner. How often does a word appear in a text?

1. Download a text file from Project Gutenberg (e.g. [https://www.gutenberg.org/files/61753/61753-0.txt](https://www.gutenberg.org/files/61753/61753-0.txt))
2. Parse the text into tokens (e.g. split on whitespace)
3. For each token count how often is appears in the text
4. Output a simple two-column list with frequency and token, e.g. like so:

```shell
...
1       hart
1       zusetzen
1       er??ffnete
2       Verhandlung
1       fortzusetzen
1       mildernden
1       h????lichsten
1       woraus
1       Rache
6       Revanche
...
```

Discussion:

* basic and more sophisticated token generation strategies
* better support for counting in the standard library
* sorting within and outside of Python 

### Misc Problems

#### Exhibition visitors

Problem: What was the average number of visitors per exhibition per German state in the year 2016?

> Discuss possible way to answer this question.
