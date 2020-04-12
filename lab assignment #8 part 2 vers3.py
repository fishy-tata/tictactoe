# main function creates the board and calls helper functions
def main():
    board = [
        ['0','0','0'],
        ['0','0','0'],
        ['0','0','0']
        ]
    print('---------')
    for row in board:
        print(*row, sep=' | ')
        print('---------')
    switches_and_tie(board)


# ---helper functions---

# switches_and_tie function declares players, switches between the players, and determines if it is a tie
def switches_and_tie(board):
    x = 'x'
    o = 'o'
    i = 0
    win = False
    while i < 9 and win == False:
        if i < 9 and win == False:
            position(x,board)
            i += 1
        if i < 9 and is_winner(x,board,win) == False:     
                position(o,board)
                i += 1
                is_winner(o,board,win)
        elif i >= 9:
            print('Tie.')
        elif win == True:
            break
    

#position function gets row and column position of the x or o
def position(player,board):
    print('Player', player, 'turn')
    row = int(input('Enter a row number (1-3):'))
    column = int(input('Enter a column number (1-3):'))
    board[row-1][column-1] = player
    print('---------')
    for row in board:
        print(*row, sep=' | ' )
        print('---------')
    return board,player

#is_winner function calls helper functions and determines who wins
def is_winner(player,board,win):
    win = False
    if win == False:
        if check_row(player,board,win) == False:
            if check_col(player,board,win) == False:
                if check_diag(player,board,win) == False:
                    return False
    else:
        return True
            
#check_row function checks the rows for a winner
def check_row(player,board,win):    
        for row in board:
            if row[0] != '0' and row[0] == row[1] and row[1] == row[2]:
                print('Player', player, 'wins!')
                return True
            else:
                return False

#check_col function checks the columns for a winner        
def check_col(player,board,win):
    if (board[0][0] != '0' and board[0][0] == board[1][0] and board[1][0] == board[2][0]) \
        or (board[0][1] != '0' and board[0][1] == board[1][1] and board[1][1] == board[2][1]) \
        or (board[0][2] != '0' and board[0][2] == board[1][2] and board[1][2] == board[2][2]):
        print('Player', player, 'wins!')
        return True            
    else:
        return False

#check_diag function checks both diagonals for a winner
def check_diag(player,board,win):
    if (board[0][0] != '0' and board[0][0] == board[1][1] and board[0][0] == board[2][2])\
       or (board[0][2] != '0' and board[0][2] == board[1][1] and board[0][2] == board[2][0]):
        print('Player', player, 'wins!')
        return True
    else:
        return False

#calls the main() function to begin the program
main()
