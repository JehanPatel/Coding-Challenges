t = int(input())
def find(arr,ele,n):
    ans = 0
    for i in range(n):
        temp = abs(ele-arr[i])
        if temp == 1 or temp%2 !=0:
            ans += 1
    return ans
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    l = []
    for i in range(n):
        if arr[i]%2 == 0:
            l.append(2)
        else:
            l.append(1)
    x = n + 1
    for k in range(1,3):
        x2 = find(arr,k,n)
        x = min(x,x2)
    print(x)