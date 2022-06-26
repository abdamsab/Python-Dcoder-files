
from collections import defaultdict

d = {}

#d['one']

d = defaultdict(object)

print(d['one'])

for item in d:
  print(item)
  
  
d = defaultdict(lambda: 0)


print(d['two'])