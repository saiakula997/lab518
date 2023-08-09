import socket

# Set the IP address and port of the server (RPI)
server_ip = "192.168.86.237"  # Replace with the actual IP address of your RPI
server_port = 12345  # Use the same port as in the server

def client_request_connect():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print(f"Connected to the server at {server_ip}:{server_port}")
    return client_socket

def get_data(name):
    f = open(name, "rb")
    data = f.read()
    f.close()
    return data, len(data)

def send_data(data, size, client_socket):
    bytes_sent = 0
    client_socket.send(str(size).encode())
    response = client_socket.recv(1024).decode()
    print(f"Server response: {response}")
    while bytes_sent+1024 < size:
        client_socket.send(data[bytes_sent:bytes_sent+1024])
        bytes_sent += 1024
    client_socket.send(data[bytes_sent:])

        

def menu(client_socket, choice):
    client_socket.send(str(choice).encode())
    if choice == 1:
        message = input ("Enter your message : ").encode()
        client_socket.send(message)
    elif choice == 2:
        pass
    elif choice == 3:
        print("Sending Image")
        image, size = get_data("send.png")
        send_data(image, size, client_socket)
    elif choice == 4:
        print("Sending File")
        data, size = get_data("send.txt")
        send_data(data, size, client_socket)
    else:
        print("Invalid Request from Client")
    response = client_socket.recv(1024).decode()
    print(f"Server response: {response}")

def print_menu():
    print("########################################################")
    print("1. Send Message")
    print("2. Request Message")
    print("3. Send an Image")
    print("4. Send a Text File")
    print("0. Exit")
    print("########################################################")
    print("Enter Choice : ")
    try : 
        return int(input())
    except:
        print("Invalid Choice, Try Again")
    

def main():
    client_socket = client_request_connect()
    while True:
        choice = print_menu()
        if choice == '0':
            break
        else:
            menu(client_socket, choice)

    # Close the connection
    client_socket.close()



if __name__ == "__main__":
    main()

