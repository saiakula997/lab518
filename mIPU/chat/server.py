import socket

# Set the IP address and port for the server
server_ip = "192.168.86.237"  # Replace with the actual IP address of your RPI
server_port = 12345  # Choose an available port

def create_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the IP address and port
    server_socket.bind((server_ip, server_port))
    
    return server_socket

def connect_client(server_socket):
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server is listening on {server_ip}:{server_port}")

    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    return client_socket, server_socket

def write_data_file(name, image):
    print("Writing image into", name)
    f = open(name, 'wb')
    f.write(image)
    f.close()

def receive_data(client_socket):
    size = int(client_socket.recv(1024).decode())
    response = "Paylod is of size : "+str(size)
    client_socket.send(response.encode())
    print(size)
    data = client_socket.recv(1024)
    while len(data) < size:
        data += client_socket.recv(1024)
    return data

def process_requests(client_socket):
    while True:
        choice = client_socket.recv(1024)
        # print("-->",choice, len(choice))
        choice = int(choice.decode())
        if choice == 1:
            message = client_socket.recv(1024).decode()
            print("Received Message : ", message)
        elif choice == 2:
            pass
        elif choice == 3:
            print("Receiving image of size", end= " ")
            image = receive_data(client_socket)
            write_data_file("received.png", image)
        elif choice == 4:
            print("Receiving File of size", end = " ")
            data = receive_data(client_socket)
            write_data_file("received.txt", data)

        else :
            print("Invalid Request from Client")
            
        
        response = "Message received by the server."
        client_socket.send(response.encode())

def main():
    server_socket = create_server()
    print("Server : Sockect Created")
    client_socket, server_socket = connect_client(server_socket)
    print("Server : Connected to Client")
    process_requests(client_socket)
    # Close the connection
    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    main()

