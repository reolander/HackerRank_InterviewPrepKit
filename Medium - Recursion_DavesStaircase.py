#!/bin/python

import math
import os
import random
import re
import sys

ways = {0: 0, 1: 1, 2: 2, 3: 4}; output = 0
def stepPerms(n):
    if n < 1:
        return ways[0]
    elif n == 1:
        return ways[1]
    elif n == 2:
        return ways[2]
    elif n == 3:
        return ways[3]
    else:
        try: 
            if ways[n-1] and ways[n-2] and ways[n-3]:
                ways[n] = ways[n-1] + ways[n-2] + ways[n-3]
                return ways[n]
        except:
            return stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(raw_input())

    for s_itr in xrange(s):
        n = int(raw_input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()


def stepPerms(n):
    if n < 1:
        return ways[0]
    elif n == 1:
        return ways[1]
    elif n == 2:
        return ways[2]
    elif n == 3:
        return ways[3]
    else:
        try: 
            if ways[n-1] and ways[n-2] and ways[n-3]:
                ways.append(ways[n-1]+ways[n-2]+ways[3])
                return ways[n-1] + ways[n-2] + ways[n-3]
        catch:
            A = stepPerms(n-1) 

            def stepPerms(n):
                if n < 1:
                    return 0
                elif n == 1:
                    return 1
                elif n == 2:
                    return 2
                elif n == 3:
                    return 4
                else:
                    return stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)