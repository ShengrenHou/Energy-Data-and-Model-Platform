import pandas as pd
import numpy as np
# from pandasgui import show
data=pd.read_excel('information for platforms.xlsx',sheet_name='data',header=0)
data=data.iloc[:,:14]
data_json=data.to_json()
data.to_json('data.json')
# print(data.columns)
# print(data_json)
model=pd.read_excel('information for platforms.xlsx',sheet_name='model',header=0)
model_json=model.to_json()
model.to_json('model.json')
