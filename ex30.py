# http://learnpythonthehardway.org/book/ex30.html

people = 30
cars = 40
trucks = 15

# Are there more cars than people?
if cars > people:
    print "We should take the cars."
# Are there more people than cars?
elif cars < people:
    print "We should not take the cars."
# Are there the same amount of people and cars?
else:
    print "We can't decide."

# Are there more trucks than cars?
if trucks > cars:
    print "That's too many trucks."
# Are there more cars than trucks?
elif trucks < cars:
    print "Maybe we could take the trucks."
# Are there the same amount of trucks and cars?
else:
    print "We still can't decide."

# Are there more people than trucks?
if people > trucks:
    print "Alright, let's just take the trucks."
# Are there less people than trucks or the same amount of people and trucks?
else:
    print "Fine, let's stay home then."