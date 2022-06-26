
from os import strerror

try:
  fo = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
  for i in range(10):
    s = "line #" + str(i+1) + "\n"
    for ch in s:
      fo.write(ch)
  fo.close()
except IOError as e:
  print("I/O error occurred: ", strerror(e.errno))



try:
  with open('newtext.txt', 'rt') as f:
    output = f.readline()
    while output != '':
      print(output)
      output = f.readline()
except IOError as ec:
  print("I/O error occurred: ", strerror(e.errno))