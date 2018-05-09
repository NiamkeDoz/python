def displayNumberGrid():
    print("| "+displaygrid[0] + " | " + displaygrid[1] + " | " + displaygrid[2] + " | ")
    print("| "+displaygrid[3] + " | " + displaygrid[4] + " | " + displaygrid[5] + " | ")
    print("| "+displaygrid[6] + " | " + displaygrid[7] + " | " + displaygrid[8] + " | ")


def displayBoard():
    print("| "+ board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("| "+ board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("| "+ board[6] + " | " + board[7] + " | " + board[8] + " | ")

def player1Move():
    player1 = (input("Player One make your move!\n"))
    player1 = int(player1) - 1
    if(board[playerMove] != "."):
        print("This location is not valid!")
    elif(board[placeMove] == "."):
        print("Move is placed")
    
displaygrid = ["1","2","3",
            "4","5","6",
            "7","8","9"]

board = [".",".",".",".",".",".",".",".","."]



print("Tic Tac Toe")
print("Pick a number a to place your piece.")
displayNumberGrid()

player1Move()


#if (board[player1] != "."):
#    print("This location is not valid!")
#elif(board[player1] == "."):
#        board[player1] = "X"

displayBoard()
    




#displayBoard()

    
#displayNumberGrid()