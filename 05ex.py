# http://learnpythonthehardway.org/book/ex5.html

# initialize variables for future user
name = 'Dorayne'
age = 31 # not a lie
height = 63 # inches
eyes = 'Blue'
teeth = 'White'
hair = 'Lavender'

# print statements using previous variables
print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, I get %d." % (
age, height, age + height)