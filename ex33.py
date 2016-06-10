# http://learnpythonthehardway.org/book/ex33.html

def while_func(num):
    # initialize variables
    i = 0
    number = []
    while i < num:
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

raw_num = raw_input("Enter maximum number: ")
int_num = int(raw_num)

while_func(int_num)