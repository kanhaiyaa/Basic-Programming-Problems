def mulitply_list(my_list):

  return ([x*len(my_list) for x in my_list])

mulitply_list([int(v) for v in input("Enter numbers separated by commas , : ").split(",")])