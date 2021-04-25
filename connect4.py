import random

# starts game by making the user choice what type of players they want
# to play
# the random player makes random moves and is mostly for testing
# player means the user is that player
# AI is an ai that chices its moves bsed on the minimax algorithm

def start(): 
    global p1
    global p2
    global board
    print("Select the type of player for player one")
    p1 = input("Type 1 for AI, 2 for Player, or 3 for Random:")
    i=0
    while i == 0:
        p1 = int(p1) 
        if p1 == 1 or p1 == 2 or p1 == 3:
            i = 1
        else:
            print("Error Please enter a valid number")
            p1 = input("Type 1 for AI, 2 for Player, or 3 for Random:")


    print("Select the type of player for player two:")
    p2 = input("Type 1 for AI, 2 for Player, or 3 for Random:")
    i=0
    while i == 0:
        p2 = int(p2) 
        if p2 == 1 or p2 == 2 or p2 == 3:
            i = 1
        else:
            print("Error Please enter a valid number")
            p2 = input("Type 1 for AI, 2 for Player, or 3 for Random:")

    print(p1, "vs", p2)

    board = ["c1","c2","c3","c4","c5","c6","c7"]
    for i in range(0,7):
        board[i] = ["-","-","-","-","-","-"]

# initulizes the game, tracks witch players turn it is and the board stat
# 

def game(p1,p2):
    global board
    global win
    turn = random.randint(1,2)
    while win == False:
        if turn == 1:
            if p1 == 1:
                AI(turn)
            elif p1 == 2:
                player(turn)
            else:
                rand(turn)
            turn = 2
        else:
            if p2 == 1:
                AI(turn)
            elif p2 == 2:
                player(turn)
            else:
                rand(turn)
            turn = 1

        printBoard()
    
        
# makes sure no rules are being broke and determins if 
# the board id at a win state
# b is the curent board
# t is the players turn

def rules(m):
    global board

    if board[m][5] != "-":
        return False
    else:
        return True



    print("not ready")
    return False


def place(t,m):
    global board

    i = 0
    while i != -1:
        if board[m][i] == "-":
            if t == 1:
                board[m][i] = "X"
            else:
                board[m][i] = "O"
            i = -1
        else:
            i = i+1
    return

def checkWin(t,m):

    global board

    # deter mine what symbole to test for based on turn
    if t == 1:
        sym = "X"  
    else:
        sym = "O"

    i = 5 # index number used to find the row the new piece is in
    while i > -1:
        if board[m][i] == sym:
            
            # check vertical
            if i >= 3:    
                if board[m][i-1] == sym and board[m][i-2] == sym and board[m][i-3] == sym:
                    return True
            
            # check horivontal
            total = 0 
            j = m

            # checks for matching pieces to the left of the piece
            while j+1 < 7: 
                if board[j+1][i] == sym:
                    total = total + 1
                    j = j + 1
                else:
                    j = 7
            j = m

            # checks for matching pieces to the right of the piece
            while j-1 > -1: 
                if board[j-1][i] == sym:
                    total = total + 1
                    j = j - 1
                else:
                    j = -1
            if total >= 3: # if there is 3 or more pice surounding the new pice
                return True

            # check diagonal left
            total = 0 
            j = m
            k = i

            # checks for matching pieces to the left and down from the piece
            while j+1 < 7 and k-1 > -1: 
                if board[j+1][k-1] == sym:
                    total = total + 1
                    j = j + 1
                    k = k - 1
                else:
                    j = 7
            j = m
            k = i

            # checks for matching pieces to the right and up from the piece
            while j-1 > -1 and k+1 < 6: 
                if board[j-1][k+1] == sym:
                    total = total + 1
                    j = j - 1
                    k = k + 1
                else:
                    j = 0
            if total >= 3: # if there is 3 or more pice surounding the new pice
                return True


            # check diagonal right
            total = 0 
            j = m
            k = i

            # checks for matching pieces to the left and up from the piece
            while j+1 < 7 and k+1 < 6: 
                if board[j+1][k+1] == sym:
                    total = total + 1
                    j = j + 1
                    k = k + 1
                else:
                    j = 7
            j = m
            k = i

            # checks for matching pieces to the right and down from the piece
            while j-1 > -1 and k-1 > -1: 
                if board[j-1][k-1] == sym:
                    total = total + 1
                    j = j - 1
                    k = k - 1
                else:
                    j = 0
            if total >= 3: # if there is 3 or more pice surounding the new pice
                return True

            # if they don't find a win state return false
            return False

        else:
            i = i-1
        



    

    return False


# prints the board state

def printBoard():
    global board
    i = 5
    while i != -1: # row
        for j in range(0,7): # colmnb
            print("|", board[j][i], end =" ")
        print("|")
        i = i-1
    
    return

def AI(t):
    print("I will rule you")

def rand(t):
    print("Duhhhh")

def player(t):
    global win 

    move = input("choose the colunb to drop your chip:") 
    move = int(move)-1
    rulling = False
    while rulling == False:
        i = False
        while i == False:
            if move > 6 or move < 0:
                print("ERROR")
                move = input("please choose a valid colunb to drop your chip:")
                move = int(move)-1
            else:
                i = True
            
        rulling = rules(move)
    place(t, move)
    win = checkWin(t, move)




p1 = None #player one type
p2 = None #player one type
board = None 
win = False
# board is a list with 7 nested lists
# the outer list represents columns and the  inner list represents rows

# board[0][n] ------> board[6][n]
# | - | - | - | - | - | - | - | board[n][5]
# | - | - | - | - | - | - | - |
# | - | - | - | - | - | - | - |
# | - | - | - | - | - | - | - |
# | - | - | - | - | - | - | - |
# | - | - | - | - | - | - | - |  board[n][0]

start() 
game(p1,p2)

