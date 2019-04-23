import Term

############################################
#
# LinkedPolynomial
#
# Adapted in java by Antonio Nicolosi from  
# https://introcs.cs.princeton.edu/java/92symbolic/LinkedPolynomial.java, (c) 2000-2018
# Adapted to Python by Justin Barish, 2018
#
############################################

# I pledge my honor that I have abided by the Stevens Honor System.
# Andrew Chuah

class LinkedPolynomial:
#this class represents a polynomial, with its terms in a list
#the polynomial will never have any terms with a 0 coefficient  
    def  __init__(self, polyList=[]):
        self.polyList = polyList.copy()


    def addTerm(self, t):
        '''adds a term to the list'''
        self.polyList.append(t)
        
    #creates a polynomial given a list of tuples
    #expects the list to be in the form [(coef1, exp1), (coef2, exp2)...]
    # there must be no duplicate exponents, and exponents must be in descending order
    # ther should be no coefficients of 0 
    def createListFromNumbers(self,numList):
        for i in range (0, len(numList)):
            
			#note here that the first Term specifies the python package (import Term),
			#and the second Term is the name of the object/class, (class Term)
			#In this exercise. they are the exact same name, but they don't always have to be.
            t = Term.Term(numList[i][0], numList[i][1])
            self.polyList.append(t)
            
    def __len__(self):
        return len(self.polyList)
    
    def __str__(self):
        '''converts the polynomial to a string'''
        ans=""
        for i in range (0, len(self.polyList)):
            coef = self.polyList[i].coef
            exp = self.polyList[i].exp
            if i == 0:
                ans = str(coef) + "x^" + str(exp)
            elif coef > 0:
                ans = ans + " + " + str(coef) + "x^" + str(exp)
            elif coef < 0:
                ans = ans + " - " + str(-coef) + "x^" + str(exp) 
        return ans

    
        
    def __add__(self, otherPoly):
        '''adds 2 polynomials together'''
        result = LinkedPolynomial()
        i = 0
        j = 0

        #since each polynomial might have a different length,
        # need to go until we reach the end of BOTH
        # but, since we might reach the end of one first,
        # we need to ensure we check for that
        #We will use i as our counter for the list for this polynomial (self), and j as the counter
        # for the list for the other polynomial (otherPoly)
        while i < len(self) or j <len(otherPoly) :

            #see if we already reached the end of this polynomial
            if i < len(self):
                x = self.polyList[i]

            #see if we already reached the end of the other polynomial
            if j < len(otherPoly):
                y = otherPoly.polyList[j]

            #if at the end of this polynomial, simply append the next element in the other polynomial.
            #since we took an element from the other polynomial, we need to increment its counter, j
            if i >= len(self):
                result.addTerm(Term.Term(y.coef, y.exp))
                j+=1

            #if at the end of other polynomial, simply append the next element in this polynomial
            #since we took an element from this polynomial, we need to increment its counter, i
            elif j >= len(otherPoly):
                result.addTerm(Term.Term(x.coef, x.exp))
                i+= 1

            #since they may not always have the same terms, if this exponent is bigger than the other one,
            #use it
            #since we took an element from this polynomial, we need to increment its counter, i
            elif x.exp > y.exp:
                result.addTerm(Term.Term(x.coef, x.exp))
                i+=1

            #since they may not always have the same terms, if the other exponent is bigger than this one,
            #use it
            #since we took an element from the other polynomial, we need to increment its counter, j
            elif x.exp < y.exp:
                result.addTerm(Term.Term(y.coef, y.exp))
                j+=1

            #if the exponents are the same, we can combine the coefficients.
            #since we took an element from BOTH polynomials (And added them), we need to increment BOTH counters
            else:
                coef = x.coef + y.coef
                exp = x.exp # could also be y.exp
                if(not coef == 0):
                    result.addTerm(Term.Term(coef, exp))
                i+=1
                j+=1
        return result
            
    def __mul__(self, otherPoly):
        '''multiply 2 polynomials together'''
        a = self.polyList
        b = otherPoly.polyList
        result = LinkedPolynomial()
        for i in range(0, len(a)):
            temp = LinkedPolynomial()
            for j in range (0, len(b)):
                temp.addTerm(Term.Term(a[i].coef * b[j].coef, a[i].exp + b[j].exp))
            result = result+temp
        return result
            
            
    def __eq__(self, other):
        '''checks if 2 polynomials are equal. Note no polynomials will have 0-coefficient terms
        to implement this, use the __eq__ function in Term.py'''
        a = len(self.polyList)
        b = len(other.polyList)
        checkArr = []
        if a > b or a < b:
            return False
        else:
            for i in range(0, a):
                coef = self.polyList[i].coef
                exp = self.polyList[i].exp
                o_coef = other.polyList[i].coef
                o_exp = other.polyList[i].exp

                check = Term.Term.__eq__(Term.Term(coef, exp), Term.Term(o_coef, o_exp))
                checkArr.append(check)

            if checkArr.count(checkArr[0]) == len(checkArr):
                if checkArr[0] == True:
                    return True
                elif checkArr[0] == False:
                    return False
            else:
                return False

    def __call__(self, input):
        '''solves the polynomial, putting in input for x
        uses the __call__ function of term to solve this'''
        for i in range(0, len(self.polyList)):
            coef = self.polyList[i].coef
            exp = self.polyList[i].exp
            result = 0
            if i == 0:
                ans = Term.Term.__call__(Term.Term(coef, exp), input)
                result = ans
            else:
                ans = ans + Term.Term.__call__(Term.Term(coef, exp), input)
                result = ans
        return result

    def __neg__(self):
        '''negate the polynomial
        does not change the original polynomial, rather returns a new polynomial
		uses the __neg__ function of term'''
        result = LinkedPolynomial()
        for i in range(0, len(self.polyList)):
            coef = self.polyList[i].coef
            exp = self.polyList[i].exp
            result.addTerm(Term.Term.__neg__(Term.Term(coef, exp)))
        return result

    def __sub__(self, other):
        '''subtracts 2 polynomials, uses negate and add'''
        b = LinkedPolynomial.__neg__(other)
        result = LinkedPolynomial.__add__(self, b)
        return result

##basic tests##
l = LinkedPolynomial()
l.createListFromNumbers([(2,2),(1,1)])
print(l)
p = LinkedPolynomial()
p.createListFromNumbers([(3,2),(-5,1)])
print(p)
r =l*p
print(r)
print(l == p)
print(l(2))
print(-p)
print(l-p)
