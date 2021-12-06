import random
import numpy

def parse_move(move):
    piece = move[0]
    x = int(move[1:3])
    y = int(move[3:5])
    return piece, x, y
def encode_move(piece, x, y):
    move = ""
    move += piece[0]
    move += str(x).zfill(2)
    move += str(y).zfill(2)
    return move
def inrange(x, y):
    if (-1 < x < 32) & (-1 < y < 32):
        return True
    return False


class aChessClient():
    size = 32
    rows, cols = (size, size)
    board = [[0]*cols]*rows
    
    name = ""
    type_of_piece = ""
    location = ""
    locationx = ""
    locationy = ""
    
    #print(board)
    def __init__(self, name):
        self.name = name[0:6]
        self.location = name[1:4]
        self.type_of_piece, self.locationx, self.locationy = parse_move(self.name)
        

    def move(self):
        x = self.locationx
        y = self.locationy
        if(self.type_of_piece == 'k'):
            x = random.randrange(-1,1)
            y = random.randrange(-1,1)
       
            x = self.locationx + x
            y = self.locationy + y
            if(not inrange(x,y)):
                x = self.locationx
                y = self.locationy
                
        new_move = encode_move(self.type_of_piece, x, y)
        return new_move
        
class aChessServer():
    size = 32

    board = numpy.empty((32,32), dtype = '|S6')
    for x in range(32):
        for y in range(32):
            board[x][y] = "x"
    locations = {}
    
    def __init__(self, name):
        print(name)
    def set_piece(self, name):
        piece, x, y = parse_move(name)
        self.board[x][y] = name
        self.locations[name] = (x,y)
        #del locations[name]

    def print_board(self):
        board_str = ""
        for x in range(32):
            for y in range(32):
                symbol = self.board[31 - y][31 - x].decode('UTF-8')
                print(x,y)
                symbol = self.convert_symbol(symbol)
                board_str += symbol
            board_str += "\n"
        print(board_str)
        
    def convert_symbol(self, name):
        piece = name[0:1]
        color = name[5:6]
        code = 0
        if (piece == ''):
            code = 0
        elif (piece == 'k'):
            code = 2654
        elif (piece == 'q'):
            code = 2655
        elif (piece == 'r'):
            code = 2656
        elif (piece == 'b'):
            code = 2657   
        elif (piece == 'n'):
            code = 2658
        elif (piece == 'p'):
            code = 2659
        if (color == 'b'):
            code = code + 6
        if (code != 0):
            code = str(code).encode("UTF-8").decode("UTF-8") + "|"
        else:
            code = " |"
        return code
