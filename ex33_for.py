# http://learnpythonthehardway.org/book/ex33.html

def for_func(max_num, inc_num):
    # initialize variables
    i = 0
    number = []
    for i in range(max_num):
        print "At the top i is %d" % i
        # append i to number list
        number.append(i)
    
        # increment i
        # this line still changes the value of i for the 'at the bottom' print statement
        # but has no effect on the value of i in 'for i in range'
        # i = i + inc_num
        print "Numbers now: ", number
        print "At the bottom i is %d\n" % i

    print "The numbers: "

    # print the contents of number list, 1 per line
    for num in number:
        print num

raw_num = raw_input("What is the maximum number you would like your variable to reach? ")
int_num = int(raw_num)

inc_raw = raw_input("By what interval do you want your variable to increment? ")
inc_num = int(inc_raw)

for_func(int_num, inc_num)