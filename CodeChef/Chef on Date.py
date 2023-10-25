# cook your dish here
a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    if(b>=c):
        print('Yes')
    else:
        print('No')