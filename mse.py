import csv
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--file1', type=str, required=True)
parser.add_argument('--file2', type=str, required=True)
args = parser.parse_args()

one = pd.read_csv(args.file1)
two = pd.read_csv(args.file2)

total_mse = 0
channels = ['ch1','ch2', 'ch3','ch4', 'ch5','ch6', 'ch7','ch8']
for ch in channels:
    mse = (one[ch].mean() - two[ch].mean())**2
    total_mse += mse
print("Total Mean Square Error", total_mse/len(channels) )