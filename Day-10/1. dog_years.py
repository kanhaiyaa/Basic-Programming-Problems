def dog_years(year):

  assert year >= 0

  if year <= 2:
    return year*10.5
  
  else:
    return (year-2)*4 + 2*10.5

dog_years(int(input("Enter human age in years: ")))