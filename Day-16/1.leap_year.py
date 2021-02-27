def check_leap_year(year):
  
  #if year is divisible by 4 and not a century year.  #if year is a century year then it also divisible by 400
  leap = False
  if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
    learp = True

  return True

check_leap_year(int(input("Enter year: ")))