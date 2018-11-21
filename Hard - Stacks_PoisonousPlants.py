#!/bin/python

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    days, i, popped_list = 0, 0, []
    while i < len(p)-1:
        if p[i+1] > p[i]:
            popped_list.append(i+1)
        i += 1
        if i == len(p) - 1:
            if popped_list:
                shifter = 0
                for index in popped_list:
                    if shifter == 0:
                        p.pop(index)
                        shifter += 1
                    else:
                        p.pop(index-shifter)
                days += 1
                popped_list = []
                i = 0
            else:
                return days
    return days

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    p = map(int, raw_input().rstrip().split())

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')
    
    fptr.close()












#!/bin/python

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    days, i, counter = 0, 0, 0
    while i < len(p)-1:
        length = len(p)-1
        if p[i+1] > p[i]:
            p.pop(i+1)
            print p
        else:
            counter += 1
        i += 1
        if i == length and counter == length:
            return days
        elif i == length:
            days += 1
            i = 0
            counter = 0
        
    return days
            
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    p = map(int, raw_input().rstrip().split())

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')
    
    fptr.close()


# Just for checking in my Python environment
def poisonousPlants(p):
    plants = p; plants2 = p
    days = 0
    print plants
    while True:
        for i in range(len(p)-1):
            print i, i+1,
            print plants[i+1]
            if plants[i+1] > plants[i]:
                plants2.pop(i+1)
        if plants == plants2:
            return days
        else:
            plants = plants2
            days += 1
        print plants, plants2


poisonousPlants([1,2,3,4,5,6,7,8,9])