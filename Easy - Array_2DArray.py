#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    length_arr = len(arr[0])
    print length_arr
    i = 0; list_hourglass_values = []
    while i < length_arr-2:
        j = 0
        while j < length_arr-2:
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            list_hourglass_values.append(sum)
            j += 1
        i += 1
    sorted_values = sorted(list_hourglass_values)
    print sorted_values
    highest_value = sorted_values[len(sorted_values)-1]
    return highest_value
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
