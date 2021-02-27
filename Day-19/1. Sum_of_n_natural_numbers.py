def sum_of_n_natural_numbers(number):

  sum = 0

  while number != 0:
    sum = sum + number
    number -= 1

  return sum

sum_of_n_natural_numbers(int(input("Enter a number: ")))