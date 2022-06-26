

d = {'A':100, 'B':200, 'C':300, 'D':100}

d2 = d.copy()

for key in d:
  print(d[key])

for key in d:
  print(key)

print(list(d))
print(list(d.values()))
print(list(d.items()))

L = [x[0] for x in d.items() if x[1]==100]
print(L)
print(d2)


letter = input('Enter a letter: ')
letter = letter.upper()
if letter in d:
  print('The value is', d[letter])
else:
  print('Not in dictionary')
  
