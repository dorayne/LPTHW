# http://learnpythonthehardway.org/book/ex5.html

# initialize static variables for future arithmetic and printing
name = 'Dorayne'
age = 31 # not a lie
height = 63 # inches
eyes = 'Blue'
teeth = 'White'
hair = 'Lavender'

# initialize relative variable for future printing
height_cm = height / 0.39370

# print statements using previous variables
print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "Which is %f centimeters tall." % height_cm
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %f, I get %f." % (
age, height, height_cm, age + height + height_cm)