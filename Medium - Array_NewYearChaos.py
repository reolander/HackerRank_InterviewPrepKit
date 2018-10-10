#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(arr):
    length = len(arr); chaotic = 0
    for index in range(length):
        if arr[index] - 3 > index:
            chaotic = 1
            break
            
    if chaotic:
        print 'Too chaotic'
    else:
        total_swaps = 0; boolean = 1
        # Using dict to look up a value instead of list's indexing.
        dicto = {}
        for index in range(len(arr)):
            dicto[arr[index]] = index

        # Check whether the array is already sorted or not. Or if it sorted in descending order.
        swaps = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                swaps += 1
        if swaps == 0:
            print swaps
            boolean = 0
        elif swaps == n-1:
            print swaps
            boolean = 0

        arr2 = sorted(arr)

        for pos in range(len(arr)-1):
            a = arr[pos]
            b = arr2[pos]
            if a != b:
                arr[pos], arr[dicto[b]] = arr[dicto[b]], arr[pos]
                dicto[a], dicto[b] = dicto[b], dicto[a]
                total_swaps += 1
        
        if boolean == 1:
            print total_swaps
      
if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)



#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    length = len(q); chaotic = 0
    for index in range(length):
        if q[index] - 3 > index:
            chaotic = 1
            break
            
    if chaotic:
        print 'Too chaotic'
    else:
        print 'cycle sort'
      
if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)



#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    length = len(q); person_swaps = {}; chaotic = 0; swaps = 0
    
    for i in range(length):
        for index in range(0, length-1-i):
            if q[index] > q[index+1]:
                if person_swaps.has_key(q[index]):                 
                    person_swaps[q[index]] += 1
                    if person_swaps[q[index]] > 2:
                        chaotic = 1
                        break
                else:
                    person_swaps[q[index]] = 1
                q[index], q[index+1] = q[index+1], q[index]
                swaps +=1 

    if chaotic == 0:
        print swaps  
    else:
        print 'Too chaotic'
      
if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)


# Working solution!!!
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(arr):
    length = len(arr); chaotic = 0
    for index in range(length):
        if arr[index] - 3 > index:
            chaotic = 1
            break
            
    if chaotic:
        print 'Too chaotic'
    else:
        bribes = 0
        for i in range(len(arr)-1):
            swaps = 0
            for j in range(len(arr)-1-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swaps += 1
                    bribes += 1
            if swaps == 0:
                break
        print bribes
      
if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
