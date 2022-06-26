
flag_register = 0x1235
bit_mask = 0x0008

flag_register &= ~bit_mask



print(flag_register)

if flag_register & bit_mask:
  print("Your bit is set")
  print(flag_register & bit_mask)
else:
  print("Your bit is clear")
"""
  print("="*25)
  
flag_register |= bit_mask
  
if flag_register & bit_mask:
   print("Your bit is set")
   print(flag_register & bit_mask)
else:
  print("Your bit is clear")
"""
  
print("="*25)
  
flag_register ^= bit_mask
  
if flag_register & bit_mask:
   print("Your bit is set")
   print(flag_register & bit_mask)
else:
  print("Your bit is clear")