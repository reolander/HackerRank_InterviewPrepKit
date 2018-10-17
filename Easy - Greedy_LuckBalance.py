#!/bin/python

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    imp_contest = []; luck = 0
    for contest in contests:
        if contest[1] == 1:
            imp_contest.append(contest[0])
            luck -= contest[0]
        else:
            luck += contest[0]
    imp_contest = sorted(imp_contest, reverse=True)
    
    i = 0
    if k > len(imp_contest):
        k = len(imp_contest)
    while i < k:
        luck += 2 * imp_contest[i]
        i += 1
    return luck
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in xrange(n):
        contests.append(map(int, raw_input().rstrip().split()))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
