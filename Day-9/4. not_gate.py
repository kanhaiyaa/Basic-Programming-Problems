def not_gate(digit):
  
  assert digit in [0,1], "Please Enter only Binary number"

  return 1 - digit
  #or return [1,0][digit]

not_gate(int(input("Enter a binary number: ")))