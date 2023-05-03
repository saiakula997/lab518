import csv
import argparse
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()

parser.add_argument('--file', type=str, required=True)
args = parser.parse_args()

df = pd.read_csv(args.file)
df1, df2 = df['ch1'], df['ch2']
 
fig, axes = plt.subplots(nrows=2, ncols=1)

df1.plot(ax=axes[0])
df2.plot(ax=axes[1])



plt.savefig(args.file[:-3]+"png")
plt.show()
