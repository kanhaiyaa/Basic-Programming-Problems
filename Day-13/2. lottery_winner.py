import random
def lottery(names):
  return random.choice(list(set(names)))

n = [n for n in input("Enter  names separated by spaces").split(" ")]
lottery(n)