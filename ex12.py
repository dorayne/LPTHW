# http://learnpythonthehardway.org/book/ex12.html

# # playing with putting prompts in raw_input
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

# printing the info acquired via raw_input as strings
print "So, you're %s old, %s tall and %s heavy." % (
    age, height, weight)