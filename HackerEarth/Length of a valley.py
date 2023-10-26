def area(arr,n):
    stack = []
    right_index = [0]*n
    index = 0
    while index<n:
        if len(stack)==0 or arr[stack[-1]]<arr[index]:
            stack.append(index)
            index += 1
        else:
            while len(stack)>0:
                x = stack.pop()
                right_index[x]= index
    
    while len(stack)>0:
        x = stack.pop()
        right_index[x]= index
        
    
    return right_index


def l_area(arr,n):
    stack = []
    left_index = [0]*n
    index = 0
    while index<n:
        if len(stack)==0 or arr[stack[-1]]<arr[index]:
            stack.append(index)
            index += 1
        else:
            while len(stack)>0:
                x = stack.pop()
                left_index[x]= index
    
    while len(stack)>0:
        x = stack.pop()
        left_index[x]= index
        
    
    return left_index


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    left_index = l_area(arr[::-1],n)
    left_index = left_index[::-1]
    for i in range(n):
        left_index[i] = n - left_index[i] + 1
    right_index = area(arr,n)
    ans = [0]*n
    for i in range(n):
        ans[i] = right_index[i] - left_index[i] + 1
    print(*ans,sep =' ')