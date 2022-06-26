from math import *
  
n = eval(input('Enter n value: '))
  
num = 1;
  
for k in range(n):
    num = num + 1/(k +1)
num = num - log(n)
print('Answer: ', num)
print()

sum = 1;
for j in range(2, 2001):
  if j % 2 == 0:
    sum -= j
  elif j % 2 != 0:
    sum += j
print()   
print('Sum = ', sum)


print()
print()

val = eval(input('Enter a number: '))

sum = 0;

for i in range(1, val+1):
  if val % i == 0:
    sum += i
    print(i)
print('Sum of divisors of ', val, ' = ', sum)
  
 