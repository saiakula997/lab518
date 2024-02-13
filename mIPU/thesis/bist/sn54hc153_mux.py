import RPi.GPIO as GPIO

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

GPIO_2_MUX_A=2
GPIO_3_MUX_B=3
GPIO_8_SPI_CS=8

GPIO.setup(GPIO_2_MUX_A, GPIO.OUT)
GPIO.setup(GPIO_3_MUX_B, GPIO.OUT)

def select_master():
    GPIO.output(GPIO_2_MUX_A, GPIO.LOW)
    GPIO.output(GPIO_3_MUX_B, GPIO.LOW)

def select_slave_1():
    GPIO.output(GPIO_2_MUX_A, GPIO.HIGH)
    GPIO.output(GPIO_3_MUX_B, GPIO.LOW)

def select_slave_2():
    GPIO.output(GPIO_2_MUX_A, GPIO.HIGH)
    GPIO.output(GPIO_3_MUX_B, GPIO.LOW)