#Fibonacci nth term

def fib(n):

  if n < 0:
    return "Incorrect Input"
  
  if n == 0:
    return 0

  if n == 1 or n == 2:
    return 1

  else:
    return fib(n-1) + fib(n-2)

fib(int(input("Enter a number: ")))