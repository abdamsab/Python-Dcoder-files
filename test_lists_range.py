
total = 0
key = list(range(1, 10))
key2 = ['1','2','3','4','5','6','7','8','9']
print(key)
print(sum([1,2,3,4,5,6,7,8,9]) == sum(key))

for ele in key2:
  total += int(ele)
print(total)