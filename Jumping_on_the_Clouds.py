#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = -1
    n = len(c)
    i = 0

    while i < n:
        if i < n-2 and c[i+2] == 0:
            i = i+2
        else:
            i=i+1
        jumps = jumps+1


    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()