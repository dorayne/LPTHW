# http://learnpythonthehardway.org/book/ex6.html

# initialize variables for future printing
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# print x and y twice, 2nd time as parts of a larger string
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

"""
initialize some more variables
joke_evaluation includes format character %r
will always print %r unless a value is specified at the end of the line
"""
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation # showing printed %r
print joke_evaluation % hilarious # showing the full string

# initializing some more variables for printing
w = "This is the left side of..."
e = "a string with a right side."

print w + e