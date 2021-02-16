# Write a function that takes in two integers of equal length. Returns the sum of the distance between its idividual digits.

def distance(num1, num2):

  assert len(num1) == len(num2)

  sum = 0

  for digit1, digit2 in zip(list(num1), list(num2)):
    diff = abs(int(digit1)- int(digit2))
    sum = sum + diff

  return sum

  #return sum([abs(int(digit1)- int(digit2)) for digit1, digit2 in zip(list(num1), list(num2))])

n1 = input("Enter a number: ")
n2 = input("Enter another number: ")
distance(n1, n2)