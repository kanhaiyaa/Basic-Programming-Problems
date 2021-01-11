#Remove Vowels

#Using List Comprehension
def remove_vowels(my_str):
    return [my_str[x] for x in range(len(my_str)) if my_str[x] not in ['a','e','i','o','u']]
