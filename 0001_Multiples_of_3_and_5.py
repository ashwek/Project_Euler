"""
Problem 1 - Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def Multiples_3_5(limit):
    Sum = 0
    for i in range(2, limit):
        if( i%3 == 0 or i%5 == 0 ):
            Sum += i
    return Sum

print(Multiples_3_5(1000))
