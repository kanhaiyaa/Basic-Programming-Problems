#sum of n natural numbers

def sum_using_recrusion(number):

  if number == 0:
    return 0

  else:
    return number + sum_using_recrusion(number-1)

sum_using_recrusion(5)