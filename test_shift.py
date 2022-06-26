
txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
shift = 1
cipher =''

for char in txt:
  print(char, ':' , ord(char), end=' ')
  
print()

for char in txt:
  code = ord(char) + shift
  if code > ord('Z'):
    code = ord('A')
  cipher += chr(code)
  
print(txt)
print(cipher)

shift = 2
cipher = ''
#print(ord('Z')-(shift-1))
for char in txt:
  code = ord(char) + shift
  if code > ord('Z'):
    code = ord('A') + (code-ord('Z')) -1
  cipher += chr(code)
  

print(cipher)

shift = 3
cipher = ''

for char in txt:
  code = ord(char) + shift
  if code > ord('Z'):
    code = ord('A') + (code-ord('Z')) -1
  cipher += chr(code)
  
print(cipher)
print(shift)