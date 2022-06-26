
def cipher(text, num):
  cipher = ''
  for char in text:
    if ord(char) >=65 and ord(char) <= 90:
      code = ord(char) + num
      if code > ord('Z'):
        code = ord('A') + (code - ord('Z')) - 1
      cipher += chr(code)
    elif ord(char) >= 97 and ord(char) <= 122:
      code = ord(char) + num
      if code > ord('z'):
        code = ord('a') + (code - ord('z')) - 1
      cipher += chr(code)
    else:
      cipher += char
  return cipher
  
  
txt = input("Enter text to encrypt: ")


key = int(input("Enter number of shift: "))

while (key < 1 or key > 25):
  print("invalid shift entered")
  key = int(input("Enter number of shift: "))

print(cipher(txt, key))

#abcxyzABCxyz 123  - shift 2 - cdezabCDEzab 123

#The die is cast - shift 25 - Sgd chd hr bzrs