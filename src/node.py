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

def server():
	
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	guessing_game_pb2_grpc.add_GuessingGameServicer_to_server(GuessingGame(), server)
	server.add_insecure_port('[::]:50051')
	server.start()
	print("server started")
	time.sleep(15)
	server.stop(10)
	#server.wait_for_termination()

def client():
	time.sleep(1)
	game = achess.aChessClient("test")
	ongoing = True
	count = 0
	
	low = 0
	high = 100000
	response = ""
	while(ongoing == True):
		time.sleep(.1)
		ran_num = random.randint(low, high)
		with grpc.insecure_channel('server:50051') as channel:
			stub = guessing_game_pb2_grpc.GuessingGameStub(channel)
			guess = guessing_game_pb2.Guess(guess = ran_num)
			response =  stub.reply(guess)
		
			print("Guess: " + str(ran_num) + " response: " + response.feed)
			if (response.feed == "correct"):
				response = stub.update_state(guessing_game_pb2.Name(name = socket.gethostname()))
				ongoing = False
			elif(response.feed == "low"):
				low = ran_num + 1
			elif(response.feed == "high"):
				high = ran_num - 1
	print("I am done!")
	time.sleep(1)
	with grpc.insecure_channel('server:50051') as channel:		
		stub = gue
		ssing_game_pb2_grpc.GuessingGameStub(channel)
		response = stub.check_state(guessing_game_pb2.GameState(state = stat))
		while (response.state != "over"):
			response = stub.check_state(guessing_game_pb2.GameState(state = stat))
		

# main function

if (socket.gethostname() == "server"):
	server()
else:
	time.sleep(3)
	client()

