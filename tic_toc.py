#python 3.7.1
from random import randint
board = [' '] * 10
#maker = ''
player = 0

def choice_first():
    if randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 1'


def display_board(board):
    #print('\n' * 100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    #print('-' + '|' + '-' + '|' + '-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    maker = ' '
    while not (maker == 'X' or maker == 'O'):
        maker = input('Player 1: Do you want to be X or O? ').upper()
    if maker == 'X':
        return ('X', 'O')
    else:
        return('O', 'X')

"""
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
 """


def place_marker(board, maker, position):
    board[position] = maker


def win_check(board, marker):
    return (
        (board[7] == marker and board[8] == marker and board[9] == marker) or
        (board[4] == marker and board[5] == marker and board[6] == marker) or
        (board[1] == marker and board[2] == marker and board[3] == marker) or
        (board[7] == marker and board[4] == marker and board[1] == marker) or
        (board[8] == marker and board[5] == marker and board[2] == marker) or
        (board[9] == marker and board[6] == marker and board[3] == marker) or
        (board[7] == marker and board[5] == marker and board[3] == marker) or
        (board[9] == marker and board[5] == marker and board[1] == marker))

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position

def replay():
    return input('Do you want to player again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    #Reset the board
    player1_marker, player2_marker = player_input()
    turn = choice_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            #Player1's turn.

            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player2's turn
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
