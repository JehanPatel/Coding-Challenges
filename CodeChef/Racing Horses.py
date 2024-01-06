# cook your dish here
a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    c.sort()
    diff=c[1]-c[0]
    for i in range(2,b):
            a1=c[i]-c[i-1]
            if a1<diff:
                diff=a1
    print(diff)   