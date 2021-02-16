# A Palindrome is a value that reads same from backwords and from front.

def palindrome(value):
  return value == value[::-1]

palindrome(input("Enter any value"))