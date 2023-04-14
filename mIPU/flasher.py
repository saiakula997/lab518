import spidev
import RPi.GPIO as GPIO

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)

# Configure SPI mode
spi.mode = 0b01

# Set chip select pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.LOW)

# Enable writing to memory
spi.xfer2([0x3D, 0x2A, 0x80])

# Send write command and address
spi.xfer2([0x84, 0x00, 0x00, 0x00])

# Send data to write
data = [0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0xCD, 0xEF]
spi.xfer2(data)

# Wait for write to complete
status = 0
while (status & 0x80) == 0:
    status = spi.xfer2([0xD7, 0x00])[1]

# Disable writing to memory
spi.xfer2([0x3D, 0x2A, 0x00])

# Set chip select pin back to high
GPIO.output(22, GPIO.HIGH)

# Close SPI bus
spi.close()
