#!/bin/python

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    hashmap = dict()
    for char in s:
        if hashmap.get(char):
            hashmap[char] += 1
        else:
            hashmap[char] = 1
    
    sortedList = hashmap.values()
    sortedList.sort()
    
    l = len(sortedList)
    if sortedList[0] == sortedList[l-1]:
        return 'YES'
    elif sortedList[0] == sortedList[l-2] and sortedList[l-1] - sortedList[0] == 1:
        return 'YES'
    elif sortedList[l-1] == sortedList[1] and sortedList[0] == 1:
        return 'YES'
    return 'NO'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
