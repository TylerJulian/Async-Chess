import random
import numpy
#docs.python.org/3/howto/unicode.html

def parse_move(move):
    piece = move[0]
    x = int(move[1:3])
    y = int(move[3:5])
    color = move[5:6]
    return piece, x, y, color
def encode_move(piece, x, y, color):
    move = ""
    move += piece[0]
    move += str(x).zfill(2)
    move += str(y).zfill(2)
    move += color[0]
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
    color = ""
    
    #print(board)
    def __init__(self, name):
        self.name = name[0:6]
        self.location = name[1:4]
        self.type_of_piece, self.locationx, self.locationy, self.color = parse_move(self.name)
        

    def move(self):
        x = self.locationx
        y = self.locationy
        if(self.type_of_piece == 'k'):
            x = random.randrange(-1,2)
            y = random.randrange(-1,2)
            x = self.locationx + x
            y = self.locationy + y
            if(not inrange(x,y)):
                x = self.locationx
                y = self.locationy
        if(self.type_of_piece == 'q'):
            dir = random.randrange(-1,5)
            x = random.randrange(-16,17)
            if(dir == 0):
                #vertical
                x = self.locationx
                y = self.locationy + x
            if(dir == 1):
                #horizontal
                x = self.locationx + x
                y = self.locationy
            if(dir == 2):
                #diag left
                x = self.locationx + x
                y = self.locationy - x
            if(dir == 3):
                #diag right
                x = self.locationx - x
                y = self.locationy + x

            if(not inrange(x,y)):
                x = self.locationx
                y = self.locationy
        if(self.type_of_piece == 'p'):
            if(self.color == 'w'):
                x = self.locationx
                y = self.locationy + 1
            else:
                x = self.locationx
                y = self.locationy - 1
            if(not inrange(x,y)):
                x = self.locationx
                y = self.locationy
                self.type_of_piece = 'q'
        if(self.type_of_piece == 'r'):
            dir = random.randrange(-1,2)
            x = random.randrange(-16,17)
            if(dir == 0):
                #vertical
                x = self.locationx
                y = self.locationy + x
            if(dir == 1):
                #horizontal
                x = self.locationx + x
                y = self.locationy
            if(not inrange(x,y)):
                x = self.locationx
                y = self.locationy
        if(self.type_of_piece == 'b'):
            dir = random.randrange(-1,2)
            x = random.randrange(-16,17)
            if(dir == 0):
                #diag left
                x = self.locationx - x
                y = self.locationy + x
            if(dir == 1):
                #diag right
                x = self.locationx + x
                y = self.locationy - x
            if(not inrange(x,y)):
                x = self.locationx
                y = self.locationy
        if(self.type_of_piece == 'n'):
            dir = random.randrange(-1,8)
            x = random.randrange(-16,17)
            if(dir == 0):
                #up right
                y = self.locationy + 2
                x = self.locationx - 1
            if(dir == 1):
                #up left
                y = self.locationy + 2
                x = self.locationx + 1
            if(dir == 2):
                #down right
                x = self.locationx - 2
                y = self.locationy + 1
            if(dir == 3):
                #down left
                x = self.locationx - 2
                y = self.locationy + 1

            if(dir == 4):
                #left up
                x = self.locationx + 1
                y = self.locationy - 2
            if(dir == 5):
                #left down
                x = self.locationx - 1
                y = self.locationy - 2
            if(dir == 6):
                #right up
                x = self.locationx + 1
                y = self.locationy + 2
            if(dir == 7):
                #right down
                x = self.locationx - 1
                y = self.locationy + 2
            if(not inrange(x,y)):
                x = self.locationx
                y = self.locationy
        new_move = encode_move(self.type_of_piece, x, y, self.color)
        return new_move
    def update_move(self, move):
        piece, x, y, color = parse_move(move)
        self.locationx = x
        self.locationy = y
        return move
class aChessServer():
    size = 32
    count = 0
    state = "ongoing" # over # ending
    board = numpy.empty((32,32), dtype = '|S6')
    for x in range(32):
        for y in range(32):
            board[x][y] = "x"
    locations = {}
    queue = [] # (name, move)
    
    def __init__(self, name):
        print(name)
    def set_piece(self, name):
        piece, x, y, color = parse_move(name)
        self.board[x][y] = name
        self.locations[name] = (x,y)
        self.count = self.count + 1
        #del locations[name]
    def update_location(self, name, move):
        #print("debug 1")
        #self.print_board()
        if(self.count < 32):
            return False
        piece, x, y, color = parse_move(move)
        piecen, xn, yn, colorn = parse_move(name)

        
        ox,oy = self.locations[name] # old x old y
        if(ox == -1):
            return "kill"
        if (self.board[x][y] == b'x'):
            self.board[x][y] = name
            self.board[ox][oy] = b'x'
            self.locations[name] = (x, y)
            return True
        else:
            occupied = self.board[x][y]
            if (occupied.decode('UTF-8')[5:6] == name[5:6]):
                return False
            else:
                if(occupied.decode('UTF-8') == name):
                    return False 
                self.board[x][y] = name
                self.board[ox][oy] = b'x'
                self.locations[name] = (x, y)
                self.locations[occupied.decode('UTF-8')] = (-1,-1)
                #print(occupied.decode('UTF-8'))
                occupied = occupied.decode('UTF-8')
                if (occupied[0:1] == 'k'):
                    self.state = "over"
                    self.print_board()
                return True
            return False

    def print_board(self):
        board_str = ""
        for x in range(32):
            for y in range(32):
                symbol = self.board[y][31 - x].decode('UTF-8')
                #print(x,y)
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
            code = 0x2654
        elif (piece == 'q'):
            code = 0x2655
        elif (piece == 'r'):
            code = 0x2656
        elif (piece == 'b'):
            code = 0x2657   
        elif (piece == 'n'):
            code = 0x2658
        elif (piece == 'p'):
            code = 0x2659
        if (color == 'b'):
            code = code + 6
        if (code != 0):
            code = chr(code)
            code.encode("UTF-8")
            code = code  + str(" |")
        else:
            code = "  |"
        return code
