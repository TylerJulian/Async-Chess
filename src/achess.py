class aChessClient():
    size = 32
    rows, cols = (size, size)
    board = [[0]*cols]*rows
    print(board)
    def __init__(self, name):
        self.name = name

