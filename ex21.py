# http://learnpythonthehardway.org/book/ex21.html

def add(a, b):
    # function for addition
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    # function for subtraction
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    # function for multiplication
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    # function for division
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"
# Calling the previous functions, assigning their returns to variables
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# printing the variables 
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."
"""
nested function calls, using previously stated variables
1: divide iq by 2
2: multiply weight by step 1
3: subtract step 2 from height
4: add age and step 3
"""
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"