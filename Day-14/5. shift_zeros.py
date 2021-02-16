# Write a function that takes a list of integers and shifts all zeros to end of the list.

def shift_zeros(my_list):

  zeros = my_list.count(0)

  arr = [value for value in my_list if value != 0]

  for zero in range(zeros):
    arr.append(0)

  return arr

shift_zeros([int(x) for x in input("Enter numbers separated by spaces: ").split(" ")])