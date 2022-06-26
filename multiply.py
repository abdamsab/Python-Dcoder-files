#python 3.7.1

def multiply(numbers):
  result = 1
  for num in numbers:
    result *= num
  return result
  
lst = [1, 2, 3, -4]

print(multiply(lst))