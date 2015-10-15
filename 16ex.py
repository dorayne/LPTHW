# http://learnpythonthehardway.org/book/ex16.html

from sys import argv

script, filename = argv

# Confirm user wants to erase the given file "filename"
# Based on user input, either continue or interrupt the script
print "We're going to erase %r." % filename
print "if you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN"

raw_input("?")
print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

# Get user input for writing the file
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# Write the filer based on user input
print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Close the file
print "And finally, we close it."
target.close()