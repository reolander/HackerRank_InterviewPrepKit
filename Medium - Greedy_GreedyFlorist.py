#!/bin/python

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    lenC = len(c)
    if k >= lenC:
        totalCost = sum(c[:lenC])
        return totalCost
    else:
        totalCost = 0
        times = lenC / k
        print times
        quotient = lenC % k
        print quotient
        sumC = sum(c[:lenC])
        totalCost += sumC * times * (times + 1) / 2
        print totalCost
        for i in range(quotient):
            totalCost += c[i] * (1 + times)
        return totalCost
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = map(int, raw_input().rstrip().split())

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    lenC = len(c)
    if k >= lenC:
        totalCost = sum(c[:lenC])
        return totalCost
    else:
        totalCost = 0
        times = lenC / k
        print times
        quotient = lenC % k
        print quotient
        sumC = sum(c[:lenC])
        totalCost += sumC * times * (times + 1) / 2
        for i in range(quotient):
            totalCost += c[i] * (1 + times)
        return totalCost

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    lenC = len(c)
    if k >= lenC:
        cost = sum(c[:lenC])
        return cost
    else:
        totalCost = 0
        times = lenC / k
        quotient = lenC % k
        for i in range(times):
            totalCost += (c[i] * times * (times + 1)) / 2
        for j in range(quotient):
            totalCost += c[i] * (1 + times)
        return totalCost

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    lenC = len(c)
    if k >= lenC:
        cost = sum(c[:lenC])
        return cost
    else:
        totalCost = 0
        times = lenC / k
        quotient = lenC % k
        sortedC = sorted(c, reverse=True)
        i = 0
        for time in range(times):
            while i < k:
                totalCost += sortedC[i] * (1 + time)
                i += 1
            k += k
        for j in range(quotient):
            totalCost += sortedC[i] * (1 + times)
            i += 1
        return totalCost

# WORKING the getMinimumCost function below.
def getMinimumCost(k, c):
    lenC = len(c)
    if k >= lenC:
        cost = sum(c[:lenC])
        return cost
    else:
        totalCost = 0
        times = lenC / k
        quotient = lenC % k
        sortedC = sorted(c, reverse=True)
        i = 1
        flowersBought = 0
        while i <= times * k:
            totalCost += sortedC[i-1] * (1 + flowersBought)
            if i % k == 0:
                flowersBought += 1
            i += 1
        for j in range(quotient):
            totalCost += sortedC[i-1] * (1 + times)
            i += 1
        return totalCost
