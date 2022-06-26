from random import shuffle

points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
               'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
               'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
               'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}
               
word = input('Enter a word: ')

word = word.upper()

score = sum([points[c] for c in word])

print('Your word: ', word, ' scored ', score)

total = 0
for c in word:
  total += points[c]

print('Your word: ', word.title(), ' scored ', total)


deck = [{'value':i, 'suit':c}
            for c in ['spades', 'clubs', 'hearts', 'diamonds']
            for i in range(2, 15)]
            
print(deck)

shuffle(deck)

print()
print(deck)