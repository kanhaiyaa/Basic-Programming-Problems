# Write a function that acts as an interpreter that quits on feeding "bye" to it.

def interpreter():
  print(">>>", end="")
  expression = input()
  if expression == 'bye': return
  print(eval(expression))

interpreter()