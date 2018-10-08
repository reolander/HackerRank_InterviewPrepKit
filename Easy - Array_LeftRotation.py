#!/bin/python

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    length_arr = len(a)
    actual_d = d % length_arr 
    print actual_d
    #moving n places to the left is same as moving len(a) - n places to the right.
    actual_d = length_arr - actual_d
    arr = [None] * len(a)
    for i in range(length_arr):
        arr[(i+actual_d)%length_arr] = a[i]
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
