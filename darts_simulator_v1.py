#################################
#
# Sergei Wallace
#
#################################

import random


def main():
    """
    Let's play darts!

    This program simulates the game of darts by producing a random (x,y) pair and evaluating whether it is within the
    target, outside of the target, or off the board surrounding the target. It counts up all the darts and categorizes
    them by where they land. The information is given as a print statement.

    :return: None
    """

    #initialize counters for target categories
    t = 0
    b = 0
    o = 0
    for i in range(1,6,1):

        #constrains the dart location to a square of specified length and width
        xi = random.uniform(-1.3,1.3)
        yi = random.uniform(-1.3,1.3)

        #checks if dart lands on the target
        if (xi ** 2 + yi ** 2) ** 0.5 <= 1:

            #counter for number of times dart hits the target
            t += 1

            #print statement if dart is on the target
            print("In the target! (x: ",xi,", y: ",yi,")",sep="")

        #checks if dart hits the board but not the target
        elif abs(xi) > 1 or abs(yi) > 1 or (xi ** 2 + yi ** 2) ** 0.5 > 2 ** 0.5:

            #counter for number of times the dart hits board but not the target
            b += 1

            #print statement for number of times the dart hits board but not the target
            print("Outside the target! (x: ",xi,", y: ",yi,")",sep="")

        #if dart is off board
        else :

            #counter if dart is off the board
            o += 1

            #print statement if dart is off the board
            print("Outside the target! (x: ",xi,", y: ",yi,")",sep="")

    #print the number of occurrences for the whether the dart is on the target, on the board, or off the board
    print("Inside the target:",t)
    print("Outside the target:",b)
    print("Off the board:",o)

main()
