#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if len(note) > len(magazine):
        print 'No'
    else:
        dictN, dictM, inMaga = {}, {}, 1
        for word in note:
            if dictN.has_key(word):
                dictN[word] += 1
            else:
                dictN[word] = 1
        for word in magazine:
            if dictM.has_key(word):
                dictM[word] += 1
            else:
                dictM[word] = 1
        for word in note:
            if not dictM.has_key(word) or dictN[word] > dictM[word]:
                inMaga = 0
                break
        if inMaga == 1:
            print 'Yes'
        else:
            print 'No'

if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine(magazine, note)
