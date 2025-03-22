import socket

HOST = "127.0.0.1"
PORT = 12345
server_address_information = (HOST, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind(server_address_information)
client_socket.connect()

while True:
    message_input = input("Please type your message: ").lower()
    if message_input != "quit":
        client_socket.send(message_input.encode())
        message_receive = client_socket.recv(1024)
        if not message_receive:
            print("The server closed the connection.")
            break

        print(message_receive.decode())
    else:
        print("Closing connection.")
        client_socket.close()