def remove_vowels(my_str):
    
    """
    This Function removes any vowels in a given string
    
    Used filter() function 
    
    """
    
    return list(filter( lambda x: x not in ['a','e','i','o','u'] , list(my_str)))
