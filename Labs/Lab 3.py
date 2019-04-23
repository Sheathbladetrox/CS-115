# I pledge my honor that I have abided by the Stevens Honor System.
# Andrew Chuah
# Alex Heifler
# 9/20/2018

def comb(L, k):
    """ This function will take list L and positive number k and output all combinations of lists with size k. """
    if k == 0:
        return [[]]
    elif not L:
        return []
    else:
        loseIt = comb(L[1:], k)
        useIt = list(map(lambda t : [L[0]] + t, comb(L[1:], k-1)))
        return useIt + loseIt
