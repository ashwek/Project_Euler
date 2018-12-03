"""
Problem 2 - Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting with
1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose
values do not exceed four million (4000000), find the
sum of the even-valued terms.

"""

def Even_Fib(limit):

    a = 1
    b = 2
    Sum = 0
    while(a<=limit):
        if not (a & 1): Sum += a
        a, b = b, a+b

    return Sum

print(Even_Fib(4000000))
