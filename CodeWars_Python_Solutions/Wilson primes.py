'''

Wilson primes satisfy the following condition. Let P represent a prime number.

Then ((P-1)! + 1) / (P * P) should give a whole number.

Your task is to create a function that returns true if the given number is a Wilson prime.

'''
import math

def am_i_wilson(n):
    new_n = float(n/1.00)
    if n > 0 and n != 1:
        print False if ((math.factorial(new_n-1) + 1) / (new_n * new_n))%1.00 != 0 else True
    else:
        print False

am_i_wilson(111)