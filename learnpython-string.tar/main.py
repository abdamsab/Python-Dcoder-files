from math import floor

num = eval(input('Enter your decimal number: '))
print(num - floor(num))

s = input('Enter your decimal number: ')
print(s[s.index('.')+1:])

s = 'Hi, What\'s My Name? Good!'

s = s.lower()
for c in ',.;:-?!()\'"':
  s = s.replace(c, '*')
print(s)

name = input('Enter your name: ')
for i in range(len(name)):
  print(name[:i+1], end=' ')

print()  
s1 = input('Enter some text: ')
doubled_s1 = ' '
for c in s1:
  doubled_s1 = doubled_s1 + c*2
print(doubled_s1)



s = 'abcdefghijabadads'

print(s[2:5])
print(s[ :5])
print(s[5: ])
print(s[-2: ])
print(s[ : ])
print(s[1:7:2])
print(s[ : :-1])

print('='*7)

s = s[ :4] + 'X' + s[5:]

print(s)

#for i in range(len(s)):
  #print(s[i])
  
print('*'*7)

#for c in s:
  #print(c)
  
  
s = s.upper()
print(s)
print()

s = s.replace('A', 'x')
print(s)

print('Occurrence of x in ', s , 'is: ', s.count('x'))

if 'X' in s:
  print('index position of X is: ', s.index('X'))
  
#help(str)

#f = 'I can \'t go'

