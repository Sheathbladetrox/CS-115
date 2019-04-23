# Andrew Chuah and Sequoy Young-Garcia
# I pledge my honor that I have abided by the Stevens Honors System.
# 9/27/2018

#Problem 1:
def dedup(L):
    """ Return a sublist where every duplicate item has been suppressed. Assume L is a list of int's.
    Solution must be recursive (no loops).

    Ex: dedup([3, 4, 3, 2, 1]) --> [3, 4, 2, 1].
        dedup([3, 3, 3, 3]) --> [3]
        dedup([]) --> []
    
    You may find the filter(f,L) function handy, Recall that filter(f,L) returns the sublist of L
    consisting of the items i for which f(i) evaluates to True.

    >>> list(filter(lambda x: x!= 1, [1, 2, 3, 4]))
    [2, 3, 4]
    """
    if not L:
        return []
    else:
        return [L[0]] + list(filter(lambda x: x != L[0], dedup(L[1:])))

# Problem 2:
def jsScore(s, t):
    """ Write a function jsScore(s, t) that takes two strings s and t 
    in input and outputs the "scrabble-jotto score" of s and t, that is,
    the scrabble score of the characters shared by s and t. Multiple occurrences
    of a letter are counted multiple times, as long as they appear multiple times in both strings
    
    Feel free to use map, reduce, filter, recursion, and small helper-functions as appropriate, but no loops.
    Recall that you can convert a string into a list of character using the list(...) built-in function:

    >>> list("hello")
    ['h', 'e', 'l', 'l', 'o']
    
    Note that if either s or t is the empty string, the scrabble-jotto score should be zero!
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
    return list1[1:] if list1[0] == x else [list1[0]] + remove(list1[1:], x)