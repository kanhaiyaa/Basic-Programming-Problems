def prime(n):

  if n <= 1:
    return "Not Prime"

  else:
    for each in range(2, n):
      if n % each == 0:
        return "Not Prime"

  return "Prime Number"

prime(int(input("Enter number: ")))