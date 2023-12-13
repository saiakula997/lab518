import socket
import pickle
import dot_sensor

# Set the IP address and port for the server
server_ip = "192.168.86.241"  # Replace with the actual IP address of your RPI
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

def send_data(data, size, client_socket):
    print("Sending Data ...")
    bytes_sent = 0
    client_socket.send(str(size).encode())
    response = client_socket.recv(1024).decode()
    print(f"Server response: {response}")
    while bytes_sent+1024 < size:
        client_socket.send(data[bytes_sent:bytes_sent+1024])
        bytes_sent += 1024
    client_socket.send(data[bytes_sent:])


def process_requests(client_socket):
    while True:
        choice = client_socket.recv(1024)
        if str(choice.decode()) == "DATA_SAMPLE":
            print(choice.decode())
            data = dot_sensor.get_readings()
            data = pickle.dumps(data)
            size = len(data)
            # print(data, size)
            send_data(data, size, client_socket)
        else :
            print("Invalid Request from Client")
            
        response = "Message received by the server."
        client_socket.send(response.encode())

def main():
    server_socket = create_server()
    print("Server : Sockect Created")
    client_socket, server_socket = connect_client(server_socket)
    print("Server : Connected to Client")
    try:
        process_requests(client_socket)
    except Exception as error:
        print("Check the error case", error)
    # Close the connection
    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    main()

