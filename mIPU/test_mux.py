import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # Turn on the LED
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED turned on")
        time.sleep(1)  # Delay for 1 second

        # Turn off the LED
        GPIO.output(led_pin, GPIO.LOW)
        print("LED turned off")
        time.sleep(1)  # Delay for 1 second

except KeyboardInterrupt:
    # Clean up GPIO on program exit
    GPIO.cleanup()
