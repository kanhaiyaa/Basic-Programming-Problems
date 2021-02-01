def abbreviations(abbs, words):
  for abb in abbs:

    count = 0
    for word in words:
      if word.startswith(abb):
        count += 1

    if count != 1: return False

  return True

b = [b for b in input("Enter abbreviations using commas").split(",")]
w = [w for w in input("Enter words using commas").split(",")]
abbreviations(b, w)