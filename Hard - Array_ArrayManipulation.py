#!/bin/python

import math
import os
import random
import re
import sys

# Working solution
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n; m = {}; listed = []
    m[n-2] = 0
    for element in queries:
        arr[element[0]-1] += element[2]
        if element[1] < n:   
            arr[element[1]] -= element[2]
            m[element[1]] = 0
        m[element[0]-1] = 0
    m = sorted(m)
    sum = 0
    for key in m:
        sum += arr[key]
        listed.append(sum) 
    return sorted(listed)[len(m)-1]
    
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n
    new_array = [0] * n
    prefix_value = 0
    least_index = []; highest_index = []
    for index in queries:
        least_index.append(index[0]-1)
        highest_index.append(index[1]-1)
        arr[index[0]-1] += index[2]
        if index[1] < n:
            arr[index[1]] += -index[2]
    print least_index, highest_index
    least_index = sorted(least_index)[0]
    highest_index = sorted(highest_index)[len(highest_index)-1]
    print least_index, highest_index
    for i in range(least_index, highest_index + 1):
        prefix_value += arr[i]
        new_array[i] = prefix_value
           
    return sorted(new_array)[n-1]       

def arrayManipulation(n, queries):
    arr = [0] * n
    new_array = [0] * n
    index_dict = {}
    prefix_value = 0
    for index in queries:
        arr[index[0]-1] += index[2]
        if index[1] < n:
            arr[index[1]] += -index[2]

        index_dict[index[0]-1] = 0
        index_dict[index[1]-1] = 0
            
    for key in index_dict:
        prefix_value += arr[key]
        new_array[key] = prefix_value
    print new_array  
    return sorted(new_array)[n-1] 

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n
    new_array = [0] * 2 * len(queries)
    print new_array
    index_dict = {}
    prefix_value = 0
    for index in queries:
        arr[index[0]-1] += index[2]
        if index[1] < n:
            arr[index[1]] += -index[2]

        index_dict[index[0]-1] = 0
        index_dict[index[1]-1] = 0
    print index_dict  
    ind = 0
    for key in index_dict:
        prefix_value += arr[key]
        new_array[ind] = prefix_value
        ind += 1
    print new_array  
    return sorted(new_array)[len(new_array)-1]

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n
    
    for index in queries:
        j = index[0] - 1
        while j < index[1]:
            arr[j] += index[2]
            j += 1
    return sorted(arr)[len(arr)-1]            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()















#!/bin/python

import math
import os
import random
import re
import sys
import collections

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n+1)
    index_dict = {}
    prefix_value = 0
    for index in queries:
        arr[index[0]] += index[2]
        if index[1] < n :
            arr[index[1]+1] += -index[2]
        index_dict[index[0]] = 0
        index_dict[index[1]] = 0
    print arr
    print index_dict  
    od_index_dict = collections.OrderedDict(sorted(index_dict.items()))
    print od_index_dict
    ind = 0 ; new_array = [0] * len(index_dict)
    for key in od_index_dict:
        print key
        prefix_value += arr[key]
        new_array[ind] = prefix_value
        ind += 1
    print new_array  
    return sorted(new_array)[len(new_array)-1]            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
