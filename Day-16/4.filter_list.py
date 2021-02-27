# [10,20,30,40,50,60,70,80,90,100] filter this list as [10,30,60,100].

def filter_this(my_list):

  count = 0
  next = 2
  new_list = []

  for index in range(0, len(my_list)):
    if index == count:
      new_list.append(my_list[index])

      count += next
      next += 1

  return new_list

filter_this([10,20,30,40,50,60,70,80,90,100])