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
    def win_check(board, white_moves,black_moves):
        if board[7] == "w" or board[8] == "w" or board[9] == "w":
            return 1
        elif board[1] == "b" or board[2] == "b" or board[3] == "b":
            return -1
        elif "w" not in board:
            return -1
        elif "b" not in board:
            return 1
        elif white_moves == []:
            return -1
        elif black_moves == []:
            return 1
        else: 
            return 0
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



ip = int(input("h"))
col = (ip-1)%3
row = int((ip-1)/3)
print(row,col)