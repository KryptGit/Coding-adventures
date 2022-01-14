class Board:

    def __init__(self):
        pass
    def generate_board():
        board = {1: "w", 2:"w", 3:"w"
        , 4:"4", 5:"5", 6:"6",
        7:"b", 8:"b", 9:"b",}
class functions:
    def __init__(self):
      pass
    def win_check(board):
        if board[7] == "w" or board[7] == "w" or board[7] == "w":
            return 1

ip = int(input("h"))
col = (ip-1)%3
row = int((ip-1)/3)
print(row,col)