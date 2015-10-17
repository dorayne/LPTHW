# http://learnpythonthehardway.org/book/ex17.html

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# confirm the from and to files
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# state the length of the from file
print "The input file is %d bytes long" % len(indata)

# confirm the to file exists
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL_C to abort."
raw_input()

# perform file copy based on previous user input
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

# close files
out_file.close()
in_file.close()