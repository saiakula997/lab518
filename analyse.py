
import os
import argparse
import pandas as pd
import  matplotlib.pyplot as plt

def get_averages(file_name):
    df = pd.read_csv(file_name)
    ch1, ch2, ch3, ch4 = df['ch1'], df['ch2'], df['ch3'], df['ch4']
    return ( ((ch1.mean()+ch3.mean())/2),  ((ch2.mean()+ch4.mean())/2))

def get_readings_subjects(subjects_dir_path):
    top_readings = {}
    bottom_readings = {}
    for name in os.listdir(subjects_dir_path):
        path = subjects_dir_path + "/" + name
        top_readings[name] = []
        bottom_readings[name] = []
        if os.path.isdir(path):    
            for file in os.listdir(path):
                top, bottom = get_averages(path+'/'+file)
                top_readings[name].append(top)
                bottom_readings[name].append(bottom)
                print(file, top, bottom)
    return top_readings, bottom_readings



def plot_readings(top_readings, bottom_readings, title):
    markers = ["." , "," , "o" , "v" , "^" , "<", ">", "*", "s", "p", "P"]
    for i,name in enumerate(top_readings.keys()):
        plt.scatter( top_readings[name], bottom_readings[name] , label=name, marker=markers[i])
    plt.legend()
    plt.title(title)
    plt.savefig(args.folder+"/"+"figure.png")
    plt.show()

parser = argparse.ArgumentParser()
parser.add_argument('--folder', type=str, required=True)
args = parser.parse_args()


top_readings, bottom_readings = get_readings_subjects(args.folder)
plot_readings(top_readings, bottom_readings, "PLOT")
