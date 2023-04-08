
import os
import pandas as pd
import  matplotlib.pyplot as plt

def get_averages(file_name):
    df = pd.read_csv(file_name)
    top, bottom = df['ch1'], df['ch2']
    return (top.mean(), bottom.mean())

def get_readings_subjects(subjects_dir_path):
    top_readings = {}
    bottom_readings = {}
    for name in os.listdir(subjects_dir_path):
        path = PATH + "/" + name
        top_readings[name] = []
        bottom_readings[name] = []
        for file in os.listdir(path):
            top, bottom = get_averages(path+'/'+file)
            top_readings[name].append(top)
            bottom_readings[name].append(bottom)
            print(file, top, bottom)
    return top_readings, bottom_readings


def plot_readings(readings, title):
    for name in readings.keys():
        plt.scatter( range(len(readings[name])), (readings[name]) , label=name)
    plt.legend()
    plt.title(title)
    plt.savefig(title + ".png")
    plt.show()


PATH = "./observations/subjects"
top_readings, bottom_readings = get_readings_subjects(PATH)
plot_readings(top_readings, "Top")
plot_readings(bottom_readings, "Bottom")
