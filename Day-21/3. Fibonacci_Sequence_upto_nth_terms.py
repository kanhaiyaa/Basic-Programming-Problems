def fib_sequence(n):

  a = 0
  b = 1

  for index in range(n):
    print(a, end=" ")
    
    temp = a
    a = b
    b = temp + a

fib_sequence(int(input("How many steps you want?: ")))