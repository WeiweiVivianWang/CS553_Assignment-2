#  -*- coding: utf-8 -*-
from threading import *
from WordCountRE import *

class WordCountThread(Thread):
        """
        docstring for WordCount:
        Each instance of this class is a thread to count the word in the file
        """
        def __init__(self, tid, wcArray, filepath, filesize, blocksize, rlock):
                Thread.__init__(self)
                self.wordsDict = dict()
                self.__tid = tid
                self.__wcArray = wcArray
                self.__filepath = filepath
                self.__filesize = filesize
                self.__blocksize = blocksize
                self.__rlock = rlock
                self.wordcount_re = WordCountRE()

        # thread.start()
        def run(self ):
                """
                thread function
                Args:
                tid:                      the id of thread
                array:                  shared by threads, used to mark the end position of every thread
                filepath:             the path of the file need to be read
                Procedure:        First, each thread get the max position from the array, and set that position as the start position
                                            Then, the end position is (startposition + blocksize) if (startposition + blocksize) < filesize else filesize
                                            if startposition == filesize, then thread will be stopped
                                            if startposition == 0, then thread start reading the file from position 0
                                            if startposition != 0, then don't do anything until second readline() to make sure there is no overlap or missing part
                                            if currentposition <= endposition, then readline()
                                                else find the start position from array again
                """

                fstream = open(self.__filepath, 'r')

                # Each thread keeps reading the file until all threads reach the end of the file
                while True:
                        # rlock makes sure no two threads can modify the array at the same time 
                        # so that there will be no overlap or missing parts when reading the file
                        self.__rlock.acquire()
                        startposition = max(self.__wcArray)
                        endposition = self.__wcArray[self.__tid] = (startposition + self.__blocksize) if (startposition + self.__blocksize) < self.__filesize else self.__filesize
                        self.__rlock.release()

                        if startposition == self.__filesize:
                                # quit because reach the end of file
                                break
                        elif startposition != 0:
                                # read one line first and do nothing to make sure no line is be separated
                                fstream.seek(startposition)
                                fstream.readline()

                        # get the current position to be read in the file
                        pos = fstream.tell()

                        # read a part of file that is $blocksize large, and then read another part of file
                        # not neccessary successive
                        while pos < endposition:
                                # read file and map the words
                                fline = fstream.readline()
                                #wcIterator = self.wordcount_re.wcfinditer(fline)
                                wcList = self.wordcount_re.wcSplit(fline)
                                self.mapping(wcList)
                                pos = fstream.tell()

                        ee = fstream.tell() # Not sure the usage of this

                        # for testing
                        print 'The thread', self.__tid, '. And startposition:', startposition, ', endposition:', endposition

                # close file handler while finish reading
                fstream.close()
                
                #self.output()   # only for testing
                
                print 'The thread', self.__tid, 'finished!\n'

        # map the words to the dictionary
        def mapping(self, wcList):
                for word in wcList:
                        if word != '':
                                if not self.wordsDict.has_key(word):
                                        self.wordsDict[word] = 1
                                else:
                                        self.wordsDict[word] += 1

        # For Testing
        def getPid(self):
                return self.__pid

        def getArray(self):
                return self.__array

        def getFilePath(self):
                return self.__filepath

        def getFileSize(self):
                return self.__filesize

        def output(self):
                keys = self.wordsDict.keys()
                keys.sort()
                for key in keys:
                    print key, self.wordsDict[key]

if __name__ == '__main__':
        pass



        