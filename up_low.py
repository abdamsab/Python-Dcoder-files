#python 3.7.1


def up_low(s):
  new_str = ''
  for c in ',.;:-?!()\'"':
    s = s.replace(c, '')
  s = list(s)
  print(s)
  
  count_low = 0
  count_high = 0
  
  for st in s:
    if st.islower():
      count_low += 1
    if st.isupper():
      count_high += 1
  print('No. of Upper case character : ', count_high)
  print('No. of Loweer case character : ', count_low)
      
   
  
  
st = 'Hello Mr. Rogers, how are you this fine Tuesday?'

up_low(st)