#Write a function that takes in a list of tuples of items and their prices. Make it return a list of items and another list of theri prices
def groceries(grocery_list):
  items, prices = zip(*grocery_list)
  return list(items), list(prices)

groceries([('milk', 29),('eggs', 19),('bananas', 40)])