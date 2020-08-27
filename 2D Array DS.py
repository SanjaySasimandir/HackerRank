'''
2D Array - DS
https://www.hackerrank.com/challenges/2d-array/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    sums=[]
    for i in range(4):
        for j in range(4):
            sums.append(sum(arr[i][j:j+3])+sum(arr[i+2][j:j+3])+arr[i+1][j+1])
            #print((arr[i][j:j+3]))
    return max(sums)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
