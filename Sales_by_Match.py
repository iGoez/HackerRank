#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pares = 0
    lista = []
    
    for i in range(0,n):
        if ar[i] not in lista:
            lista.append(ar[i])
            pares = pares + int((ar.count(ar[i]))/2)
                    

    return pares

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')

    fptr.close()
