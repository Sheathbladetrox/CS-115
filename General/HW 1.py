# I pledge my honor that I have abided by the Stevens Honor System.
# Andrew Chuah
# 9/7/2018

from cs115 import *
from math import *
import math

def add(x, y):
    """Takes two integers and returns the sum of the two."""
    return x + y

def square(n):
    """Takes an integer n and squares it."""
    if n == 0:
        return 1
    return n * n

def sum(n):
    """Takes a positive integer n and returns the sum: 1 + 2 + 3 +...+ n."""
    return reduce(add, range(1, 1 + n))

def sumOfSquares(n):
    """Takes a positive integer n and returns the sum: 1^2 + 2^2 + 3^2 +...+ n^2."""
    return reduce(add, map(square, range(1, 1 + n)))

print(sum(5))
print(sumOfSquares(5))
