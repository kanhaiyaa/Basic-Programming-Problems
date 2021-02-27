def factorial(n):

  if n <= 0:
    return "Please Provide a positive integer."

  fact = 1

  for i in range(n, 0, -1):
    fact = i*fact

  return fact

factorial(int(input("Enter a number: ")))