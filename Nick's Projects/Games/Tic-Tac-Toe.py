from random import randrange
import time


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
# def quit(func):
#    try:
#       func()
#    except(ValueError,KeyboardInterrupt):
#       print("Exiting Game...")
#       time.sleep(3)


def game_start():
   board = [[1,2,3],[4,5,6],[7,8,9]]
   print("WELCOME TO TIC-TAC-TOE~!")
   display_board(board)
   while True:
      count = 0   
      print("PLAYER TURN:")
      enter_move(board)
      if victory_for(board, 'O') == False:
         break
      count + 1
      if count >= 9:
         print("TIE!")
      print("COMPUTER TURN:")
      draw_move(board)
      if victory_for(board, 'X') == False:
         break
      count + 1
      make_list_of_free_fields(board)
   print("Game Over")
   key = input("Press Enter to quit or 'r' to play again: ")
   if key == 'r':
      game_start()



#  The function accepts one parameter containing the board's current status
#  and prints it out to the console.

def display_board(board):
   current_board = (f'+-------+-------+-------+\n|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |\n+-------+-------+-------+\n|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |\n+-------+-------+-------+\n|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |\n+-------+-------+-------+')
   print(current_board)
   return current_board

# The function accepts the board current status, asks the user about their move, # checks the input and updates the board according to the user's decision.

def enter_move(board):
   try:
      while True:
         move = input("Enter square # to select (ctrl + c or press enter to skip turn): ")
         move = int(move)
         if    move in range(1,4):
            select = (move - 1)
            if board[0][select] == "O" or board[0][select] == "X":
               print("\nSelect Unused Square!\n")
            else:
               board[0][select] = "O"
               display_board(board)
               return False
     
         elif move in range(4,7):
            select = (move - 4)
            if board[1][select] == "O" or board[1][select] == "X":
               print("\nSelect Unused Square!\n")
            else:
               board[1][select] = "O"
               display_board(board)
               return False
    
         elif move in range(7,10):
            select = (move - 7)
            if    board[2][select] == "O" or board[2][select] == "X":
               print("\nSelect Unused Square!\n")
            else:
               board[2][select] = "O"
               display_board(board)
               return False
   except(KeyboardInterrupt,ValueError):
         print("Skipping turn...")
         time.sleep(1.5)
      
# The function draws the computer's move and updates the board.

def draw_move(board):
   while True:
      move = randrange(0,10)
      move = int(move)
      # print(move)
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


# The function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game

def victory_for(board, sign):
   win_array = [sign,sign,sign]
   combo = [[board[0][0],board[0][1],board[0][2]],[board[1][0],board[1][1],board[1][2]],[board[2][0],board[2][1],board[2][2]],[board[0][0],board[1][0],board[2][0]],[board[0][1],board[1][1],board[2][1]],[board[0][1],board[1][1],board[2][1]],[board[0][2],board[1][2],board[2][2]],[board[0][0],board[1][1],board[2][2]],[board[0][0],board[1][1],board[2][2]],[board[2][0],board[1][1],board[0][2]]]
   
   if win_array in combo:
      print(f"Player '{sign}' wins!")
      return False



game_start()





    



