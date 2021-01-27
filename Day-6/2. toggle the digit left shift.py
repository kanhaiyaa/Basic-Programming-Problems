def toggle(num, pos):

  #left shift the entered number by position 1 and xor with the num
  num ^= (1 << pos)
  return num

x = int(input("Enter an integer: "))
p = int(input("Enter a position: "))

toggle(x, p)