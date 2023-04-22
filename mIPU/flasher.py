import spidev
import RPi.GPIO as GPIO

# Dummy Bits
DUMMY_BITS_8 =  [0x00]
DUMMY_BITS_16 = [0x00, 0x00]
DUMMY_BITS_24 = [0x00, 0x00, 0x00]
DUMMY_BITS_32 = [0x00, 0x00, 0x00, 0x00]


# Additional Commands
CMD_SW_RESET = [0xF0, 0x00, 0x00, 0x00]  # Halts Program or Erase Operation and bring device to Idle operation
CMD_DEVICE_ID = [0x9F, 0x00, 0x00, 0x00, 0x00, 0x00] # cmd + manfacture ID + Device ID Byte 1 + Device ID Byte 2 + EDI string len + (optional) EDI Data (Extended Device Information)
CMD_CONF_BUFFER_SIZE_528 = [0x3D, 0x2A, 0x80, 0xA7] # DataFlash page size (528 bytes) (Default) 
CMD_CONF_BUFFER_SIZE_512 = [0x3D, 0x2A, 0x80, 0xA6] # “Power of 2” binary page size (512 bytes)
CMD_STATUS_REG_READ = [0xD7, 0x00, 0x00] # cmd + Status Reg Byte 1 + Status Reg Byte 2
CMD_ULTRA_DEEP_POWER_DOWN = "DONT USE" # [0x79] # Stops listening to all commands
CMD_MAIN_MEM_PG_BUF1_TRANSFER = "0x53 + address" # Address 0x123456 [0x12, 0x34, 0x56]
CMD_MAIN_MEM_PG_BUF2_TRANSFER = "0x55 + address"
CMD_AUTO_PG_RW_BUF1 = "0x58 + address"
CMD_AUTO_PG_RW_BUF2 = "0x59 + address"

def address_split(address): return [ (address >> 16) & 0xFF, (address >> 8) & 0xFF, (address >> 0) & 0xFF]

# Read Commands
def CMD_MAIN_MEM_PG_READ(address): return [0xD2] + address_split(address) + DUMMY_BITS_32 # cmd + address (to read a page)
def CMD_CONT_ARRAY_READ_LF(address): return [0x03] + address_split(address)  # cmd + address 

# Write Commands


def Print_Status_Register():
    pass

def Read_Status_Register():
    response = spi.xfer2(CMD_STATUS_REG_READ)
    return response[1], response[2] 

def Wait_Device_Ready():
    byte1, byte2 = Read_Status_Register()
    return (byte1 & 0x01)
    
def Get_Device_ID():
    response = spi.xfer2(CMD_DEVICE_ID)
    M_ID, D_ID = response[1], (response[2]<<8 | response[3]) # ignoring response[4,5] EDI Data  
    return M_ID, D_ID

def Read_n_Bytes_Address(address, n):
    data = [ 0x00, ] * n
    response = spi.xfer2(CMD_CONT_ARRAY_READ_LF(address) + data)
    return response[-n:]

def Write_n_Bytes_Address(address, data):
    pass

def read_status(txt):
    # Send command to read status register
    command = [0xD7]  # Status register read command
    response = spi.xfer2(command + [0x00, 0x00, 0x00, 0x00])  # Send command and receive 1 byte of response
    print(txt, end='')
    print(" --> Status Register", [hex(x) for x in response] )

def print_menu():
    print("################################################################")
    print("1. Get Status Register")
    print("2. Write 'n' Bytes into Address")
    print("3. Read 'n' Bytes from Address")
    print("4. Write into multiple pages")
    print("5. Read from multiple pages")
    print("6. Get Device ID(s)")
    print("q. quit")
    print("################################################################")
    print("Enter Command Choice : ")
    choice = input()
    return choice

def execute_cmd(choice):
    if choice == '1':
        Print_Status_Register()
    elif choice == '2':
        pass
    elif choice == '6':
        print(Get_Device_ID())


# Set up SPI interface
spi = spidev.SpiDev()
spi.open(0, 0)  # SPI bus 0, device 0
spi.max_speed_hz = 5000000  # Set SPI clock speed
spi.mode = 0b11

# setup GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)

if __name__ == "__main__" :

    while True:
        choice = print_menu()
        execute_cmd(choice)
        
        if choice == 'q':
            break

    # exit routine
    GPIO.cleanup()
    spi.close()




    # Send command to read device ID
command = [0x9F]  # Device ID read command
response = spi.xfer2(command + [0x00, 0x00, 0x00, 0x00, 0x00])  # Send command and receive 4 bytes of response
print("raw device ID : ", ([hex(x) for x in response]))

#device_id = (response[1] << 16) | (response[2] << 8) | response[3]  # Combine response bytes into device ID
#print("Device ID: 0x{:06X}".format(device_id))

read_status("After reading Device ID ")

# Send command to write data to memory
#command = [0x82, 0x00, 0x00, 0x00]  # Page program command and memory address
#spi.xfer2(command)

#data = [0xDE, 0xAD, 0xBE, 0xEF]  # Data to write
#print(spi.xfer2([0x84] + data + [0x00, 0x00, 0x00])) # Send command and data

#read_status("After Writing ")

# Send command to read data from memory
command = [0x03, 0x00, 0x00, 0x00]  # Read data command and memory address
response = spi.xfer2(command + [0x00, 0x00, 0x00, 0x00])  # Send command and receive 4 bytes of response
print([hex(x) for x in response])

read_status("After Reading ")

#read_data = response[4:]  # Extract data bytes from response
#print("Read Data: ", read_data)


