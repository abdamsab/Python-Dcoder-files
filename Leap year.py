year = int(input("Enter a year: "))

#
# Write your code here.
#  
if year >= 1582:
  if year % 4 == 0:
    if year % 100 == 0:
    
      if year % 400 == 0:
        print("Leap year")
      else:
        print("Common year")
    
    else:
      print("Leap year")    
  
  else:
    print("Common year")

else:
  print("Not within the Gregorian Calender period")
  