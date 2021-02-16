# Write a funtion that takes in a list of lists and concatenate all the immediate sublists into one.

def my_lists(*lists):
  
  arr = []
  for i in lists:
    for l in i:
      arr.append(l)

  return arr
  #return [i for l in lists for i in l]

my_lists([1,2,3], [4,5,6])