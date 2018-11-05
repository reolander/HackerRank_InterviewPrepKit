#!/bin/python

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    sortedPrices = sorted(prices)
    print sortedPrices
    i = 0; sum = 0; numToys = 0
    while i < len(sortedPrices):
        if sum + sortedPrices[i] >= k:
               return numToys
        else:
            sum += sortedPrices[i]
            numToys += 1
        i += 1
    return numToys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = map(int, raw_input().rstrip().split())

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
