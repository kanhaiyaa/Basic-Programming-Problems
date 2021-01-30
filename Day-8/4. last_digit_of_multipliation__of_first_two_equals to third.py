
# Write a function that takes 3 integers and returns ture if the last digit of the result of multiplication of first two equals that of the third.


def last_digit(num1, num2, num3):

  mul = num1*num2

  if str(mul)[-1] == str(num3):
    return True

  return False

last_digit(5,4,4)