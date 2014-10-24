#  -*- coding: utf-8 -*-
import re

class WordCountRE(object):
        """
        docstring for WordCountRE:
        Regular Expression for match
        """
        def __init__(self):
                super(WordCountRE, self).__init__()
                self.__reString = ur'[\u1100-\u11FF]+|[\uAC00-\uD7AF]+|[\u0400-\u052f]+|[\u2e80-\u9fff]+|\d+\.\d+|([1-9]+,)+\d+|\w+\'s|\w*\d*'

        # return a pattern string
        def __wccompile(self):
                return re.compile(self.__reString)

        # decode the fileStr to unicode and than return an iterator of the result
        def wcfinditer(self, fileStr):
                self.__patternString = self.__wccompile()
                unicodeStr = fileStr.decode('utf-8')
                return self.__patternString.finditer(unicodeStr)
        
        def wcSplit(self, fileStr):
                return re.split('[\t\n \[\],.;=+\'\"()|<>-?!]+', fileStr)

        def getReString(self):
                return self.__reString

        # def setReString(self, reString):
        #         self.__reString = reString


if __name__ == '__main__':
        pass