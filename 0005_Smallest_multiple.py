"""
Problem 5 - Smallest multiple

2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""

from fractions import gcd

def Smallest_multiple():

    LCM = lambda x, y : (x*y) // gcd(x, y)

    Ans = 1
    for i in range(2, 21):
        Ans = LCM(Ans, i)

    return Ans

print(Smallest_multiple())
