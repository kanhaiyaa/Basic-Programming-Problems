# Use List comprehension to build a function that returns multiple of 3 that are smaller than the number n

def my_list(num):
  return [item for item in range(num) if item%3 == 0]

my_list(int(input("Enter a number: ")))