import RPi.GPIO as GPIO

GPIO_2_MUX_A=2
GPIO_3_MUX_B=3
GPIO_8_SPI_CS=8

def init():
    # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_8_SPI_CS, GPIO.OUT)
    GPIO.setup(GPIO_2_MUX_A, GPIO.OUT)
    GPIO.setup(GPIO_3_MUX_B, GPIO.OUT)