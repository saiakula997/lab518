from pin_mux import * 

def select_master():
    GPIO.output(GPIO_2_MUX_A, GPIO.LOW)
    GPIO.output(GPIO_3_MUX_B, GPIO.LOW)

def select_slave_1():
    GPIO.output(GPIO_2_MUX_A, GPIO.HIGH)
    GPIO.output(GPIO_3_MUX_B, GPIO.LOW)

def select_slave_():
    GPIO.output(GPIO_2_MUX_A, GPIO.HIGH)
    GPIO.output(GPIO_3_MUX_B, GPIO.LOW)