import math

def next_perfect_square(num):

    #get sqrt of number
    sr = math.sqrt(num)

    #check if sqrt is integer to ensure entered number is itself perfect square.
    assert ( sr - math.floor(sr) ) == 0, "Provided number is not a perfect square..Try Again"

    #get the floor value of sqrt and add 1 to it
    next_num = math.floor(sr)+1

    return next_num**2

next_perfect_square(int(input("Enter an integer: ")))