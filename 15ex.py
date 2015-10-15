# http://learnpythonthehardway.org/book/ex15.html

from sys import argv

script, filename = argv

# open file from argv, assign to variable txt and print it
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

# get filename from raw_input, open it, assign to new variable, and print it
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()