from pymarc import MARCReader

with open('marc.dat', 'rb') as fh:
    reader = MARCReader(fh)
    for record in reader:
        print(record.title())

# The pragmatic programmer : from journeyman to master /
# Programming Python /
# Learning Python /
# Python cookbook /
# Python programming for the absolute beginner /
# Web programming : techniques for integrating Python, Linux, Apache, and MySQL /
# Python programming on Win32 /
# Python programming : an introduction to computer science /
# Python Web programming /
# Core python programming /
# Python and Tkinter programming /
# Game programming with Python, Lua, and Ruby /
# Python programming patterns /
# Python programming with the Java class libraries : a tutorial for building Web
# and Enterprise applications /
# Learn to program using Python : a tutorial for hobbyists, self-starters, and all
# who want to learn the art of computer programming /
# Programming with Python /
# BSD Sockets programming from a multi-language perspective /
# Design patterns : elements of reusable object-oriented software /
# Introduction to algorithms /
# ANSI Common Lisp /
