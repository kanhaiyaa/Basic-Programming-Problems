# Conflicts - A function takes in a list. Adjacent numbers don't like to stand together. Write a function that creates tuples from alternate numbers in the list.

def conflicts(my_list):
  return list(zip(my_list[:], my_list[2:] ))
conflicts([1,2,3,4,5,6,7])