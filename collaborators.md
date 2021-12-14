Here are the following resources I used. 

Christan Grant, Instructor, Canvas and lectures were used to create this project.
The project webpage was used as a reference for the creation of the game. 

I reused the docker setup from our first project in this project. I renamed the files, but kept the general structure during development.

grpc.github.io/grpc/python, GRPC docs

docs.python.org/3/howto/unicode.html, unicode chess figure.

I used the following librarys and resources to develop my program. 

Linux VM - virtualbox on Ubuntu 20
Version control - Git, so I could switch between multiple VMs for testing.
Docker - Used docker to start each client and server.
Python - programmed using python
gRPC, handles the messaging between the client and server, and it has a built in queue for handling the scheduling of the moves. The moves are processed using a queue.
protcol buffers, these are the messages sent between devices. The most common messages are the move message and the acknowledge message. 
