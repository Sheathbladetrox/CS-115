# Andrew Chuah
# Michael DelGaudio
# I pledge my honor that I have abided by the Stevens Honor System.
# 9/13/2018

#Problem 1:
def dotProduct(L, K):
    """ This function will output dot products of lists L and K. """
    if L == [] or K == []:
        return 0.0
    else:
        return dotProduct(L[1:], K[1:]) + (L[0]*K[0])

#Problem 2
def expand(S):
    """ This function will take a string and put each letter into a list. """
    if type(S) == type(0):
        return S
    elif S == "":
        return ""
    else:
        return [S[0]] + expand(S[1:])

#Problem 3
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

#Problem 4
def removeAll(e, L):
    """ This function will find the input e in a list L and remove it. """
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])

#Problem 5
def deepReverse(L):
    """ This function will take a list L and reverse it. """
    if not L or type(L) == type(0):
        return L
    else:
        return deepReverse(L[1:]) + [deepReverse(L[0])]
