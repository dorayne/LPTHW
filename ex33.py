# http://learnpythonthehardway.org/book/ex33.html

# initialize variables
i = 0
number = []

while i < 6:
    print "At the top i is %d" % i
    # append i to number list
    number.append(i)
    
    # increment i
    i = i + 1
    print "Numbers now: ", number
    print "At the bottom i is %d\n" % i

print "The numbers: "

# print the contents of number list, 1 per line
for num in number:
    print num