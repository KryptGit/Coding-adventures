
class Board:
  def __init__(self):
    pass
  def generate_board():
    board = {1: "1", 2:"2", 3:"3"
    , 4:"4", 5:"5", 6:"6",
    7:"7", 8:"8", 9:"9",}
    return board
  def edit(action ,pos, board, player = None):
    default_value = str(pos)
    if action == "remove":
      board[pos] = default_value
    if action == "add":
      board[pos] = player
  def move(player, startingpos, targetpostion, board):
    if not startingpos == player:
      print('you cant move the opponents peice')
      return 
    edit("remove", startingpos, board)
    edit('add', targetpostion, board, player)
  class Player:
    def __init__(self, name, symbol):
      self.name = name
      self.symbol = symbol
  class functions:
    def __init__(self):
      pass
    def win_check(board):
      if board[1] == board[2] and board[2] == board[3]:
        return board[1]
      elif board[4] == board[5] and board[5] == board[6]:
        return board[4]
      elif board[7] == board[8] and board[8] == board[9]:
        return board[7]
      elif board[1] == board[4] and board[4] == board[7]:
        return board[1]
      elif board[2] == board[5] and board[5] == board[8]:
        return board[2]
      elif board[3] == board[6] and board[6] == board[9]:
        return board[3]
      elif board[1] == board[5] and board[5] == board[9]:
        return board[1]
      elif board[7] == board[5] and board[5] == board[3]:
        return board[7]
      else:
        return 0
    def Which_Player_Won(board):
      return win_check(board)
      
    