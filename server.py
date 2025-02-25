import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 12345
server_config = ((HOST, PORT))

#Function to start server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_config)
    server_socket.listen()
    print(f"Server is listioning on {HOST}:{PORT}")