# importing the functions
from fractions import Fraction
from functools import reduce


# defining the function
def product(fracs):
    
    # using the reduce() method with lambda
    t = Fraction(reduce(lambda x, y: x * y, fracs))
    return t.numerator, t.denominator

# the main function
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)