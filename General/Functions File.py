# Master File for Functions
# Andrew Chuah

def dotProduct(L, K):
    """ This function will output dot products of lists L and K. """
    if L == [] or K == []:
        return 0.0
    else:
        return dotProduct(L[1:], K[1:]) + (L[0]*K[0])

def expand(S):
    """ This function will take a string and put each letter into a list. """
    if type(S) == type(0):
        return S
    elif S == "":
        return ""
    else:
        return [S[0]] + expand(S[1:])

def deepMember(e, L):
    """ This function takes in an element e and and a list L, and look for the value e in the list. """
    if not L:
        return False
    elif e == L[0]:
        return True
    elif type(L[0]) == type ([]):
        return deepMember(e, L[0])
    else:
        return deepMember(e, L[1:])

def removeAll(e, L):
    """ This function will find the input e in a list L and remove it. """
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])

def deepReverse(L):
    """ This function will take a list L and reverse it. """
    if not L or type(L) == type(0):
        return L
    else:
        return deepReverse(L[1:]) + [deepReverse(L[0])]

def myFilter(f, L):
    """ This function will take a function and apply it to a list. It then returns a filtered list. """
    if not L:
        return L
    elif f(L[0]):
        return [L[0]] + myFiter(f, L[1:])
    else:
        return myFilter(f, L[1:])

def even(x):
	""" This function will return True iff x is even. """
	return x % 2 == 0

def powerset(L):
    """ Returns the set of all possible subsets of a set. """
    if not L:
        ans = [[]]
    else:
        oneFewer = powerset(L[1:])
        useIt = list(map(lambda T: [L[0]] + T, oneFewer))
        ans = oneFewer + useIt
    return ans

def dedup(L):
    """ Return a sublist where every duplicate item has been suppressed. """
    if not L:
        return []
    else:
        return [L[0]] + list(filter(lambda x: x != L[0], dedup(L[1:])))

def jsScore(s, t):
    """ Takes two strings s and t in input and outputs the "scrabble-jotto score" of s and t, that is,
    the scrabble score of the characters shared by s and t. Multiple occurrences of a letter are counted
    multiple times, as long as they appear multiple times in both strings.
    """
    if len(s) < len(t):
        list1 = list(s)
        list2 = list(t)
    else:
        list1 = list(t)
        list2 = list(s)
    return helper(list1, list2, 0)

def helper(list1, list2, score):
    """ Helper function for jsScore """
    scrabbleLetterScore = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4,
                           "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1,
                           "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1,"t": 1,
                           "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}
    if not list1 or not list2:
        return score
    else:
        if list1[0] in list2:
            score = score + scrabbleLetterScore[list1[0]]
            list2 = remove(list2, list1[0])
        return helper(list1[1:], list2, score)

def remove(list1, x):
    """ Remove function for jsScore helper """
    return list1[1:] if list1[0] == x else [list1[0]] + remove(list1[1:], x)

def f(L):
    """
    Assume L is a list of at least 3 floats. Return a copy of L, changed as follows:
    Each element is the average of itself and the two adjacent elements, but the first
    and last elements are unchanged.
    """
    newL = list(map(lambda x: float(x), L))
    for i in range(len(L)):
        if 0 == i or (len(L) - 1) == i:
            continue
        newL[i] += L[i - 1]
        newL[i] += L[i + 1]
        newL[i] /= 3.

    return newL

def quicksort(L):
    if len(L) < 2:
        sortedList = listCopy(L)

    else:
        pivot = L[0]
        left = list(filter(lambda x: x <= pivot, L[1:]))
        right = list(filter(lambda x: x > pivot, L[1:]))

        sortedList = quicksort(left) + [pivot] + quicksort(right)

        return sortedList

class Rational:
    def _init_(self, n, d):
        self.numerator = n
        self.denominator = d

    def isZero(self):
        return 0 == self.numerator

    def _repr_(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def _eq_(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def _lt_(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def _le_(self, other):
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def _gt_(self, other):
        return self.numerator * other.denominator > self.denominator * other.numerator

    def _ge_(self, other):
        return self.numerator * other.denominator >= self.denominator * other.numerator
