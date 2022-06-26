




password = 'passwd'
count = 0
passw = input('Enter password: ')
while passw != password and count<4:
  count += 1
  if passw == password:
    print('***password correct***')
    break
  print('Invalid password ', 5-count, ' chance left')
  passw = input('Enter password: ')
  if count == 4:
    print('Time out')



weight = eval(input('Enter weight: '))
while weight < 0:
  print('Entry is Invalid')
  weight = eval(input('Enter weight: '))
print(weight, 'Kg', ' = ' , weight * 2.205, 'pound')



i = 1
while i < 51:
  print(i, end=' ')
  i += 1
  
  
  
print()  
s = 'Hello Python World'
j = 0
while j < len(s):
  print(s[j])
  j+=1
  
  
  
L = s.split(' ')
print(L)
j = 0
while j < len(L):
  w = L[j]
  print(w[1])
  j+=1
