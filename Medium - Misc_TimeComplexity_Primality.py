#!/bin/python

import math
import os
import random
import re
import sys

# Complete the primality function below.
def primality(num):
    if num == 1:
        return 'Not prime'
    elif num == 2:
        return 'Prime'
    elif num % 2 == 0:
        return 'Not prime'
    else:
        i = 3
        while i*i <= num:
            if num % i == 0:
                return 'Not prime'
            i += 2
    return 'Prime'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(raw_input())

    for p_itr in xrange(p):
        n = int(raw_input())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
