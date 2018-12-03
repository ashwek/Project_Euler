"""
Problem 6 - Sum square difference

The sum of the squares of the first 10 natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first 10 natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum
is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.

"""

def Sum_square_difference(limit):

    return sum(range(1,limit+1))**2 - sum((i*i for i in range(1,limit+1)))

print(Sum_square_difference(100))
