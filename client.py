import socket
import threading
import time


SERVER_HOST = '127.0.0.1'
SERVICE_PORT = 1234
BUFFER_SIZE = 1024
ENCODER = 'UTF-8'

name = input("Name: ")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVICE_PORT))
print("Connection done...")
time.sleep(1)
print("Receiving name to server...")
client_socket.send(bytes(name, ENCODER))
time.sleep(1)
print("Receiving done!")
print("You can start the chat...")


def send_message():
    while True:
        msg = input()
        client_socket.send(bytes(f"{name}: {msg}", ENCODER))


def receive_message():
    while True:
        msg = client_socket.recv(BUFFER_SIZE).decode(ENCODER)
        print(msg)


send_message_thread = threading.Thread(target=send_message).start()
receive_message_thread = threading.Thread(target=receive_message).start()