import pandas as pd
import numpy as np
from matplotlib import pyplot
import csv

data_raw = pd.read_csv('/Users/davidkuchelmeister/Downloads/daily-minimum-temperatures-in-me.csv')

data['Temperatures'] = data_raw['Temperatures'].astype('float64')

data = pd.DataFrame()
data = data_raw.Temperatures.astype(float)
data.index = pd.to_datetime(data_raw["Date"], format="%Y-%m-%d")

df_avg = data.resample('D', how = 'mean')

df = pd.DataFrame(np.random.randn(1000, 4), columns=['a', 'b', 'c', 'd'])
pd.scatter_matrix(df)