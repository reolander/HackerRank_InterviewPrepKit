#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    numSwaps = 0
    for i in range(len(a)):
        for j in range(len(a)-1 ):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                numSwaps += 1
    print "Array is sorted in %s swaps.\nFirst Element: %s\nLast Element: %s" %(
           numSwaps, a[0], a[len(a)-1])

if __name__ == '__main__':
    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    countSwaps(a)
.