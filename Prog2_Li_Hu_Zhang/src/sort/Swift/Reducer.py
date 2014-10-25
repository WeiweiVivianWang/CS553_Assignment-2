#! /usr/bin/python
# -*- coding: utf-8 -*-

from operator import itemgetter
import sys
filepath = sys.argv[1]
word = None
dict = {}
inputfile = open(filepath, 'rU')
for line in inputfile:
    line = line.strip()
    word, count = line.split('\t', 1)
    if dict.has_key(word):
        dict[word] = dict.get(word)+int(count)
    else:
        dict[word] = 1
order_dict = sorted(dict.items(), key = lambda d:d[1])
for key, value in order_dict:
    print "%s\t%s" % (key, value)
