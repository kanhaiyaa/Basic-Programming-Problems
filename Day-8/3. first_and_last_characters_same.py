def same_subs(sentence):

  """ 
  This function returns the number of times a word has its first and last characters the same as those of entire sentence
  """
  
  count = 0
  
  for word in sentence.split(' '):
    if (word[0]+word[-1]).lower() == (sentence[0]+sentence[-1]).lower():
      count += 1

  return count

same_subs(input("Enter a sentence"))