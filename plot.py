import csv
import argparse
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()

parser.add_argument('--file', type=str, required=True)
args = parser.parse_args()

df = pd.read_csv(args.file)
df1, df2, df3, df4, df5, df6, df7, df8 = df['ch1'], df['ch2'], df['ch3'], df['ch4'], df['ch5'], df['ch6'], df['ch7'], df['ch8']
 
fig, axes = plt.subplots(nrows=4, ncols=1)

df1.plot(ax=axes[0])
df2.plot(ax=axes[1])
df3.plot(ax=axes[2])
df4.plot(ax=axes[3])


plt.savefig(args.file[:-3]+"png")
plt.show()
