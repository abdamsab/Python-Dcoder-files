import random


def gensquares(N):
  for x in range(N):
    yield x**2
    
for number in gensquares(10):
  print(number)
  
print('='*20)
  
def rand_num(L,H,N):
  for x in range(N):
    yield (random.randint(L,H))

for number in rand_num(1,10,5):
  print(number)

print('='*20)
 
s = 'Hello'
  
itera = iter(s)
for n in s:
  print(next(itera))
  
print('='*20)
  
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item >3)
for n in gencomp:
  print(n)