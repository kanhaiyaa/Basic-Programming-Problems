#Write a function that takes two lists and from that, gets the value common in the two lists. Do this without making an intersection on the two sets.
def common(list1, list2):
  return set([num for num in list2 if num in list1])

common([1,2,3,4], [3,4,1,6])