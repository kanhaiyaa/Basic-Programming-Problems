def super_isogram(sentence):
  for word in sentence.split(' '):
    for letter in word:
      if word.count(letter)>1:
        return False
  return True

super_isogram(input("Enter a sentence: "))