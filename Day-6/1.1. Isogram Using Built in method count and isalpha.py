def is_isogram(word):

  for letter in word:
    if word.count(letter)>1 and letter.isalpha(): return False

  return True
is_isogram(input("Enter a string: "))