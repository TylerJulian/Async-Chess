import time
import socket
import guessing_game_pb2
import grpc
import grpc.experimental
import random
from concurrent import futures

random.seed()
stat = "on" # "won", "over"
ran_num = random.randint(0, 100000)

import guessing_game_pb2_grpc
import guessing_game_pb2

import achess
chess_server = achess.aChessServer(socket.gethostname())

class GuessingGame(guessing_game_pb2_grpc.GuessingGameServicer):
    def check_state(self, request, context):
        return guessing_game_pb2.acknowledge()
    def update_state(self, request, context):
        return guessing_game_pb2.acknowledge()
    def set_piece(self, request, context):
        name = request.name
        piece, x, y = achess.parse_move(name)
        chess_server.set_piece(name)
        return guessing_game_pb2.acknowledge()
    def move(self, request, context):
        chess_server.update_location(request.name, request.new_move)
        return guessing_game_pb2.acknowledge()

def server():
    print("hello")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    guessing_game_pb2_grpc.add_GuessingGameServicer_to_server(GuessingGame(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    x = 0
    while(chess_server.state == "ongoing"):
        x = x + 1
        if(x == 5):
            chess_server.print_board()
            x = 0
        time.sleep(1)
    server.stop(3)
    #server.wait_for_termination()

def client():
    name = socket.gethostname()
    print(name + "client")
    client_name = name
    type_of_piece = name[0]
    location = name[1:3]
    game = achess.aChessClient(client_name)
    ongoing = True

    response = ""

    with grpc.insecure_channel('server:50051') as channel:
        stub = guessing_game_pb2_grpc.GuessingGameStub(channel)
        name = guessing_game_pb2.Name(name = name)
        response = stub.set_piece(name)
    count = 0
    while(ongoing == True):
        try:
            with grpc.insecure_channel('server:50051') as channel:
                stub = guessing_game_pb2_grpc.GuessingGameStub(channel)
                move = game.move()
                moved = move
                game.update_move(moved)
                move = guessing_game_pb2.new_move(name = client_name, new_move = move)
                move = stub.move(move)
                if count == 10000:
                    ongoing = False
                else: 
                    count = count + 1
        except:
            ongoing = False
	    

    # main function

if (socket.gethostname() == "server"):
    server()
else:
    time.sleep(3)
    client()

