#OVERVIEW OF PROJECT:
#board
#display board
#play game
#handle turn
#check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip player

#Global variable
    

#created board in list
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#if game is still going
game_still_going = True

#Who won ? or tie?
winner = None

#Whose turn is it
current_player = "X"

#Now display Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    
#Testimg display
display_board()
print()


#play_game function drags entire game
#Play game of tic tac toe
def play_game(): 
    
    
    #Display initial board
    display_board()
    #Now we want a loop to loop thorugh turns untill game is over X turn O turn'
    #While game is still going:
    while game_still_going:
        
        #handle a single turn of an arbitary player
        handle_turn(current_player)
        
        
        #check if game has ended
        check_if_game_over()
        
        
        #Flip to other player
        flip_player()
        
    # the game has ended
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("Tie!")
    

#handle a single turn of an arbitary player
#Where we get the input
def handle_turn(player):
    #When enter pressed
    print(player + "'s turn.")
    position = input("\nChoose position from 1-9:") 
    
    valid = False
    while not valid:
    #instead of IF use WHILE to keep checking
        while position not in ["1","2","3","4","5","6","7","8","9"] : 
            position = input("Invalid input. Choose a position from 1-9: ")
        
        position = int(position) - 1
    
    
        if board[position] == "-":
            valid = True
        else:
            print("You can not go there. Try again")
        
    
    #Now putting something on the board
    board[position] = player
    display_board() #Testing board with X
    
    
    
def check_if_game_over():
    check_for_winner()
    check_if_tie()
    
def check_for_winner():
    #set up global variables
    global winner
    
    #check rows
    row_winner = check_rows()
    
    #Check columns
    column_winner = check_columns()
    
    #check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
        
    else:
        #there was no winner
        winner = None
    return


def check_rows():
    #set up global variable
    global game_still_going
    #Check if any of the rows have the same value and is not same
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    #Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    #set up global variable
    global game_still_going
    #Check if any of the rows have the same value and is not same
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    #if any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    #Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
    

def check_diagonals():
    #set up global variable
    global game_still_going
    #Check if any of the rows have the same value and is not same
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    #if any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    #Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

def check_if_tie():
    global game_still_going
    #since board is a list
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    #Global variable we need
    global current_player
    #If current player was X, then change it into O
    if current_player == "X":
        current_player = "O"
    #If current player was O, then change it into X
    elif current_player == "O":
        current_player = "X"
    return
    

play_game()
    



    
    