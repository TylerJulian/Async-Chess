# cs5113fa21-fproj
Tyler Julian

The project implements asynchronous chess. Each chess piece is a client that connects to the board (server). Each piece makes a move independently of each other piece without a set turn order. You can read more on the project description [here](https://oudatalab.com/cs5113fa21/projects/project). 

There is no turn timer and no turn order, so each piece is constantly making new moves until a checkmate is determined. Since a check isn't a guaranteed loss using normal chess rules, I have determined that the game is over when the king is taken. 

## Here is a quick overview of the project. 
- The chess board is 32 x 32, but the pieces are located normally in their respective spots. (This can be easily changed)
- Each chess piece on the board is a player (client) that connects to the board (server)
- There is no turn order and each piece makes a move independent of the other pieces. The piece then sends its proposed move to the server. 
- The server puts the move request on the queue and then processes the first move request on the queue.
- Once the request is processed, the server determines if the move is legal then replies back with an acknowledge message.
- The acknowledge message tells the player (client) if their piece was moved or not. 
- The client then detemines its state from the acknowledge mesaage and updates its eternal state.
- Each client will continue to make moves until one of the following happens.
    - The game is over due to a checkmate (A king is taken)
    - The client is taken
    - The client has no legal moves. (It will wait until there is a legal move.)

The following technologies were used in my implementation. 
    - Python
        -Numpy, The board is stored as a 32x32 array
        -random, The moves are not determined by an AI. The moves are randomly determined.
        -socket, get hostname of the clients (usernames of players)
        -time, This is used for the 10 hz refresh rate of the game board.
        -grpc, see above for the grpc uses.
    - (Docker)[https://www.docker.com/] , Docker was used to launch the 32 clients and the server.
    - (gRPC)[https://www.grpc.io/docs/what-is-grpc/introduction/], gRPC handled the queue and the messages between the client and server.
    - (protool buffers)[https://developers.google.com/protocol-buffers], Protocol buffers provided the messages sent between the server and client.

The project can be ran by running the startup.bash file in the src folder. 

The project video can be found here. Click on the thumbnail.
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)