#python 3.7.1

def palindrome(s):
  s = s.lower().replace(' ', '')
  #print(s)
  if s == s[::-1]:
    return True
  else:
    return False
  
st = 'helleh'

print(palindrome(st))