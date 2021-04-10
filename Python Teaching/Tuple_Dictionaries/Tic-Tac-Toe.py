from random import randrange

'''
Notes:

# print(board)
# for i in range(3):
#row = [i for i in range(3)]
#board.append(row)
# empty = " "
# board = [[empty for i in range(3)] for r in range(3)]
# print(f'{board[0]}\n{board[1]}\n{board[2]}')
# boardtemplate = print(f"+-------+-------+-------+\n|       |       |       |\n|   O   |   X   |   3   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   4   |   X   |   6   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   7   |   O   |   9   |\n|       |       |       |\n+-------+-------+-------+")
'''


board = [[1,2,3],[4,5,6],[7,8,9]]


#  The function accepts one parameter containing the board's current status
#  and prints it out to the console.

def display_board(board):
   current_board = (f'+-------+-------+-------+\n|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |\n+-------+-------+-------+\n|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |\n+-------+-------+-------+\n|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |\n+-------+-------+-------+')
   print(current_board)
   return current_board

# The function accepts the board current status, asks the user about their move, # checks the input and updates the board according to the user's decision.
def enter_move(board):
   while True:
      move = input("Enter square # to select: ")
      move = int(move)
      if move in range(0,4):
         select = (move - 1)
         if board[0][select] == "O" or board[0][select] == "X":
            print("\nSelect Unused Square!\n")
         else:
            board[0][select] = "O"
            display_board(board)
            return False
     
      elif move in range(4,7):
         select = (move - 4)
         if board[1][select] == "O" or board[0][select] == "X":
            print("\nSelect Unused Square!\n")
         else:
            board[1][select] = "O"
            display_board(board)
            return False
    
      elif move in range(7,10):
         select = (move - 7)
         if board[2][select] == "O" or board[0][select] == "X":
            print("\nSelect Unused Square!\n")
         else:
            board[2][select] = "O"
            display_board(board)
            return False
      
# The function draws the computer's move and updates the board.
def draw_move(board):
   while True:
      move = randrange(0,10)
      move = int(move)
      print(move)
      if board[1][1] != "X" and board[1][1] != "O":
         board[1][1] = "X"
         display_board(board)
         return False
      elif move == 5:
         pass
   
      elif move in range(1,4):
            select = (move - 1)
            if board[0][select] == "O" or board[0][select] == "X":
               pass
            else:
               board[0][select] = "X"
               display_board(board)
               return False
     
      elif move in range(4,7):
         select = (move - 4)
         if board[1][select] == "O" or board[1][select] == "X":
            pass
         else:
            board[1][select] = "X"
            display_board(board)
            return False
    
      elif move in range(7,10):
         select = (move - 7)
         if board[2][select] == "O" or board[2][select] == "X":
            pass
         else:
            board[2][select] = "X"
            display_board(board)
            return False
   
# function browses the board and builds a list of all the free squares;
# the list consists of tuples, while each tuple is a pair of row and column numbers
def make_list_of_free_fields(board):
   # print(board)
   for r in enumerate(board):
      for free in str(r):
         squares = ["1","2","3","4","5","6","7","8","9"]
         # print(squares)
         if free in squares:
            if "X" in r or "O" in r:
               print("Char %s found at list %s at index %s" % (free,r, r.index(free)))



   

print("WELCOME TO TIC-TAC-TOE~!")
while True:
   print("PLAYER TURN: ")
   current = display_board(board)
   # print(current)
   enter_move(board)
   print("Done!")
   display_board(board)
   print("COMPUTER TURN: ")
   draw_move(board)
   make_list_of_free_fields(board)



    




# def victory_for(board, sign):
#     # The function analyzes the board status in order to check if 
#     # the player using 'O's or 'X's has won the game


