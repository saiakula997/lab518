import csv
import time
import argparse
import Adafruit_ADS1x15

GAIN = (2/3)
TIME_S = 30
CHANNEL_COUNT = 2
SAMPLE_FREQUENCY = (128)
CSV_FILE_NAME = "tset.csv"


TOTAL_READINGS = (float(SAMPLE_FREQUENCY)/float(CHANNEL_COUNT))*(float(TIME_S))

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
SENSORS_UTILIZED = 2 #top and bottom of hand

ADC_CSV_FILE_NAME = "ADC_" + CSV_FILE_NAME
VOLTAGE_CSV_FILE_NAME = "VOLTAGE_" + CSV_FILE_NAME

parser = argparse.ArgumentParser()

parser.add_argument('--file', type=str, required=False)
args = parser.parse_args()
CSV_FILE_NAME = args.file

def get_readings():
    global GAIN, SAMPLE_FREQUENCY, TOTAL_READINGS
    print("Getting Readings wait for", TIME_S, "seconds ...")
    data = []
    adc1 = Adafruit_ADS1x15.ADS1115(address=0x48)
    #adc2 = Adafruit_ADS1x15.ADS1115(address=0x49,busnum=1)
    start = time.time()
    while TOTAL_READINGS > 0:
        data.append( [adc1.read_adc(0,gain=GAIN, data_rate=SAMPLE_FREQUENCY), 
                      adc1.read_adc(1,gain=GAIN, data_rate=SAMPLE_FREQUENCY)])
        TOTAL_READINGS -= 1
    end = time.time()
    print("Total Readings Taken", len(data))
    print("Total Time Taken ", end - start)
    print("Ideally Time Taken Should Be ", TIME_S, int(end-start)==TIME_S)
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
    my_write.writerow(['ch1', 'ch2'])
    my_write.writerows(data)
    print("Created file", file_name)

data = get_readings()
write_csv_file(data, ADC_CSV_FILE_NAME)

v_data = convert_adc_voltage(data)
write_csv_file(v_data, VOLTAGE_CSV_FILE_NAME)







