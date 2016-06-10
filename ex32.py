# http://learnpythonthehardway.org/book/ex32.html

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list with numbers
for number in the_count:
    print "This is count %d" % number

# for-loop goes through a list of strings
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# for-loop of mixed data types
# need to use %r since the contents of the list are not of the same type
for i in change:
    print "I got %r" % i

# starting with an empty list
elements = []

# fill list elements using range
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append i to elements
    elements.append(i)

# print newly built list
for i in elements:
    print "Elements was: %d" % i