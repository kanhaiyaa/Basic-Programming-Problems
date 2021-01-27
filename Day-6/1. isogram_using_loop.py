def is_isogram(word):

  #Nested Loops
  for letter in range(len(word)):
    
    #Store each word one by one, starting from first word
    first = word[letter]

    for each in range(len(word)):

      #Check if word is hyphen or space or the same word that we stored
      if (word[each] == first and each == letter) or (word[each] == " ") or (word[each] == "-"):
        continue
      
      #If Stored word appear more than once
      elif word[each] == first and each != letter:
        return ("{} is not Isogram".format(word))
  
  #If loop runs successfully, It means there is no repeating character.
  else:
    return ("{} is Isogram".format(word))

is_isogram(input("Enter a string: "))