#!/bin/python

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for char in s:
        if char == '{' or char == '[' or char == '(':
            stack.append(char)
        elif char == '}' or char == ']' or char == ')':
            if len(stack) == 0:
                return 'NO'
            else:
                popped = stack.pop()
                if popped == '{' and char == '}':
                    continue
                elif popped == '[' and char == ']':
                    continue
                elif popped == '(' and char == ')':
                    continue
                else:
                    return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        s = raw_input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
