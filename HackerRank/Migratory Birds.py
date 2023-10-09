#!/bin/python3

import sys
from collections import Counter
import operator

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
# your code goes here
mydict = dict(Counter(types))
maximum = max(mydict, key=mydict.get)  
print(maximum)