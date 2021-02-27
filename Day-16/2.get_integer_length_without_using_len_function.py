#4. WAf that takes in a integer and get its length without using the len function.

def get_len(num):

  count = 0
  for each_digit in str(num):
    count += 1
  
  return count

get_len(5555)