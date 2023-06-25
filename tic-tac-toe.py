def display_board(board):
   for row in board:
       print(" | ".join(row))
       print("-" * 9)

def check_winner(board):
   for row in board:
       if row[0] == row[1] == row[2] != ' ':
           return True

   for col in range(3):
       if board[0][col] == board[1][col] == board[2][col] != ' ':
           return True

   if board[0][0] == board[1][1] == board[2][2] != ' ':
       return True

   if board[0][2] == board[1][1] == board[2][0] != ' ':
       return True

   return False

def get_user_input(board, player):
   while True:
       try:
           row = int(input(f"Player {player}, enter the row (1-3): ")) - 1
           col = int(input(f"Player {player}, enter the column (1-3): ")) - 1

           if board[row][col] == ' ':
               board[row][col] = player
               break
           else:
               print("This cell is already occupied. Try again.")
       except (ValueError, IndexError):
           print("Invalid input. Try again.")

def tic_tac_toe():
   board = [[' ' for _ in range(3)] for _ in range(3)]
   player = 'X'
   moves = 0

   while not check_winner(board) and moves < 9:
       display_board(board)
       get_user_input(board, player)
       player = 'O' if player == 'X' else 'X'
       moves += 1

   display_board(board)

   if moves == 9 and not check_winner(board):
       print("It's a draw!")
   else:
       winner = 'O' if player == 'X' else 'X'
       print(f"Player {winner} wins!")

if __name__ == "__main__":
   tic_tac_toe()
