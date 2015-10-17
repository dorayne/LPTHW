# http://learnpythonthehardway.org/book/ex24.html

print "Let's practice everything."
# Playing with \ escapaes
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

# Playing with arithmetic
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    # function takes a starting value returns number of jelly_beans, jars, and crates
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# set starting value of 10,000, call secret formula
start_point = 10000
# set variables beans, jars, and crates to hold secret_formula return
beans, jars, crates = secret_formula(start_point)

# print data from previous calculations
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# set new start_point by dividing previous value by 10
start_point = start_point / 10

# call the function via the print statements instead of on separate lines
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)