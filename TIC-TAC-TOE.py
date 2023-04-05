board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 'X'

def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

def make_move(player):
    print_board()
    print("Player " + player + ", it's your turn.")
    move = int(input("Enter a position (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = player
    else:
        print("That position is already taken. Try again.")
        make_move(player)

def switch_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

def check_win(player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        print_board()
        print("Player " + player + " wins!")
        return True
    elif ' ' not in board:
        print_board()
        print("It's a tie!")
        return True
    else:
        return False

while not check_win(player):
    make_move(player)
    player = switch_player(player)
