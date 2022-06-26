
wordlist = [line.strip() for line in open('wordlist.txt')]

print('Total words: {}'.format(len(wordlist)))

"""
for word in wordlist:
  if len (word) == 3 and (word[0] =='a' or word[0] == 'b'):
    print(word)


for word in wordlist:
  if word[:2] == 'gn' or word[:2] == 'kn':
    print(word)
"""    
count = 0
for word in wordlist:
  if word[0] in 'aeiou':
    count = count + 1
print('Total word starting with vowels: {}'.format(count))
print('Percentage of words starting with vowels: {0:5.3f}%'.format(100*count/len(wordlist)))

"""
for word in wordlist:
  if len(word) ==7 and word[:2] == 'th' and word[-2:] == 'ly':
    print(word)
"""
    
i = 0
while wordlist[i] != 'q':
  i = i+1
print(wordlist[i:i+10])