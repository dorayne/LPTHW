# http://learnpythonthehardway.org/book/ex35.html

from sys import exit

def gold_room():
    # this room is accessed by the door behind the door
    print "This room is full of gold. How much do you talk?"
    
    choice = raw_input("> ")
    
    # poor design. This only recognizes numbers that contain a 1 or a 0
    # i.e. with this logic, 85 is not a number
    if "0" in choice or "1" in choice:
        how_much=int(choice)
    else:
        dead("Man, learn to type a number.")
    
    # the only method to win the game
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    # this room is accessed by the left door in the starting room
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    while True:
        choice = raw_input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    # this room is accessed by the right door in the starting room
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for you life or eat your head?"
    
    choice = raw_input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty.")
    else:
        cthulhu_room()

def dead(why):
    # getting the method of death from the other functions
    # exiting the game
    print why, "Good job!"
    exit(0)

def start():
    # the starting room
    # can also be accessed by fleeing Cthulhu_room
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    choice = raw_input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()