# Write a function that accepts some numbers in a list and then prints the ones appearing in the list more than ones

def duplicates(numbers):

  dup = []

  for num in numbers:
    if numbers.count(num) > 1:
      if num not in dup:
        dup.append(num)
  
  return f"Duplicate numbers are {dup}"

duplicates([int(x) for x in input("Enter numbers separated by commas , :").split(",")])