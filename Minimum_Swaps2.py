#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    res = 0
    temp = 0
    i = 0
    while i < (len(arr)-1):
        if (i+1) != arr[i]:
            temp = arr[i]
            arr[i] = arr[temp-1]
            arr[temp-1] = temp
            res = res + 1
            i = i-1
        i = i + 1

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
