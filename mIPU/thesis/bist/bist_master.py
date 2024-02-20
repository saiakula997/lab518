import time
import json
import string
import random
import gpio
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

def print_menu():
    print('##############################################')
    print('1. Signal Slave-1')
    print('2. Signal Slave-2')
    print('3. Select Slave-1')
    print('4. Select Slave-2')
    print('5. Enter Input to Slave-1')
    print('6. Enter Input to Slave-2')
    print('7. Output from Slave-1')
    print('8. Output from Slave-2')
    print('##############################################')
    return input("Enter your choice : ")

def process(choice):
    if(choice == 1):
        gpio.signal_slave_1()
    elif(choice == 2):
        gpio.signal_slave_2()
    elif(choice == 3):
        bus_controller.select_slave_1()
    elif(choice == 4):
        bus_controller.select_slave_2()
    elif(choice == 5):
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
    elif(choice == 6):
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
    elif(choice == 7):
        print('7. Output from Slave-1')
        print('Bus controller select Master')
        bus_controller.select_master()
        print('Read from external memory at : ', prj_conf['SLAVE_1_OUTPUT_ADDR'])
        ext_mem.Read_String_n_Bytes_Address(prj_conf['SLAVE_1_OUTPUT_ADDR'], 16)
    elif(choice == 8):
        print('8. Output from Slave-2')
        print('Bus controller select Master')
        bus_controller.select_master()
        print('Read from external memory at : ', prj_conf['SLAVE_2_OUTPUT_ADDR'])
        ext_mem.Read_String_n_Bytes_Address(prj_conf['SLAVE_2_OUTPUT_ADDR'], 16)

prj_conf = get_project_config()
if __name__ == "__main__":
    gpio.init("MASTER")
    ext_mem.init()
    

    bus_controller.select_master()
    random_string = gen_random_string()
    ext_mem.Write_String_n_Bytes_Address(prj_conf["SLAVE_1_INPUT_ADDR"], random_string)
    time.sleep(1)
    string_read = ext_mem.Read_String_n_Bytes_Address(prj_conf["SLAVE_1_INPUT_ADDR"], len(random_string))
    print("random_string : ", random_string)
    print("string_read : ", string_read)
    assert string_read == random_string, "string_read is not equal to random_string"

    bus_controller.select_master()
    random_string = gen_random_string()
    ext_mem.Write_String_n_Bytes_Address(prj_conf["SLAVE_2_INPUT_ADDR"], random_string)
    time.sleep(1)
    string_read = ext_mem.Read_String_n_Bytes_Address(prj_conf["SLAVE_2_INPUT_ADDR"], len(random_string))
    print("random_string : ", random_string)
    print("string_read : ", string_read)
    assert string_read == random_string, "string_read is not equal to random_string"

    bus_controller.select_master()
    random_string = gen_random_string()
    ext_mem.Write_String_n_Bytes_Address(prj_conf["SLAVE_2_OUTPUT_ADDR"], random_string)
    time.sleep(1)
    string_read = ext_mem.Read_String_n_Bytes_Address(prj_conf["SLAVE_2_OUTPUT_ADDR"], len(random_string))
    print("random_string : ", random_string)
    print("string_read : ", string_read)
    assert string_read == random_string, "string_read is not equal to random_string"

    bus_controller.select_slave_2()
    gpio.signal_slave_2()
    time.sleep(5)
    
    bus_controller.select_slave_1()
    gpio.signal_slave_1()
    time.sleep(5)

    while(True):
        choice = print_menu
        process(choice)

    gpio.deinit()
    ext_mem.deinit()


    
    





