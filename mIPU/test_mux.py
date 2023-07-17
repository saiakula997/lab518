import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin
led_pin = 17
GPIO_TEST_LED=2 
GPIO_MUX_SELECT=21
GPIO_G_PIN=13
GPIO_MUX_1A=26
GPIO_MUX_1B=20
GPIO_MUX_2A=19
GPIO_MUX_2B=16


GPIO.setup(GPIO_MUX_SELECT, GPIO.OUT)
GPIO.setup(GPIO_MUX_1A, GPIO.OUT)
GPIO.setup(GPIO_MUX_1B, GPIO.OUT)
GPIO.setup(GPIO_MUX_2A, GPIO.OUT)
GPIO.setup(GPIO_MUX_2B, GPIO.OUT)


def print_menu():
    print("Enter Choice :")
    print("0. Toggle Test Led")
    print("1. Select Mux A")
    print("2. Select Mux B")
    print("3. Turn on 1A")
    print("4. Turn on 1B")
    print("5. Turn on 2A")
    print("6. Turn on 2B")
    print("7. Turn off 1A")
    print("8. Turn off 1B")
    print("9. Turn off 2A")
    print("10. Turn off 2B")
    print("11. Enable IC")
    print("12. Disable IC")

try:
    while True:
        print_menu()
        choice = int(input())
        if choice == 0:
            GPIO.output(GPIO_TEST_LED, not GPIO.input(GPIO_TEST_LED))
        elif choice == 1: # select A
            GPIO.output(GPIO_MUX_SELECT, GPIO.LOW)
        elif choice == 2: # select B
            GPIO.output(GPIO_MUX_SELECT, GPIO.HIGH)
        elif choice == 3: # 1A ON 
            GPIO.output(GPIO_MUX_1A, GPIO.HIGH)
        elif choice == 4: # 1B ON 
            GPIO.output(GPIO_MUX_1B, GPIO.HIGH)
        elif choice == 5: # 2A ON 
            GPIO.output(GPIO_MUX_2A, GPIO.HIGH)
        elif choice == 6: # 2B ON 
            GPIO.output(GPIO_MUX_2B, GPIO.HIGH)
        elif choice == 7: # 1A OFF 
            GPIO.output(GPIO_MUX_1A, GPIO.LOW)
        elif choice == 8: # 1B OFF
            GPIO.output(GPIO_MUX_1B, GPIO.LOW)
        elif choice == 9: # 2A OFF
            GPIO.output(GPIO_MUX_2A, GPIO.LOW)
        elif choice == 10: # 2B OFF 
            GPIO.output(GPIO_MUX_2B, GPIO.LOW)
        elif choice == 11: # Enable IC 
            GPIO.output(GPIO_G_PIN, GPIO.LOW)
        elif choice == 12: # Disable IC 
            GPIO.output(GPIO_G_PIN, GPIO.HIGH)
        else : 
            print("Invalid Input")
    
except KeyboardInterrupt:
    # Clean up GPIO on program exit
    GPIO.cleanup()
