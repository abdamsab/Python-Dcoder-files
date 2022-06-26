def is_prime(num):
  for i in range(2, num):
    if num%i==0:
      return False
  return True
   
#
# Write your code here.
#

for i in range(1, 20):
  if is_prime(i + 1):
      print(i + 1, end=" ")
print()
