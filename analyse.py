
import os
import pandas as pd
import  matplotlib.pyplot as plt

def get_averages(file_name):
    df = pd.read_csv(file_name)
    top, bottom = df['ch1'], df['ch2']
    return (top.mean(), bottom.mean())

def get_readings_subjects(subjects_dir_path):
    readings = {}
    for name in os.listdir(subjects_dir_path):
        path = PATH + "/" + name
        readings[name] = []
        for file in os.listdir(path):
            top, bottom = get_averages(path+'/'+file)
            readings[name].append(top)
            readings[name].append(bottom)
    return readings


def plot_readings(readings):
    for name in readings.keys():
        print(name, readings[name])
        plt.scatter( range(len(readings[name])), (readings[name]) , label=name)
    plt.legend()
    plt.show()


PATH = "./observations/subjects"
readings = get_readings_subjects(PATH)
plot_readings(readings)
