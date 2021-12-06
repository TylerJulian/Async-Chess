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
    locations = {}
    
    def __init__(self, name):
        print(name)
    def set_piece(self, name):
        piece, x, y = parse_move(name)
        self.board[x][y] = name
        self.locations[name] = (x,y)
        #del locations[name]

    
