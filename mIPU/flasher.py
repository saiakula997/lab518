import spidev

# Set up SPI interface
spi = spidev.SpiDev()
spi.open(0, 0)  # SPI bus 0, device 0
spi.max_speed_hz = 5000000  # Set SPI clock speed

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

# Close SPI interface
spi.close()
