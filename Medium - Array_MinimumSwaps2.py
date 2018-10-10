#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    #Apparently for all the sorting algos minimum swaps take place in selection sort!
    swaps = 0
    for i in range(len(arr)-1):
        j = i+1; min_index = i
        while j < len(arr):
            if arr[j] < arr[min_index]:
                min_index = j
            j += 1
        if min_index != i:
            temp = arr[min_index]
            arr[min_index] = arr[i]
            arr[i] = temp
            swaps += 1
    return swaps
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()


def minimumSwaps(arr):
    swaps = 0 
    for i in range(len(arr)-1):
        min_value_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_value_index]:
                min_value_index = j
        if min_value_index != i:
            temp = arr[min_value_index]
            arr[min_value_index] = arr[i]
            arr[i] = temp
            swaps += 1
    return swaps


def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            swaps += 1
        elif arr[i] > arr[i+1]:
            swaps += 1
    if swaps == 0:
        return 0
    elif swaps == n-1:
        return n/2
    for i in range(len(arr)/2):
        print arr
        oneCycle(arr, i)
    return list[0]

listed = [0]; dictionary = {}
def oneCycle(arr, position):
    while True:
        numb_elements = 0
        if dictionary.has_key(position):
            break
        else:
            for index in range(position+1, len(arr)):
                if arr[index] < arr[position]:
                    numb_elements += 1

            if numb_elements == 0:
                break
            else:
                temp = arr[position]
                arr[position] = arr[position+numb_elements]
                arr[position+numb_elements] = temp
                listed[0] += 1
                dictionary[position+numb_elements] = arr[position+numb_elements]
        
def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            swaps += 1
        elif arr[i] > arr[i+1]:
            swaps += 1
    if swaps == 0:
        return 0
    elif swaps == n-1:
        return n/2
    
    for i in range(len(arr)-1):
        oneCycle(arr, i)
    return listed[0]


listed = [0]; dictionary = {}        
def minimumSwaps(arr):
    for position in range(len(arr)-1):
        swaps = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                swaps += 1
            elif arr[i] > arr[i+1]:
                swaps += 1
        if swaps == 0:
            return listed[0]
        elif swaps == n-1:
            return n/2

        while True:
            numb_elements = 0
            if dictionary.has_key(position):
                break
            else:
                for index in range(position+1, len(arr)):
                    if arr[index] < arr[position]:
                        numb_elements += 1
                        
                if numb_elements == 0:
                    break
                else:
                    temp = arr[position]
                    arr[position] = arr[position+numb_elements]
                    arr[position+numb_elements] = temp
                    listed[0] += 1
                    dictionary[position+numb_elements] = arr[position+numb_elements]
                    
    return listed[0]

def minimumSwaps(arr):
    total_swaps = 0; dictionary = {}
    
    # Check whether the array is already sorted or not. Or if it sorted in descending order.
    swaps = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            swaps += 1
    if swaps == 0:
        return total_swaps
    elif swaps == n-1:
        return n/2
    
    
    for pos in range(len(arr)-1):
        while True:
            numb_elements = 0
            if dictionary.has_key(pos):
                break
            else:
                for index in range(pos+1, len(arr)):
                    if arr[index] < arr[pos]:
                        numb_elements += 1
                        
                if numb_elements == 0:
                    break
                else:
                    arr[pos], arr[pos+numb_elements] = arr[pos+numb_elements], arr[pos]
                    total_swaps += 1
                    dictionary[pos+numb_elements] = 0
    return total_swaps


def minimumSwaps(arr):
    total_swaps = 0; dictionary = {}
    # Using dict to look up a value instead of list's indexing.
    dicto = {}
    for index in range(len(arr)):
        dicto[index] = arr[index]
        
    # Check whether the array is already sorted or not. Or if it sorted in descending order.
    swaps = 0
    for i in range(len(dicto)-1):
        if dicto[i] > dicto[i+1]:
            swaps += 1
    if swaps == 0:
        return total_swaps
    elif swaps == n-1:
        return n/2
    
    
    
    for pos in range(len(dicto)-1):
        while True:
            numb_elements = 0
            if dictionary.has_key(pos):
                break
            else:
                for index in range(pos+1, len(dicto)):
                    if dicto[index] < dicto[pos]:
                        numb_elements += 1
                        
                if numb_elements == 0:
                    break
                else:
                    dicto[pos], dicto[pos+numb_elements] = dicto[pos+numb_elements], dicto[pos]
                    total_swaps += 1
                    dictionary[pos+numb_elements] = 0
    return total_swaps


# Working solution but using extra space! Timing out when using in-place algo!
def minimumSwaps(arr):
    total_swaps = 0
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
        return total_swaps
    elif swaps == n-1:
        return n/2
    
    arr2 = sorted(arr)
    
    for pos in range(len(arr)-1):
        a = arr[pos]
        b = arr2[pos]
        if a != b:
            arr[pos], arr[dicto[b]] = arr[dicto[b]], arr[pos]
            dicto[a], dicto[b] = dicto[b], dicto[a]
            total_swaps += 1
    return total_swaps


