import csv
import argparse
import pandas as pd
from sklearn.metrics import mean_squared_error

parser = argparse.ArgumentParser()
parser.add_argument('--file1', type=str, required=True)
parser.add_argument('--file2', type=str, required=True)
args = parser.parse_args()

one = pd.read_csv(args.file1)
two = pd.read_csv(args.file2)

total_mse = 0
cols = min(len(one), len(two))
channels = ['ch1','ch2', 'ch3','ch4', 'ch5','ch6', 'ch7','ch8']
for ch in channels:
    mse = mean_squared_error(one[ch][:cols], two[ch][:cols])
    print("Mean Square Error - ", ch, mse)
    total_mse += mse
print("Total Mean Square Error", total_mse/len(channels))


    



