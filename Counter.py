
from collections import Counter

mylist = [1,1,1,1,12,2,2,2,3,3,3,3,4,4,4,4,5,5,6,6]

print(Counter(mylist))

print("="*20)

print(Counter("abbababababbbbabbbabbbabbbb"))

print("="*20)

s = "How many time does each time is word apeared in the words word each each"

words = s.split()

c = Counter(words)

print(c)

print(c.most_common(2))