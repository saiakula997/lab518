
import os
import argparse
import pandas as pd
import  matplotlib.pyplot as plt



def get_averages(file_name):
    df = pd.read_csv(file_name)
    top,bottom = df['ch2'], df['ch1']
    return (top.mean(), bottom.mean())

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

markers = ["." , "," , "o" , "v" , "^" , "<", ">"]
person = 0 
def plot_readings(top_readings, bottom_readings, title):
    global person
    for name in top_readings.keys():
        plt.scatter( top_readings[name], bottom_readings[name] , label=name, marker=markers[person])
        person += 1
    plt.legend()
    plt.title(title)
    plt.savefig(args.folder+"/"+"figure.png")
    plt.show()

parser = argparse.ArgumentParser()
parser.add_argument('--folder', type=str, required=True)
args = parser.parse_args()


top_readings, bottom_readings = get_readings_subjects(args.folder)
plot_readings(top_readings, bottom_readings, "PLOT")
