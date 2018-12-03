"""
Problem 7 - 10001st prime

By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
"""

def isPrime(Num):
    if( Num > 2 and Num & 1 == 0 ): return False

    for i in range(3, int(Num**0.5)+1, 2):
        if(Num%i == 0):
            return False
    return True

def n_prime(limit):

    i = 2
    while( limit > 0 ):
        if( isPrime(i) ):
            limit -= 1
        i += 1

    return i-1

print(n_prime(10001))
