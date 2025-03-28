import pandas as pd
import numpy as np

data = [10,20,30,40]
serie_1 = pd.Series(data,index=['x','y','z','w'])
print(serie_1)

serie_1 = pd.Series(data,index=list('abcd'))

print(serie_1['b'])
print(serie_1.loc['b'])

serie_2 = pd.Series([1,2,3,4])
serie_3 = pd.Series([10,20,30,40])
summe = serie_2 + serie_3
print(summe)

serie_4 = pd.Series([1,np.nan,3,np.nan,5])
# option 1
# filter_serie_4 = serie_4.dropna()
# option 2
filter_serie_4 = serie_4[~serie_4.isnull()]
print(filter_serie_4)

d = {'城市': ['北京', '上海', '广州'], '人口': [2154, 2428, 1530]}
print(d)
df = pd.DataFrame(d,index=['A','B','C'])
print(df.loc[['A','B']])

df2 = pd.DataFrame(np.random.randint(1,100,(5,4)),columns = ['col1','col2','col3','col4'])
print(df2)
print(df2['col2'])

print(df2.iloc[2:5])

print(df2.loc[0:2,['col1','col3']])
