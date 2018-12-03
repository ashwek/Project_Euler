"""
Problem 3 - Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
(29 being the largest)

What is the largest prime factor of the number 600851475143 ?
"""

def Largest_Prime_Factor(Num):

    i = 2
    Max = -1
    while Num > i :
        if Num % i == 0:
            Num //= i
            i = 1
        i += 1

    return Num

print(Largest_Prime_Factor(600851475143))
