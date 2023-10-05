input();
a=list(map(int, input().split()))
b=list(map(int, input().split()))
ans=0
for i in range(1, 101):
    if all(i%x==0 for x in a) and all(x%i==0 for x in b):
        ans+=1
print(ans)