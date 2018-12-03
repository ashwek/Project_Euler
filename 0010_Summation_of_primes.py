"""
Problem 10 - Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million (2000000).
"""

def isPrime(Num):
    if(Num > 2 and Num & 1 == 0): return False
    for i in range(3, int(Num**0.5)+1, 2):
        if(Num%i == 0):
            return False
    return True

def Sum_of_Primes(limit):
    return sum(i for i in range(2, limit) if(isPrime(i)))

print(Sum_of_Primes(2000000))
