import socket

HOST = "127.0.0.1"
PORT = 12345
server_address_information = (HOST, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind(server_address_information)
client_socket.connect()