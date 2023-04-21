import spidev
import RPi.GPIO as GPIO

# Set up SPI interface
spi = spidev.SpiDev()
spi.open(0, 0)  # SPI bus 0, device 0
spi.max_speed_hz = 5000000  # Set SPI clock speed
spi.mode = 0b11


def read_status(txt):
    # Send command to read status register
    command = [0xD7]  # Status register read command
    response = spi.xfer2(command + [0x00, 0x00, 0x00, 0x00])  # Send command and receive 1 byte of response
    print(txt, end='')
    print(" --> Status Register", [hex(x) for x in response] )


GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)


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

GPIO.cleanup()
# Close SPI interface
spi.close()
