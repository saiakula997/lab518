import time
import RPi.GPIO as GPIO

GPIO_2_MUX_A=2
GPIO_3_MUX_B=3
GPIO_8_SPI_CS=8
GPIO_SIG_SLAVE_1=14
GPIO_ACK_SLAVE_1=15
GPIO_SIG_SLAVE_2=20
GPIO_ACK_SLAVE_2=21

def init(device=None):
    # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_8_SPI_CS, GPIO.OUT)

    if device == "MASTER":
        from bist_master import callback_from_slave_1, callback_from_slave_2
        GPIO.setup(GPIO_2_MUX_A, GPIO.OUT)
        GPIO.setup(GPIO_3_MUX_B, GPIO.OUT)
        GPIO.setup(GPIO_SIG_SLAVE_1, GPIO.OUT)
        GPIO.setup(GPIO_SIG_SLAVE_2, GPIO.OUT)
        GPIO.setup(GPIO_ACK_SLAVE_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(GPIO_ACK_SLAVE_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(GPIO_ACK_SLAVE_1, GPIO.RISING, callback=callback_from_slave_1)
        GPIO.add_event_detect(GPIO_ACK_SLAVE_2, GPIO.RISING, callback=callback_from_slave_2)

    elif device == "SLAVE":
        from bist_slave import callback_fun
        GPIO.setup(GPIO_ACK_SLAVE_1, GPIO.OUT)
        GPIO.setup(GPIO_ACK_SLAVE_2, GPIO.OUT)
        GPIO.setup(GPIO_SIG_SLAVE_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(GPIO_SIG_SLAVE_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(GPIO_SIG_SLAVE_1, GPIO.RISING, callback=callback_fun)
        GPIO.add_event_detect(GPIO_SIG_SLAVE_2, GPIO.RISING, callback=callback_fun)
    else:
        assert device not in ["MASTER", "SLAVE"], "Pin Mux device is neither master or slave"

def signal_slave_1():
    GPIO.output(GPIO_SIG_SLAVE_1, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GPIO_SIG_SLAVE_1, GPIO.LOW)

def signal_slave_2():
    GPIO.output(GPIO_SIG_SLAVE_2, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GPIO_SIG_SLAVE_2, GPIO.LOW)

def ack_slave_1():
    GPIO.output(GPIO_ACK_SLAVE_1, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GPIO_ACK_SLAVE_1, GPIO.LOW)

def ack_slave_2():
    GPIO.output(GPIO_ACK_SLAVE_2, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GPIO_ACK_SLAVE_2, GPIO.LOW)

def deinit():
    GPIO.cleanup()