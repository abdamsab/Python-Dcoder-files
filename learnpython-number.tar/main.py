from random import randint, uniform
from math import * 


power = eval(input('Enter power: '))
number = 2**power
lastdigit = number % 10;

print('Last digit of 2 power ', power, ' = ', lastdigit)



hrs = eval(input('Enter hour: '))
hrsf =eval(input('How many hours ahead? '))
newhrs = (hrs+hrsf)%12

print('New hour: ', newhrs, ' o', ' clock')

sec = eval(input('Enter a number in second: '))

mint = sec // 60

secs = sec % 60

print(sec, ' second is ', mint, ' minutes and ', secs, ' seconds ' )



h = randint(1, 10)
for k in range(h):
  print('Damisa')
  
deci = round(uniform(1, 10), 2)
print('Decimal random number btw 1 and 10: ', deci)
  
x = randint(1, 50)
y = randint(2, 5)

print(x, ' power ' , y, ' = ', x**y)

for k in range(50):
  print(randint(3, 6), end=' ')
print()

x = randint(1, 20)
print('A random number between 1 and 10: ', x)

print('Pi is roughly ', pi)
print('sin(30) = ', sin(30))

print(abs(-4.3))
print(round(3.336, 2))
print(round(345.2, -1))

#for j in range(50):
 # print('Random number between 1 and ', j+2, ' = ' , randint(1, (j+2)))
  
x1 = eval(input('Enter X1 value: '))
y1 = eval(input('Enter Y1 value: '))

print('Answer: ', ((abs(x1-y1))/x1+y1))

