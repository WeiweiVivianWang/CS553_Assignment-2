#  -*- coding: utf-8 -*-
import datetime
import os
from SortingThread import *
from threading import *

WORKERS = 8
BLOCKSIZE = 100000000
WORDSDICT = {}
FILEPATH = '10GB.txt'
#FILEPATH = 'tmp_pid0_jobs100000000'
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
        for d in dicts:
            totalDict.update(d)
#        for key in keys:
#                totalDict[key] = [d.get(key) for d in dicts]
        return totalDict

# output the result
def output():
        keys = WORDSDICT.keys()
        keys.sort()
        fstream = open('output_key', 'w')
        for key in keys:
            oString = key + '  ' + WORDSDICT[key]
            fstream.write(oString)


def main():
        global WORDSDICT
        rlock = RLock()
        wcThreads = []
        # Array() is used with multiple processes
        # array = Array('l', WORKERS, lock=rlock)
        wcArray = [0 * i for i in xrange(WORKERS)]
        #print wcArray  #for testing

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
        #dictList = [wcThreads[i].wordsDict for i in xrange(WORKERS)]
        #WORDSDICT = wcReduce(*dictList)

        endtime = datetime.datetime.now()

        print 'The main thread finished!'
        print 'StarTtime:', starttime.strftime("%Y/%d/%m %H:%M:%S")
        print 'EndTime:', endtime.strftime("%Y/%d/%m %H:%M:%S")
        # output the result
        #output()
        
if __name__ == '__main__':
        main()
