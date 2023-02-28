import pandas as pd
import numpy as np

def load_data():
    # Converter for datetime string to datetime64 conversion
    conv = {
        "DATE_TIME": lambda x: np.datetime64(x)
    }

    #15-05-2020 00:00
    #2020-05-15 00:00:00
    conv_modified = {
        "DATE_TIME": lambda a: np.datetime64(a[6:10] + "-" + a[3:5] + "-" + a[0:2] + " " + a[11:] + ":00")
    }

    # Plant 1
    plant1 = pd.read_csv("archive/Plant_1_Generation_Data.csv", converters=conv_modified)
    weather1 = pd.read_csv("archive/Plant_1_Weather_Sensor_Data.csv", converters=conv)

    # Plant 2
    plant2 = pd.read_csv("archive/Plant_2_Generation_Data.csv", converters=conv)
    weather2 = pd.read_csv("archive/Plant_2_Weather_Sensor_Data.csv", converters=conv)
    
    return (plant1, plant2, weather1, weather2)


if __name__ == "__main__":
    pass