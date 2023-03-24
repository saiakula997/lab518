import csv
import time
import argparse
import Adafruit_ADS1x15

GAIN = (2/3)
TIME_S = (5)
CHANNEL_COUNT = 4
SAMPLE_FREQUENCY = (8)
CSV_FILE_NAME = "sample.csv"

pga_fsv = { 
	2/3 : 6.144,
	1   : 4.096,
	2   : 2.048,
	4   : 1.024,
	8   : 0.512,
	16  : 0.256,
}

READINGS =  TIME_S * int(SAMPLE_FREQUENCY/CHANNEL_COUNT)
ADC_CSV_FILE_NAME = "ADC_" + CSV_FILE_NAME
VOLTAGE_CSV_FILE_NAME = "VOLTAGE_" + CSV_FILE_NAME

parser = argparse.ArgumentParser()

parser.add_argument('--file', type=str, required=False)
args = parser.parse_args()
CSV_FILE_NAME = args.file

def get_readings():
    global READINGS, GAIN, SAMPLE_FREQUENCY
    
    data = []
    adc1 = Adafruit_ADS1x15.ADS1115(address=0x48)
    adc2 = Adafruit_ADS1x15.ADS1115(address=0x49,busnum=1)
    
    while READINGS :
        values = [0]*8                                                                                                  
        for i in range(4):
            values[i] = adc1.read_adc(i,gain=GAIN, data_rate=SAMPLE_FREQUENCY)
            values[i+4] = adc2.read_adc(i,gain=GAIN, data_rate=SAMPLE_FREQUENCY)
        data.append(values)
        READINGS -= 1
    return data

def convert(x):
   return (x * pga_fsv[GAIN]) / ((2**16) * (GAIN))  

def convert_adc_voltage(data):
    v_data = []
    for row in data:
        v_row = [ convert(x) for x in row]
        v_data.append(v_row)
    return v_data

def write_csv_file(data, file_name):
    csvfile = open(file_name, "w")
    my_write = csv.writer(csvfile, delimiter = ',')
    my_write.writerow(['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8'])
    my_write.writerows(data)

data = get_readings()
write_csv_file(data, ADC_CSV_FILE_NAME)

v_data = convert_adc_voltage(data)
write_csv_file(v_data, VOLTAGE_CSV_FILE_NAME)







