
print("FINDING DIGIT OF LIFE!!\n")

dates = input("Enter date in the format yyyymmdd  or ddmmyyyy: ")

tot = 10
while tot >= 10:
  tot=0
  for char in dates:
    tot += int(char)
  dates = str(tot)
  
print(dates)  
  