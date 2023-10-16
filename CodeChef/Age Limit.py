# cook your dish 
for _ in range(int(input())):
    a=list(map(int,input().split()))
    if a[2] >= a[0] and a[2] < a[1]:
        print('YES')
    else:
        print('NO')