# Andrew Chuah and Bhagyesh Patel
# I pledge my honor that I have abided by the Stevens Honor System.
# 10/4/2018

# Problem 1
def decimal2R2L(x):
    """
    Convert the non-negative integer x into binary using R2L list representation.

    Under R2L (right-to-left), a binary number (b_k, ..., b_1,b_0)_2 is represented
    as a list of ints in right-to-left (i.e.,least-to-most significant) order, [b_0, b_1, b_k].

    For example, the R2L representation of the decimal number 6 (which is 110 in binary),
    is [0, 1, 1], whereas the R2L representation of the 16, (which is 10000 in binary),
    is [0, 0, 0, 0, 1].
    
    As a special case, zero can be represented both as an empty list[] or as [0].
    """
    if x == 0:
        return []
    else:
        return [x % 2] + decimal2R2L(x // 2)

# For the decimal2R2L function
print(decimal2R2L(0))
print(decimal2R2L(1))
print(decimal2R2L(42))
print(decimal2R2L(5))
print(decimal2R2L(12))

print("==========================") # Divider

# Problem 2
def R2L2decimal(num):
    """
    Convert the number num from R2L list representation to decimal.
    """
    if not num:
        return 0
    elif num[-1] == 0:
        return (R2L2decimal(num[:-1]))
    else:
        length = len(num) - 1
        return (R2L2decimal(num[:-1])) + (2**length)

# For the R2L2decimal function
print(R2L2decimal([]))
print(R2L2decimal([1]))
print(R2L2decimal([0,1,0,1,0,1]))
print(R2L2decimal([1,0,1]))
print(R2L2decimal([0,0,1,1]))

print("==========================") # Divider

# Problem 3
def incrementR2L(num):
    """
    Increment by one the binary number num in R2L representation.
    """
    if not num:
        return 0
    else:
        return decimal2R2L(R2L2decimal(num) + 1)

# For the incrementR2L function
print(incrementR2L(0))
print(incrementR2L([1,1]))
print(incrementR2L([0,1,0,1]))
print(incrementR2L([1,1,0,1]))
print(incrementR2L([0,1,1]))

print("==========================") # Divider

# Problem 4
def addR2L(num1, num2):
    """
    Add two binary numbers under R2L representation.
    Make sure to handle the case where the two inputs are represented by lists of differing length.
    """
    if not num1:
        return num2
    elif not num2:
        return num1

    extra = addR2L(num1[:-1], num2[:-1])

    if num1[-1] == 0:
        return extra + [num2[-1]]
    if num2[-1] == 0:
        return extra + [1]

    return [0] + addR2L(extra, [1])

# For the addR2L function
print(addR2L([0], [0]))
print(addR2L([1,1], [1]))
print(addR2L([1], [1,0,1]))
print(addR2L([1,0,1,0,1], [0,0,1,1]))
print(addR2L([0,1,0,0,1], [1,0,1]))