# http://learnpythonthehardway.org/book/ex3.html

print "I will now count my chickens:"

# Some basic arithmetic
print "Hens", float(25 + 30 / 6)
print "Roosters", float(100 - 25 * 3 % 4)

print "Now I will count the eggs:"

# A really complicated way to get to 7, demonstrating PEMDAS
print float(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print "Is it true that 3 + 2 < 5 - 7?"

# Some basic inequalities
print float(3 + 2) < float(5 - 7)

print "What is 3 + 2?", float(3 + 2)
print "What is 5 - 7?", float(5-7)

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2