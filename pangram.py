#python 3
import string

def pangram_check(s, alphabet):
  print(s)
  s = s.lower().replace(' ', '')
  print(s)
  s = list(s)
  print(s)
  s =  list(set(s))
  print(s)
  s.sort()
  print(s)
  s = ''.join(s)
  print(s)
  if s == alphabet:
    return True
  else:
    return False
  
  
  
st = 'The quick brown fox jumps over the lazy dog'

print(pangram_check(st, alphabet=string.ascii_lowercase))