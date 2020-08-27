'''
Strings: Making Anagrams
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def removeCommon(a,b):
    for x in a:
        if x in b:
            a.remove(x)
            b.remove(x)
    for x in b:
        if x in a:
            b.remove(x)
            a.remove(x)
    return a,b
def commonCheck(a,b):
    for x in a:
        if x in b:
            return True
    return False
def makeAnagram(a, b):
    a=sorted(list(a))
    b=sorted(list(b))
    while(commonCheck(a,b)):
        a,b=removeCommon(a,b)
        print("".join(a),"".join(b))
    return len(a)+len(b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()