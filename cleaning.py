#Import the model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Load the dataset
df = pd.read_csv('WeatherHistory.csv')
df.head()
# Data Preparation
df.columns
df.shape
df.size
df.describe()
df.info()
df.dtypes
# Data Cleaning
df=df.drop(['Summary','Precip Type','Temperature (C)','Wind Speed (km/h)',
            'Wind Bearing (degrees)','Visibility (km)','Pressure (millibars)','Daily Summary'], axis=1)
df.head()
