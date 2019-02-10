#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
inversions = 0
def mergeSort(arr):
    global inversions
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr)//2
        s = []
        a = mergeSort(arr[:mid])
        b = mergeSort(arr[mid:])
        i = j = k = 0
        while i < len(a) + len(b):
            if j < len(a) and k >= len(b):
                s.append(a[j])
                j += 1
            elif j >= len(a) and k < len(b):
                s.append(b[k])
                k += 1
            else:
                if a[j] > b[k]:
                    inversions += len(a) - j
                    s.append(b[k])
                    k += 1
                else:
                    s.append(a[j])
                    j += 1
            i += 1
    return s

def countInversions(arr):
    global inversions
    mergeSort(arr)
    res = inversions
    inversions = 0
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
