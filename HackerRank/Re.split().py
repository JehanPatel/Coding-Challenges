import re
s = input()
for t in re.split(r",|\.", s):
    if t != '': print(t)