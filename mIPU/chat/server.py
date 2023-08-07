import socket

# Set the IP address and port for the server
server_ip = "10.0.0.3"  # Replace with the actual IP address of your RPI
server_port = 12345  # Choose an available port

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server is listening on {server_ip}:{server_port}")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(f"Received data: {data}")
    
    response = "Message received by the server."
    client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
