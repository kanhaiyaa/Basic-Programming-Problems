def first_digit(n):

  while len(str(n)) != 1:

    n = n // 10

  return n

first_digit(int(input("Enter number: ")))