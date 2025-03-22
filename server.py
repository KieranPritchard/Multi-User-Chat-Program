import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 12345
server_config = ((HOST, PORT))

# Keeps a list of all the connected clients
clients = []

#Function to handle and broadcast messages
def handle_client(client_socket):
    while True:
        received_message = client_socket.recv(1024).decode()
        if received_message:
            for client in clients:
                if HOST != client:
                    client.send(received_message.encode())
                else:
                    continue

#Function to start server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_config)
    server_socket.listen()
    print(f"Server is listioning on {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)

        # Starts a new thread to stop any blocking
        client_thread = threading.Thread(target=handle_client, args=(client_socket))
        client_thread.start()