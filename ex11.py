# http://learnpythonthehardway.org/book/ex11.html

# playing with raw_input
# ended print statements with , to prevent ending with a new line
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# printing the info acquired via raw_input as strings
print "So, you're %s old, %s tall, and %s heavy." % (
    age, height, weight)