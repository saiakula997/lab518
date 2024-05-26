import time
import json
import string
import random
import argparse
import gpio
import AT45DB321E as ext_mem
import mnist_model

parser = argparse.ArgumentParser()
parser.add_argument('--slave', type=str, required=True)
args = parser.parse_args()
SLAVE_ID = args.slave
SLAVE_INPUT_ADDR = "SLAVE_" + SLAVE_ID + "_INPUT_ADDR"
SLAVE_OUTPUT_ADDR = "SLAVE_" + SLAVE_ID + "_OUTPUT_ADDR"

def get_project_config():
    return json.load(open("ext_mem_config.json"))

def gen_random_string(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def slave_ack_master():
    ack = { "1" : gpio.ack_slave_1, "2" : gpio.ack_slave_2 }[SLAVE_ID]
    ack()

def callback_fun(channel):
    print("Received Signal from Master")
    
    random_string = gen_random_string()
    ext_mem.Write_String_n_Bytes_Address(prj_conf[SLAVE_INPUT_ADDR], random_string)
    time.sleep(1)
    string_read = ext_mem.Read_String_n_Bytes_Address(prj_conf[SLAVE_INPUT_ADDR], len(random_string))
    print("random_string : ", random_string)
    print("string_read : ", string_read)
    #assert string_read == random_string, "string_read is not equal to random_string"

    random_string = gen_random_string()
    ext_mem.Write_String_n_Bytes_Address(prj_conf[SLAVE_OUTPUT_ADDR], random_string)
    time.sleep(1)
    string_read = ext_mem.Read_String_n_Bytes_Address(prj_conf[SLAVE_OUTPUT_ADDR], len(random_string))
    print("random_string : ", random_string)
    print("string_read : ", string_read)
    #assert string_read == random_string, "string_read is not equal to random_string"

    slave_ack_master()

def print_menu():
    print('##############################################')
    print('r. Read n Bytes from Slave-{0} Input'.format(SLAVE_ID))
    print('w. Write n Bytes to Slave-{0} Output'.format(SLAVE_ID))
    print('q. Quit')
    print('##############################################')
    

def process_input(choice):
    if choice == 'r':
        print("Enter Number of Bytes to Read :", end='')
        n = int(input())
        data = ext_mem.Read_n_Bytes_Address(prj_conf[SLAVE_INPUT_ADDR], n)
        print("Sending Input data to model")
        mnist_model.model(data)
    

if __name__ == "__main__":
    gpio.init("SLAVE")
    ext_mem.init()
    prj_conf = get_project_config()
    time.sleep(5)
    while(True):
        choice = input("Enter your choice :")
        print_menu()
        process_input(choice)
        if choice == 'q':
            break

    gpio.deinit()
    ext_mem.deinit()
    
