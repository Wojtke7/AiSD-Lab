import random

def change_area(place, mark, board, check_board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == place:
                board[i][j] = mark
    
    if place in check_board:
        check_board.remove(place)
        if not check_board:
            display(board)
            print("Every place is ocuppied, draw!")
            return True
        else:
            return False

def check_place_and_change(check_board, mark, board):
    while True:
        place = input() 
        if place in check_board:
            logical = change_area(place, mark, board, check_board)
            return logical
        else:
            print("Wrong field, try again!")

def check_winner(board):
    if board[0][1] == board[0][3] and board[0][1] == board[0][5] and board[0][3] == board[0][5]:
        return True
    elif board[0][1] == board[2][1] and board[0][1] == board[4][1] and board[2][1] == board[4][1]:
        return True
    elif board[0][1] == board[2][3] and board[0][1] == board[4][5] and board[2][3] == board[4][5]:
        return True
    elif board[0][3] == board[2][3] and board[0][3] == board[4][3] and board[2][3] == board[4][3]:
        return True
    elif board[0][5] == board[2][5] and board[0][5] == board[4][5] and board[2][5] == board[4][5]:
        return True
    elif board[2][1] == board[2][3] and board[2][1] == board[2][5] and board[2][3] == board[2][5]:
        return True
    elif board[4][1] == board[4][3] and board[4][1] == board[4][5] and board[4][3] == board[4][5]:
        return True
    elif board[0][5] == board[2][3] and board[4][1] == board[2][3] and board[4][1] == board[0][5]:
        return True
    return False


def display(board): #displays board
    for x in board:
        print(''.join(x))



board = [['|', '1', '|','2', '|', '3','|'],
        ['-', '-', '-', '-', '-', '-','-'],
        ['|', '4', '|', '5', '|', '6','|'],
        ['-', '-', '-', '-', '-', '-','-'],
        ['|', '7', '|', '8', '|', '9','|']]

check_board = ['1','2','3','4','5','6','7','8','9']

#beggining
print("Welcome in Tic Tac Toe!") 
player1 = input("Player 1 type your name: ")
player2 = input("Player 2 type your name: ")

print('\n'"Hello", player1, "and" , player2, "!!!" '\n')

X = random.choice([player1,player2])

if X == player1:
    O = player2
    print(player1, "You have X's, and", player2, "you have O's!")
else:
    O = player1
    print(player2, "You have X's, and", player1, "you have O's!")

X_ = 'X'
O_ = 'O'

while True:
    
    display(board)
    print("Your turn," , X , "choose where you want to place your sign!")
    outOfPlaces = check_place_and_change(check_board, X_, board)
    
    if outOfPlaces == True:
        break
    
    winnerX = check_winner(board)
    if winnerX == True:
        display(board)
        print("The end," , X , "you win, congratulations!")
        break

    
    display(board)
    print("Your turn," , O , "choose where you want to place your sign!")
    outOfPlaces = check_place_and_change(check_board, O_, board)

    if outOfPlaces == True:
        break

    winnerY = check_winner(board)
    if winnerY == True:
        display(board)
        print("The end,", O , "you win, congratulations!")
        break

    

    
    

     


        

