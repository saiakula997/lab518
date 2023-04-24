
import os
import argparse
import pandas as pd
import  matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def get_averages(file_name):
    df = pd.read_csv(file_name)
    ch1, ch2, ch3, ch4 = df['ch1'], df['ch2'], df['ch3'], df['ch4']
    print(file_name, ch1.mean(), ch2.mean(), ch3.mean(), ch4.mean())
    return [ ch1.mean(), ch2.mean(), ch3.mean(), ch4.mean() ]

def get_readings_subjects(subjects_dir_path):
    readings = {}
    for name in os.listdir(subjects_dir_path):
        path = subjects_dir_path + "/" + name
        if os.path.isdir(path):
            readings[name] = []     
            for file in os.listdir(path):
                if file[-3:] == "csv":
                    readings[name].append(get_averages(path+'/'+file))             
    return readings

def plot_readings(x, title):
    markers = ["." , "," , "o" , "v" , "^" , "<", ">", "*", "s", "p", "P"]
    for i,name in enumerate(x.keys()):
        for l in x[name]:
            plt.scatter( l[0], l[1] , label=name, marker=markers[i])
    plt.legend()
    plt.title(title)
    plt.savefig(args.folder+"/"+"figure.png")
    plt.show()

parser = argparse.ArgumentParser()
parser.add_argument('--folder', type=str, required=True)
args = parser.parse_args()

readings = get_readings_subjects(args.folder)

data = []
for name in readings.keys():
    for x in readings[name]:
        data.append(x)

scalar = StandardScaler()
scalar.fit(data)
scaled_data = scalar.transform(data)

print("scaled_data", scaled_data)

pca = PCA(n_components = 2)
 
res = pca.fit_transform(data)
print("predicted", res)

pred = {}
for i, name in  enumerate(readings.keys()):
    pred[name] = [res[i*3 : (i*3)+3 ]]

print(pred)
plot_readings(pred, "PLOT")
