# Solution as follows

t = int(input())
for i in range(t):
    N, M = map(int, input().split())
    if N <= M:          
        print(N)
    else:
        print(2*N-M)