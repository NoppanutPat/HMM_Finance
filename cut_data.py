import pandas as pd 
import numpy as np 

d = pd.read_csv("AAPL.csv")

d = d[:int(len(d)*0.8)]

d.to_csv('train_data.csv')
