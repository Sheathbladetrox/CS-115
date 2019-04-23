#CS-115 Exam 3 Review
import math

#Loops
print("===============================================")
print("######### Loops #########")

'''Counts the number of a selected character in a word.'''
def countCharacters(word, character):
    count = 0
    for c in word:
        if c == character:
            count += 1
    return count
print("===============================================")
print(countCharacters("hello", "l"))
print("===============================================")

'''Prints out n rows of the Pascal triangle.'''
def pascal(n):
    p = [[1]]
    for i in range(1, n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row += [1]
            else:
                topleft = p[i - 1][j - 1]
                topright = p[i - 1][j]
                row += [topleft + topright]
        p += [row]
    return p

p = pascal(4)
print(p)
print("===============================================")

for row in p:
    print(row)

print("===============================================")


#Object-Oriented Programming
print("######### Object-Oriented Programming #########")
print("===============================================")

'''Creates an object "point", and initializes it with an x-coordinate and a y-coordinate.'''
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    '''Finds the distance between two given points.'''
    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    #__eq__ overwrites the equal sign, __sub__ for subtraction, etc.
    '''Checks if the two given points are equal to each other.'''
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

pointA = point(1,2)
pointB = point(3,4)
print(pointA.x)
print(pointA.dist(pointB))
print(pointA == pointB)
print("===============================================")

'''Creates an object "animal" and assigns it a sound.'''
class animal:
    def __init__(self, sound):
        self.sound = sound

    def speak(self):
        print(self.sound)

'''Creates an animal object "pig" and inherits speak() from the class "animal".'''
class pig(animal):
    def __init__(self, name):
        self.name = name
        super().__init__("oink!")
    
    def printMyName(self):
        print(self.name)

'''Creates a pig object "piglet" and inherits functions from the class "pig".'''
class piglet(pig):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)
    
    def printMyAge(self):
        print("I'm " + str(self.age) + " years old!")

    def printMyName(self):
        print("Hi! I'm " + self.name + "!")

'''Creates an animal object "cow" and inherits speak() from the class "animal".'''
class cow(animal):
    def __init__(self):
        super().__init__("moo!")

animalA = animal("quack!")
animalA.speak()
print("===============================================")

pigA = pig("Wilbur")
pigA.speak()
pigA.printMyName()
print("===============================================")

cowA = cow()
cowA.speak()
cow().speak()
print("===============================================")

pigletA = piglet("Snowball", 30)
pigletA.printMyAge()
pigletA.printMyName()
print("===============================================")

class Human:
    def __init__(self, gender):
        self.gender = gender
    
    def printGender(self):
        print(str(self.gender))

class Child(Human):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("male")
    
    def printName(self):
        print(self.name)
    
    def printAge(self):
        print(str(self.age))

c1 = Child("Alex", 14)
c1.printGender()

import unittest
VERBOSITY = 2

class TestChild(unittest.TestCase):
    def setUp(self):
        c1 = Child("Jerry", 18)
        c2 = Child("Jerry", 17)
        c3 = Child("Jerry", 20)
        self.cList = [c1,c2,c3]
    
    def test_name_eq(self):
        for c in self.cList:
            self.assertTrue(c.name == c.name)
    
    def test_age_eq(self):
        for c in self.cList:
            self.assertFalse(c.age != c.age)

    def test_gender_eq(self):
        for c in self.cList:
            self.assertTrue(c.gender == c.gender)
    
if VERBOSITY > 1:
    testClassList = [TestChild]
    loadTestsFunction =  lambda C : unittest.TestLoader().loadTestsFromTestCase(C)
    suiteList = list(map(loadTestsFunction, testClassList))
    alltests = unittest.TestSuite(suiteList)

    main = lambda : unittest.TextTestRunner(verbosity=VERBOSITY).run(alltests)
else:
    main = unittest.main
                   
if __name__ == "__main__":
    main()
