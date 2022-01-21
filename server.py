import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

# handles connection from one sender
def handle_connection(connection, address):
    connected = True
    while connected:
        msg = connection.recv(1024).decode(FORMAT)
        if msg:
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{address}] {msg}")

    connection.close()


# accept connections and handle them
def start():
    server.listen()
    print(f"[START] Server is listening on {SERVER}:{PORT}...")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_connection, args=(connection, address))
        thread.start()


start()
