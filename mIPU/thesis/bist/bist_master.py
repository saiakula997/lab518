import time
import json
import string
import random
import pin_mux
import sn54hc153_mux as mux
import AT45DB321E as ext_mem

def get_project_config():
    return json.load(open("ext_mem_config.json"))

def gen_random_string(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

if __name__ == "__main__":
    pin_mux.init()
    ext_mem.init()
    prj_conf = get_project_config()

    mux.select_master()
    random_string = gen_random_string()
    ext_mem.Write_String_n_Bytes_Address(prj_conf["SLAVE_1_INPUT_ADDR"], random_string)
    string_read = ext_mem.Read_String_n_Bytes_Address(prj_conf["SLAVE_1_INPUT_ADDR"], len(random_string))
    print("random_string : ", random_string)
    print("string_read : ", string_read)
    assert string_read == random_string, "string_read is not equal to random_string"





