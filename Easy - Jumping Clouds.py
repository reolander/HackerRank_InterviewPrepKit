#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0; i = 0
    while i < len(c)-1:
        print i
        try:
            if (c[i+1] == 0 and c[i+2] == 0) or (c[i+1] == 1):
                i += 2
            else:
                i += 1
        except:
            i += 1
        count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
