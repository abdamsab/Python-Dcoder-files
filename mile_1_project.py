#python 3.7.1
from random import randint
board = [' '] * 10
maker = ''
player = 0

def choice_first():
  result = randint(1,2)
  if result == 1:
    print('Player 1 go first')
  elif result == 2:
    print('Player 2 go first')
  return result

def display_board(board):
  #print('\n' * 100)
  print(board[7] + '|' + board[8] + '|' + board[9])
  #print('-' + '|' + '-' + '|' + '-')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print(board[1] + '|' + board[2] + '|' + board[3])
  
def player_input():
  choice = 'wrong'
  inrange = False;
  while choice.isdigit()==False or inrange == False:
    choice = input('Enter position (1 - 9): ')
    if choice.isdigit() == False:
      print('Sorry, enter digit from 1 - 9 to try again')
    if choice.isdigit() == True:
      if int(choice) in range(1,10):
        inrange = True
      else:
        inrange = False
        print('Number out of range, enter from 1-9')
  return int(choice)
  

  
def place_maker(board, player, position):
  if player == 1:
    maker = 'X'
  elif player == 2:
    maker = 'O'
  board[position] = maker

#position = player_input()
#print(position)
#board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

player = choice_first()
display_board(board)
position = player_input()
place_maker(board, player, position)
display_board(board)
#print(player)