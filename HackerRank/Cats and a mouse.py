import sys


q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    if abs(x-z)>abs(y-z):
        print('Cat B')
    elif abs(x-z)<abs(y-z):
        print('Cat A')
    else:
        print('Mouse C')