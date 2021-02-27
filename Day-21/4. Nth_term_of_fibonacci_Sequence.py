def fib_recursion(n):

  if n == 0:
    return 0

  if n == 1:
    return 1

  else:
    return fib_recursion(n-1) + fib_recursion(n-2)

fib_recursion(5)