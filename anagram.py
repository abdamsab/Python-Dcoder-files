
print('WELCOME TO CHECK FOR ANAGRAM: \n')
tot1 = 0
tot2 = 0
txt1 = input("Enter the first words: ")
txt2 = input("Enter the second words: ")

txt1= txt1.lower().replace(' ', '')
txt2=txt2.lower().replace(' ', '')

for char in txt1:
  tot1 += ord(char)
  
for char in txt2:
  tot2 += ord(char)
  
if tot1 == tot2:
  print('We have an anagram ')
  
else:
  print("It is not an anagram")