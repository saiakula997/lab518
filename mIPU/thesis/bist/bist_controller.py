import time
import json
import string
import random
import gpio
import csv
import sn54hc153_mux as bus_controller
import AT45DB321E as ext_mem

def get_project_config():
    return json.load(open("ext_mem_config.json"))

def gen_random_string(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def callback_from_slave_1(channel):
    global prj_conf
    print("callback_from_slave_1")
    print('Bus controller select Master')
    bus_controller.select_master()
    print('Read from external memory at : ', prj_conf['SLAVE_1_OUTPUT_ADDR'])
    ext_mem.Read_String_n_Bytes_Address(prj_conf['SLAVE_1_OUTPUT_ADDR'], 16)

def callback_from_slave_2(channel):
    global prj_conf
    print("callback_from_slave_2")
    print('Bus controller select Master')
    bus_controller.select_master()
    print('Read from external memory at : ', prj_conf['SLAVE_2_OUTPUT_ADDR'])
    ext_mem.Read_String_n_Bytes_Address(prj_conf['SLAVE_2_OUTPUT_ADDR'], 16)

def create_buffer(data):
  json_bytes = json.dumps(data).encode('utf-8')
  data_size = len(json_bytes)
  buffer = bytearray(data_size.to_bytes(4, byteorder='big'))
  buffer.extend(json_bytes)
  return buffer

def print_menu():
    print('##############################################')
    print('0. Select Master')
    print('1. Select Slave-1')
    print('2. Select Slave-2')
    print('3. Signal Slave-1')
    print('4. Signal Slave-2')
    print('5. Enter Input to Slave-1')
    print('6. Enter Input to Slave-2')
    print('7. Output from Slave-1')
    print('8. Output from Slave-2')
    print('w. Write Image data to address')
    print('r. Read Image data from address')
    print('q. Quit')
    print('##############################################')
    return input()

def process(choice):
    if(choice == '0'):
        bus_controller.select_master()
    elif(choice == '1'):
        bus_controller.select_slave_1()
    elif(choice == '2'):
        bus_controller.select_slave_2()
    elif(choice == '3'):
        gpio.signal_slave_1()
    elif(choice == '4'):
        gpio.signal_slave_2()
    elif(choice == '5'):
        print('5. Enter Input to Slave-1')
        print('Bus controller select Master')
        bus_controller.select_master()

        print("Write text into external memory at : ", prj_conf['SLAVE_1_INPUT_ADDR'])
        time.sleep(1)
        
        print('Bus controller select Slave-1')
        bus_controller.select_slave_1()

        print('Signal Slave-1')
        gpio.signal_slave_1()

        print('Wait for Ack from slave-1')
    elif(choice == '6'):
        print('6. Enter Input to Slave-2')
        print('Bus controller select Master')
        bus_controller.select_master()

        print("Write text into external memory at : ", prj_conf['SLAVE_2_INPUT_ADDR'])
        time.sleep(1)
        
        print('Bus controller select Slave-2')
        bus_controller.select_slave_2()

        print('Signal Slave-2')
        gpio.signal_slave_2()

        print('Wait for Ack from slave-2')
    elif(choice == '7'):
        print('7. Output from Slave-1')
        print('Bus controller select Master')
        bus_controller.select_master()
        print('Read from external memory at : ', prj_conf['SLAVE_1_OUTPUT_ADDR'])
        ext_mem.Read_String_n_Bytes_Address(prj_conf['SLAVE_1_OUTPUT_ADDR'], 16)
    elif(choice == '8'):
        print('8. Output from Slave-2')
        print('Bus controller select Master')
        bus_controller.select_master()
        print('Read from external memory at : ', prj_conf['SLAVE_2_OUTPUT_ADDR'])
        ext_mem.Read_String_n_Bytes_Address(prj_conf['SLAVE_2_OUTPUT_ADDR'], 16)
    elif(choice == 'w'):
        image_name = input('Enter Image name :')
        address = int(input("Enter address :"), 16)
        f = open(image_name, mode="rb")
        data = f.read()
        f.close()
        ext_mem.Erase_Write_n_Bytes_Address(address, data)
    elif(choice == 'r'):
        address = int(input("Enter address :"), 16)
        n = int(input('Enter number of bytes :'))
        data = ext_mem.Read_n_Bytes_Address(address, n)
        output_image = "verify.png"
        f = open(output_image, 'wb')
        f.write(data)
        f.close()
        print("Image Re-Written into", output_image)

prj_conf = get_project_config()
if __name__ == "__main__":

    start= time.time_ns()
    gpio.init("MASTER")
    end= time.time_ns()
    print("Time Taken [gpio.init] ", end-start)

    start= time.time_ns()
    ext_mem.init()
    end= time.time_ns()
    print("Time Taken [ext_mem.init] ", end-start)
    
    start= time.time_ns()
    bus_controller.select_master()
    end= time.time_ns()
    print("Time Taken [bus_controller.select_master] ", end-start)

    random_string = gen_random_string()
    start= time.time_ns()
    ext_mem.Write_String_n_Bytes_Address(prj_conf["SLAVE_1_INPUT_ADDR"], random_string)
    end= time.time_ns()
    time.sleep(1)
    print("Time Taken [ext_mem.Write_String_n_Bytes_Address] ", end-start)
    
    start= time.time_ns()
    string_read = ext_mem.Read_String_n_Bytes_Address(prj_conf["SLAVE_1_INPUT_ADDR"], len(random_string))
    end= time.time_ns()
    print("Time Taken [ext_mem.Read_String_n_Bytes_Address] ", end-start)

    print("random_string : ", random_string)
    print("string_read : ", string_read)
    assert string_read == random_string, "string_read is not equal to random_string"

    start= time.time_ns()
    bus_controller.select_master()
    end= time.time_ns()
    print("Time Taken [bus_controller.select_master] ", end-start)

    random_string = gen_random_string()
    start= time.time_ns()
    ext_mem.Write_String_n_Bytes_Address(prj_conf["SLAVE_2_INPUT_ADDR"], random_string)
    end= time.time_ns()
    time.sleep(1)
    print("Time Taken [ext_mem.Write_String_n_Bytes_Address] ", end-start)

    start= time.time_ns()
    string_read = ext_mem.Read_String_n_Bytes_Address(prj_conf["SLAVE_2_INPUT_ADDR"], len(random_string))
    end= time.time_ns()
    print("Time Taken [ext_mem.Read_String_n_Bytes_Address] ", end-start)
    print("random_string : ", random_string)
    print("string_read : ", string_read)
    assert string_read == random_string, "string_read is not equal to random_string"

    start= time.time_ns()
    bus_controller.select_master()
    end= time.time_ns()
    print("Time Taken [bus_controller.select_master] ", end-start)
    random_string = gen_random_string()
    start= time.time_ns()
    ext_mem.Write_String_n_Bytes_Address(prj_conf["SLAVE_2_OUTPUT_ADDR"], random_string)
    end= time.time_ns()
    time.sleep(1)
    print("Time Taken [ext_mem.Write_String_n_Bytes_Address] ", end-start)

    start= time.time_ns()
    string_read = ext_mem.Read_String_n_Bytes_Address(prj_conf["SLAVE_2_OUTPUT_ADDR"], len(random_string))
    end= time.time_ns()
    print("Time Taken [ext_mem.Read_String_n_Bytes_Address] ", end-start)
    print("random_string : ", random_string)
    print("string_read : ", string_read)
    assert string_read == random_string, "string_read is not equal to random_string"

    start= time.time_ns()
    bus_controller.select_slave_2()
    end= time.time_ns()
    print("Time Taken [bus_controller.select_slave_2] ", end-start)
    start= time.time_ns()
    gpio.signal_slave_2()
    end= time.time_ns()
    print("Time Taken [gpio.signal_slave_2] ", end-start)
    time.sleep(5)

    start= time.time_ns()
    bus_controller.select_slave_1()
    end= time.time_ns()
    print("Time Taken [bus_controller.select_slave_1] ", end-start)
    
    start= time.time_ns()
    gpio.signal_slave_1()
    end= time.time_ns()
    print("Time Taken [gpio.signal_slave_1] ", end-start)
    time.sleep(5)

    while(True):
        print("Enter your choice : ")
        choice = print_menu()
        process(choice)
        if choice == 'q':
            break

    start= time.time_ns()
    gpio.deinit()
    end= time.time_ns()
    print("Time Taken [gpio.deinit] ", end-start)
    
    start= time.time_ns()
    ext_mem.deinit()
    end= time.time_ns()
    print("Time Taken [ext_mem.deinit] ", end-start)


    
    





