
height = 0
use_block = 0
loop_control = 1
blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#  

while loop_control:
    for i in range(1,blocks+1):
       use_block += i
       if use_block <= blocks:
           height +=1
           continue
       else:
           loop_control = 0
           break
           
       
           

print("The height of the pyramid:", height)
