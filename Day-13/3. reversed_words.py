def reverse_words(sen):

  my_list = sen.split( )

  for word in my_list:
    for letter in word[::-1]:
      print(letter, end="")

    print(end=" ")
reverse_words("Hello My name is kanhaiya")