# http://learnpythonthehardway.org/book/ex16.html

from sys import argv

script, filename = argv

# Confirm user wants to erase the given file "filename"
# Based on user input, either continue or interrupt the script
print "We're going to erase %r." % filename
print "if you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN"
raw_input("?")

# Open file in write mode
print "Opening the file..."
target = open(filename, 'w')

# Get user input for writing the file
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# Create a string based on user input
new_txt = "%s\n%s\n%s\n" % (line1, line2, line3)

# Write the file using string new_txt
print "I'm going to write these to the file."

target.write(new_txt)

# Close the file
print "And finally, we close it."
target.close()