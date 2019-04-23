# I pledge my honor to abide by the Stevens Honor System.
# Andrew Chuah and Paul Gurman

from cs115 import map, reduce
from math import *

def inverse(n):
    """ Returns the inverse of the input. """
    return 1/n

def e(n):
    """ Returns the approximation of e by using Taylor's expansion. """
    list1 = list(range(1, n+1))
    list2 = map(inverse, map(factorial, list1))
    return sum(list2) + 1

def error(n):
    """ Returns the error of the value of e to the approximation from e(n) function. """
    return abs(math.e - e(n))
    
    
