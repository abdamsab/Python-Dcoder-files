def is_year_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#
# Your code from LAB 4.3.1.6.
#


def days_in_month(year, month):
  
  days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  total = 0
  if is_year_leap(year):
    days_of_month[1] = 29
  
  for i in range((month-1)):
    total += days_of_month[i]
    
  return total
    
"""
  if is_year_leap(year):
    if month == 2:
      return 29
    else:
      return days_of_month[month-1]
  else:
    return days_of_month[month-1]
"""
"""
 Your task is to write and test a function which takes three arguments
  (a year, a month, and a day of the month) and returns the 
  corresponding day of the year, or returns None if any of the 
  arguments is invalid.

Use the previously written and tested functions. 
Add some test cases to the code. This test is only a beginning.
 """
    
    
def day_of_year(year, month, day):
  
  result = days_in_month(year, month)
  
  return result + day
#
# Write your new code here.
#

print(day_of_year(2000, 12, 30))
