def beautifulDays(i, j, k):
    beautifulDays = 0
    for day in range(i, j+1):
        rev = int(str(day)[::-1])
        if abs(rev-day)%k==0:
            beautifulDays+=1 
         
    return beautifulDays