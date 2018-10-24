#!/bin/python

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
binary_table = [1] * 32
for index in range(1, 32):
    binary_table[index] = binary_table[index-1]*2
print binary_table

def flippingBits(n):
    binary_rep = []
    while True:
        if n/2 != 0 :
            binary_rep.append(n%2)
            n = n/2
        elif n/2 == 0 and n == 1:
            binary_rep.append(1)
            break
        else:
            binary_rep.append(0)
            break
    output = 0
    for index in range(len(binary_rep)):
        output += binary_rep[index] * binary_table[index]
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        n = int(raw_input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
max_value = 1; power_2 = 1
for index in range(1, 32):
    power_2 = power_2*2
    max_value += power_2

def flippingBits(n):
    return max_value - n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        n = int(raw_input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
