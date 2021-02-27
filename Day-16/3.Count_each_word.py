#Count the occurrences of each word in a given sentence and sort the words., Developer-5times, Tester-3Times,, Designer-1 times
import pprint

def sort_and_count(sen):

  mydict = {}

  #sort() - Modifies the original..
  #sorted() - Does't modify the original..will sort and retrun new sorted list

  words = sorted(sen.split(" "))  #sorting based on the character based on the ascii value of character

  for word in words:
    mydict.update({word:words.count(word)})

  pprint.pprint(mydict)

sort_and_count(input("Enter a sentence: "))