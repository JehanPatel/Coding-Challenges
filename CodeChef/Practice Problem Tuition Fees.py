# Solution as follows

t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    #Create a variable 'tuition' to store the tuition fees
    tuition = X * Y         
    print(tuition)