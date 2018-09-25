#!/bin/python

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dict_a = {}
    for index in range(len(a)):
        if dict_a.has_key(a[index]):
            dict_a[a[index]] += 1
        else:
            dict_a[a[index]] = 1
    
    dict_b = {}
    for index in range(len(b)):
        if dict_b.has_key(b[index]):
            dict_b[b[index]] += 1
        else:
            dict_b[b[index]] = 1
    
    deletions = 0
    for key in dict_b:
        if not dict_a.has_key(key):
            deletions += dict_b[key]
            
    for key in dict_a:
        if dict_b.has_key(key):
            deletions += abs(dict_b[key] - dict_a[key])
        else:
            deletions += dict_a[key]
    return deletions      
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
