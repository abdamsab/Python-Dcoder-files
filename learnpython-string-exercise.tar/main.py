

L = eval(input('Enter a list: '))
print('The first element is ', L[0])


letter = input('Enter word: ')

revLetter = letter[ : :-1]

for i in range(len(letter)):
  if letter[i] != revLetter[i]:
    print('The word is not a palindrome')
    break
  else:
    print('Hurray!!! We have a palindrome')
    



count1 = 0
count2 = 0
formulae = input('Enter formular: ')

for c in formulae:
  if c == '(':
    count1 += 1
  if c == ')':
    count2 += 1
if count1 == count2:
  print('The parentheses is complete')
else:
  print('Invalid parentheses')