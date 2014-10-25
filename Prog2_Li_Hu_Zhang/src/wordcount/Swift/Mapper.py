#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
filepath = sys.argv[1]
inputfile = open(filepath, 'rU')
for line in inputfile:
    line = line.strip()
    words = line.split()
    for word in words:
        print "%s\t%s" % (word, 1)
