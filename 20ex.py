# http://learnpythonthehardway.org/book/ex20.html

from sys import argv

script, input_file = argv

def print_all(f):
    # small function, prints the entire file
    print f.read()

def rewind(f):
    # sets file position back to the beginning
    f.seek(0)

def print_a_line(line_count, f):
    # prints the line count and the string from that line
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"
# run function print_all to print the entire file
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# run function rewind to reset file position
# without this call, the current_line calls would only print the line count
rewind(current_file)

print "Let's print three lines:"
# print the line count and line string
# simple iteration without a loop
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)