#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    n = len(a)

    if d%n == 0 or d == 0:
        return a

    if d > n:
        d = d%n
    
    return a[d:]+a[:d]

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = []
    if len(a) == n:
        result = rotLeft(a, d)
        print(result)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
