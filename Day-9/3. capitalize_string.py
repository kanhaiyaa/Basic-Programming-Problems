def capitalize(mystr):

  """
  This function capitalize the letter if ascii value of letter is even 
  
  and lowercase if ascii value is odd
  """

  for letter in mystr:

    if ord(letter) % 2 == 0:
      print(letter.upper(), end="")
    
    else:
      print(letter.lower(), end="")

capitalize("kanha")