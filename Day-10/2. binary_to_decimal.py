def bin_to_decimal(num):
  assert num == eval(bin(num))

  decimal = 0
  for digit in str(num):
    decimal = decimal*2 + int(digit)

  #binary_form = eval('0b'+str(num))
  #decimal =  int(binary_form) 

  return decimal

bin_to_decimal(int(input("Enter a binary number: ")))