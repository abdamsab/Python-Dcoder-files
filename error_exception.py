#pytho
try:
  for i in ['a', 'b', 'c']:
    print(i**2)
except:
  print('Operation can\'t be performed on the variables') 
  
try:  
  x = 5
  y = 0
  z = x/y
except:
  print('Invalid operation')
finally:
  print('All Done')
  
def ask():
  
  while True:
    try:
      result = int(input('Enter a number: '))
    except:
      print('Enter a valid number')
    else:
      return result**2
      
      
print(ask())