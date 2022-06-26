from random import randint

count = 0;
for k in range(10):
  print()
  num1 = randint(1, 10)
  num2 = randint(1, 10)
  
  print('Question ', k+1, ':  ', num1, ' x ', num2, end=' ')
  answer = eval((input('= ')))
  if answer == (num1* num2):
    print('Right!')
    count += 1
  else:
    print('Wrong! The answer is ', num1 * num2)
    
print('You scored ', count, ' out of 10')
    
  
  
