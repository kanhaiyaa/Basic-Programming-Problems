def to_gerund(verb):
  if verb[-1] == 'e':
    return verb[:-1] + 'ing'
  
  if verb[-3:] != 'ing':
    return verb + 'ing'