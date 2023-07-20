import RPi.GPIO as GPIO

def my_callback(channel):
    print("GPIO pin {} is HIGH.".format(channel))

# Set the GPIO mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)


# Specify the GPIO pin you want to monitor
gpio_pin = 17

# Set up the GPIO pin as an input pin with a pull-down resistor
GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Add the event detection for a rising edge (from LOW to HIGH)
GPIO.add_event_detect(gpio_pin, GPIO.RISING, callback=my_callback)

try:
    # Your main code or tasks can go here
    while True:
        pass

except KeyboardInterrupt:
    print("\nExiting program.")
    GPIO.cleanup()  # Cleanup the GPIO settings on program exit

