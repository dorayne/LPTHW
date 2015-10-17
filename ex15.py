# http://learnpythonthehardway.org/book/ex15.html

from sys import argv

script, filename = argv

# open file from argv, assign to variable, print, and then close the file
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

# get filename via raw_input
print "Type the filename again:"
file_again = raw_input("> ")

# open the file from raw_input, assign it to variable, print, and then close the file
txt_again = open(file_again)

print txt_again.read()