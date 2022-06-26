import math

import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)



try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")


test = 1

while test != 0:
  x = (input("Enter x: "))
  try:
    x = float(x)
    test = 0
  except ValueError:
    print("The value of x entered is invalid")
    
y = math.sqrt(x)
print("The square root of", x, "equals to", y)


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")

print("THE END.")

