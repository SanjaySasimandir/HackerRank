'''
https://www.hackerrank.com/challenges/diagonal-difference/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    a=0
    b=0
    for i in range(len(arr)):
        a+=arr[i][i]
        b+=arr[len(arr)-1-i][i]
    return abs(a-b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
