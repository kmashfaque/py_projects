import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

winner = None
currentPlayer = "X"
gamerunning = True


def print_board(board):
    print(board[0] + "|"+board[1]+"|"+board[2]+"|")
    print("------")
    print(board[3] + "|"+board[4]+"|"+board[5]+"|")
    print("------")
    print(board[6] + "|"+board[7]+"|"+board[8]+"|")


def player_input(board):

    playerInp = int(input("Enter a position from 0-8: "))

    if board[playerInp] == "-":
        board[playerInp] = currentPlayer
    else:
        print("Oops, position is already been taken!!")


def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def checkHorizontal(board):
    global winner
    if board[0] == board[1] and board[0] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] and board[3] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] and board[6] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkVertical(board):
    global winner
    if board[0] == board[3] and board[0] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != "-":
        winner = board[3]
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] and board[0] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] and board[2] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def whoWins(board):
    global gamerunning

    if checkHorizontal(board):
        print_board(board)
        print(f"The winner is {winner}")
        gamerunning = False

    elif checkVertical(board):
        print_board(board)
        print(f"The winner is {winner}")
        gamerunning = False

    elif checkDiag(board):
        print_board(board)
        print(f"The winner is {winner}")
        gamerunning = False


def check_draw(board):
    global gamerunning
    if "-" not in board:
        print_board(board)
        print("The match is drawn!!")
        gamerunning = False


def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)

        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gamerunning:
    print_board(board)
    player_input(board)
    whoWins(board)
    check_draw(board)
    switchPlayer()
    computer(board)
    whoWins(board)
    check_draw(board)
