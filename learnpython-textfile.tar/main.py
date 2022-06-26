
f = open('temps.txt', 'w')
print(-32, file=f)
print(50, file=f)
print(212, file=f)
f.close()

file1 = open('ftemps.txt', 'w')
temperatures = [line.strip() for line in open('temps.txt')]
for t in temperatures:
  t = int(t)
  print(t*(9/(5+32)), file=file1)
file1.close()

s = open('ftemps.txt').read()
print(s)



#s = open('example.txt').read()
#print(s)





lines = [line.strip() for line in open('example.txt')]
#The string method strip removes any whitespace characters from the beginning
#and end of a string.
print(lines)