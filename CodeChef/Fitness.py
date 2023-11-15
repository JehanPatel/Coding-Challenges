#solution as follows

t = int(input())
for i in range(t):
    X = int(input())
    #Create a new variable Y for total distance. 
    #5 days a week - Chef will travel 2*X daily - i.e. return trip walk to office
    Y = 2 * X * 5           
    #Output distance traveled for each test case
    print(Y)                