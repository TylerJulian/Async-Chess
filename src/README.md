# cs5113fa21 Final project
cs5113fa21 Final project

There are 3 nodes for the following application. 1 Server node and 2 client nodes. The nodes are ran all at the same time using Docker. The nodes communicate with each other using GRPC and its various tools. The only two non node.py python files are generated using GRPC tools.

I used one file for the whole application, but separated it into 2 major functions: client and server.
The server function runs the server, maintains the states, and eventually shuts it down while the client function creates the players and has them guess.

[Link to node.py](https://github.com/TylerJulian/cs5113fa21-assignment2/blob/main/src/node.py)

The server has 4 requests that it can process. 

* reply: You give the server your guess and it responds if it is too high or too low.
* tell_name: The server returns your name.
* check_state: The server returns the current state of the game. (ON, WON, OVER)
* update_state: The server changes the state from ON to WON, WON to OVER.

The client uses the 4 requests to try to guess the correct number as fast as possible. The first correct guesser wins the game. Once both clients guess the number then the game is over.
I used the following algorithm to guess the number.

* Guess a random number from 1 - 100000
* Check if it correct. 
* Adjust the floor or ceiling
* Guess a new random from floor - ceiling
* check if it correct
* repeat until player is correct.


![Demo example](media/demo.gif)
