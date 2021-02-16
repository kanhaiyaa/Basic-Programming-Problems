#Game of tuples. Write a function that asks the user to input a string of integers separated by spaces. it then returns a tuple from these values.
def my_tuple(s):
  return tuple([int(item) for item in s.split(" ")])

my_tuple(input("Enter a string of numbers separated by space"))