import socket
import threading
import flask_socketio

connected_clients = []

def start_server():
    #open socket server
    pass

def handle_client():
    #handles requests
    pass

"""
SOCKET_IP = "127.0.0.1"
SOCKET_PORT = 5000
server = None
client = None
connected_clients = []

def start_server():
    #open socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SOCKET_IP, SOCKET_PORT))
    server.listen(5)
    print(f"WebSocket server listening on {SOCKET_IP}:{SOCKET_PORT}")
    main() # constantly look for requests 

def handle_client(client_socket):
        data = client_socket.recv(1024)
        data = 0;
        # process the data for each client
        client.send(data)

def main():
    while True:
        try:
            client, addr = server.accept()
            print(f"Accepted connection from {addr[0]}:{addr[1]}")

            # Create a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client,))
            client_thread.start()
        except:
             print("Hello")
             continue
"""