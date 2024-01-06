# cook your dish here
n=int(input())
a=[]
for i in range(n):
    k=int(input())
    a.append(k)
a.sort()
for i in range(n):
    print(a[i])