# CS 115 Final Review

# -----------------------Topics----------------------- #
# Binary Conversion #
# Binary Addition/Subtraction #
# Recursion #
# Use it/Lose it #
# n^2 sorting == Bubble, insertion, selection
# Dictionaries #
# Lists #
# For/while loops #
# Tracing Code #
# Flow charts #
# HMM Assembly (tracing) #
# Circuits: Gates, Truth Table, Converting to Equation #
# Classes and Object-Oriented Programming #
# Inheritance #
# Unit Testing #
# -----------------------------------------------------#

# Binary Conversion #

'''
47 |              Divide by 2 all the way down the list
-------           Consider remainders, and build the number
23 |  1           up backwards.
11 |  1
5  |  1
2  |  1
1  |  0
0  |  1

101111

101101010 to decimal
2 + 2^3 + 2^4 + 2^6 + 2^8 = 362

Go from right to left starting from 2^0 onward.

-34 to binary

34 = 100010
-34 = 011101 + 000001 = 011110

Negate the binary number and then add 1.

'''

# Binary Addition/Subtraction #

'''
  1001110
+ 0101101
---------
  1111011

  00101101
- 01110100
----------
This expression is equal to:

  00101101
+ 10001100
----------
  10111001

Negate the number that is going to subtract, not the one that is being subtracted from

'''
print("-------------------------------")
# Recursion #

def fibo(n):
    # f(0) = 0; f(1) = 1; f(n) = f(n-1) + f(n-2)
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(4))
print('-------------------------------')

# Use it/Lose it #

def knapsack(items, w_max, value = 0):
    if not items:
        # No items #
        return value
    
    # Grab item at the head #
    wt, val = items[0]

    # Value if the item is lost #
    no = knapsack(items[1:], w_max, value)

    if wt < w_max:
        # Value if the item is used #
        yes = knapsack(items[1:], w_max - wt, value + val)

        # Choose the better of the two cases #
        return max(yes, no)
    else:
        # Item is too heavy #
        return no
items = [
    # Soda #
    (1,4),
    # Sword #
    (2,4),
    # Shield #
    (3,2),
    # Armor #
    (4,7)
]
max_wt = 6

print("Items: ", items)
print("Max Weight: ", max_wt)
print("Best: ", knapsack(items, max_wt))

# n^2 Sorting #
# Know how the sorts work #
'''
def bubblesort(arr):
    for i in range(len(arr)-1):
        # Sift the largest unsorted element backward #
        for j in range(1, len(arr)-i):
            if arr[j-1] > arr[j]:
                swap(arr, j-1, j)

def insertionsort(arr):
    
    Example:
    1 3 5 2 4 |
    1 3 2 5 4 |
    1 2 3 5 4 |
    1 2 3 4 5 V
    
    for i in range(len(arr)-1):
        # Insert the ith item into the sorted section #
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                # Item is still out of order #
                swap(arr, j-1, j)
            else:
                # List is sorted #
                break

def selectionsort(arr):
    
    Example:
    1 3 5 2 4 |
    1 2 5 3 4 |
    1 2 3 5 4 |
    1 2 3 4 5 V
    
    for i in range(len(arr)-1):
        # Find the index of the smallest unsorted element #
        p = i
        for j in range(i+1, len(arr)):
            if arr[p] > arr[j]:
                p = j
        
        # Place the element at the end of the list #
        swap(arr, i, p)
'''

# For Loop #

a = "Hello World"
for c in a:
    print(c)
print("-------------------------------")

for i in range(0,10):
    print(i)
print("-------------------------------")

column = [[]]
for i in range(1,12):
    row = []
    for j in range(1,12):
        row += [i*j]
    column += [row]

for i in column:
    print(i)
print('-------------------------------')

# Dictionaries and While Loop #

password_dictionary = {
    "password": "trigger",
    "emacs": "valid",
    "recursion": "valid",
    "nicolosi": "trigger",
    "": "trigger"
}

guess = ""
while password_dictionary[guess] == "trigger":
    guess = input("Guess my password: ")
print("-------------------------------")
