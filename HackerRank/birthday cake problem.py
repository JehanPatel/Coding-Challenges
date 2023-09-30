#!/bin/python3

import math
import os
import random
import re
import sys


def birthdayCakeCandles(ar):
    c = 0
    temp = ar[0]
    for i in range(1,len(ar)):
        if ar[i] > temp:
            temp = ar[i]
    for i in range(0,len(ar)):
        if ar[i] == temp:
            c = c + 1
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()