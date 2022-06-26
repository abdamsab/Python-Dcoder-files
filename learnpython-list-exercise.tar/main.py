

from random import randint

L = []

frequencies = []

for i in range(100):
  L.append(randint(1, 100))
  
print(L)

for i in range(1, 101):
  frequencies.append(L.count(i))
  
print('='*101)
print(frequencies)