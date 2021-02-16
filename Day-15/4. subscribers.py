# Write a function that takes in the id's of the people who subscribed to Netflix and of those who subscribed to Hotstar. Make it return the number of people that have atleast one subscription.

def subcribers(netflix, hotstar):
  return len(set(netflix).union(set(hotstar)))

subscribers([22,24,56,3,5], [44,55,891,24,56])