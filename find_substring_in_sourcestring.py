
source_string = input("Enter sourcestring to be search: ")
substring = input("Enter substring to search for: ")
pos = 0
text =''

source_string.lower()
substring.lower()

for char in substring:
  pos = source_string.find(char, pos)
  if pos != -1:
    text += char
    
if text == substring:
  print("Yes")
else:
  print("No")
  
  
#donor
#Nabucodonosor

#donut
#Nabucodonosor