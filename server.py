import socket
import threading


HOST = '127.0.0.1'
PORT = 1234
ENCODER = 'UTF-8'
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server listenting at '{HOST}:{PORT}'")


clients_sockets_list = []
clients_names = []


def broadcast_messages_to_all_clients(message: str) -> None:
    for client_socket in clients_sockets_list:
        client_socket.send(bytes(message, ENCODER))


def handle_client(client_socket):
    while True:
        msg = client_socket.recv(BUFFER_SIZE).decode(ENCODER)
        broadcast_messages_to_all_clients(msg)


def handle_connections():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New Connection '{client_address[0]}:{client_address[1]}'")

        client_name = client_socket.recv(BUFFER_SIZE).decode(ENCODER)
        clients_sockets_list.append(client_socket)
        clients_names.append(client_name)

        client_handle_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_handle_thread.start()


handle_connections()
