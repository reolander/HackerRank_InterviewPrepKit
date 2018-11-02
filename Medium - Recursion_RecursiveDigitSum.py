#!/bin/python

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    output = 0
    for char in n:
        output += int(char)
    if output % 9 == 0:
        return 9
    else:
        output *= k
        if output % 9 == 0:
            return 9
        else:
            return output % 9
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
