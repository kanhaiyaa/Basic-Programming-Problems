# Write a function that takes in an integer, then check whether it is greater than the integer that of its mirror image.


def mirror(num):

  mr = str(num)[::-1]

  return num > int(mr)

mirror(int(input("Enter an integer: ")))