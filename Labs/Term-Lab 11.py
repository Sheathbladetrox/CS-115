class Term:
    def __init__(self, coef=0, exp=0):
        self.coef = coef
        self.exp = exp
    def __str__(self):
        ans = ""
        return ans+ str(self.coef) + "x^" + str(self.exp)
    def __eq__(self, other):
        return self.coef == other.coef and self.exp == other.exp

    def __call__(self, input):
        return self.coef * input**self.exp

    def __neg__(self):
        return Term(-self.coef, self.exp)

