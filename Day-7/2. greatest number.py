def greatest(numbers):

  winner = numbers[0]

  for num in numbers:

    if num > winner:
      winner = num

  return winner

my_list = [int(x) for x in input("Enter numbers separated by commas").split(',')]

greatest(my_list)