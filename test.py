from platform import platform, machine, processor, system
import os
import sys
print(platform(aliased = False, terse = False))
print(platform())
print(platform(1))
print(platform(0, 1))
print(machine())
print(processor())
print(system())

for p in sys.path:
  print(p)
 
import math
 
result = math.e != math.pow(2, 4)
print(int(result))