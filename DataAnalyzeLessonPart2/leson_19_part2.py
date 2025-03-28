# 26.03.2025

import pandas as pd
import numpy as np

data = np.random.randint(1,100,(6,6))
index = [['1.class','1.class','1.class','2.class','2.class','2.class'],['a','b','c','d','e','f']]
columns = [['middle','middle','middle','end','end','end'],['German','Math','English','German','Math','English']]
df = pd.DataFrame(data,index=index,columns=columns)
print(df)

print(df.loc[('2.class','d')])
print(df.loc[('2.class','d'),('middle','Math')])
print(df.iloc[0,1]) # 0 means columns, 1 menas row

print(df['middle']['Math'])
print(df['middle']['Math']['1.class']['b'])

df1_middle = df.loc['1.class','middle']
print(df1_middle)
print(df1_middle.sum(axis = 1))

print(df1_middle)
print(df1_middle.max())
print(df1_middle.max(axis = 1))