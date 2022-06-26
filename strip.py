
def mysplit(strng):
  strng += ' '
  wordlist = []
  fnal = []
  temp = 0
  fnd = strng.find(' ')
  wordlist.append(strng[:fnd].strip())
  while fnd != -1:
    temp = fnd
    fnd = strng.find(' ', temp+1)
    out = strng[temp+1:fnd].strip()
    wordlist.append(out)
  for words in wordlist:
    if words != '':
      fnal.append(words)
  return fnal
   
"""
wordlist=[]
temp = 0
strng = "To be or not to be, that is the question"
 
fnd = strng.find(' ')

wordlist.append(strng[:fnd])
temp = fnd
fnd = strng.find(' ', temp+1)
wordlist.append(strng[temp+1:fnd])
temp=fnd
fnd =strng.find(' ', temp+1)
wordlist.append(strng[temp+1:fnd])
print(wordlist)
"""
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
