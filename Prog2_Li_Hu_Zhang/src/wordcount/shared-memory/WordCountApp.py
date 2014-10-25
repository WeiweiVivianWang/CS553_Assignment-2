#! /usr/bin/python
#  -*- coding: utf-8 -*-
import datetime
import os
import argparse
from WordCountThread import *
from threading import *

WORKERS = 1
BLOCKSIZE = 50000000
WORDSDICT = {}
FILEPATH = 'output.txt'
#FILEPATH = 'small-dataset'
#FILEPATH = 'wiki10gb'

# get the size of the file 
def getFileSize(filepath):
        fstream = open(filepath, 'r')
        fstream.seek(0, os.SEEK_END) # locate to the end of the file
        filesize = fstream.tell()
        fstream.close()
        return filesize

# merge all threads' own dictionary to one
def wcReduce(*dicts):
        keys = set(sum([d.keys() for d in dicts], []))
        totalDict = dict()
        for key in keys:
                totalDict[key] = sum([d.get(key, 0) for d in dicts])
        return totalDict

# output the result
def output(arg):
        if arg == 'value':
                lis = sorted(WORDSDICT.items(), key = lambda d:d[1], reverse = True)
                fstream = open('output_value', 'w')
                for i in lis:
                    oString = i[0] + '    ' + str(i[1]) + '\n'
                    fstream.write(oString)
        elif arg == 'key':
                keys = WORDSDICT.keys()
                keys.sort()
                fstream = open('output_key', 'w')
                for key in keys:
                    oString = key + '    ' + str(WORDSDICT[key]) + '\n'
                    fstream.write(oString)


def main():
        global WORDSDICT
        global WORKERS
        
        parser = argparse.ArgumentParser()
        parser.add_argument('--t', type = int, help = 'Number of Threads.')
        args = parser.parse_args()

        rlock = RLock()
        WORKERS = args.t

        wcThreads = []
        # Array() is used with multiple processes
        # array = Array('l', WORKERS, lock=rlock)
        wcArray = [0 * i for i in xrange(WORKERS)]
        print wcArray  #for testing

        filesize = getFileSize(FILEPATH)

        starttime = datetime.datetime.now()

        # for testing
        print 'filesize: ', filesize #should be 1,100,000 for small-dataset

        # initialize threads
        for i in xrange(WORKERS):
                wcthread = WordCountThread(i, wcArray, FILEPATH, filesize, BLOCKSIZE, rlock)
                wcThreads.append(wcthread)
        # start threads
        for i in xrange(WORKERS):
                wcThreads[i].start()
        # wait for threads to be finished
        for i in xrange(WORKERS):
                wcThreads[i].join()

        # reduce()
        dictList = [wcThreads[i].wordsDict for i in xrange(WORKERS)]
        WORDSDICT = wcReduce(*dictList)

        endtime = datetime.datetime.now()

        print 'The main thread finished!'
        print 'StarTtime:', starttime.strftime("%Y/%d/%m %H:%M:%S")
        print 'EndTime:', endtime.strftime("%Y/%d/%m %H:%M:%S")
        # output the result
        output('key')
        output('value')

        
if __name__ == '__main__':
        main()
