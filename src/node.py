import time
import socket
import grpc
import grpc.experimental
import random
from concurrent import futures

random.seed()
stat = "on" # "won", "over"
ran_num = random.randint(0, 100000)

import chess_game_pb2_grpc
import chess_game_pb2

import achess
chess_server = achess.aChessServer(socket.gethostname())

class ChessGame(chess_game_pb2_grpc.ChessGameServicer):
    def check_state(self, request, context):
        return chess_game_pb2.acknowledge()
    def update_state(self, request, context):
        return chess_game_pb2.acknowledge()
    def set_piece(self, request, context):
        name = request.name
        piece, x, y, color = achess.parse_move(name)
        chess_server.set_piece(name)
        return chess_game_pb2.acknowledge()
    def move(self, request, context):
        move = chess_server.update_location(request.name, request.new_move)
        
        if(move == "kill"):
            move = False
            kill = True
        else:
            kill = False

        return chess_game_pb2.acknowledge(state = chess_server.state, moved = move)

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 32))
    chess_game_pb2_grpc.add_ChessGameServicer_to_server(ChessGame(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    x = 0
    while(chess_server.state == "ongoing"):
        #print(chr(27) + "[2J")
        if(chess_server.count < 32):
            print(chess_server.count)

        else: 
            chess_server.print_board()
        
        time.sleep(.1)
    time.sleep(1)
    server.stop(3)
    #server.wait_for_termination()

def client():
    name = socket.gethostname()
    client_name = name
    type_of_piece = name[0]
    location = name[1:3]
    color = name[5:6]
    
    game = achess.aChessClient(client_name)
    ongoing = True

    response = ""

    with grpc.insecure_channel('server:50051') as channel:
        stub = chess_game_pb2_grpc.ChessGameStub(channel)
        name = chess_game_pb2.Name(name = name)
        response = stub.set_piece(name)
    count = 0
    while(ongoing == True):

        with grpc.insecure_channel('server:50051') as channel:
            stub = chess_game_pb2_grpc.ChessGameStub(channel)
            move = game.move()
            moved = move

            move = chess_game_pb2.new_move(name = client_name, new_move = move)
            move = stub.move(move)
            if(move.moved == True): # check if the piece actually moved.
                game.update_move(moved)
            if(move.kill == True):
                ongoing = False
            if(move.state != "ongoing"):
                ongoing = False
            else: 
                count = count + 1
        
	    

    # main function

if (socket.gethostname() == "server"):
    server()
else:
    time.sleep(15)

    client()


