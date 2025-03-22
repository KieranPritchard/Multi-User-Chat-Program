import socket

# Server configuration
HOST = "127.0.0.1"
PORT = 12345
server_address_information = (HOST, PORT)

# This creates the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(server_address_information)
    print("Connected to the server. Type 'quit' to exit.")

    while True:
        # This takes in user input then formats and checks it for the quit message
        message_input = input("Please type your message: ").lower()
        if message_input != "quit":
            client_socket.send(message_input.encode())
            message_receive = client_socket.recv(1024)
            if not message_receive:
                print("The server closed the connection.")
                break

            print(message_receive.decode())
        else:
            # This closes the connection if the 
            print("Closing connection.")
            client_socket.close()
except Exception as e:
    print(f"Encountered Error {e}")