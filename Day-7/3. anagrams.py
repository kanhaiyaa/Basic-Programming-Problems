def anagram(word1, word2):
  return sorted(word1.lower()) == sorted(word2.lower())

w1 = input("Enter a string: ")
w2 = input("Enter another string: ")

anagram(w1, w2)