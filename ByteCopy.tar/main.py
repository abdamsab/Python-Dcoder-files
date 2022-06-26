
from os import strerror

"""
data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('srcname.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.

"""
src = input("Enter the source file name: ")
try:
    src = open(src, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)  

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)  

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    print('first-readin:', readin)
    while readin > 0:
        written = dst.write(buffer[:readin])
        print('written: ',written)
        total += written
        print('total: ', total)
        readin = src.readinto(buffer)
        print('readin:', readin)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)  
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()
