import spidev
import time
import RPi.GPIO as GPIO

# Set GPIO pins
GPIO_CS = 8
GPIO_WP = 7

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)

# Set SPI speed and mode
spi.max_speed_hz = 1000000
spi.mode = 0b00

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_CS, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(GPIO_WP, GPIO.OUT, initial=GPIO.LOW)

# Enable chip
GPIO.output(GPIO_CS, GPIO.LOW)

# Wait for chip to be ready
while True:
    status = spi.xfer([0xD7, 0x00])[1]
    if (status & 0x80) == 0x80:
        break
    time.sleep(0.01)

# Erase first sector (4KB)
GPIO.output(GPIO_WP, GPIO.LOW)
spi.xfer([0x81, 0x00, 0x00, 0x00])
GPIO.output(GPIO_WP, GPIO.HIGH)

# Wait for erase to complete
while True:
    status = spi.xfer([0xD7, 0x00])[1]
    if (status & 0x80) == 0x80:
        break
    time.sleep(0.01)

# Write data to memory
GPIO.output(GPIO_WP, GPIO.LOW)
data = [0x02, 0x00, 0x00, 0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC]
spi.xfer([0x82, 0x00, 0x00, 0x00] + data)
GPIO.output(GPIO_WP, GPIO.HIGH)

# Wait for write to complete
while True:
    status = spi.xfer([0xD7, 0x00])[1]
    if (status & 0x80) == 0x80:
        break
    time.sleep(0.01)

# Read data from memory
GPIO.output(GPIO_WP, GPIO.LOW)
spi.xfer([0x03, 0x00, 0x00, 0x00])
data = spi.xfer([0x00]*16)
print("Read data: ", data)
GPIO.output(GPIO_WP, GPIO.HIGH)

# Disable chip
GPIO.output(GPIO_CS, GPIO.HIGH)

# Close SPI bus
spi.close()
