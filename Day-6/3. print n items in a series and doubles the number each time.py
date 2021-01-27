def doubles(n):

  #series starts at 3
  num = 3

  for index in range(n):

    #left shift the number to double it
    num = num << 1

    print(num)

doubles(int(input("How many times you want to print: ")))