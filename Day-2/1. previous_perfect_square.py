import math
def prev_perfect_square(num):

  #get square root of number
  sqrt = math.sqrt(num)

  #check if square root is integer, if yes then number provided is perfect square
  assert ( sqrt - math.floor(sqrt) == 0 ), "Provided number is not perfect square"

  #get previous perfect square

  prev = sqrt-1

  return prev**2

prev_perfect_square(int(input("Enter Positive Integer: ")))
