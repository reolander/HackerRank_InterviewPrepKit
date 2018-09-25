#!/bin/python

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletions = 0
    for index in range(0, len(s)-1):
        if s[index+1] == s[index]:
            deletions += 1
    return deletions
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
