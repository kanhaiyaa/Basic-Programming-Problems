def expand(num):

  return [num[index] + '0'*(len(num)-1-index) for index in range(len(num)) if num[index] != '0']

expand(input("Enter a number: "))