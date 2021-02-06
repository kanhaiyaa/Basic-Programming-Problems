# Fibonacci series

def n_terms(n):
  first = 0
  second = 1

  for i in range(n):
    print(first, end=" ")
    
    temp = first
    first = second
    second = temp + second

n_terms(int(input("Enter a number: ")))