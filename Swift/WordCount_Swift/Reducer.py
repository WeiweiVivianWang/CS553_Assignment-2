#! /usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import os

class Reducer():
    def __init__(self):
        self.wordDict = dict()
        return

    def reduce(self, items):
        self.collect(items)
        return

    def readFileToDict(self, file = 'input'):
        fstream = open(file, 'r')
        m = __import__('csv')
        for key, value in m.reader(fstream):
            self.collect({key : int(value)})
        fstream.close()
        return

    def writeToFile(file = 'output'):
        fstream = open(file, 'w')
        tmp = sorted(self.wordDict.items(), key = lambda x: x[1], reverse = True)
        for i in tmp:
            if i[0] == '' or i[0] == '\n':
                continue
            fstream.write('%s%t%d\n' % (i[0], i[1]))
        fstream.close()
        return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type = str, help = 'Input Folder')
    parser.add_argument('--output', type = str, help = 'Output File')

    reducer = Reducer()

    inputs = os.listdir(os.path.abspath(args.input)
    
    for file in inputs:
        filePath = os.path.join(args.input, file)
        reducer.readFileToDict(file = os.path.abspath(filePath))

    reducer.writeToFile(file = os.path.abspath(args.outputfile))
