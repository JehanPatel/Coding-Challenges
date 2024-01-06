for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    amx, bmx = 0, 0
    cura, curb = 0, 0
    for i in range(n):
        if a[i] == 0: cura = 0
        else: cura += 1
        
        if b[i] == 0: curb = 0
        else: curb += 1
        
        amx = max(amx, cura)
        bmx = max(bmx, curb)
    print('Om' if amx > bmx else ('Addy' if amx < bmx else 'Draw'))