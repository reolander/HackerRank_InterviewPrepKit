#!/bin/python

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    dict_s1 = {}; dict_s2 = {}
    for element in s1:
        dict_s1[element] = 0
            
    for element in s2:
        dict_s2[element] = 0
            
    for key in dict_s1:
        if dict_s2.has_key(key):
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s1 = raw_input()

        s2 = raw_input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
