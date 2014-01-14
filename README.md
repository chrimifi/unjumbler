unjumbler
=========

A script for solving jumbles, created for a coding challenge.

Usage
--------

Place the dictionary you want to use in the directory you'll run from. Name it "dictionary". It should be a list of valid words, one per line.

Run the script, and it will prompt you for a jumble to solve. This script is case sensitive.

Notes on efficiency
--------

This was a pedagogical exercise with strict rules: no modules, no imports. Hence, it is not maximally efficient, and
some design decisions may seem odd (e.g. prompting for the jumble instead of using command line arguments).