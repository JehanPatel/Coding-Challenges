n,k = map(int,input().split())
a = list(map(int,input().split()))
b = [0]*k
for i in range(n):
    b[a[i]%k] += 1
ans = 0
for i in range(k):
    ans += b[i]*(b[i]-1)

print(ans)