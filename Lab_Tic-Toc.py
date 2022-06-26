
"""
Your task is to write a simple program which pretends to play
 tic-tac-toe with the user. To make it all easier for you, we've decided 
 to simplify the game. Here are our assumptions:

*the computer (i.e., your program) should play the game using 'X's;
*the user (e.g., you) should play the game using 'O's;
*the first move belongs to the computer - it always puts its first 'X' in 
  the middle of the board;
*all the squares are numbered row by row starting with 1 
  (see the example session below for reference)
*the user inputs their move by entering the number of the square 
  they choose - the number must be valid, i.e., it must be an integer, 
  it must be greater than 0 and less than 10, and it cannot point to a 
  field which is already occupied;
*the program checks if the game is over - there are four possible 
  verdicts: the game should continue, or the game ends with a tie, 
  your win, or the computer's win;
*the computer responds with its move and the check is repeated;
*don't implement any form of artificial intelligence - a random field 
  choice made by the computer is good enough for the game.
"""
from random import randint

board = [' '] *10
game_on = True
turn = 0
player_1 = 'COMPUTER'
player_2 = 'PLAYER'

#board[9] = 'X'
#board[8] = 'X'
#board[7] = 'O'
#board[6] = 'O'
#board[5] = 'X'
#board[4] = 'X'
#board[3] = 'X'
#board[2] = 'O'
#board[1] = 'X'

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
  print("+" + 6 * "-" + "+" +  6 * "-" + "+" + 6 * "-" + "+" )
  print("|" + " "*10  + "|"  + " "*10 + "|" + " "*10 + "|\n" , end="" )
  print("|" + " "*4 + board[7] + " "*4  + "|"  + " "*4 + board[8] + " "*4 + "|" + " "*4 + board[9] + " "*4 + "|\n" , end="" )
  print("|" + " "*10  + "|"  + " "*10 + "|" + " "*10 + "|\n", end="" )
  
  print("+" + 6 * "-" + "+" +  6 * "-" + "+" + 6 * "-" + "+")
  
  print("|" + " "*10  + "|"  + " "*10 + "|" + " "*10 + "|\n" , end="" )
  print("|" + " "*4 + board[4] + " "*4  + "|"  + " "*4 + board[5] + " "*4 + "|" + " "*4 + board[6] + " "*4 + "|\n" , end="" )
  print("|" + " "*10  + "|"  + " "*10 + "|" + " "*10 + "|\n", end="" )
  
  print("+" + 6 * "-" + "+" +  6 * "-" + "+" + 6 * "-" + "+")
  
  print("|" + " "*10  + "|"  + " "*10 + "|" + " "*10 + "|\n" , end="" )
  print("|" + " "*4 + board[1] + " "*4  + "|"  + " "*4 + board[2] + " "*4 + "|" + " "*4 + board[3] + " "*4 + "|\n" , end="" )
  print("|" + " "*10  + "|"  + " "*10 + "|" + " "*10 + "|\n", end="" )
  print("+" + 6 * "-" + "+" +  6 * "-" + "+" + 6 * "-" + "+")
  

def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
  print("\nPlayer turn to play")
  pos = int(input("\nEnter your position 1 - 9\n"))
  while pos not in make_list_of_free_fields(board):
    print("\nPosition occupied try again")
    pos = int(input("\nEnter your position 1 - 9\n"))
  board[pos] = 'O'
  display_board(board)
  
    
   


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
  temp = []
  for i in range(1, 10):
     if board[i] == ' ':
       temp.append(i)
  return temp
   

def victory_for(board, marker):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
  return (
        (board[7] == marker and board[8] == marker and board[9] == marker) or
        (board[4] == marker and board[5] == marker and board[6] == marker) or
        (board[1] == marker and board[2] == marker and board[3] == marker) or
        (board[7] == marker and board[4] == marker and board[1] == marker) or
        (board[8] == marker and board[5] == marker and board[2] == marker) or
        (board[9] == marker and board[6] == marker and board[3] == marker) or
        (board[7] == marker and board[5] == marker and board[3] == marker) or
        (board[9] == marker and board[5] == marker and board[1] == marker))

def draw_move(board):
    # The function draws the computer's move and updates the board.
  print("\nComputer turn to play")
  valid_move = True
  while valid_move:
    pos = randint(1, 9)
    if pos in make_list_of_free_fields(board):
      valid_move = False
      board[pos] = 'X'
      display_board(board)
     
     
def check_win(board, sign):
  if victory_for(board, sign):
    return True
  
def check_tie(board):
  if len(make_list_of_free_fields(board)) == 0:
    return True
  
  
"""
display_board(board)
print(make_list_of_free_fields(board))
draw_move(board)
check_win_tie(board, 'X', player_1)
enter_move(board)
check_win_tie(board, 'O', player_2)
"""

while True:
  if turn == 0:
    if check_win(board, 'O'):
      print("\nGAME OVER")
      print("\nPlayer won the game")
      break
    elif check_tie(board):
      print("\nGAME OVER")
      print("\nThe game end in draw")
      break
    draw_move(board)
    if check_win(board, 'X'):
      print("\nGAME OVER")
      print("\nComputer won the game")
      break
    elif check_tie(board):
      print("\nGAME OVER")
      print("\nThe game end in draw")
      break
    turn = 1
  elif turn == 1:
    if check_win(board, 'X'):
      print("\nGAME OVER")
      print("\nPlayer won the game")
      break
    elif check_tie(board):
      print("\nGAME OVER")
      print("\nThe game end in draw")
      break
    enter_move(board)
    if check_win(board, 'O'):
      print("\nGAME OVER")
      print("\nPlayer won the game")
      break
    elif check_tie(board):
      print("\nGAME OVER")
      print("\nThe game end in draw")
      break
    turn = 0