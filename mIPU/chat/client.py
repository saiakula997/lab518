import socket

# Set the IP address and port of the server (RPI)
server_ip = "RPI_IP_ADDRESS"  # Replace with the actual IP address of your RPI
server_port = 12345  # Use the same port as in the server

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))
print(f"Connected to the server at {server_ip}:{server_port}")

while True:
    message = input("Enter a message to send to the server: ")
    if message.lower() == "exit":
        break
    
    client_socket.send(message.encode())
    
    response = client_socket.recv(1024).decode()
    print(f"Server response: {response}")

# Close the connection
client_socket.close()
