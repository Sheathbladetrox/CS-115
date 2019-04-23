# I pledge my honor that I have abided by the Stevens Honor System.
# Andrew Chuah

class Term:
    def __init__(self, coef=0, exp=0):
        self.coef = coef
        self.exp = exp
        
    def __str__(self):
        ans = ""
        return ans+ str(self.coef) + "x^" + str(self.exp)
        
    def __eq__(self, other):
        '''returns true if the two terms are equal'''
        return self.coef == other.coef and self.exp == other.exp
    
    def __call__(self, input):
        '''returns the result of coef * input ^exp
        note that power in python is x**y'''
        return self.coef*(input**self.exp)
    
    def __neg__(self):
        '''returns a new term, with the coef negated'''
        return Term(-self.coef, self.exp)
    
