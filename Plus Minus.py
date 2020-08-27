'''
https://www.hackerrank.com/challenges/plus-minus/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    for i in arr:
        if i>0:
            pos+=1
        if i<0:
            neg+=1
        if i==0:
            zer+=1
    print(pos/len(arr))
    print(neg/len(arr))
    print(zer/len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
