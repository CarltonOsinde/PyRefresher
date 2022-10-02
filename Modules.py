#Module and Library are interchangeable

import time
import os #Use this to check for file path and other items
import pandas as pd
import numpy as np



#IMPORTING CSV data - Pandas is a data analyis library
while True:
    if os.path.exists("files/temps_today.csv"):
        data = pd.read_csv("files/temps_today.csv")
        table_mean = data.mean()
        mean_col1 = data.mean()["st1"]
        print(data)
        print(table_mean)
        print(mean_col1)
    else:
        print("File does not exist")
    time.sleep(5)


while True:
    if os.path.exists("files/Jobs.txt"):
        with open("files/Jobs.txt") as file:
            print(file.read())

    else:
        print("File does not exist")
    time.sleep(5) #Use this to re-run the script after a short intervalc