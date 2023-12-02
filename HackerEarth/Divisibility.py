N = int(input())
arr = list(map(int,input().split()))
ele = arr[N-1]
if ele % 10 == 0:
    print("Yes")
else:
    print("No")