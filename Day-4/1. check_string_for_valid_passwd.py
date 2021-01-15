def check_valid_passwd(password):

  p = list(password)

  if not (len(password) >= 6 and len(password) <= 12): return False
  if not (any(i.isdigit() for i in p )): return False
  if not (any(i in '#$@' for i in p)): return False
  if not (any(i.isalpha() for i in p)): return False

  return True

check_valid_passwd(input("Enter a string to Check for Valid Password(Ex- Afjdk5j#): " ))
