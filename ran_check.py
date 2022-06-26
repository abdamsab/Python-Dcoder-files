#python 3.7.1

def ran_check(num, low, high):
  if num>=low and num<=high:
    return True
  else:
    return False
    
print(ran_check(11, 1, 10))