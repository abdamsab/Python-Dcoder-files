print('the value of 3+4 is',3+4, '.')

print('the value of 3+4 is', 3+4, '.', sep=': ')


print('On the first line')
print('On the second line')

print('On the first line', end=' ')
print('On the second line')


for k in range(4):
  print()
  for j in range(20):
    print('*', end='')
    
print()
    
    
for k in range(15):
  print('*', end='')
for j in range(2):
  print()
  print('*', end='')
  for p in range(20):
    print(' ', end='')
    if p==19:
      print('*')
for g in range(15):
    print('*', end='')
      
  