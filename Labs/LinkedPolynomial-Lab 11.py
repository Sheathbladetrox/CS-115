import Term-Lab 11

#Andrew Chuah
#Alex Heifler
#I pledge my honor that I have abided by the Stevens Honor System.

############################################
#
# LinkedPolynomial
#
# Adapted in java by Antonio Nicolosi from  
# https://introcs.cs.princeton.edu/java/92symbolic/LinkedPolynomial.java, (c) 2000-2018
# Adapted to Python by Justin Barish, 2018
#
############################################

class LinkedPolynomial:
#this class represents a polynomial, with its terms in a list
#the polynomial will never have any terms with a 0 coefficient  
    def  __init__(self, polyList=[]):
        self.polyList = []

        #make deep copy of the list
        #in doing so, need to make new terms
        for p in polyList:
            self.polyList.append(Term.Term(p.coef, p.exp))

    def addTerm(self, t):
        '''adds a term to the list'''
        self.polyList.append(t)

    def copy(self):
        return LinkedPolynomial(self.polyList)
    
    #creates a polynomial given a list of tuples
    #expects the list to be in the form [(coef1, exp1), (coef2, exp2)...]
    # there must be no duplicate exponents, and exponents must be in descending order
    # ther should be no coefficients of 0 
    def createListFromNumbers(self,numList):
        for i in range (0, len(numList)):
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
            if i ==0:
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
        if len(self) != len(other):
            return False
        for i in range (0, len(self)):
            if self.polyList[i] != other.polyList[i]:
                
                return False
        return True

    def __call__(self, input):
        '''solves the polynomial, putting in input for x
        uses the __call__ function of term to solve this'''
        result = 0
        for i in range (0, len(self)):
            result += self.polyList[i](input)
        return result
    
    def __neg__(self):
        '''negate the polynomial
        does not change the original polynomial, rather returns a new polynomial'''
        res = LinkedPolynomial()
        for i in range(0, len(self)):
            res.addTerm(-self.polyList[i])
        return res

    def __sub__(self, other):
        '''subtracts 2 polynomials, uses negate and add'''
        return self + -other   


############################################################
import unittest
VERBOSITY = 2

#To start the test cases, run the python code and type main()

class TestEq(unittest.TestCase):            
    def setUp(self):
        p1 = LinkedPolynomial()
        p2 = LinkedPolynomial()
        p3 = LinkedPolynomial()
        p4 = LinkedPolynomial()
        p1.createListFromNumbers([(1,1)])
        p2.createListFromNumbers([(2,1),(1,1)])
        p3.createListFromNumbers([(2,1)])
        p4.createListFromNumbers([(2,1),(1,0)])
        self.pList = [p1,p2,p3,p4]
    
    def test_eq_true(self):
        #check that each polynomial is equal with itself
        for p in self.pList:
            self.assertEqual(p,p, "Error with Polynomial " + str(p))

    def test_neq(self):
        #check each pairing of polynomials (note the use of the nested for loop
        #also note the differnt type of for loop used here
        #it could have been the same one as above, but a different one was used here just for example
        for i in range (0, len(self.pList)):
            for j in range (0,len(self.pList)):

                #if i ==j, then we have the same polynomial. We need to skip those cases
                if i != j:
                    self.assertNotEqual(self.pList[i], self.pList[j], "Error with Polynomials " + str(self.pList[i]) + " and " + str(self.pList[j]))

class TestCall(unittest.TestCase):            
    '''Pick 5 polynomials
    At least 2 of them must have at least 1 term with a negative coefficient
    At least 2 must be longer than 2 terms

    On each polynomial, test all numbers from -2 to 2
    Assert that the result of the call is the expected result
    Use a list of polynomials (like used in TestEq), but also have a list of lists of correct answers 
    to verify against ( a list for each polynomial, with each list having the correct answers 
    for invoking call for -2,-1,0,1,2 for that specific polynomial)

    Solution must use loops.
    Note that unlike TestEq where we test eq_true and neq, we will only have 1 test function here.
    '''
    def setUp(self):
        p1 = LinkedPolynomial()
        p2 = LinkedPolynomial()
        p3 = LinkedPolynomial()
        p4 = LinkedPolynomial()
        p5 = LinkedPolynomial()
        p1.createListFromNumbers([(3,1)])
        p2.createListFromNumbers([(2,1),(-1,0)])
        p3.createListFromNumbers([(-2,1)])
        p4.createListFromNumbers([(3,2),(2,1),(1,0)])
        p5.createListFromNumbers([(3,2),(-2,1),(3,0)])
        self.pList = [p1,p2,p3,p4,p5]
    
    def test_call(self):
        a = []
        b = [-6,-3,0,3,6,-5,-3,-1,1,3,4,2,0,-2,-4,9,2,1,6,17,19,8,3,4,11]

        for p in self.pList:
            for i in list(map(lambda x: x-2, range(5))):
                a.append(p(i))
        for x in range(len(a)):
            print(str(b[x])+ " " + str(a[x]))
            self.assertTrue(int(b[x])==int(a[x]))
            
                
                


class TestNeg(unittest.TestCase):
    '''pick 5 polynomials
    at least 2 of them must have at least 1 term with a negative coefficient
    at least 2 must be longer than 2 terms
    Put the 5 polynomials in a list (pListA)

    THEN, iterate over that list, and put a copy of each polynomial into another list (use the copy() 
    function of LinkedPolynomial to make a copy of the polynomial. I.E. newPoly = oldPoly.copy() 
    DO NOT JUST MAKE A COPY OF THE WHOLE LIST. Iterate through the list of polynomials, 
    and make a copy of each one, appending it to your new list (pListB))

    For each polynomial in pListA, negate it
    assert that the result of the negate is the expected result

    THEN assert that the polynomial in pListA that you just negated 
    (the original polynomial, NOT the result of the negation) still equals the original one. 
    Note that negate should return a new negated polynomial, not negate the original.
    I.E. print(p1) --> 2x^2; print(negate(p1)) --> -2x^2;  print(p1) --> 2x^2 NOT -2x^2
    Do this by asserting that the polynomial still equals the matching polynomial in pListB

    Solution must use loops.
    '''
    def setUp(self):
        p1 = LinkedPolynomial()
        p2 = LinkedPolynomial()
        p3 = LinkedPolynomial()
        p4 = LinkedPolynomial()
        p5 = LinkedPolynomial()
        p1.createListFromNumbers([(3,1)])
        p2.createListFromNumbers([(2,1),(-1,1)])
        p3.createListFromNumbers([(-2,1)])
        p4.createListFromNumbers([(3,2),(2,1),(1,0)])
        p5.createListFromNumbers([(3,2),(-2,1),(3,0)])
        self.pListA = [p1,p2,p3,p4,p5]
    
    def test_neg(self):
        pListB = self.pListA.copy()
                
        for p in self.pListA:
            self.assertTrue(p(1) + -p(1) == 0)

        for n in range(len(self.pListA)):
            self.assertTrue(pListB == self.pListA)

    
if VERBOSITY > 1:
    testClassList = [TestEq, TestCall, TestNeg]
    loadTestsFunction =  lambda C : unittest.TestLoader().loadTestsFromTestCase(C)
    suiteList = list(map(loadTestsFunction, testClassList))
    alltests = unittest.TestSuite(suiteList)

    main = lambda : unittest.TextTestRunner(verbosity=VERBOSITY).run(alltests)
else:
    main = unittest.main
                   
if __name__ == "__main__":
    main()
