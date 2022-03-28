# Virtual Machine

A virtal machine (vm) image for LV2.2/2022 for experimentation.

* Username: lv22
* Password: lv22

The VM is based on a minimal [Ubuntu 20.04.4 LTS](https://ubuntu.com/download/desktop) (iso sha1: cd90ca5e95a4479cb1e31402988d49357e4ac261).

## How to use

* [ ] Download [VirtualBox](https://en.wikipedia.org/wiki/VirtualBox) open source
  virtualization software for your operating system (e.g. MacOS, Windows,
  Linux, ...): [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads) -- learn more about what VirtualBox is on Wikipedia: [VirtualBox](https://en.wikipedia.org/wiki/VirtualBox), [Hypervisor](https://en.wikipedia.org/wiki/Hypervisor)
* [ ] Download virtual machine image for this course from: []()...
* [ ] Start VirtualBox and import appliance


## Software Installed

* [x] code editor, e.g. [VS Code](https://code.visualstudio.com/) - including plugins for Python, HTML, CSS
* [x] firefox, google chrome
* [x] extra: bat, procs, dust

Packages:

* bash-completion
* bash-doc
* bzip2
* curl
* emacs
* git
* git-extras
* git-gui
* golang
* golang-doc
* hollywood
* htop
* hugo
* ipython3
* jq
* jupyter
* libxml2-dev
* libxml2-utils
* links
* moreutils
* nano
* ncdu
* p7zip
* pandoc
* pigz
* python3
* python3-imageio
* python3-nltk
* python3-pandas
* python3-pandocfilters
* python3-requests
* python3-scrapy
* ranger
* rar
* screen
* ssh
* tig
* tmux
* tree
* unzip
* vim
* wget
* xsltproc
* xzip
* yaz
* yaz-doc
* zstd

Additional setup:

```
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Additional installations:

```
$ go install github.com/miku/metha/cmd/...@latest
```


## Your VM

This is your experimental VM. It runs in a sandbox, you can hardly break
anything. There is always a fresh copy to start over (if you need).

