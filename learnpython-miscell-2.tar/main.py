

for x in range(1, 100):
  for y in range(x, 100):
    for z in range(y, 100):
      if x**2 + y**2 == z**2:
        for i in range(2, x):
          if x%i==0 and y%i==0 and z%i==0:
            break
        else:
           print((x, y, z), end=' ')


print()
#for x in range(1, 100):
  #for y in range(x, 100):
    #for z in range(y, 100):
      #if x**2 + y**2 == z**2:
        #print(x, y, z)



#for x in range(1, 100):
  #for y in range(1, 100):
    #for z in range(1, 100):
      #if x**2 + y**2 == z**2:
        #print(x, y, z)



#for x in range(-50, 50):
  #for y in range(-50, 51):
    #if 2*x + 3*y ==4 and x-y == 7:
      #print(x, y)



#for i in range(1, 11):
  #for j in range(1, 11):
    #print(j, ' x ', i, ' = ',  '{:3d}'.format(i*j))
  #print()


#for i in range(1, 11):
  #for j in range(1, 11):
    #print('{:3d}'.format(i*j), end=' ')
  #print()




L = [8,7,6]

x, y, z = L

print('x', '=', x, 'y', '=', y, 'z', '=', z)

x,y,z = y,z,x

print('x', '=', x, 'y', '=', y, 'z', '=', z)


a = 23.6 * 0.25

print('The tip is {:.2f}'.format(a))

bill = 55.34
tip = 55.34 * 0.25

print('Tip: ${:.2f}, Total: ${:.2f}'.format(tip, bill+tip))

print()
print('{:5d}'.format(2))
print('{:4d}'.format(25))
print('{:2d}'.format(138))

print()
print('{:^5d}'.format(2))
print('{:^5d}'.format(222))
print('{:^5d}'.format(13834))


print()
print('{:<5d}'.format(2))
print('{:<5d}'.format(222))
print('{:<5d}'.format(13834))


print()
print('{:,d}'.format(1000000))
#for i in range(1, 10001):
  #s = str(i)
  #if s == s[::-1]:
    #print(s) 
