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
def CMD_CONT_ARRAY_READ_LF(address): return [0xD2] + address_split(address) + DUMMY_BITS_32 # cmd + address (to read a page)

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



# Set up SPI interface
spi = spidev.SpiDev()
spi.open(0, 0)  # SPI bus 0, device 0
spi.max_speed_hz = 5000000  # Set SPI clock speed
spi.mode = 0b11

GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)

# Send command to read device ID
command = [0x9F]  # Device ID read command
response = spi.xfer2(command + [0x00, 0x00, 0x00])  # Send command and receive 4 bytes of response
device_id = (response[1] << 16) | (response[2] << 8) | response[3]  # Combine response bytes into device ID

print("Device ID: 0x{:06X}".format(device_id))

# Send command to read status register
command = [0xD7]  # Status register read command
response = spi.xfer2(command + [0x00])  # Send command and receive 1 byte of response
status_register = response[1]  # Get status register value

print("Status Register: 0x{:02X}".format(status_register))

# Send command to write data to memory
command = [0x82, 0x00, 0x00, 0x00]  # Page program command and memory address
data = [0xDE, 0xAD, 0xBE, 0xEF]  # Data to write
spi.xfer2(command + data)  # Send command and data

# Send command to read data from memory
command = [0x03, 0x00, 0x00, 0x00]  # Read data command and memory address
response = spi.xfer2(command + [0x00, 0x00, 0x00])  # Send command and receive 4 bytes of response
read_data = response[4:]  # Extract data bytes from response

print("Read Data: ", read_data)

GPIO.cleanup()
# Close SPI interface
spi.close()
