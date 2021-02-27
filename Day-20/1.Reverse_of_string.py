def reverse(sen):
  #return sen[::-1]

  l = len(sen)-1
  rev_sen = ''
  for each in range(l, -1, -1):
    rev_sen += sen[each]

  return rev_sen
    
reverse(input("Enter a string: "))