# http://learnpythonthehardway.org/book/ex33.html

i = 0
number = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The number: "

for num in numbers:
    print num