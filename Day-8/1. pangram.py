def pangram(sentence):

  for letter in 'abcdefghijklmnopqrstuvwxyz':
    if letter  not in sentence.lower():
      return False
  return True
pangram(input("Enter a sentence: "))