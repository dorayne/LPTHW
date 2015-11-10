# http://learnpythonthehardway.org/book/ex29.html

# initialize variables
people = 20
cats = 30
dogs = 15

# compare the previously initialized variables, print statements if comparison is met
if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

# change variable dogs, adding 5 to previous value
dogs += 5

# since people and dogs are both set at 20, all 3 of these statements will print
if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."