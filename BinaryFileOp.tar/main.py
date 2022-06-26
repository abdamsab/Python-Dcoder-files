

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.


from os import strerror

data1 = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data1)
    bf.close()

    for b in data1:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))




"""try:
  fb = open('file.bin', 'rb')
  output = fb.read(1)
  while output:
    print(output)
    output = fb.read(1)
  fb.close()
except IOError as ec:
  print("I/O error occurred:", strerror(e.errno))
"""