#Any number which is greater than 1 and only divisible by 1 and itself, is prime number.

def check_prime(num):

  if num <= 1:
    return f"{num} is not a Prime number"

#Check each number between 2 and provide number-1, whether it is divisibile by any number in between.
  else:

    for each in range(2, num):
      if num%each==0:
        return f"{num} is not a Prime number"

    #if above for loop runs successfully, then only this else block will run, so return number is prime.
    else:
      return f"{num} is a Prime number"

check_prime(int(input("Enter an ineger: ")))
