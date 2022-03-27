# Collaboration

Today:

* [ ] How to collaborate with software?
* [ ] What is git? And github, gitlab, and other websites?
* [ ] Basic ideas and commands

## Version Control

> An important problem in program development and maintenance is version
> control, i.e. the task of keeping a software system consisting of many
> versions and configurations well organized. -- [Rcs — a system for version control](https://fatcat.wiki/release/j66jbj3safaclbcoe3a7lujik4) (1985)

A common topic in software development, but increasingly discovered by other fields.

> Many scientists write code as part of their research. Just as experiments are
> logged in laboratory notebooks, it is important to document the code you use
> for analysis. However, a few key problems can arise when iteratively
> developing code that make it difficult to document and track which code
> version was used to create each result. First, you often need to experiment
> with new ideas, such as adding new features to a script or increasing the
> speed of a slow step, but you do not want to risk breaking the currently
> working code. One often-utilized solution is to make a copy of the script
> before making new edits. However, this can quickly become a problem because
> it clutters your file system with uninformative filenames, e.g., `analysis.sh`,
> `analysis_02.sh`, `analysis_03.sh`, etc. It is difficult to remember the
> differences between the versions of the files and, more importantly, which
> version you used to produce specific results, especially if you return to the
> code months later. Second, you will likely share your code with multiple lab
> mates or collaborators, and they may have suggestions on how to improve it.
> If you email the code to multiple people, you will have to manually
> incorporate all the changes each of them sends.

> Fortunately, software engineers have already developed software to manage
> these issues: version control. A version control system (VCS) allows you to
> track the iterative changes you make to your code. Thus, you can experiment
> with new ideas but always have the option to revert to a specific past
> version of the code you used to generate particular results. -- [10.1371/journal.pcbi.1004668](https://doi.org/10.1371/journal.pcbi.1004668)

## Git

* a tool for [version control](https://en.wikipedia.org/wiki/Version_control)
* first released in 2005, originally written by Linus Torvalds
* has been widely [adopted](https://en.wikipedia.org/wiki/Git#Adoption) in the past decade

Usage numbers (estimates):

> In 32% in 2012 (eclipse software foundation survey) used git as primary
> version control system; another survey from Stack Overflow reports: 69.3% in
> 2015, and 87.2% in 2018.

For many projects, the whole industry shifted from CVS and subversion
(centralized systems) to git (decentralized).

From an [early site](http://web.archive.org/web/20080618074823/http://git.or.cz/):

> Git is an open source version control system designed to handle very large
> projects with speed and efficiency, but just as well suited for small
> personal repositories; it is especially popular in the open source community,
> serving as a development platform for projects like the Linux Kernel, WINE or
> X.org.

> Git falls in the category of distributed source code management tools,
> similar to e.g. Mercurial or Bazaar. Every Git working directory is a
> full-fledged repository with complete history and full revision tracking
> capabilities, not dependent on network access or a central server. Still, Git
> stays extremely fast and space efficient.

## GitHub, GitLab, SourceHut, and others

* first: you can use git without any of these ("git != github")
* hosting sites for git repositories
* early snapshot of GitHub (2008): [http://web.archive.org/web/20080705211438/http://github.com/](http://web.archive.org/web/20080618201317/http://github.com/)

> What is it?

> Not only is Git the new hotness, it's a fast, efficient, distributed version
> control system ideal for the collaborative development of software.

> GitHub is the easiest (and prettiest) way to participate in that
> collaboration: fork projects, send pull requests, monitor development, all
> with ease.

GitHub was an early site (2008), but others followed. Most importantly, GitLab
(2014), which is used by many academic institutions (i.e. in
[Germany](https://www.google.com/search?q=inurl%3Agit+site%3Ade+%22universit%C3%A4t%22)).
Other open source tools are SourceHut, Gitea, Gogs, ...

## Goals

* keep track of work (text)
* enable contributions

In the early 2010s, git started to gain popularity; through sites like GitHub,
open source got a lot of attention.

Today, many large projects are developed on GitHub.

* [Uses of git and github in GLAM and elsewhere](https://github.com/miku/lc-extra#git-use-cases-in-glam-and-elsewhere)

Example pull request (live):

* [https://github.com/hbunke/BibsOnGitHub](https://github.com/hbunke/BibsOnGitHub) -- may want to change "Persons" to "People" ...


## General Ideas

* it is ok to not publish perfect projects immediately all the time
* iteration is important
* documenting features, so others can understand, whether a project is useful
* separate specific problems and solutions from more general ones

Examples of more generic projects:

* [pymarc](https://pypi.org/project/pymarc/)
* [VuFind](https://vufind.org/vufind/)
* [zek](https://github.com/miku/zek) -- [online](https://www.onlinetool.io/xmltogo/)
* ...

## How it works

Some terminology:

* repository - a directory (and everything below it) that is version controlled with git
* commit - the unit of change; contains changes to one or more files

Cheat sheets:

* [https://education.github.com/git-cheat-sheet-education.pdf](https://education.github.com/git-cheat-sheet-education.pdf)
* [https://about.gitlab.com/images/press/git-cheat-sheet.pdf](https://about.gitlab.com/images/press/git-cheat-sheet.pdf)

### Create a repository

```
$ mkdir myproj
$ cd myproj
$ git init
```

### Add and edit a file

In `myproj` add a file, e.g. named "README.md" - write something into that file.

```
$ echo "Hello" > README.md
$ git status
```

Git noticed the file.

### Add and commit

```
$ git add README.md
$ git commit -m "my first commit"
```

### Showing the history

Various way to see the history, but the very first command would be:

```
$ git log
```

### Checking the status again

The git status command is purely informational.

```
$ git status
```

### Wrap up: Local operations

That is the basic local workflow. You can build up a local history that way.


## Remote operations

* each repository is independent of the others (and contains the whole project history) - this is why it is called decentralized
* remote operations can synchronize the history one (often) one, but possibly more repositories

