#Prime Number
def is_prime(num):

  prime = True
  
  if num < 1:
    prime = False
    return prime

  else:
    for each_number in range(2, num):
      if num % each_number == 0:
        prime = False
        return prime
  
  return prime

is_prime(int(input("Enter a number: ")))