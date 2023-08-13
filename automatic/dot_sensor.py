import csv
import time
import Adafruit_ADS1x15

GAIN = (2/3)
TIME_S = 15

CHANNEL_COUNT = 4
SAMPLE_FREQUENCY = (128)


pga_fsv = { 
    2/3 : 6.144,
    1   : 4.096,
    2   : 2.048, 
    4   : 1.024,
    8   : 0.512,
    16  : 0.256,
}

ADC_COUNT = 1
SENSORS_PER_ADC = 4
TOTAL_SENSORS_COUNT = ADC_COUNT * SENSORS_PER_ADC
SENSORS_UTILIZED = 4 #top and bottom of hand

def convert(x):
   return (x * pga_fsv[GAIN]) / ((2**16) * (GAIN))  

def convert_adc_voltage(data):
    v_data = []
    for row in data:
        v_row = [ convert(x) for x in row]
        v_data.append(v_row)
    return v_data

def get_readings():
    global GAIN, SAMPLE_FREQUENCY
    print("Getting Readings wait for", TIME_S, "seconds ...")
    data = []
    adc1 = Adafruit_ADS1x15.ADS1115(address=0x48)
    
    start = time.time()
    while int(time.time() - start) < TIME_S:
        values = [0]*SENSORS_UTILIZED                                                                                                  
        for i in range(SENSORS_UTILIZED):
            values[i] = adc1.read_adc(i,gain=GAIN, data_rate=SAMPLE_FREQUENCY)
            #values[i+4] = adc2.read_adc(i,gain=GAIN, data_rate=SAMPLE_FREQUENCY)
        data.append(values)
        print(values)
    print("Total readings", len(data))
    return data














