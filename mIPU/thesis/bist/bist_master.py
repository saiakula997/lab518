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
    print("callback_from_slave_1")

def callback_from_slave_2(channel):
    print("callback_from_slave_2")

if __name__ == "__main__":
    gpio.init("MASTER")
    ext_mem.init()
    prj_conf = get_project_config()

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

    bus_controller.select_slave_1()
    gpio.signal_slave_1()
    time.sleep(30)
    
    gpio.deinit()
    ext_mem.deinit()


    
    





