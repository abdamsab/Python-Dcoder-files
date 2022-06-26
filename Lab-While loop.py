
from random import randint

loop_control = 1

count = 0

secret_number = randint(1, 9)

val = int(input("Enter Your Guess: "))



while loop_control:
  
  count+=1
  
  if val == secret_number:
    print("Welldone, muggle! You are free now. ")
    print("After ", count, " trial")
    loop_control = 0
  else:
    print("Ha ha! You re struck in my loop! ")
  
    val = int(input("Enter Your Guess: "))
  
  