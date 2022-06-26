
for i in range(4):
  print('*' * (i+1))
  
  
firstTerm =0;
secondTerm =1
num1 = eval(input('Enter number of Fibonacci: '))
for i in range(num1):
  print(firstTerm, end=' ')
  nextTerm = firstTerm + secondTerm
  firstTerm = secondTerm
  secondTerm = nextTerm
print()

num4 =eval(input('Enter width of the box: '))
num5 = eval(input('Enter height of the box: '))

print('*' * num4)
for k in range(num5):
  print('*', ' ' * (num4),  '*')
print('*' * num4)



num2 = eval(input('Enter width of box: '))
num3 = eval(input('Enter height of box: '))
for k in range(num3):
  print('*' * num2)

print()
name = input('Enter name: ')
num = eval(input('Enter number: '))
for i in range(num):
  print(name)
  
  