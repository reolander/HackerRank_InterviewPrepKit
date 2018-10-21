#!/bin/python

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr = sorted(arr)
    minUnfairness = arr[k-1] - arr[0]
    for index in range(1, len(arr)-k+1):
        print index
        unfairness = arr[index+k-1] - arr[index]
        print unfairness
        if minUnfairness > unfairness:
            minUnfairness = unfairness
    return minUnfairness

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    k = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr_item = int(raw_input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
