from random import choice, sample, shuffle, randint
from string  import punctuation
from pprint import pprint


names = ['Joe', 'Bob', 'Sue', 'Sally', 'Kim', 'Paul', 'Sane', 'Blake']
current_player = choice(names)

print(current_player)

team = sample(names, 4)
print()
print(team)

s = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'

for i in range(1000):
  print(choice(s), end='')
  
players = []
  
players = names[ : ]
print()  
print('Name List: ', names)
print('Player List: ', players)

shuffle(players)

print('Name List: ', names)
print('Player List: ', players)

for p in players:
  print(p, 'it is your turn.')
  
squad = []

for i in range(0, len(players), 2):
  squad.append([players[i], players[i+1]])

print('Squad List: ' , squad)
  
  
h = 'Hi! This is a test.'
for c in punctuation:
  h = h.replace(c, ' ')
  
print(h)
print(h.split())


L = ['A', 'B', 'C']

print(' '.join(L))
print(''.join(L))
print(', '.join(L))
print('**'.join(L))

print([i for i in range(5)])


string = 'Hello'

L = [1, 14, 5, 9, 12]
M = ['one', 'two', 'three', 'four', 'five', 'six']

print([0 for i in range(10)])
print([i**2 for i in range(1,8)])
print([i*10 for i in L])
print([c*2 for c in string])
print([m[0] for m in M])
print([i for i in L if i<10])
print([m[0] for m in M if len(m)==3])

K = []

for m in M:
  if len(m) ==3:
    K.append(m)
print(K)

H = [randint(1, 100) for i in range(50)]

print(H)

print([i**2 for i in H])

print([i for i in H if i>50])

print([H.count(i) for i in range(1, 101)])

alphabet = 'abcdefghijklmnopqrstuvwxyz'

s = ''.join([choice(alphabet) for i in range(1000)])

print(s)

P = [[1,2], [3,4], [5,6]]
print(P)
print([[y,x] for x, y in P])

G = [[1,2,3],
        [4,5,6],
        [7, 8,9]]
        
for r in range(3):
  for c in range(3):
    print(G[r][c], end=' ')
  print()
  
pprint(G)