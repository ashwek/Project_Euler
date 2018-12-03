"""
Problem 4 - Largest palindrome product

A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two
3-digit numbers.
"""

def Largest_palindrome_product():

    i = 999
    End = 99
    Ans = (-1, 0,0)

    while i > End :
        for j in range(i, End, -1):
            temp = i*j
            if str(temp) == str(temp)[::-1] :
                if temp > Ans[0] :
                    Ans = (temp, i, j)
                End = j
        i -= 1

    return Ans

print(Largest_palindrome_product())
