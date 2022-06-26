
# Caesar cipher.
def cipher(text):
  cipher = ''
  for char in text:
    if not char.isalpha():
      continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
      code = ord('A')
    cipher += chr(code)
  return cipher
  
  
def de_cipher(text):
  de_cipher = ''
  for char in text:
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
      code = ord('Z')
    de_cipher += chr(code)
  return de_cipher
    


text = input("Enter your message: ")

output = cipher(text)

print(output)

print()

sec_out = de_cipher(output)

print(sec_out)