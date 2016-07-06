#################################
#
# Sergei Wallace
#
################################


import random


def main():
    """
    Let's play darts!

    This program simulates the game of darts by producing a random (x,y) pair and evaluating whether it is within the
    target of radius 1, off the target, or off the square board of side length 2 bordering the target. It counts up all
    the darts and categorizes them by where they land. The information is given as a print statement.

    Note, the darts_simulator_v2 has more specification as to where the dart lands on the board by creating rings, as
    is the case in the real game of darts. It does not count the number of times that the darts land in each ring,
    though this can be added rather easily with counters and the appropriate print statement at the end.

    :return: None
    """

    #initialize counters for target categories
    t = 0
    b = 0
    o = 0

    for i in range(1,6,1):

        #constrains the dart location to a square of specified length and width
        xi = round(random.uniform(0,1.3),3)
        yi = round(random.uniform(0,1.3),3)


        #checks if dart lands on the target
        if xi ** 2 + yi ** 2 < 1:

            #counter for number of times dart hits the target
            t += 1

            #print statement if dart is on the target
            print("In the target (outermost ring)! (x: ",xi," y: ",yi,")",sep="")

            #Checks if the dart lands inside the edge of the target by 1% (outermost ring)
            if 0.99 <= xi ** 2 + yi ** 2 <= 1:

                print("Inside the edge of the target by 1% (outermost ring)! (x: ",xi," y: ",yi,")",sep="")

            #Checks if the dart lands in the 4th ring
            if xi ** 2 + yi ** 2 < .75:

                print("In the target (4th ring)! (x: ",xi," y: ",yi,")",sep="")

            #Checks if the dart lands in the 3rd innermost ring
            if xi ** 2 + yi ** 2 < .50:

                print("In the target (3rd ring)! (x: ",xi," y: ",yi,")",sep="")

            #Checks if the dart lands in the 2nd innermost ring
            if xi ** 2 + yi ** 2 < .25:

                print("In the target (2nd ring)! (x: ",xi," y: ",yi,")",sep="")

            #Checks if the dart lands in the innermost ring
            if xi ** 2 + yi ** 2 < .10:

                print("In the target (1st ring)! (x: ",xi," y: ",yi,")",sep="")

            #Checks if the dart is a bullseye
            if xi ** 2 + yi ** 2 < .05:

                print("In the target (bullseye)! (x: ",xi," y: ",yi,")",sep="")

            #Checks if the dart lands exactly on the edge of the target
            if xi ** 2 + yi ** 2 == 1:

                print("On the edge of the target! (x: ",xi," y: ",yi,")",sep="")

        #checks if dart hits the board but not the target
        elif 1 < xi ** 2 + yi ** 2 <= 2 ** (1/2) and xi ** 2 <= 1 and yi ** 2 <= 1:

            #counter for number of times the dart hits board but not the target
            b += 1

            #print statement for number of times the dart hits board but not the target
            print("Outside the target, but on the board! (x: ",xi," y: ",yi,")",sep="")

            #checks if dart lands outside the edge of the target by %1
            if 1 < xi ** 2 + yi ** 2 <= 1.01 and xi ** 2 <= 1 and yi ** 2 <= 1:

                print("Outside the edge of the target by 1%! (x: ", xi, " y: ", yi, ")", sep="")

        #if dart is off board
        else:

           #counter if dart is off the board
            o += 1

            #print statement if dart is off the board
            print("Off the board! (x: ",xi," y: ",yi,")",sep="")

    #print the number of occurrences for the whether the dart is on the target, on the board, or off the board
    print("The number of darts that hit the target are:", t)
    print("The number of darts that missed the target but not the board are:", b)
    print("The number of darts that missed the target and board:", o)
main()
