# http://learnpythonthehardway.org/book/ex13.html

from sys import argv

# playing with argv, assigning the arguments to variables
script, first, second, third = argv

# print the variables from argv
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third