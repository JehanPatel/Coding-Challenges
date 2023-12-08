T = int(input())

for i in range(T):
    n, m, k = map(int, input().split())
    total = 0
    rooms_b = 0
    rooms_g = 0
    rooms_b = n//k
    if (n - (rooms_b * k)) != 0:
        rooms_b += 1
    rooms_g = m//k
    if (m - (rooms_g * k)) != 0:
        rooms_g += 1
    total = rooms_b + rooms_g
    print(total)