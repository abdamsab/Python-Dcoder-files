step = 0
loop_ctrl = 1

c0 = int(input("Enter a non-nehative and non-zero integer "))

while loop_ctrl:
    if c0%2==0:
        c0//=2
        step+=1
    else:
        c0 = 3 * c0 +1
        step+=1
    print(c0)
    if c0 != 1:
        continue
    else:
        loop_ctrl=0
print("Step: ", step)
