from IPython.display import clear_output
def display_board(board):
    clear_output()
    print('{7} | {8} | {9}\n{4} | {5} | {6}\n{1} | {2} | {3}'.format(*game_board))
    
def player_input():
    player = 0;
    while not player in ['X', 'O']:
        player = str(input('choose player: X or O >>> ')).upper()
    return player

def place_marker(board, marker, position):
    return board.__setitem__(position, marker) or board 
    
def win_check(board, mark):
    # return list(mark*3) in [board[1:4], board[4:7], board[7:], board[1::3], board[2::3], board[3::3], board[1::4], board[3:8:2]]
    return [*mark*3] in [board[x:y:z] for x,y,z in [[1,4,1],[4,7,1],[7,10,1],[1,8,3],[2,9,3],[3,10,3],[1,10,4],[2,7,2]]]

import random
def choose_first():
    return ('X', 'O')[random.randint(0, 1)]

def space_check(board, position):
    return not board[position] in ['X', 'O']

def full_board_check(board):
    return not '#' in board[1:10]

def player_choice(board):
    choice = 0;
    while not choice in range(1, 10):
        choice = int(input('Choose a position >>> '))
    return choice if space_check(board, choice) else False
    
def replay():
    return input('Do you want to play again? [y] >>> ').upper() == 'Y'

while True:
    game_board = ['#','#','#','#','#','#','#','#','#','#']
    display_board(game_board)
    player = player_input()
    playing = True
    
    while playing:
        pos = player_choice(game_board)
        if pos: 
            game_board = place_marker(game_board, player, pos)
            display_board(game_board)
            if win_check(game_board, player):
                print('{} wins!'.format(player))
                playing = False
            elif full_board_check(game_board):
                print('Draw!')
                playing = False 
            player = 'X' if player = 'O' else player = 'X'
      
    if not replay():
        break