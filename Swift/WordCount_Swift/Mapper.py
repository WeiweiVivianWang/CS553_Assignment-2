#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import argparse

class Mapper():
    def __init__(self):
        self.wordDict = dict()
        self.skip = list()
        return
 
    def map(self, fline):
        mapList = re.split('[ \t\n\[\],.;=+\'\"()|<>-?!]+', fline)
        for term in mapList:
            self.collect({term : 1})
        return

    def collect(self, item):
        assert type(item) == type({})
        for i in item.items():
            if self.wordDict.has_key(i[0]):
                self.wordDict[i[0]] += i[1]
            else:
                self.wordDict[i[0]] = i[1]
        return

    def writeToFile(self, file = 'output'):
        f = open(file, mode='w')
        tmp = sorted(self.output.items(), key=lambda x: x[1], reverse=True)
        for i in tmp:
            if i[0] == '' or i[0] == '\n': continue
            f.write('%s\t%d\n' % (i[0], i[1]))
        f.close()
        return

if __name__ == '__main__':
    mapper = Mapper()
    
    parse = argparse.ArgumentParser()
    parser.add_argument('--inputfile', type = str, help = 'Inputfile.')
    parser.add_argument('--pid', metavar = 'NUM', type = int, help = 'ID')

    filePath = os.path.abspath(args.inputfile)
    fileSize = os.path.getsize(filePath)

    fstream = open(filePath, 'r')
    pos = fstream.tell()
    
    while pos < fileSize:
        fline = fstream.readline()
        mapper.map(fline)
        pos = fstream.tell()

    ostream = os.path.abspath('temp') + '/' + ('tmp_mapper_%d' % args.pid)
    mapper.writeToFile(file = ostream)
