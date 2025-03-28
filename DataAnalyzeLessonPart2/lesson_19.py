# 26.03.2025

import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randint(1,100,(3,3)),index=['a','b','c'],columns=['python','java','web'])
df2 = pd.DataFrame(np.random.randint(1,100,(3,3)),index=['a','b','c'],columns=['python','java','web'])

print(df1)
print(df2)
print(df1+df2)

df3 = pd.DataFrame(np.random.randint(1,100,(4,4)),index=['a','b','c','d'],columns=['python','java','web','c++'])
print(df1+df3) #insert null if there are no info

print(df1.add(df3,fill_value=0))

s = pd.Series([100,10,1],index=df1.index)
print(s)
print(df1.add(s,axis=0))
print(df1.add(s,axis='index'))