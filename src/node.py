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



class GuessingGame(guessing_game_pb2_grpc.GuessingGameServicer):
	def reply(self, request, context):
		
		if ( request.guess > ran_num):
			rep = guessing_game_pb2.Feedback(feed = "high")
		elif (request.guess < ran_num):
			rep = guessing_game_pb2.Feedback(feed = "low")
		else:
			rep = guessing_game_pb2.Feedback(feed = "correct")
		return rep
	def tell_name(self, request, context):
		return guessing_game_pb2.Name(name = "test")
	def check_state(self, request, context):
		return guessing_game_pb2.GameState(state = stat)
	def update_state(self, request, context):
		global stat
		if (stat == "on"):
			stat = "won"
			print(request.name + " won the game!")
		if (stat == "won"):
			stat = "over"
		return guessing_game_pb2.GameState(state = stat)
	def set_piece(self, request, context):
	    name = request.name
	    piece, x, y = achess.parse_move(name)
	    chess_server.set_piece(name)
	    return request
	        
chess_server = achess.aChessServer(socket.gethostname())
def server():
	
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	guessing_game_pb2_grpc.add_GuessingGameServicer_to_server(GuessingGame(), server)
	server.add_insecure_port('[::]:50051')
	server.start()

	print("server started")
	time.sleep(15)
	#print(chess_server.board)
	#print(chess_server.locations)
	chess_server.print_board()
	server.stop(3)
	#server.wait_for_termination()

def client():
	time.sleep(1)
	name = socket.gethostname()
	type_of_piece = name[0]
	location = name[1:3]
	
	game = achess.aChessClient(name)
	ongoing = True

	response = ""
	while(ongoing == True):
		with grpc.insecure_channel('server:50051') as channel:
			stub = guessing_game_pb2_grpc.GuessingGameStub(channel)
			name = guessing_game_pb2.Name(name = name)
			
			response = stub.set_piece(name)
			#print(game.move())
			
			ongoing = False
		

# main function

if (socket.gethostname() == "server"):
	server()
else:
	time.sleep(3)
	client()

