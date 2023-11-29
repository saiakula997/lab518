import os
import csv
import socket
import pickle
import camera
import threading

# number of samples to be collected per subject
SAMPLES_COUNT = 1
GAIN = (2/3)

# Set the IP address and port of the server (RPI)
server_ip = "172.16.0.5"  # Replace with the actual IP address of your RPI
server_port = 12345  # Use the same port as in the server

pga_fsv = { 
    2/3 : 6.144,
    1   : 4.096,
    2   : 2.048, 
    4   : 1.024,
    8   : 0.512,
    16  : 0.256,
}

def convert(x):
       return (x * pga_fsv[GAIN]) / ((2**16) * (GAIN))  

def convert_adc_voltage(data):
    v_data = []
    for row in data:
        v_row = [ convert(x) for x in row]
        v_data.append(v_row)
    return v_data

def client_request_connect():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print(f"Connected to the server at {server_ip}:{server_port}")
    return client_socket

def receive_data(client_socket):
    size = int(client_socket.recv(1024).decode())
    response = "Paylod is of size : "+str(size)
    client_socket.send(response.encode())
    print(response)
    data = client_socket.recv(1024)
    while len(data) < size:
        data += client_socket.recv(1024)
    return data

def get_data(client_socket):
    client_socket.send("DATA_SAMPLE".encode())
    data = receive_data(client_socket)
    data = pickle.loads(data)
    return data, convert_adc_voltage(data)

def write_into_file(data, file_name):
    csvfile = open(file_name, "w")
    my_write = csv.writer(csvfile, delimiter = ',')
    my_write.writerow(['ch1', 'ch2','ch3', 'ch4'])
    my_write.writerows(data)

def dot_data_collection(name, count, client_socket):
    data, v_data =  get_data(client_socket)
    print("------- dot_data_collection --------")
    file_name = name+"/ADC_sample_"+str(count)+".csv"
    write_into_file(data, file_name)
    file_name = name+"/VOLTAGE_sample_"+str(count)+".csv"
    write_into_file(v_data, file_name)

def main():
    client_socket = client_request_connect()
    while True:
        name = input("Enter q or Subject Name : ")
        if name == "q":
            break
        try:
            os.mkdir(name)
            dot_name = name+"/dot/"
            images_name = name+"/images/"
            os.mkdir(dot_name)
            os.mkdir(images_name)

        except:
            print("Invalid Name or Folder Alredy Exists ", name)
        for count in  range(SAMPLES_COUNT):
            enter = "Hit Enter to Collect Sample " + str(count)
            _ = input(enter)
            t1 = threading.Thread(target=camera.StartCamera, args=(images_name, count))
            t2 = threading.Thread(target=dot_data_collection, args=(dot_name, count, client_socket))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        print("Done")
    # Close the connection
    client_socket.close()



if __name__ == "__main__":
    main()

