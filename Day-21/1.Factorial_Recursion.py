#factorial of number

def fact_recursion(number):

  if number <= 0:
    return 0

  elif number == 1:
    return 1

  else:
    return number * fact_recursion(number-1)

fact_recursion(5)