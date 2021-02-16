# Reverse a sentence.

def reverse(sen):
  #return sen[::-1]
  for letter in sen[::-1]:
    print(letter, end="")
reverse(input("Enter a sentence: "))