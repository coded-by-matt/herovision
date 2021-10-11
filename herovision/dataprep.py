#This script will be used to create a csv file
#that will connect our data model with the labels we want to use to identify objects.

#based on google's csv data prep notebook: https://gist.github.com/yufengg/984ed8c02d95ce7e95e1c39da906ee04

import os
import pandas as pd

#names of folders where our data is held.
data_folders = [
    'invoker',
    'juggernaut',
    'legioncommander',
    'lina',
    'ogre',
    'phantomassassin',
    'pudge',
    'shadowfiend',
    'silencer',
    'slark',
    'sniper',
    'windrunner'
    ]

artifact_count = 101

base_gcs_path = 'gs://heroset/Data Set'

# What we want:
# gs://cloudml-demo-vcm/chairs_table_bike/chair_black/chair_black157.jpg, 'chair_black'
# base_gcs_path + dict_key + '/' + filename

data_array = []
for current_folder in data_folders:
    for index in range(artifact_count):
        filenum = str(index).zfill(4)
        filename = current_folder + "_render"+filenum+".png"
        print(filename)
        filepath = base_gcs_path + '/'+ current_folder + '/' + filename
        print(filepath)
        label = current_folder
        data_array.append((filepath, label))

dataframe = pd.DataFrame(data_array)
dataframe.to_csv('all_data.csv', index=False, header=False)
print(dataframe.to_string())