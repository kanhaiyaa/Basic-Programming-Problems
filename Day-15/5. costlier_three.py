#The costiliest three: you are given a dictionary holding items form a store, and their prices. Write a function that returns the items with the highest price, the second highest and the third heighest. If two items costs the same. Include both.

def the_costiliest_three(items):
  for item in [(item, price) for (item, price) in items.items() if price in sorted(items.values())[-3:]]:
    print(item)

the_costiliest_three({'shoes': 79, 'scarves': 25, 'berets':39, 'bodysuits':59})