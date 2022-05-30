# Cheetsheet Coding

A few common things, a reference. Other, helpful projects:

* [Online man pages](https://man7.org/linux/man-pages/index.html)
* [tldr](https://tldr.sh/)
* [explainshell](https://explainshell.com/)

## Command Line

We are using the Unix/Linux flavor. Other terms used for command line:
[terminal](https://en.wikipedia.org/wiki/Computer_terminal#Text_terminals) or
[shell](https://en.wikipedia.org/wiki/Shell_(computing)). 

### Help

* manual pages
* info documents

Examples:

```
$ man man
```

Search for a specific term in manual pages:

```
$ man -k "absolute path"
canonicalize_file_name (3) - return the canonicalized absolute pathname
pwd (3tcl)           - Return the absolute path of the current working directory
realpath (3)         - return the canonicalized absolute pathname
```

Online man pages: [https://man7.org/linux/man-pages/index.html](https://man7.org/linux/man-pages/index.html)

```
$ info coreutils 
```

The info format is a text format (see e.g. `/usr/share/info/*.info*`).

### List files in a directory

```
$ ls
```

Long, human readable format:

```
$ ls -la
```

### Create an empty file

```
$ touch notes.txt
```

### Change directory

* a path with out leading slash is a *relative* path
* a path with a leading slash is called an *absolute* path
* ".." is the parent path
* "." is the current path
* "/" is the root directory and has no parent

```
$ cd /tmp
```

To find the absolute path for any file, you can use `realpath`:

```
$ realpath ~/../../etc/passwd
/etc/passwd
```

Change back home:

```
$ cd
```

### Create directory

```
$ mkdir
```

### Remote directory

```
$ rmdir
```

### Delete file

```
$ touch dummy
$ rm dummy
```

### Show list of processes

```
$ ps
```

Show all processes with username:

```
$ ps -ef
```

Notably, each process has a process identifier (PID), which can be used to force stop a process.

### Stop a program with a signal

The `kill` command sends a signal. There are different, specified signals
available with fixed semantics:
[](https://www-uxsup.csx.cam.ac.uk/courses/moved.Building/signals.pdf)

```
$ kill -9 1234
```

### Browse the web from the command line

links is a terminal browser.

```
$ links https://haw-hamburg.de
```

You can convert any HTML to text with links:

```
$ links -dump https://haw-hamburg.de
```

## Git

A minimal life-cycle would be:

```
$ mkdir myproject
$ cd myproject
$ git init 
$ echo 'Hello' > README.md
$ git add .
$ git commit -m "initial import"
$ git log
```

* init initializes a repository - remember, *everything is local*
* commit records a set of changes with a message

## Python

## Pandas

